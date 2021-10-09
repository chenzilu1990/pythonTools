import os
from PIL import Image
import tinifyCompress


# for root,dirs,files in os.walk('.'):
	# print(root)
	# print(dirs)
	# print(files)

def blendWithFlag(file):
	if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
		flag = Image.open("./filter.png").convert('RGBA')
		r,g,b,a = flag.split()

		baseName = os.path.basename(file)
		name = os.path.splitext(baseName)[0]
		# print(baseName, name)
		img = Image.open(file).convert('RGBA')
		img = img.resize((1000, 1000))

		img2 = Image.composite(flag, img , a)
		# img2.show()
		img2.save('./withFlag/'+ name + '.png', 'PNG')


def toWebp(file):
	if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
		baseName = os.path.basename(file)
		name = os.path.splitext(baseName)[0]
		# print(baseName, name)
		img = Image.open(file).convert("RGBA")
		img.save('./webp/'+ name + '.webp', "WEBP")


def compress(file):
	if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.webp'):

		baseName = os.path.basename(file)
		name = os.path.splitext(baseName)[0]
		print(baseName, name)
		toFilePath = './compress/' + name + '.webp'
		tinifyCompress.compress_core(file,toFilePath, -1)