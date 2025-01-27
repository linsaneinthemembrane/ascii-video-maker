from PIL import Image, ImageDraw, ImageFont

class ASCIIPlayer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.frames = []
        self.frame_duration = int(1000 / 24)  # Default 24 FPS

    def add_frame(self, ascii_frame):
        img = Image.new('RGB', (self.width * 10, self.height * 20), color='black')
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        
        for y, row in enumerate(ascii_frame):
            for x, char in enumerate(row):
                draw.text((x * 10, y * 20), char, font=font, fill='white')
        
        self.frames.append(img)

    def save_gif(self, filename):
        if self.frames:
            self.frames[0].save(filename, 
                              save_all=True, 
                              append_images=self.frames[1:], 
                              duration=self.frame_duration, 
                              loop=0)
