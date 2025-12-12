# Task 5: Image Cartoonification

## What I Learned

- Bilateral filtering for edge-preserving smoothing
- Edge detection using adaptive thresholding
- Combining filtered images with masks
- Understanding sigma parameters (spatial and range)
- Creating artistic effects from photographs

## Files

- `cartoonification.py` - Cartoon effect script
- `cartoon_output1.jpg` - Cartoonified messi image
- `cartoon_output2.jpg` - Cartoonified freedom image

## Key Concepts

### Bilateral Filter
Smooths colors while keeping edges sharp:
```python
color = cv2.bilateralFilter(img, diameter, sigma_color, sigma_space)
```
- `sigma_s` (spatial): Controls blur radius
- `sigma_r` (range): Controls color similarity threshold

### Edge Detection
```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blur = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray_blur, 255, 
                              cv2.ADAPTIVE_THRESH_MEAN_C, 
                              cv2.THRESH_BINARY, 9, 5)
```

### Combining Images
```python
cartoon = cv2.bitwise_and(color, color, mask=edges)
```

## Alternative Techniques

1. **K-Means Color Quantization** - Reduces number of colors
2. **Pencil Sketch** - Creates sketch effect
3. **Stylization** - Built-in cartoon effect
4. **Detail Enhancement** - Enhances image details
5. **Oil Painting** - Multiple bilateral filters

## How to Run

```bash
python cartoonification.py
```

The script will display both original and cartoonified images and save the cartoon versions.

## Parameters to Experiment With

- Bilateral filter: diameter, sigma_color, sigma_space
- Median blur: kernel size
- Adaptive threshold: block size, constant
