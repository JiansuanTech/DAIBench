python ./multiproc.py --nproc_per_node 8 ./main.py /data/imagenet --raport-file raport.json -j5 -p 100 --arch resnext101-32x4d --label-smoothing 0.1 --workspace $1 -b 128 --amp  --static-loss-scale 128 --optimizer-batch-size 1024 --lr 1.024 --mom 0.875 --lr-schedule cosine --epochs 250 --mixup 0.2 -c fanin --data-backend dali-cpu --lr 1.024 --wd 3.0517578125e-05 --warmup 4