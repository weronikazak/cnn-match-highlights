import cv2
import numpy as numpy
import os
from random import shuffle
import random

video_list_url = os.path.join(os.getcwd(), "videos")

videos = os.listdir(video_list_url)
videos = [video for video in videos if video.split(".")[-1] == "mp4"]

video_shape = (224, 224)
each = 70

i = 1
for video in videos:
	video_link = os.path.join(video_list_url, video)
	cap = cv2.VideoCapture(video_link)
	resized_list = []

	while cap.isOpened():
		ret, frame = cap.read()
		if not ret:
			break

		i += 1

		if i % each == 0:
			resized = cv2.resize(frame, video_shape)
			cv2.imwrite(f"frames/frame_{i // each}.jpg", resized)
