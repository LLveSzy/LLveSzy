#-*- coding:utf-8 -*-

import pygame

pygame.init()
n = 0
with open('/home/szy/train/dd.txt') as f:
	for line in f.readlines():
		for s in line:
			print (s)
			text = s
			#设置字体和字号
			font = pygame.font.SysFont('AR PL UKai CN', 64)
			#渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
			ftext = font.render(text, True, (255, 255, 255),(0, 0, 0))
			#保存图片
			pygame.image.save(ftext, "/home/szy/train/image"+str(n)+".jpg")#图片保存地址
			n=n+1


