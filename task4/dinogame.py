import cv2
import numpy as np

# Game settings
WIDTH, HEIGHT = 800, 400
ground_y = 300
dino_x = 100
dino_y = ground_y
dino_radius = 20
jump_speed = 0
gravity = 1
jump_power = -15
is_jumping = False

# Obstacle settings
obstacle_width = 30
obstacle_height = 60
obstacle_x = WIDTH
obstacle_speed = 5

# Score
score = 0
game_over = False

while True:
    # Create blank frame (white background)
    frame = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8) * 255
    
    if not game_over:
        # Handle jump
        if is_jumping:
            jump_speed += gravity
            dino_y += jump_speed
            
            # Land on ground
            if dino_y >= ground_y:
                dino_y = ground_y
                is_jumping = False
                jump_speed = 0
        
        # Move obstacle
        obstacle_x -= obstacle_speed
        
        # Reset obstacle and increase score
        if obstacle_x < -obstacle_width:
            obstacle_x = WIDTH
            score += 1
        
        # Draw ground line
        cv2.line(frame, (0, ground_y + dino_radius), (WIDTH, ground_y + dino_radius), (0, 0, 0), 2)
        
        # Draw dino (circle)
        cv2.circle(frame, (dino_x, dino_y), dino_radius, (0, 255, 0), -1)
        
        # Draw obstacle (rectangle)
        cv2.rectangle(frame, (obstacle_x, ground_y + dino_radius - obstacle_height), 
                     (obstacle_x + obstacle_width, ground_y + dino_radius), (0, 0, 255), -1)
        
        # Check collision
        if (obstacle_x < dino_x + dino_radius and 
            obstacle_x + obstacle_width > dino_x - dino_radius and
            dino_y + dino_radius > ground_y + dino_radius - obstacle_height):
            game_over = True
        
        # Display score
        cv2.putText(frame, f'Score: {score}', (WIDTH - 150, 40), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    else:
        # Game over screen
        cv2.putText(frame, 'GAME OVER', (WIDTH//2 - 150, HEIGHT//2), 
                   cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        cv2.putText(frame, f'Final Score: {score}', (WIDTH//2 - 120, HEIGHT//2 + 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, 'Press R to Restart or Q to Quit', (WIDTH//2 - 250, HEIGHT//2 + 100), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    
    # Show frame
    cv2.imshow('Dino Game', frame)
    
    # Handle key presses
    key = cv2.waitKey(30) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord(' ') and not is_jumping and not game_over:
        is_jumping = True
        jump_speed = jump_power
    elif key == ord('r') and game_over:
        # Restart game
        dino_y = ground_y
        obstacle_x = WIDTH
        score = 0
        game_over = False
        is_jumping = False
        jump_speed = 0

cv2.destroyAllWindows()