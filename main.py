import constant as cst
import pygame
import main_menu
import ending

# intialisation pygame
pygame.init()

# window creation
window = pygame.display.set_mode((cst.WIDTH, cst.HEIGHT))
click_area = pygame.Rect((cst.WIDTH / 2, cst.HEIGHT / 3, cst.WIDTH / 2, cst.HEIGHT / 3))

# clock creation
clock = pygame.time.Clock()

# clock start
start_ticks = pygame.time.get_ticks()

# font
txt_font = pygame.font.Font(cst.FONT, 18)
descri_font = pygame.font.Font(cst.FONT, 12)

# setting default variables
damage = 1
score = 0
running = True
timer = 0

bonus1_level = 0
bonus2_level = 0
bonus2_activated = False
bonus3_level = 0
bonus3_activated = False


# Main screen informations :
# bonus1 button area
bonus1_button = txt_font.render("> Add 1 to click <", True, cst.WHITE)
bonus1_button_pos_x = cst.WIDTH / 50
bonus1_button_pos_y = 10 * cst.HEIGHT / 50
bonus1_button_rect = bonus1_button.get_rect(topleft=(bonus1_button_pos_x, bonus1_button_pos_y))
bonus1_description = descri_font.render(f"Actual level : {bonus1_level}", True,
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
bonus2_description = descri_font.render(f"Actual level : {bonus2_level}", True,
                                        cst.WHITE)
bonus2_cost = descri_font.render(f"next level cost : {((bonus2_level + 1) * 20)}", True, cst.WHITE)
window.blit(bonus2_button, bonus2_button_rect)
window.blit(bonus2_description, (cst.WIDTH / 50, (20 * cst.HEIGHT / 50) + bonus2_button.get_height()))
window.blit(bonus2_cost, (cst.WIDTH / 50, (20 * cst.HEIGHT / 50) + bonus2_button.get_height()
                          + bonus2_description.get_height()))

# bonus3 button area
bonus3_button = txt_font.render(f"> click power by {(damage + bonus1_level) ** bonus3_level} <", True, cst.WHITE)
bonus3_button_pos_x = cst.WIDTH / 50
bonus3_button_pos_y = 30 * cst.HEIGHT / 50
bonus3_button_rect = bonus3_button.get_rect(topleft=(bonus3_button_pos_x, bonus3_button_pos_y))
bonus3_description = descri_font.render(f"Actual level : {bonus3_level}", True,
                                        cst.WHITE)
bonus3_cost = descri_font.render(f"next level cost : {((damage + bonus1_level) ** bonus3_level) ** 2}", True, cst.WHITE)
window.blit(bonus3_button, bonus3_button_rect)
window.blit(bonus3_description, (cst.WIDTH / 50, (30 * cst.HEIGHT / 50) + bonus3_button.get_height()))
window.blit(bonus3_cost, (cst.WIDTH / 50, (30 * cst.HEIGHT / 50) + bonus3_button.get_height()
                          + bonus3_description.get_height()))


# Functions
# In-game UI
def draw_on_screen_in_game():

    text_surface = txt_font.render(f"Score : {score}", True, cst.WHITE)
    pygame.draw.rect(window, cst.RED, click_area)
    window.blit(text_surface, (cst.WIDTH / 50, cst.HEIGHT / 50))
    click_damage = 0
    if bonus2_level == 0:
        click_damage = (damage + bonus1_level)
    if bonus2_level > 0:
        click_damage = ((damage + bonus1_level) * (bonus2_level + 1))
    if bonus3_level > 0:
        click_damage = ((damage + bonus1_level) * (bonus2_level + 1)) * (bonus3_level * 20)

    actual_click_damage = descri_font.render(
        f"Actual click value : {click_damage}", True, cst.WHITE)
    window.blit(actual_click_damage, (cst.WIDTH / 50, cst.HEIGHT / 50 + text_surface.get_height()))

    # bonus1
    bonus1_button = txt_font.render(f"> Add {bonus1_level} to click <", True, cst.WHITE)
    bonus1_description = descri_font.render(f"Actual level : {bonus1_level}", True, cst.WHITE)
    bonus1_cost = descri_font.render(f"next level cost : {bonus1_level + 1}", True, cst.WHITE)
    window.blit(bonus1_button, bonus1_button_rect)
    window.blit(bonus1_description, (cst.WIDTH / 50, (10 * cst.HEIGHT / 50) + bonus1_button.get_height()))
    window.blit(bonus1_cost, (cst.WIDTH / 50, (10 * cst.HEIGHT / 50) + bonus1_button.get_height()
                              + bonus1_description.get_height()))

    if bonus2_activated:
        # bonus2
        bonus2_button = txt_font.render(f"> Multiply click by {(bonus2_level + 1)} <", True, cst.WHITE)
        bonus2_description = descri_font.render(f"Actual level : {bonus2_level}", True, cst.WHITE)
        bonus2_cost = descri_font.render(f"next level cost : {((bonus2_level + 1) * 20)}", True, cst.WHITE)
        window.blit(bonus2_button, bonus2_button_rect)
        window.blit(bonus2_description, (cst.WIDTH / 50, (20 * cst.HEIGHT / 50) + bonus2_button.get_height()))
        window.blit(bonus2_cost, (cst.WIDTH / 50, (20 * cst.HEIGHT / 50) + bonus2_button.get_height()
                                  + bonus2_description.get_height()))

    if bonus3_activated:
        # bonus3
        if bonus3_level == 0 :
            bonus3_button = txt_font.render(f"> Multiply click by 1 <", True,
                                            cst.WHITE)
        else :
            bonus3_button = txt_font.render(f"> Multiply click by {bonus3_level * 20} <", True,
                                            cst.WHITE)
        bonus3_description = descri_font.render(f"Actual level : {bonus3_level}", True, cst.WHITE)
        bonus3_cost = descri_font.render(f"next level cost : {(bonus3_level + 1) * (bonus3_level * 200)}", True, cst.WHITE)
        bonus3_next = descri_font.render(f"Next level value : {(bonus3_level + 1) * 20}", True, cst.WHITE)
        window.blit(bonus3_button, bonus3_button_rect)
        window.blit(bonus3_description, (cst.WIDTH / 50, (30 * cst.HEIGHT / 50) + bonus3_button.get_height()))
        window.blit(bonus3_cost, (cst.WIDTH / 50, (30 * cst.HEIGHT / 50) + bonus3_button.get_height()
                                  + bonus3_description.get_height()))
        window.blit(bonus3_next, (cst.WIDTH / 50, (30 * cst.HEIGHT / 50) + bonus3_button.get_height()
                                  + bonus3_description.get_height() * 2))

    # Update screen
    pygame.display.update()

# Main Screen
running = main_menu.print_main_menu(window)
main = True
end = False
draw_on_screen_in_game()
while running:
    while main:
        # Elapsed time
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                end = False
                quit()

            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Set mouse click
            left_click, middle_click, right_click = pygame.mouse.get_pressed()

            # The player click in the click zone
            if event.type == pygame.MOUSEBUTTONDOWN and click_area.collidepoint(mouse_x, mouse_y) and event.button == 1:
                if bonus2_level == 0:
                    score += (damage + bonus1_level)
                if bonus2_level > 0:
                    score += ((damage + bonus1_level) * (bonus2_level + 1))
                if bonus3_level > 0:
                    score += ((damage + bonus1_level) * bonus2_level) * (bonus3_level * 20)

            # The player click on bonus1 zone
            if event.type == pygame.MOUSEBUTTONDOWN and bonus1_button_rect.collidepoint(mouse_x, mouse_y) and \
                    event.button == 1 and score >= (bonus1_level + 1):
                score -= (bonus1_level + 1)
                bonus1_level += 1
                bonus2_activated = True

            if bonus1_level > 0:
                # The player click on bonus2 zone
                if event.type == pygame.MOUSEBUTTONDOWN and bonus2_button_rect.collidepoint(mouse_x, mouse_y) and \
                        event.button == 1 and score >= ((bonus2_level + 1) * 20):
                    score -= ((bonus2_level + 1) * 20)
                    bonus2_level += 1
                    bonus3_activated = True

            # The player click on bonus3 zone
            if event.type == pygame.MOUSEBUTTONDOWN and bonus3_button_rect.collidepoint(mouse_x, mouse_y) and \
                    event.button == 1 and score >= ((bonus3_level + 1) * (bonus3_level * 200)):
                score -= ((bonus3_level + 1) * (bonus3_level * 200))
                bonus3_level += 1

            text_surface = txt_font.render(f"Score : {score}", True, cst.WHITE)

            window.fill(cst.BLACK)
            window.set_alpha(255)

            # print elapsed time
            elapsed_time = txt_font.render(f"Elapsed time : {seconds}", True, cst.WHITE)
            window.blit(elapsed_time, (cst.WIDTH / 2, cst.HEIGHT / 20))

            draw_on_screen_in_game()

            # fps limit
            clock.tick(60)

            if score > 1000000000:
                main = False
                end = True

    if end:
        running = ending.ending_screen(window, seconds)
        if running:
            damage = 1
            score = 0
            running = True
            timer = 0

            bonus1_level = 0
            bonus2_level = 0
            bonus3_level = 0
            end = False
            main = True



