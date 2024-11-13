import pygame
import sys
import random
import math

# Initialize pygame
pygame.init()

# Set dimensions for a 9:16 aspect ratio canvas
canvas_width = 405
canvas_height = 720

# Create the screen directly with canvas dimensions
screen = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Bouncing Ball with Segment Sounds")

# Initialize the mixer for sound playback
pygame.mixer.init()

# Load sound files for each segment (replace 'noteX.wav' with actual sound file paths)
segment_sounds = [
    pygame.mixer.Sound('music/314819__modularsamples__yamaha-cs-30l-space-bass-c4-space-bass-60-127.wav'),
    pygame.mixer.Sound('music/314820__modularsamples__yamaha-cs-30l-space-bass-c4-space-bass-61-127.wav'),
    # pygame.mixer.Sound('music/314821__modularsamples__yamaha-cs-30l-space-bass-d4-space-bass-62-127.wav'),
    pygame.mixer.Sound('music/314822__modularsamples__yamaha-cs-30l-space-bass-d4-space-bass-63-127.wav'),
    # pygame.mixer.Sound('music/314823__modularsamples__yamaha-cs-30l-space-bass-e4-space-bass-64-127.wav'),
    # pygame.mixer.Sound('music/314824__modularsamples__yamaha-cs-30l-space-bass-e4-space-bass-65-127.wav'),
    pygame.mixer.Sound('music/314825__modularsamples__yamaha-cs-30l-space-bass-f4-space-bass-67-127.wav'),
    pygame.mixer.Sound('music/314826__modularsamples__yamaha-cs-30l-space-bass-g4-space-bass-68-127.wav'),
    pygame.mixer.Sound('music/314827__modularsamples__yamaha-cs-30l-space-bass-a4-space-bass-69-127.wav'),
    # pygame.mixer.Sound('music/314828__modularsamples__yamaha-cs-30l-space-bass-a4-space-bass-70-127.wav'),
    # pygame.mixer.Sound('music/314829__modularsamples__yamaha-cs-30l-space-bass-b4-space-bass-71-127.wav'),
    pygame.mixer.Sound('music/314822__modularsamples__yamaha-cs-30l-space-bass-d4-space-bass-63-127.wav'),  # Dupe
]

# Ball settings
ball_radius = 20
ball_color = (255, 255, 255)  # White color for the ball
ball_x = canvas_width // 2  # Center X on the canvas
ball_y = canvas_height // 2  # Start in the middle of the canvas
ball_speed_x = 2             # Horizontal speed
ball_speed_y = 0             # Initial vertical speed
gravity = 0.1                # Gravity to increase speed over time
bounce_factor = -0.9         # Bounce factor for the ball's bounce off boundaries
min_bounce_speed = 2.0       # Threshold for triggering a big bounce
big_bounce_speed = -10.0     # Speed for the big bounce

# Ring settings
ring_radius = 200            # Radius for the ring boundary
ring_thickness = 10          # Thickness of the ring
num_segments = len(segment_sounds)  # Number of segments in the ring
segment_colors = [
    (210, 253, 255),
    (193, 241, 243),
    (193, 213, 243),
    (227, 238, 255),
    (243, 227, 255),
    (234, 209, 253),
    (251, 209, 253),
    (209, 253, 239),
]

# Helper function to generate a random color


# Main loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

    # Draw the ring in segments
    ring_center = (canvas_width // 2, canvas_height // 2)
    angle_per_segment = 360 / num_segments
    for i in range(num_segments):
        start_angle = i * angle_per_segment
        end_angle = start_angle + angle_per_segment
        pygame.draw.arc(
            screen, segment_colors[i],
            pygame.Rect(ring_center[0] - ring_radius, ring_center[1] - ring_radius, ring_radius * 2, ring_radius * 2),
            math.radians(start_angle), math.radians(end_angle), ring_thickness
        )

    # Apply gravity to the ball's vertical speed
    ball_speed_y += gravity
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Calculate distance from ball center to ring center
    distance_to_center = ((ball_x - ring_center[0]) ** 2 + (ball_y - ring_center[1]) ** 2) ** 0.5

    # Check if the ball hits the inner boundary of the ring
    if distance_to_center + ball_radius > ring_radius:
        # Calculate the angle of collision from the center of the ring to the ball
        dx = ball_x - ring_center[0]
        dy = ball_y - ring_center[1]
        collision_angle = (math.degrees(math.atan2(-dy, dx)) + 360) % 360  # Adjusted for pygame's y-axis direction

        # Determine which segment was hit
        segment_index = int(collision_angle // angle_per_segment)
        segment_colors[segment_index] = random.choice(segment_colors)

        # Play the sound associated with the collided segment
        # segment_sounds[segment_index].play(maxtime=500)
        random.choice(segment_sounds).play(maxtime=500)

        # Reflect the ball's velocity based on the angle of collision
        direction = pygame.math.Vector2(ball_speed_x, ball_speed_y).reflect(pygame.math.Vector2(dx, dy).normalize())
        ball_speed_x, ball_speed_y = direction.x * abs(bounce_factor), direction.y * abs(bounce_factor)

        # Position the ball right at the edge of the ring to prevent sticking
        ball_x = ring_center[0] + (ring_radius - ball_radius) * (dx / distance_to_center)
        ball_y = ring_center[1] + (ring_radius - ball_radius) * (dy / distance_to_center)

        # If the bounce speed is too low, apply a big bounce
        if abs(ball_speed_y) < min_bounce_speed:
            ball_speed_y = big_bounce_speed

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Add a small delay to slow down the loop
    pygame.time.delay(10)
