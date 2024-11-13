import pygame
import sys
import random
import math
import time

# Initialize pygame
pygame.init()

# Set dimensions for a 9:16 aspect ratio canvas
canvas_width = 405
canvas_height = 720

# Create the screen directly with canvas dimensions
screen = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Bouncing Music")

# Initialize the mixer for sound playback
pygame.mixer.init()

# Music
# pygame.mixer.Sound('music/314855__modularsamples__yamaha-cs-30l-straight-guitar-c4-straight-guitar-60-127.wav'),
# pygame.mixer.Sound('music/314856__modularsamples__yamaha-cs-30l-straight-guitar-c4-straight-guitar-61-127.wav'),
# pygame.mixer.Sound('music/314857__modularsamples__yamaha-cs-30l-straight-guitar-d4-straight-guitar-62-127.wav'),
# pygame.mixer.Sound('music/314858__modularsamples__yamaha-cs-30l-straight-guitar-d4-straight-guitar-63-127.wav'),
# pygame.mixer.Sound('music/314859__modularsamples__yamaha-cs-30l-straight-guitar-e4-straight-guitar-64-127.wav'),
# pygame.mixer.Sound('music/314860__modularsamples__yamaha-cs-30l-straight-guitar-e4-straight-guitar-65-127.wav'),
# pygame.mixer.Sound('music/314861__modularsamples__yamaha-cs-30l-straight-guitar-f4-straight-guitar-66-127.wav'),
# pygame.mixer.Sound('music/314862__modularsamples__yamaha-cs-30l-straight-guitar-f4-straight-guitar-67-127.wav'),
# pygame.mixer.Sound('music/314863__modularsamples__yamaha-cs-30l-straight-guitar-g4-straight-guitar-68-127.wav'),
# pygame.mixer.Sound('music/314864__modularsamples__yamaha-cs-30l-straight-guitar-a4-straight-guitar-69-127.wav'),
# pygame.mixer.Sound('music/314865__modularsamples__yamaha-cs-30l-straight-guitar-a4-straight-guitar-70-127.wav'),
# pygame.mixer.Sound('music/314866__modularsamples__yamaha-cs-30l-straight-guitar-b4-straight-guitar-71-127.wav'),
# pygame.mixer.Sound('music/314867__modularsamples__yamaha-cs-30l-straight-guitar-c5-straight-guitar-72-127.wav'),
# pygame.mixer.Sound('music/314868__modularsamples__yamaha-cs-30l-straight-guitar-c5-straight-guitar-73-127.wav'),
# pygame.mixer.Sound('music/314869__modularsamples__yamaha-cs-30l-straight-guitar-d5-straight-guitar-74-127.wav'),
# pygame.mixer.Sound('music/314870__modularsamples__yamaha-cs-30l-straight-guitar-d5-straight-guitar-75-127.wav'),
# pygame.mixer.Sound('music/314871__modularsamples__yamaha-cs-30l-straight-guitar-e5-straight-guitar-76-127.wav'),
# pygame.mixer.Sound('music/314872__modularsamples__yamaha-cs-30l-straight-guitar-e5-straight-guitar-77-127.wav'),
# pygame.mixer.Sound('music/314873__modularsamples__yamaha-cs-30l-straight-guitar-f5-straight-guitar-78-127.wav'),
# pygame.mixer.Sound('music/314874__modularsamples__yamaha-cs-30l-straight-guitar-f5-straight-guitar-79-127.wav'),
# pygame.mixer.Sound('music/314875__modularsamples__yamaha-cs-30l-straight-guitar-g5-straight-guitar-80-127.wav'),
# pygame.mixer.Sound('music/314876__modularsamples__yamaha-cs-30l-straight-guitar-a5-straight-guitar-81-127.wav'),
# pygame.mixer.Sound('music/314877__modularsamples__yamaha-cs-30l-straight-guitar-a5-straight-guitar-82-127.wav'),
# pygame.mixer.Sound('music/314878__modularsamples__yamaha-cs-30l-straight-guitar-b5-straight-guitar-83-127.wav'),
# pygame.mixer.Sound('music/314879__modularsamples__yamaha-cs-30l-straight-guitar-c6-straight-guitar-84-127.wav'),

themes = {
    "Prometheus_4": {
        "sounds": [
            pygame.mixer.Sound('music/314863__modularsamples__yamaha-cs-30l-straight-guitar-g4-straight-guitar-68-127.wav'),
            pygame.mixer.Sound('music/314864__modularsamples__yamaha-cs-30l-straight-guitar-a4-straight-guitar-69-127.wav'),
            pygame.mixer.Sound('music/314866__modularsamples__yamaha-cs-30l-straight-guitar-b4-straight-guitar-71-127.wav'),
            pygame.mixer.Sound('music/314856__modularsamples__yamaha-cs-30l-straight-guitar-c4-straight-guitar-61-127.wav'),
            pygame.mixer.Sound('music/314859__modularsamples__yamaha-cs-30l-straight-guitar-e4-straight-guitar-64-127.wav'),
            pygame.mixer.Sound('music/314861__modularsamples__yamaha-cs-30l-straight-guitar-f4-straight-guitar-66-127.wav'),
            pygame.mixer.Sound('music/314875__modularsamples__yamaha-cs-30l-straight-guitar-g5-straight-guitar-80-127.wav'),
        ],
        "color_palette": [
            (247, 160, 200),
            (239, 152, 200),
            (255, 205, 191),
            (220, 139, 197),
            (255, 213, 196),
            (119, 95, 173),
            (255, 186, 196),
            (255, 200, 192),
            (168, 118, 187),
            (243, 174, 195),
            (113, 91, 164),
            (255, 164, 201),
            (255, 191, 194),
            (212, 136, 195),
            (255, 218, 187),
            (255, 215, 188),
            (255, 182, 197),
            (255, 196, 193),
            (203, 132, 194),
            (118, 98, 177),
            (243, 167, 197),
            (255, 225, 186),
            (150, 111, 183),
            (134, 105, 180),
            (245, 184, 193),
        ]
    },
    "Prometheus_5": {
        "sounds": [
            pygame.mixer.Sound('music/314867__modularsamples__yamaha-cs-30l-straight-guitar-c5-straight-guitar-72-127.wav'),
            pygame.mixer.Sound('music/314869__modularsamples__yamaha-cs-30l-straight-guitar-d5-straight-guitar-74-127.wav'),
            pygame.mixer.Sound('music/314871__modularsamples__yamaha-cs-30l-straight-guitar-e5-straight-guitar-76-127.wav'),
            pygame.mixer.Sound('music/314874__modularsamples__yamaha-cs-30l-straight-guitar-f5-straight-guitar-79-127.wav'),
            pygame.mixer.Sound('music/314876__modularsamples__yamaha-cs-30l-straight-guitar-a5-straight-guitar-81-127.wav'),
            pygame.mixer.Sound('music/314877__modularsamples__yamaha-cs-30l-straight-guitar-a5-straight-guitar-82-127.wav'),
            pygame.mixer.Sound('music/314879__modularsamples__yamaha-cs-30l-straight-guitar-c6-straight-guitar-84-127.wav'),
        ],
        "color_palette": [
            (247, 160, 200),
            (239, 152, 200),
            (255, 205, 191),
            (220, 139, 197),
            (255, 213, 196),
            (119, 95, 173),
            (255, 186, 196),
            (255, 200, 192),
            (168, 118, 187),
            (243, 174, 195),
            (113, 91, 164),
            (255, 164, 201),
            (255, 191, 194),
            (212, 136, 195),
            (255, 218, 187),
            (255, 215, 188),
            (255, 182, 197),
            (255, 196, 193),
            (203, 132, 194),
            (118, 98, 177),
            (243, 167, 197),
            (255, 225, 186),
            (150, 111, 183),
            (134, 105, 180),
            (245, 184, 193),
        ]
    },
    "Chinese_4": {
        "sounds": [
            pygame.mixer.Sound('music/314863__modularsamples__yamaha-cs-30l-straight-guitar-g4-straight-guitar-68-127.wav'),
            pygame.mixer.Sound('music/314866__modularsamples__yamaha-cs-30l-straight-guitar-b4-straight-guitar-71-127.wav'),
            pygame.mixer.Sound('music/314856__modularsamples__yamaha-cs-30l-straight-guitar-c4-straight-guitar-61-127.wav'),
            pygame.mixer.Sound('music/314857__modularsamples__yamaha-cs-30l-straight-guitar-d4-straight-guitar-62-127.wav'),
            pygame.mixer.Sound('music/314862__modularsamples__yamaha-cs-30l-straight-guitar-f4-straight-guitar-67-127.wav'),
            pygame.mixer.Sound('music/314875__modularsamples__yamaha-cs-30l-straight-guitar-g5-straight-guitar-80-127.wav'),
        ],
        "color_palette": [
            (48, 48, 49),
            (124, 68, 64),
            (129, 123, 115),
            (236, 60, 53),
            (86, 58, 55),
            (161, 82, 77),
            (234, 230, 217),
            (61, 70, 78),
            (90, 87, 82),
            (244, 162, 64),
            (170, 183, 197),
            (233, 160, 186),
            (144, 148, 173),
            (93, 100, 115),
        ],
    },
    "Chinese_5": {
        "sounds": [
            pygame.mixer.Sound('music/314867__modularsamples__yamaha-cs-30l-straight-guitar-c5-straight-guitar-72-127.wav'),
            pygame.mixer.Sound('music/314871__modularsamples__yamaha-cs-30l-straight-guitar-e5-straight-guitar-76-127.wav'),
            pygame.mixer.Sound('music/314873__modularsamples__yamaha-cs-30l-straight-guitar-f5-straight-guitar-78-127.wav'),
            pygame.mixer.Sound('music/314875__modularsamples__yamaha-cs-30l-straight-guitar-g5-straight-guitar-80-127.wav'),
            pygame.mixer.Sound('music/314878__modularsamples__yamaha-cs-30l-straight-guitar-b5-straight-guitar-83-127.wav'),
            pygame.mixer.Sound('music/314879__modularsamples__yamaha-cs-30l-straight-guitar-c6-straight-guitar-84-127.wav'),
        ],
        "color_palette": [
            (48, 48, 49),
            (124, 68, 64),
            (129, 123, 115),
            (236, 60, 53),
            (86, 58, 55),
            (161, 82, 77),
            (234, 230, 217),
            (61, 70, 78),
            (90, 87, 82),
            (244, 162, 64),
            (170, 183, 197),
            (233, 160, 186),
            (144, 148, 173),
            (93, 100, 115),
        ],
    },
}


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
inner_radius = 190           # Inner radius to keep it circular

last_color = (0, 0, 0)
rotation_angle = 0  # Rotation angle for the segments
rotation_speed = 0.5  # Speed of rotation, adjust for faster/slower rotation

last_time = time.time()  # Record the starting time
interval = 60  # Interval in seconds

font = pygame.font.Font(None, 36)  # You can replace None with a font path

# Function to draw a filled segmented circle with rotation


def draw_rotating_segmented_circle(surface, center, outer_radius, inner_radius, num_segments, colors, rotation_angle):
    angle_per_segment = 360 / num_segments
    for i in range(num_segments):
        # Calculate start and end angles for the segment, adjusted by rotation
        start_angle = math.radians(i * angle_per_segment + rotation_angle)
        end_angle = math.radians((i + 1) * angle_per_segment + rotation_angle)

        # Calculate the points for the segment as a quadrilateral
        points = [
            (center[0] + inner_radius * math.cos(start_angle), center[1] + inner_radius * math.sin(start_angle)),
            (center[0] + outer_radius * math.cos(start_angle), center[1] + outer_radius * math.sin(start_angle)),
            (center[0] + outer_radius * math.cos(end_angle), center[1] + outer_radius * math.sin(end_angle)),
            (center[0] + inner_radius * math.cos(end_angle), center[1] + inner_radius * math.sin(end_angle))
        ]

        # Draw the filled polygon segment
        pygame.draw.polygon(surface, colors[i], points)


def random_color():
    color = random.choice(color_palette)
    if color != last_color:
        return color
    last_color_index = color_palette.index(color)
    if last_color_index + 1 > len(color_palette):
        return color_palette[0]
    return color_palette[last_color_index + 1]


# initial startup
theme_list = list(themes.keys())
print(theme_list)
theme = random.choice(theme_list)
current_theme = theme
theme = themes[theme]
segment_sounds = theme["sounds"]
segment_colors = theme["color_palette"]
color_palette = theme["color_palette"]
num_segments = len(theme["sounds"])

text = current_theme.split("_")[0]
text_surface = font.render(text, True, (255, 255, 255))
text_rect = text_surface.get_rect(center=(canvas_width // 2, text_surface.get_height() // 2))

# Main loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current time
    current_time = time.time()

    # Check if 60 seconds have passed
    if current_time - last_time >= interval:
        # Perform the random choice action
        theme_list = list(themes.keys())
        theme_list.remove(current_theme)
        theme = random.choice(theme_list)
        current_theme = theme
        print(f"switching to theme {theme}")
        theme = themes[theme]
        segment_sounds = theme["sounds"]
        segment_colors = theme["color_palette"]
        color_palette = theme["color_palette"]
        num_segments = len(theme["sounds"])

        text = current_theme.split("_")[0]
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(canvas_width // 2, text_surface.get_height() // 2))

        # Reset the timer
        last_time = current_time

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

    screen.blit(text_surface, text_rect)

    # Update the rotation angle
    rotation_angle = (rotation_angle + rotation_speed) % 360

    # Draw the rotating segmented circle
    ring_center = (canvas_width // 2, canvas_height // 2)
    draw_rotating_segmented_circle(screen, ring_center, ring_radius, inner_radius, num_segments, segment_colors, rotation_angle)

    # Apply gravity to the ball's vertical speed
    ball_speed_y += gravity
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Calculate distance from ball center to ring center
    distance_to_center = ((ball_x - ring_center[0]) ** 2 + (ball_y - ring_center[1]) ** 2) ** 0.5

    # Check if the ball hits the inner boundary of the ring
    if distance_to_center + ball_radius > inner_radius:
        # Calculate the angle of collision from the center of the ring to the ball
        dx = ball_x - ring_center[0]
        dy = ball_y - ring_center[1]
        collision_angle = (math.degrees(math.atan2(dy, dx)) - rotation_angle + 360) % 360  # Adjust for rotation

        # Determine which segment was hit
        segment_index = int(collision_angle // (360 / num_segments))
        last_color = random_color()
        segment_colors[segment_index] = last_color

        # Play the sound associated with the collided segment
        segment_sounds[segment_index].play(maxtime=500)

        # Reflect the ball's velocity based on the angle of collision
        direction = pygame.math.Vector2(ball_speed_x, ball_speed_y).reflect(pygame.math.Vector2(dx, dy).normalize())
        ball_speed_x, ball_speed_y = direction.x * abs(bounce_factor), direction.y * abs(bounce_factor)

        # Position the ball right at the edge of the ring to prevent sticking
        ball_x = ring_center[0] + (inner_radius - ball_radius) * (dx / distance_to_center)
        ball_y = ring_center[1] + (inner_radius - ball_radius) * (dy / distance_to_center)

        # If the bounce speed is too low, apply a big bounce
        if abs(ball_speed_y) < min_bounce_speed:
            ball_speed_y = big_bounce_speed

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Add a small delay to slow down the loop
    pygame.time.delay(10)
