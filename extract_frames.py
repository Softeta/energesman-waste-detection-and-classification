import os
import cv2

def extract_frames(video_path, output_dir, frame_interval_sec):
    """
    Extract frames from a video and save them as images.

    Args:
        video_path (str): Path to the video file.
        output_dir (str): Directory to save extracted frames.
        frame_interval_sec (int): Interval between frames to save (in seconds).
    """
    cap = cv2.VideoCapture(video_path)
    
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second
    frame_interval = int(fps * frame_interval_sec)  # Convert seconds to frame interval
    
    os.makedirs(output_dir, exist_ok=True)

    frame_count = 0
    saved_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Save frame at the specified interval
        if frame_count % frame_interval == 0:
            output_path = os.path.join(output_dir, f"frame_{frame_count:05d}.jpg")
            cv2.imwrite(output_path, frame)
            print(f"Saved: {output_path}")
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Extraction complete. Saved {saved_count} frames to {output_dir}.")
    
video_file = "/Users/gvmaka/Desktop/energsman_test_video.mp4" # If needed, you can extract directly from stream
output_directory = "frames" 
frame_interval_seconds = 2  # Save a frame every 2 seconds

extract_frames(video_file, output_directory, frame_interval_seconds)