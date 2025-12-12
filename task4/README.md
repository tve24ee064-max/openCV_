# Task 4: Dino Game

## What I Learned

- Creating interactive applications with OpenCV
- Implementing game physics (gravity, jumping)
- Collision detection between shapes
- Real-time rendering with numpy arrays
- Handling user input for game controls
- Drawing shapes: circles, rectangles, text
- Game state management

## Files

- `dinogame.py` - Main game script

## Game Features

- **Dino**: Green circle controlled by the player
- **Obstacles**: Red vertical rectangles moving from right to left
- **Score System**: Increments when obstacles are passed
- **Game Over**: Displays when collision occurs
- **Restart**: Press R to restart after game over

## Controls

- **SPACE** - Make the dino jump
- **Q** - Quit the game
- **R** - Restart after game over

## Key Concepts

### Physics
```python
jump_speed += gravity  # Applies gravity
dino_y += jump_speed   # Updates position
```

### Collision Detection
```python
if (obstacle_x < dino_x + dino_radius and 
    obstacle_x + obstacle_width > dino_x - dino_radius and
    dino_y + dino_radius > ground_y + dino_radius - obstacle_height):
    game_over = True
```

### Drawing Functions
```python
cv2.circle(frame, (x, y), radius, color, -1)  # Filled circle
cv2.rectangle(frame, (x1, y1), (x2, y2), color, -1)  # Filled rectangle
cv2.putText(frame, text, (x, y), font, size, color, thickness)  # Text
```

### Creating Blank Images
```python
frame = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8) * 255  # White background
```

## How to Run

```bash
python dinogame.py
```

Press SPACE to jump over obstacles and try to get the highest score!
