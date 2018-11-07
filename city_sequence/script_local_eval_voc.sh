export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/deeplab
python deeplab/eval.py \
  --logtostderr \
  --eval_split="val" \
  --model_variant="xception_65" \
  --atrous_rates=6 \
  --atrous_rates=12 \
  --atrous_rates=18 \
  --output_stride=16 \
  --decoder_output_stride=4 \
  --eval_crop_size=513 \
  --eval_crop_size=513 \
  --checkpoint_dir="deeplab/datasets/pascal_voc_seg/exp/train_on_trainval_set/train" \
  --eval_logdir="deeplab/datasets/pascal_voc_seg/exp/train_on_trainval_set/eval" \
  --dataset_dir="deeplab/datasets/pascal_voc_seg/tfrecord" \
  --max_number_of_evaluations=1 \
  --eval_scales=0.5 \
  --eval_scales=0.75 \
  --eval_scales=1.0 \
  --eval_scales=1.25 \
  --eval_scales=1.5 \
  --eval_scales=1.75 \
  --add_flipped_images