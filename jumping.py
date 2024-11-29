"""Create a jumping game where a rectangle jumps over barriers that spawn at random.

Requirements:
Import pygame
Screen (width bigger than height)
Character: black rectangle
Automatic Movement
Jumping Movement: use space bar (Must be high enough to jump over barriers)
barriers: black triangles (must spawn at random)
Add barriers as game progresses
position: bottom of the screen
Death (collision)
Points
    text: Add point each time you jump over a barrier
Restart

Pseudocode:
import module
pygame.init()

Screen size = (700 x 500)
Background color = green

screen = display(screen_size, color)

character_size = (10x10)
character_pos = (0, 450)
character = rect(size, position)

character.display(character, black)

Figure out how to make movement automatiic

character_keys = space bar

barriers_size = (7x7)
barriers_pos = (0, 450)
barriers_rand = random.randint(random position at the bottom of the screen)

add a barrier as game progresses

barriers = triangle(size, position)

barriers.display(barriers, black)

Add points: Text (points) (number)
    Add points each time you jump over barriers
    Start at zero

when character hits barrier restart game and points to zero"""

import pygame
from jumping_barrier import Barrier

pygame.init()

CLOCK = pygame.time.Clock()

# SCREEN
screen = pygame.display.set_mode((500,300))
pygame.display.set_caption("Jump Man")


# Character
char_w = 30
char_h = 40

char_size = (char_w,char_h)

char_x = 25
char_y = 230

char_pos = (char_x, char_y)
char_rect = pygame.Rect(char_pos, char_size)

# Platform
platform_size = (500,30)

platform_x = 0
platform_y = 270

platform_pos = (platform_x, platform_y)
platform_rect = pygame.Rect(platform_pos, platform_size)

# Ground Level
ground = 230

# Jumping
jumping = False # Store whether we are jumping. False by default because we are not jumping

gravity = 0.9

jump_height = 15 # How high we jump

velocity_y = jump_height # The speed at which we are jumping

# Barriers: these are moving in the negative direction on the x-axis
barriers = Barrier(ground)

# SPEED
speed = 5

# Running Loop
running = True

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("green")

    # RENDER YOUR GAME HERE

    # Platform
    pygame.draw.rect(screen, "black", platform_rect)

    # Keys
    keys = pygame.key.get_pressed() # Returns a dictionary of all the keys that you can press and whether or not your pressing them

    if keys[pygame.K_SPACE] and char_y >= ground:
        jumping = True

    if jumping:
        char_y += velocity_y  # Character is moving upwards
        # Ex: If the y velocity is 20, then our y position would get subtracted by 20, and we would move up 20 pixels.

        velocity_y -= gravity  # Gravity is pulling the character downwards
        # Ex: If the gravity is 1, then the y velocity would get subtracted by 1 pixel.

        if velocity_y < -jump_height:  # Stop jumping when the character reaches the peak of the jump
            jumping = False
            velocity_y = jump_height  # Reset velocity for downward movement

    else:
        velocity_y += gravity
        char_y += velocity_y

        if char_y >= ground:
            char_y = ground
            velocity_y = 0

    # Draw Character and barriers
    pygame.draw.rect(screen, "black", char_rect)

    char_rect.topleft = (char_x, char_y)  # Update character's position

    # Barrier positions
    barriers.barrier1_x -= speed
    # barriers.barrier2_x -= speed

    if barriers.barrier1_x < -barriers.barrier_size1_x:
        barriers.barrier1_x = 500  # or screen_width

    # if barriers.barrier2_x < -barriers.barrier_size2_x:
    #     barriers.barrier2_x = 500

    screen.blit(barriers.barrier1, (barriers.barrier1_x, barriers.ground))  # shows on the screen
    # screen.blit(barriers.barrier2, (barriers.barrier2_x, barriers.ground))

    # flip() the display to put your work on screen
    pygame.display.flip()

    CLOCK.tick(60)

pygame.quit()
