pip install opencv-python numpy moviepy
import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def apply_sketch_effect(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    inverted_blurred = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)
    return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

def process_video(input_path, output_path):
    clip = VideoFileClip(input_path)
    processed_clip = clip.fl_image(apply_sketch_effect)
    processed_clip.write_videofile(output_path, codec="libx264", fps=clip.fps)

if __name__ == "__main__":
    import sys
    input_video = sys.argv[1]
    output_video = sys.argv[2]
    process_video(input_video, output_video)
