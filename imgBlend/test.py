import os
import imgLib as imgTool


for file in os.listdir('./imgs'):
	imgTool.toWebp('./imgs/' + file)

for file in os.listdir('./imgs'):
	imgTool.blendWithFlag('./imgs/' + file)
