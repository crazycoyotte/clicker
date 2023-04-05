import constant as cst
import pygame

# intialisation pygame
pygame.init()

# window creation
window = pygame.display.set_mode((cst.WIDTH, cst.HEIGHT))
click_area = pygame.Rect((cst.WIDTH / 2, 0, cst.WIDTH / 2, cst.HEIGHT))

# font
font_score = pygame.font.Font(f"{cst.FONT}HIGH SPEED.ttf", 48)

# setting default variables
damage = 1
score = 0
running = True
timer = 0

# Draw on the screen
text_surface = font_score.render(f"Score : {score}", True, cst.WHITE)
window.fill(cst.BLACK)
window.blit(text_surface, (cst.WIDTH / 50, cst.HEIGHT / 50))

# Update screen
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Set mouse click
        left_click, middle_click, right_click = pygame.mouse.get_pressed()

        # If left click is on click area
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("click detected")
            score += damage


        """if timer == 10:
            timer = 0
            score += damage
        else:
            timer += 1"""

        text_surface = font.render(f"Score : {score}", True, cst.WHITE)

        # Draw on the screen
        window.fill(cst.BLACK)
        window.blit(text_surface, (cst.WIDTH / 50, cst.HEIGHT / 50))

        # Update screen
        pygame.display.update()