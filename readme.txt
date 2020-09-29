



pip install paddlepaddle-gpu==1.8.4.post107 -i https://mirror.baidu.com/pypi/simple



# 解压预训练模型
cd ~/w*
cp ../data/data53741/output.zip ./output.zip
unzip output.zip
rm -f output.zip




# 安装依赖、解压COCO2017数据集
nvidia-smi
cd ~
pip install pycocotools
cd data
cd data7122
unzip ann*.zip
unzip val*.zip
unzip tes*.zip
unzip image_info*.zip
unzip train*.zip
cd ~/w*






-------------------------------- SPADE --------------------------------
训练
python download.py --dataset=mnist

export FLAGS_eager_delete_tensor_gb=0.0
export FLAGS_fast_eager_deletion_mode=1
export FLAGS_fraction_of_gpu_memory_to_use=0.01
CUDA_VISIBLE_DEVICES=0



为了支持np.put_along_axis(input_label, index, 1.0, 0)：
pip install numpy>=1.15.0 -i https://mirror.baidu.com/pypi/simple


--data_dir是cityscapes文件夹的父目录。


算法网络结构：
https://blog.csdn.net/u014380165/article/details/100110065


crop_height减小
python train.py --model_net SPADE --data_dir E://BaiduNetdiskDownload/ --dataset cityscapes --train_list E://BaiduNetdiskDownload/cityscapes/train_list.txt --test_list E://BaiduNetdiskDownload/cityscapes/val_list.txt --crop_type Random --batch_size 1 --epoch 200 --load_height 356 --load_width 612 --crop_height 256 --crop_width 512 --label_nc 36





（二）恢复训练
接着上次继续训练。比如上次训练时留下了一个最新的模型，代号是1000，恢复训练时加-r参数：



预测
python infer.py --model_net SPADE --dataset_dir E://BaiduNetdiskDownload/cityscapes/ --test_list E://BaiduNetdiskDownload/cityscapes/val_list.txt --load_height 356 --load_width 612 --crop_height 256 --crop_width 512 --init_model ./output/checkpoints/3/


结果压缩成zip方便下载：
rm -f out.zip
zip -r out.zip output/*.jpg



验证





导出
python tools/export_model.py  -c configs/solov2/solov2_r50_fpn_8gpu_3x.yml --output_dir=./inference_model -o weights=output/solov2_r50_fpn_8gpu_3x/model_final


python tools/export_model.py  -c configs/solov2/solov2_light_448_r50_fpn_8gpu_3x.yml --output_dir=./inference_model -o weights=output/solov2_light_448_r50_fpn_8gpu_3x/model_final




用导出后的模型预测1张图片：（测速）
python deploy/python/infer.py --model_dir=./inference_model/solov2_r50_fpn_8gpu_3x --image_file=./test_imgs/000000000019.jpg --use_gpu=True


python deploy/python/infer.py --model_dir=./inference_model/solov2_light_448_r50_fpn_8gpu_3x --image_file=./test_imgs/000000000019.jpg --use_gpu=True



用导出后的模型预测./test_imgs/目录下的图片：
python deploy/python/infer.py --model_dir=./inference_model/solov2_light_448_r50_fpn_8gpu_3x --image_dir=./test_imgs/ --use_gpu=True



用导出后的模型预测视频：
python deploy/python/infer.py --model_dir=./inference_model/solov2_light_448_r50_fpn_8gpu_3x --video_file D://PycharmProjects/moviepy/che3.mp4 --use_gpu=True



用导出后的模型播放视频：（按esc键停止播放）
python deploy/python/infer.py --model_dir=./inference_model/solov2_light_448_r50_fpn_8gpu_3x --play_video D://PycharmProjects/moviepy/che3.mp4 --use_gpu=True



















