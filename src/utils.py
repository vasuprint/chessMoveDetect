import cv2
import matplotlib.pyplot as plt
import os

def read_video_properties(video_path, show_Image = True):
    """
    Reads and displays the properties of a video file, optionally displaying the first frame.

    Parameters:
    video_path (str): Path to the video file.
    show_image (bool): If True, displays the first frame of the video. Default is True.

    Returns:
    dict: A dictionary containing video properties such as frame count, FPS, and frame dimensions.
    
    Example:
    w,h,c,fps = read_video_properties('data/video.mp4')
    """
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    
    if not ret:
        print('Error: Unable to read video file')
        return None
    
    # Get video properties
    print('Frame can readable:',ret)
    print('Frame shape Width:',frame.shape[0])
    print('Frame shape Height:',frame.shape[1])
    print('Count Frame:',cap.get(cv2.CAP_PROP_FRAME_COUNT), 'frames')
    print('Count FPS:',cap.get(cv2.CAP_PROP_FPS))
    
    if show_Image:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        plt.imshow(frame)
        plt.title('First Frame'); plt.axis('off')
        plt.imshow(frame)
        plt.show()
    
    # Release the VideoCapture object
    cap.release()
    
    return {
            'frame_width': frame.shape[0],
            'frame_height': frame.shape[1],
            'frame_count': cap.get(cv2.CAP_PROP_FRAME_COUNT),
            'fps': cap.get(cv2.CAP_PROP_FPS)
            }
    


def extract_frames(video_file, output_dir, frame_skip=30, rotation=cv2.ROTATE_90_CLOCKWISE, name='frame'):
    """
    Extracts and saves frames from a video file.

    Parameters:
        video_file (str): Path to the input video file.
        output_dir (str): Directory where the frames will be saved.
        frame_skip (int): Number of frames to skip between saves. Defaults to 30.
        rotation (int): Rotation flag for cv2.rotate. Defaults to 90 degrees clockwise.
        name (str): Base name for the saved frames.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_file)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Get the total number of frames in the video
    frame_number = 0

    while cap.isOpened():
        if frame_number >= frame_count:
            print("Reached the end of the video. Exiting ...")
            break

        # Set the current position of the video file to the desired frame number
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Rotate the frame
        frame = cv2.rotate(frame, rotation)

        # Save the frame as an image file
        output_path = f'{output_dir}{name}_{frame_number}.jpg'
        cv2.imwrite(output_path, frame)

        # Increment frame number by the specified frame skip amount
        frame_number += frame_skip

    # Release the video capture object
    cap.release()
