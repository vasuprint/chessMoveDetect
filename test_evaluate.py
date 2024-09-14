# Import the read_video_properties function from the utils module
from src.utils import read_video_properties

def main():
    # Path to your video file
    video_path = 'chessVideo.mp4'
    
    # Call the function and retrieve video properties
    video_properties = read_video_properties(video_path)
    
    # Check and use the returned video properties
    if video_properties is not None:
        print("Video properties have been successfully retrieved:")
        print(video_properties)
    else:
        print("Failed to retrieve video properties.")

if __name__ == "__main__":
    main()
