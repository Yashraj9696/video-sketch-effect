import cv2
import numpy as np
import os

def apply_sketch_effect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_gray = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)
    inverted_blurred = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)
    return sketch

def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height), isColor=False)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        sketch_frame = apply_sketch_effect(frame)
        out.write(sketch_frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_video = "input_video.mp4"  # Upload this file in GitHub
    output_video = "output_sketch_video.mp4"

    if os.path.exists(input_video):
        process_video(input_video, output_video)
        print("Processing completed! Output saved as", output_video)
    else:
        print("No input video found.")
