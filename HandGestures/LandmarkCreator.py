import mediapipe as mp
from mediapipe.tasks.python import vision

# Define the path to your .pbtxt file
model_path = '/absolute/path/to/hand_landmark_tracking_cpu.pbtxt'

# Set up the hand landmarker
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.IMAGE
)

with HandLandmarker.create_from_options(options) as landmarker:
    # Your code to use the landmarker
    pass
