import os, shutil

main_prefix = '/media/hdc/data3/lzk_ur_main/20201125_ODexps/yolov3_v8/yolov3_v8/data/shipdata/'
input_dir_prefix = main_prefix + 'images/1344_frames/'
output_dir_prefix_img = '/media/hdc/data3/lzk_ur_main/20201125_ODexps/yolov3_v8_original/yolov3-8/coco/images/valid/'
output_dir_prefix_lab = '/media/hdc/data3/lzk_ur_main/20201125_ODexps/yolov3_v8_original/yolov3-8/coco/labels/valid/'

with open(main_prefix + 'dataset_txt/1344_frames/val.txt', 'r') as file:
    images0 = file.readlines()

images = [image.split('/')[-1].strip('\n') for image in images0]

for image in images:
    shutil.copyfile(input_dir_prefix + image, output_dir_prefix_img + image)
    try:
        shutil.copyfile(input_dir_prefix.replace('images', 'labels') +
                        image.replace('.bmp', '.txt'),
                        output_dir_prefix_lab + image.replace('.bmp', '.txt'))
    except:
        print(f'There\'s no corresponding txt file to {image}')