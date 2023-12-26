## T1   715
# grids_x = [112, 144, 208, 224, 224, 208, 144, 112, 160]
# grids_y = [112, 144, 208, 224, 224, 208, 144, 112, 160]

## T10  500  2940
grids_x = [240, 300, 330, 390, 390, 330, 300, 240, 420]
grids_y = [240, 300, 330, 390, 390, 330, 300, 240, 420]

Template = {'DP84': {'grids': [112, 144, 208, 224, 224, 208, 144, 112, 160], 'pitch': 715},
            'SS84': {'grids': [112, 144, 208, 224, 224, 208, 144, 112, 160], 'pitch': 715},
            'FP2': {'grids': [240, 300, 330, 390, 390, 330, 300, 240, 420], 'pitch': 500},
            'SS2': {'grids': [240, 300, 330, 390, 390, 330, 300, 240, 420], 'pitch': 500},
            'FP1': {'grids': [192, 240, 288, 312, 312, 288, 240, 192, 384], 'pitch': 600},
            'SS1': {'grids': [192, 240, 288, 312, 312, 288, 240, 192, 384], 'pitch': 600}}

ratio = 2.232
norm_magnify = 4.0

## 用于生成缩略图
magnify_set = True
Image_magnify = 1.0

## 切图的种类
crop = False
crop_size = 10000

## 最后取旋转角和scale的区间
Up_boundary = 0.6
Low_boundary = 0.4

# ratio  6.8376
# slideio http://www.slideio.com/tutorial.html