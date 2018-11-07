import glob
import math
import os.path
import re
import sys

import tensorflow as tf

usr_dir = os.path.expanduser('~')
sys.path.insert(0, os.path.join(usr_dir, 'tensorflow-research/models/research/deeplab/datasets'))
import build_data

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('cityscapes_root', 'datasets/Cityscapes', 'Cityscapes dataset root folder.')
tf.app.flags.DEFINE_string('output_dir', 'tfrecord', 'Path to save converted SSTable of TensorFlow examples.')
tf.app.flags.DEFINE_string('data_split', 'train', 'train or val')
tf.app.flags.DEFINE_integer('seq_idx', 0, 'index of sequence')


# A map from data type to folder name that saves the data.
_FOLDERS_MAP = {
    'image': 'video_clip',
    'label': 'video_mask_fake',
}

# A map from data type to filename postfix.
_POSTFIX_MAP = {
    'image': '_leftImg8bit',
    'label': '_gtFine_labelTrainIds',
}

# A map from data type to data format.
_DATA_FORMAT_MAP = {
    'image': 'png',
    'label': 'png',
}

# Image file pattern.
_IMAGE_FILENAME_RE = re.compile('(.+)' + _POSTFIX_MAP['image'])


def _get_files(data, seq_idx):
  """Gets files for the specified data type and dataset split.

  Args:
    data: String, desired data ('image' or 'label').
    dataset_split: String, dataset split ('train', 'val', 'test')

  Returns:
    A list of sorted file names or None when getting label for
      test set.
  """
  pattern = '*%s.%s' % (_POSTFIX_MAP[data], _DATA_FORMAT_MAP[data])
  search_files = os.path.join(
      usr_dir, FLAGS.cityscapes_root, _FOLDERS_MAP[data], FLAGS.data_split, 'seq%04d'%seq_idx, pattern)
  filenames = glob.glob(search_files)
  return sorted(filenames)


def _convert_dataset(seq_idx):
  """Converts the specified dataset split to TFRecord format.

  Args:
    dataset_split: The dataset split (e.g., train, val).

  Raises:
    RuntimeError: If loaded image and label have different shape, or if the
      image file with specified postfix could not be found.
  """
  image_files = _get_files('image', seq_idx)
  label_files = _get_files('label', seq_idx)

  image_reader = build_data.ImageReader('png', channels=3)
  label_reader = build_data.ImageReader('png', channels=1)

  shard_filename = 'seq-%05d-of-%05d.tfrecord' % (0, 1)
  output_filename = os.path.join(usr_dir, FLAGS.cityscapes_root, FLAGS.output_dir, shard_filename)
  with tf.python_io.TFRecordWriter(output_filename) as tfrecord_writer:
      for i in xrange(len(image_files)):
        # Read the image.
        image_data = tf.gfile.FastGFile(image_files[i], 'rb').read()
        height, width = image_reader.read_image_dims(image_data)
        # Read the semantic segmentation annotation.
        seg_data = tf.gfile.FastGFile(label_files[i], 'rb').read()
        seg_height, seg_width = label_reader.read_image_dims(seg_data)
        if height != seg_height or width != seg_width:
          raise RuntimeError('Shape mismatched between image and label.')
        # Convert to tf example.
        re_match = _IMAGE_FILENAME_RE.search(image_files[i])
        if re_match is None:
          raise RuntimeError('Invalid image filename: ' + image_files[i])
        filename = os.path.basename(re_match.group(1))
        example = build_data.image_seg_to_tfexample(
            image_data, filename, height, width, seg_data)
        tfrecord_writer.write(example.SerializeToString())


def main(unused_argv):
  # Only support converting 'train' and 'val' sets for now.
  #for dataset_split in ['train', 'val']:
  _convert_dataset(FLAGS.seq_idx)


if __name__ == '__main__':
  tf.app.run()
