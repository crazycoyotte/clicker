import constant as cst
import pygame
import main_menu

# intialisation pygame
pygame.init()

# window creation
window = pygame.display.set_mode((cst.WIDTH, cst.HEIGHT))
click_area = pygame.Rect((cst.WIDTH / 2, 0, cst.WIDTH / 2, cst.HEIGHT))

# font
txt_font = pygame.font.Font(cst.FONT, 24)
descri_font = pygame.font.Font(cst.FONT, 12)

# setting default variables
damage = 1
score = 0
running = True
timer = 0

bonus1_level = 0
bonus2_level = 1
bonus3_level = 1
bonus4_level = 1

# Main screen informations :
# bonus1 button area
bonus1_button = txt_font.render("> Add 1 to click <", True, cst.WHITE)
bonus1_button_pos_x = cst.WIDTH / 50
bonus1_button_pos_y = 10 * cst.HEIGHT / 50
bonus1_button_rect = bonus1_button.get_rect(topleft=(bonus1_button_pos_x, bonus1_button_pos_y))
bonus1_description = descri_font.render(f"Actual level : {bonus1_level} - Actual click value : {damage}", True,
                                        cst.WHITE)
bonus1_cost = descri_font.render(f"next level cost : {damage + bonus1_level}", True, cst.WHITE)
window.blit(bonus1_button, bonus1_button_rect)
window.blit(bonus1_description, (cst.WIDTH / 50, (10 * cst.HEIGHT / 50) + bonus1_button.get_height()))

window.blit(bonus1_cost, (cst.WIDTH / 50, (10 * cst.HEIGHT / 50) + bonus1_button.get_height()
                          + bonus1_description.get_height()))

# bonus2 button area
bonus2_button = txt_font.render(f"> Multiply by {bonus2_level} click <", True, cst.WHITE)
bonus2_button_pos_x = cst.WIDTH / 50
bonus2_button_pos_y = 20 * cst.HEIGHT / 50
bonus2_button_rect = bonus2_button.get_rect(topleft=(bonus2_button_pos_x, bonus2_button_pos_y))
bonus2_description = descri_font.render(f"Actual level : {bonus2_level} - Actual click value : {damage}", True,
                                        cst.WHITE)
bonus2_cost = descri_font.render(f"next level cost : {damage * bonus2_level * 10}", True, cst.WHITE)
window.blit(bonus2_button, bonus2_button_rect)
window.blit(bonus2_description, (cst.WIDTH / 50, (20 * cst.HEIGHT / 50) + bonus2_button.get_height()))
window.blit(bonus2_cost, (cst.WIDTH / 50, (20 * cst.HEIGHT / 50) + bonus2_button.get_height()
                          + bonus2_description.get_height()))

# bonus3 button area
bonus3_button = txt_font.render(f"> click power by {bonus3_level} <", True, cst.WHITE)
bonus3_button_pos_x = cst.WIDTH / 50
bonus3_button_pos_y = 30 * cst.HEIGHT / 50
bonus3_button_rect = bonus3_button.get_rect(topleft=(bonus3_button_pos_x, bonus3_button_pos_y))
bonus3_description = descri_font.render(f"Actual level : {bonus3_level} - Actual click value : {damage}", True,
                                        cst.WHITE)
bonus3_cost = descri_font.render(f"next level cost : {damage + 1 ** bonus3_level ** 10}", True, cst.WHITE)
window.blit(bonus3_button, bonus3_button_rect)
window.blit(bonus3_description, (cst.WIDTH / 50, (30 * cst.HEIGHT / 50) + bonus3_button.get_height()))
window.blit(bonus3_cost, (cst.WIDTH / 50, (30 * cst.HEIGHT / 50) + bonus3_button.get_height()
                          + bonus3_description.get_height()))


# Functions
# In-game UI
def draw_on_screen_in_game():
    text_surface = txt_font.render(f"Score : {score}", True, cst.WHITE)
    window.fill(cst.BLACK)
    window.set_alpha(255)
    pygame.draw.rect(window, cst.RED, click_area)
    window.blit(text_surface, (cst.WIDTH / 50, cst.HEIGHT / 50))
    actual_click_damage = descri_font.render(f"Actual click value : {((damage + bonus1_level) * bonus2_level) ** bonus3_level}",
                                             True, cst.WHITE)
    window.blit(actual_click_damage, (cst.WIDTH / 50, cst.HEIGHT / 50 + text_surface.get_height()))

    # bonus1
    bonus1_description = descri_font.render(f"Actual level : {bonus1_level}", True, cst.WHITE)
    bonus1_cost = descri_font.render(f"next level cost : {damage + bonus1_level}", True, cst.WHITE)
    window.blit(bonus1_button, bonus1_button_rect)
    window.blit(bonus1_description, (cst.WIDTH / 50, (10 * cst.HEIGHT / 50) + bonus1_button.get_height()))
    window.blit(bonus1_cost, (cst.WIDTH / 50, (10 * cst.HEIGHT / 50) + bonus1_button.get_height()
                              + bonus1_description.get_height()))

    # bonus2
    bonus2_description = descri_font.render(f"Actual level : {bonus2_level}", True, cst.WHITE)
    bonus2_cost = descri_font.render(f"next level cost : {damage * bonus2_level * 10}", True, cst.WHITE)
    window.blit(bonus2_button, bonus2_button_rect)
    window.blit(bonus2_description, (cst.WIDTH / 50, (20 * cst.HEIGHT / 50) + bonus2_button.get_height()))
    window.blit(bonus2_cost, (cst.WIDTH / 50, (20 * cst.HEIGHT / 50) + bonus2_button.get_height()
                              + bonus2_description.get_height()))

    # bonus3
    bonus3_description = descri_font.render(f"Actual level : {bonus3_level}", True, cst.WHITE)
    bonus3_cost = descri_font.render(f"next level cost : {(damage + 1) ** bonus3_level}", True, cst.WHITE)
    window.blit(bonus3_button, bonus3_button_rect)
    window.blit(bonus3_description, (cst.WIDTH / 50, (30 * cst.HEIGHT / 50) + bonus3_button.get_height()))
    window.blit(bonus3_cost, (cst.WIDTH / 50, (30 * cst.HEIGHT / 50) + bonus3_button.get_height()
                              + bonus3_description.get_height()))

    # Update screen
    pygame.display.update()


# Main Menu
running = main_menu.print_main_menu(window)

draw_on_screen_in_game()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Set mouse click
        left_click, middle_click, right_click = pygame.mouse.get_pressed()

        # The player click in the click zone
        if event.type == pygame.MOUSEBUTTONDOWN and click_area.collidepoint(mouse_x, mouse_y) and event.button == 1:
                score += ((damage + bonus1_level) * bonus2_level) ** bonus3_level

        # Are the bonus activated?
        if score >= 10:
            bonus1_visible = True
        elif score >= 100:
            bonus2_visible = True
        elif score >= 1000:
            bonus3_visible = True
        elif score >= 100:
            bonus4_visible = True

        print(damage, bonus1_level, bonus2_level)
        print((damage + bonus1_level) * bonus2_level)
        # The player click on bonus1 zone
        if event.type == pygame.MOUSEBUTTONDOWN and bonus1_button_rect.collidepoint(mouse_x, mouse_y) and \
                event.button == 1 and score >= (damage + bonus1_level):
            score -= (damage + bonus1_level)
            bonus1_level += 1

        # The player click on bonus2 zone
        if event.type == pygame.MOUSEBUTTONDOWN and bonus2_button_rect.collidepoint(mouse_x, mouse_y) and \
                event.button == 1 and score >= (damage * bonus2_level * 10):
            score -= (damage * bonus2_level * 10)
            bonus2_level += 1

        # The player click on bonus3 zone
        if event.type == pygame.MOUSEBUTTONDOWN and bonus3_button_rect.collidepoint(mouse_x, mouse_y) and \
                event.button == 1 and score >= ((damage + 1) ** bonus3_level):
            score -= ((damage + 1) ** bonus3_level)
            bonus3_level += 1

        text_surface = txt_font.render(f"Score : {score}", True, cst.WHITE)

        draw_on_screen_in_game()
