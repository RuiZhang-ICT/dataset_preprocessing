NUM_ITERATIONS=1
python deeplab/train.py \
  --logtostderr \
  --train_split="train" \
  --model_variant="xception_71" \
  --dense_prediction_cell_json="deeplab/core/dense_prediction_cell_branch5_top1_cityscapes.json" \
  --atrous_rates=12 \
  --atrous_rates=24 \
  --atrous_rates=36 \
  --output_stride=8 \
  --decoder_output_stride=4 \
  --train_crop_size=1025 \
  --train_crop_size=2049 \
  --train_batch_size=1 \
  --dataset="cityscapes" \
  --training_number_of_steps="${NUM_ITERATIONS}" \
  --fine_tune_batch_norm=true \
  --tf_initial_checkpoint="deeplab/models_cityscapes/deeplab_cityscapes_xception71_trainvalfine_2018_09_08/model.ckpt" \
  --train_logdir="deeplab/datasets/cityscapes/exp/train_on_trainval_set/train" \
  --dataset_dir="deeplab/datasets/cityscapes/tfrecord"
