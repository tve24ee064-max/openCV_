# Task 1: Basic Image Processing

## What I Learned

- Reading images using `cv2.imread()`
- Converting images to grayscale using `cv2.cvtColor()`
- Displaying images with `cv2.imshow()`
- Saving images with `cv2.imwrite()`
- Accessing and manipulating individual pixels
- Working with color channels
- Creating patterns (chessboard pattern)

## Files

- `sample1.py` - Main image processing script
- `messi.jpg` - Sample image 1
- `freedom.png` - Sample image 2
- `messi_gray.jpg` - Output grayscale image 1
- `freedom_gray.png` - Output grayscale image 2

## Key Concepts

### Image Shape
```python
img.shape  # Returns (height, width, channels)
```

### Pixel Access
```python
img[5, 5]  # Access pixel at row 5, column 5
```

### Color Channels
```python
B = img[:, :, 0]  # Blue channel
G = img[:, :, 1]  # Green channel
R = img[:, :, 2]  # Red channel
```

### Chessboard Pattern
Created a 4x4 chessboard by dividing the image into 16 tiles and alternating black (0,0,0) and white (255,255,255) colors based on the sum of row and column indices.

## How to Run

```bash
python sample1.py
```
