import cv2
import os

class BuildFrames():
    
    def get_clip(self, clip):#file path to video clip
        self.cap = cv2.VideoCapture(clip)
        
        if not self.cap.isOpened():
            print("Error: Could not open video file.")
            exit()
    
    def make_new_dir(self, new_dir):# name of new directory
        
        self.frame_dir = r"R:\\DataFrames\\" + new_dir # Set parent directory
        os.makedirs(self.frame_dir, exist_ok=True)
        
    def make_frames(self):
        
        frame_count = 0

        # Read and save each frame
        while True:
            ret, frame = self.cap.read()
            
            if not ret:
                break  # End of video
            
            frame_filename = os.path.join(self.frame_dir, f"frame_{frame_count:04d}.jpg")
            
            # Save the frame as an image
            cv2.imwrite(frame_filename, frame)
            
            frame_count += 1
        
        # Release the video file and close all windows
        self.cap.release()
        cv2.destroyAllWindows()
        
        print(f"Saved {frame_count} frames to {self.frame_dir}")
        