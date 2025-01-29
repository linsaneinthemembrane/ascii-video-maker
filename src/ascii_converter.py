import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

class ASCIIVideoProcessor:
    def __init__(self, width, height, style='default'):
        self.width = width
        self.height = height
        self.frames = []
        self.style = style
        self.frame_buffer = []
        self.buffer_size = 30
        
        # different ascii styles for scene types
        self.styles = {
            'default': ['@', '#', '8', '&', '%', 'X', '+', '=', '-', ':', '.'],
            'dense': ['█', '▓', '▒', '░'],
            'minimal': ['@', '%', '#', '*', '+', '=', '-', '.']
        }  
        self.char_range = int(255 / len(self.styles[style]))

    def get_char(self, val):
        if val > 240:  # handle bright areas
            return ' '
        val = 255 - val  # invert for contrast
        chars = self.styles[self.style]
        return chars[min(int(val/self.char_range), len(chars)-1)]

    def process_frame(self, frame):
        # detect green screen (RGB values for green)
        lower_green = np.array([35, 150, 35])
        upper_green = np.array([85, 255, 85])
        
        # create mask for green pixels
        mask = cv2.inRange(frame, lower_green, upper_green)
        
        # enhance image quality
        frame = cv2.convertScaleAbs(frame, alpha=1.3, beta=10)
        frame = cv2.GaussianBlur(frame, (3, 3), 0)
        edges = cv2.Canny(frame, 100, 200)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # set green screen pixels to white (which will become spaces)
        gray[mask > 0] = 255
        
        gray[edges > 0] = 0
        resized = cv2.resize(gray, (self.width, self.height))
        
        # convert to ascii art
        ascii_frame = [[self.get_char(pixel) for pixel in row] for row in resized]
        return ascii_frame


    def create_frame_image(self, ascii_frame):
        # set dimensions
        char_width = 10
        char_height = 20
        img_width = self.width * char_width
        img_height = self.height * char_height
        
        # create and draw ascii frame
        image = Image.new('RGB', (img_width, img_height), color='black')
        draw = ImageDraw.Draw(image)
        
        try:
            font = ImageFont.truetype('DejaVuSansMono.ttf', 16)
        except:
            font = ImageFont.load_default()
        
        for y, row in enumerate(ascii_frame):
            for x, char in enumerate(row):
                draw.text(
                    (x * char_width, y * char_height),
                    char,
                    font=font,
                    fill='white'
                )
        return image

    def process_video(self, input_path, output_path, fps=24):
        cap = cv2.VideoCapture(input_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(f"Total frames to process: {total_frames}")
        
        frame_count = 0
        processed_count = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # process alternate frames for performance
            if frame_count % 2 == 0:
                ascii_frame = self.process_frame(frame)
                frame_image = self.create_frame_image(ascii_frame)
                self.frames.append(frame_image)
                processed_count += 1
                
                if processed_count % 10 == 0:
                    print(f"Processed {frame_count}/{total_frames} frames")
            
            frame_count += 1
        
        cap.release()
        print(f"Processing complete! Total frames processed: {processed_count}")
        
        # save output gif
        if self.frames:
            print("Saving GIF...")
            self.frames[0].save(
                output_path,
                save_all=True,
                append_images=self.frames[1:],
                duration=int(1000/fps),
                loop=0
            )
            print(f"GIF saved successfully to: {output_path}")
