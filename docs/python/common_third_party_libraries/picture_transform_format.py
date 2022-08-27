import os

# PIL : Python Imaging Library
from PIL import Image

# # 获取目录下文件名
# files = os.listdir()
# # 图标大小
# size = (256, 256)
# # 给图标文件单独创建一个icon目录
# if not os.path.exists('icon'):
#     os.mkdir('icon')
# for inName in files:
#     # 分离文件名与扩展名
#     tmp = os.path.splitext(inName)
#     # 因为python文件跟图片在同目录，所以需要判断一下
#     if tmp[1] == '.png':
#         outName = tmp[0] + '.ico'
#     # 打开图片并设置大小
#     im = Image.open(inName).resize(size)
#     try:
#         # 图标文件保存至icon目录
#         path = os.path.join('icon', outName)
#         im.save(path)
#         print('{} --> {}'.format(inName, outName))
#     except IOError:
#         print('connot convert :', inName)

src = "./Assets/Square44x44Logo.altform-unplated_targetsize-256.png"
src1 = "./StoreLogo.scale-200.png"
out = "ubuntu1.ico"
im = Image.open(src)
im.save(out)
print(f"current dir is :{os.getcwd()}")
