#!/bin/bash
START=493

NUM=1
let END=$START+$NUM
for ((i=START; i<END; i++))
do
    echo $i
    python 1_generate_fake_label.py --seq_idx=$i
    python 2_build_city_seq_data.py --seq_idx=$i
    bash 3_script_city_vis.sh
    python 4_get_res_label.py --seq_idx=$i
done

