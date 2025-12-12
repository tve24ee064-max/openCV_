# Task 2: Webcam and Video Processing

## What I Learned

- Capturing video from webcam using `cv2.VideoCapture(0)`
- Reading frames in a loop with `cam.read()`
- Setting video properties (width, height, FPS)
- Getting video properties with `cam.get()`
- Recording video using `cv2.VideoWriter()`
- Using different video codecs (XVID)
- Handling keyboard input with `cv2.waitKey()`

## Files

- `sample2vdo.py` - Basic webcam capture
- `sample3vdo.py` - Webcam capture with video recording
- `output_video.avi` - Recorded video output

## Key Concepts

### Video Capture
```python
cam = cv2.VideoCapture(0)  # 0 for default webcam
_, frame = cam.read()  # Read one frame
```

### Setting Properties
```python
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cam.set(cv2.CAP_PROP_FPS, 15)
```

### Getting Properties
```python
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cam.get(cv2.CAP_PROP_FPS)
```

### Video Writer
```python
output = cv2.VideoWriter(filename, codec, fps, (width, height))
output.write(frame)  # Write each frame
```

### Bitwise Operations
- `& 0xFF` masks the last 8 bits for cross-platform key code compatibility
- `ord('q')` converts character to ASCII value

## How to Run

Basic webcam:
```bash
python sample2vdo.py
```

Record video (press Q to stop):
```bash
python sample3vdo.py
```
