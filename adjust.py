# encoding=utf-8
# function: 更改图片尺寸大小
import os
import os.path
from PIL import Image

'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''


def ResizeImage(filein, fileout, width, height, type):
	img = Image.open(filein)
	out = img.resize((width, height), Image.ANTIALIAS)  # resize image with high-quality
	out.save(fileout, type)


if __name__ == "__main__":
	filein = r'assets\img\shop\pay.jpg'
	fileout = r'assets\img\shop\payNew.jpg'
	width = 550
	height = 660
	type = 'png'
	ResizeImage(filein, fileout, width, height, type)
