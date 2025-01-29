import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

class ASCIIVideoProcessor:

    def __init__(self, width=None, height=None, style='default'):
        self.width = width
        self.height = height
        self.frames = []
        self.style = style
        self.frame_buffer = []
        self.buffer_size = 30

        # Different ASCII styles for various scene types
        self.styles = {
            'default': ['@', '#', '8', '&', '%', 'X', '+', '=', '-', ':', '.'],
            'dense': ['█', '▓', '▒', '░'],
            'minimal': ['@', '%', '#', '*', '+', '=', '-', '.']
        }
        self.char_range = int(255 / len(self.styles[style]))

    def get_char(self, val):
        if val > 240:  # Very bright areas
            return ' '
        val = 255 - val  # Invert for better contrast
        chars = self.styles[self.style]
        return chars[min(int(val / self.char_range), len(chars) - 1)]

    def process_frame(self, frame):
        # Enhance contrast
        frame = cv2.convertScaleAbs(frame, alpha=1.3, beta=10)
        
        # Motion blur reduction
        frame = cv2.GaussianBlur(frame, (3, 3), 0)
        
        # Edge detection for better detail
        edges = cv2.Canny(frame, 100, 200)
        
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Enhance edges
        gray[edges > 0] = 0
        
        # Resize frame
        resized = cv2.resize(gray, (self.width, self.height))
        
        # Convert to ASCII
        ascii_frame = [[self.get_char(pixel) for pixel in row] for row in resized]
        
        return ascii_frame

    def create_frame_image(self, ascii_frame):
        # Calculate image dimensions
        char_width = 10
        char_height = 20
        img_width = self.width * char_width
        img_height = self.height * char_height
        
        # Create new image
        image = Image.new('RGB', (img_width, img_height), color='black')
        draw = ImageDraw.Draw(image)  # This line creates the draw object
        
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
                )  # Add closing parenthesis here

        return image

    def process_video(self, input_path, output_path, fps=24):
        cap = cv2.VideoCapture(input_path)
        
        if self.width is None or self.height is None:
            self.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Process every other frame for performance
            if frame_count % 2 == 0:
                ascii_frame = self.process_frame(frame)
                frame_image = self.create_frame_image(ascii_frame)
                self.frames.append(frame_image)

            frame_count += 1

        cap.release()

        # Save as GIF
        if self.frames:
            self.frames[0].save(
                output_path,
                save_all=True,
                append_images=self.frames[1:],
                duration=int(1000/fps),
                loop=0
            )


            # Save as GIF
            if self.frames:
                self.frames[0].save(
                    output_path,
                    save_all=True,
                    append_images=self.frames[1:],
                    duration=int(1000 / fps),
                    loop=0
                )
