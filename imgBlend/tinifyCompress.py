#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import os.path
# import click
import tinify
import platform

tinify.key = "xww1Cyky5lmJDjXnrrBYF62m8hGRtCw7"		# API KEY
version = "1.1.0"		# 版本号
author = "chenzilu"          # 修改者
voice = True			# 是否语音提示

def say(content):
	if platform.system() == "Darwin" and voice == True:
		print(content)
		os.system("say '"+content+"' ")
	else:
		print("tinypng---"+content)
	pass

# 压缩的核心
def compress_core(inputFile, outputFile, img_width):
	source = tinify.from_file(inputFile)
	if img_width is not -1:
		resized = source.resize(method = "scale", width  = img_width)
		resized.to_file(outputFile)
	else:
		source.to_file(outputFile)

# 压缩一个文件夹下的图片
def compress_path(path, width):
#	print "压缩指定目录下文件!"
	if not os.path.isdir(path):
		say("骗纸! 这根本不是一个文件夹!")
		return
	else:
		say("尝试压缩, 请稍后!")
		fromFilePath = path 			# 源路径
		toFilePath = path+"/tiny" 		# 输出路径
#		print "fromFilePath=%s" %fromFilePath
#		print "toFilePath=%s" %toFilePath
		for root, dirs, files in os.walk(fromFilePath):
			print("root = %s" %root)
			print("dirs = %s" %dirs)
			print("files= %s" %files)
			for name in files:
				fileName, fileSuffix = os.path.splitext(name)
				if fileSuffix == '.png' or fileSuffix == '.jpg' or fileSuffix == '.jpeg':
					toFullPath = toFilePath + root[len(fromFilePath):]
					toFullName = toFullPath + '/' + name
					if os.path.isdir(toFullPath):
						pass
					else:
						os.mkdir(toFullPath)
					compress_core(root + '/' + name, toFullName, width)
			break									# 仅遍历当前目录

# 仅压缩指定文件
def compress_file(inputFile, width):
#	print "压缩指定文件!"
	if not os.path.isfile(inputFile):
		say("骗纸! 这根本不是文件!")
		return
	say("尝试压缩, 请稍后!")
#	print "file = %s" %inputFile
	dirname  = os.path.dirname