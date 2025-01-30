# main.py
import os
from src.ascii_converter import ASCIIVideoProcessor  # make sure this matches the class name

def main():
    # add print statements for debugging
    print("Starting video processing...")
    
    processor = ASCIIVideoProcessor(style='default', width=160, height=60)
    
    # add video file path verification
    file_name = 'gear_5_reveal'  # replace with your actual video file name
    input_file = f'mp4s_and_gifs\{file_name}.mp4'  # replace with your actual video file name
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return
    else:
        print(f"Processing video: {input_file}")
    
    processor.process_video(
        input_path=input_file,
        output_path= f'{file_name}.gif',
        fps=24
    )
    
    print("Processing complete!")

if __name__ == "__main__":
    main()
