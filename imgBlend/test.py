#!/usr/bin/env python3
import os
import imgLib as imgTool
import tinifyCompress

for file in os.listdir('./imgs'):
	imgTool.toWebp('./imgs/' + file)

for file in os.listdir('./imgs'):
	imgTool.blendWithFlag('./imgs/' + file)

for file in os.listdir('./webp'):
	imgTool.compress('./webp/' + file)