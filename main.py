# main.py
from src.ascii_converter import ASCIIVideoProcessor  # Make sure this matches the class name

def main():
    # Add print statements for debugging
    print("Starting video processing...")
    
    processor = ASCIIVideoProcessor(style='default')
    
    # Add video file path verification
    file_name = 'gear_5'
    input_file = f'{file_name}.mp4'  # Replace with your actual video file name
    print(f"Processing video: {input_file}")
    
    processor.process_video(
        input_path=input_file,
        output_path= f'{file_name}.gif',
        fps=24
    )
    
    print("Processing complete!")

if __name__ == "__main__":
    main()
