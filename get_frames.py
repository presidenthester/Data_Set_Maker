import cv2
import os

# Open the video file
video_file = r"R:\\TemporaryFiles\Desktop\\mariotest.mp4"  # Replace with your video file path
cap = cv2.VideoCapture(video_file)

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Create a directory to save the frames
frame_dir = r"R:\\DataFrames"
os.makedirs(frame_dir, exist_ok=True)

frame_count = 0

# Read and save each frame
while True:
    ret, frame = cap.read()
    
    if not ret:
        break  # End of video
    
    frame_filename = os.path.join(frame_dir, f"frame_{frame_count:04d}.jpg")
    
    # Save the frame as an image
    cv2.imwrite(frame_filename, frame)
    
    frame_count += 1

# Release the video file and close all windows
cap.release()
cv2.destroyAllWindows()

print(f"Saved {frame_count} frames to {frame_dir}")
