import cv2
import os

class VideoProcessor:
    def __init__(self, video_path):
        if isinstance(video_path, str) and not os.path.isfile(video_path):
            print(f"Failed to find video at: {video_path}")
        try:
            self.video = cv2.VideoCapture(int(video_path))
        except ValueError:
            self.video = cv2.VideoCapture(video_path)
        self.frame_count = 0

    def get_next_frame(self):
        ret, frame = self.video.read()
        if ret:
            self.frame_count += 1
            return frame
        return None

    def get_video_properties(self):
        width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = self.video.get(cv2.CAP_PROP_FPS)
        return width, height, fps

    def release(self):
        self.video.release()
