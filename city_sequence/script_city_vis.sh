python deeplab/vis.py \
  --logtostderr \
  --eval_split="val" \
  --model_variant="xception_71" \
  --dense_prediction_cell_json="deeplab/core/dense_prediction_cell_branch5_top1_cityscapes.json" \
  --atrous_rates=12 \
  --atrous_rates=24 \
  --atrous_rates=36 \
  --output_stride=8 \
  --decoder_output_stride=4 \
  --vis_crop_size=1025 \
  --vis_crop_size=2049 \
  --dataset="cityscapes" \
  --colormap_type="cityscapes" \
  --checkpoint_dir="deeplab/datasets/cityscapes/exp/train_on_trainval_set/train" \
  --vis_logdir="deeplab/datasets/cityscapes/exp/train_on_trainval_set/vis" \
  --dataset_dir="deeplab/datasets/cityscapes/tfrecord" \
  --max_number_of_evaluations=1 \
  --also_save_raw_predictions \
  --eval_scales=0.75 \
  --eval_scales=1.0 \
  --eval_scales=1.25 \
  --eval_scales=1.5 \
  --eval_scales=1.75 \
  --eval_scales=2.0 \
  --add_flipped_images
