# ASCII Video Converter

A Python-based tool that converts videos into ASCII art animations, with special support for green screen videos.

## Features

- Converts video files to ASCII art GIF animations
- Green screen background removal
- Real-time processing progress tracking
- Multiple ASCII character style options
- Frame-by-frame processing optimization

## Technologies Used

- OpenCV (cv2) for video processing and frame manipulation
- NumPy for efficient array operations
- PIL/Pillow for image creation and GIF generation
- Python for core programming

## Technical Highlights

- Implemented edge detection using Canny algorithm
- Utilized contrast enhancement and motion blur reduction
- Created custom character mapping for grayscale values
- Developed green screen detection and removal
- Optimized performance through selective frame processing

## Installation

1. Clone the repository
2. Install required dependencies:
3. 
```
pip install opencv-python numpy pillow
```

## Usage
```
from src.ascii_converter import ASCIIVideoProcessor
processor = ASCIIVideoProcessor(
width=120,
height=60,
style='default'
)
processor.process_video(
input_path='your_video.mp4',
output_path='output.gif',
fps=24
)
```


## ASCII Style Options
There are three styles that can be chosen
- Default: `@#8&%X+=-:.`
- Dense: `█▓▒░`
- Minimal: `@%#*+=-:.`

## Skills Demonstrated

- Video processing and manipulation
- Image processing algorithms
- Object-oriented programming
- Performance optimization
- File I/O operations
- Real-time progress tracking
- Green screen background removal
- GIF animation creation


## Future Improvements

- Additional ASCII art styles
- Support for more video formats
- Custom character set definition
- Parallel processing for faster conversion
- GUI interface for easier usage

## License

This project is licensed under the MIT License - see the LICENSE file for details.
