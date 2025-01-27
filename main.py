# main.py
from src.ascii_converter import ASCIIVideoProcessor  # Make sure this matches the class name

def main():
    # Add print statements for debugging
    print("Starting video processing...")
    
    processor = ASCIIVideoProcessor(
        width=120,
        height=60,
        style='default'
    )
    
    # Add video file path verification
    input_file = 'your_video.mp4'  # Replace with your actual video file name
    print(f"Processing video: {input_file}")
    
    processor.process_video(
        input_path=input_file,
        output_path='output2.gif',
        fps=24
    )
    
    print("Processing complete!")

if __name__ == "__main__":
    main()
