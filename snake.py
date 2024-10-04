import pygame
import random

x = pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

game_width = 500
game_height = 500
game_screen = pygame.display.set_mode((game_width, game_height))

# Load the background image
background_image = pygame.image.load("D:\\background.jpg")
background_image = pygame.transform.scale(background_image, (game_width, game_height))

# Set window caption
pygame.display.set_caption("Snakes with Divyanshu")
pygame.display.update()

# Game-specific variables
exit_game = False
over_game = False
x = 300  # initial position along x-axis
y = 300  # initial position along y-axis
init_velocity = 2
velocity_x = 0
velocity_y = 0
food_x = random.randint(0, game_width - 10)
food_y = random.randint(0, game_height - 10)
score = 0
snake_size = 10  # diameter of circle
fps = 40

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

def text_screen(text, color, a, b):
    screen_text = font.render(text, True, color)
    game_screen.blit(screen_text, [a, b])

def plot_snake(game_screen, color, snk_list, snake_size):
    for i, (a, b) in enumerate(snk_list):
        # Dynamic sizing or color shifting effect
        circle_size = snake_size - (len(snk_list) - i) // 2
        if circle_size < 6:  # Avoid the size getting too small
            circle_size = 6
        pygame.draw.circle(game_screen, color, (a, b), circle_size)

snk_list = []
snk_length = 1

# Initialize mixer module
pygame.mixer.init()

# Load background music
pygame.mixer.music.load(r"D:\\Fluffing-a-Duck(chosic.com).mp3")

# Play background music
pygame.mixer.music.play(-1)  # -1 means loop the music

# Creating game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    x = x + velocity_x
    y = y + velocity_y

    # Add boundary conditions
    if x < 0 or x > game_width - snake_size or y < 0 or y > game_height - snake_size:
        over_game = True
        exit_game = True

    if abs(x - food_x) < 10 and abs(y - food_y) < 10:
        score = score + 1
        food_x = random.randint(0, game_width - snake_size)
        food_y = random.randint(0, game_height - snake_size)
        snk_length += 3  # Increase length by more for a visual effect

    # Draw background image
    game_screen.blit(background_image, (0, 0))

    # Draw food as a circle
    pygame.draw.circle(game_screen, red, (food_x, food_y), snake_size)

    # Display score
    text_screen("Score is = " + str(score * 10),black, 2, 2)

    head = [x, y]
    snk_list.append(head)

    if len(snk_list) > snk_length:
        del snk_list[0]

    # Draw the snake
    plot_snake(game_screen, '#9D00FF', snk_list, snake_size)

    pygame.display.update()
    clock.tick(fps)

# For quitting the game as soon as it overcomes the game loop
if over_game:
    game_screen.fill(red)
    text_screen("Game Over! Press close button to quit.", white, 100, 250)
    pygame.display.update()

pygame.quit()
quit()
