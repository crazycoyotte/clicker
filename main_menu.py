# import
import constant as cst
import pygame


def print_main_menu(window):
    # Font
    game_name_font = pygame.font.Font(cst.FONT, 75)
    button_font = pygame.font.Font(cst.FONT, 24)

    # Print on screen
    window.fill(cst.BLACK)
    game_name = game_name_font.render(f"Clicker Race", True, cst.WHITE)
    window.blit(game_name, (cst.WIDTH / 2 - game_name.get_width() / 2, cst.HEIGHT / 50))

    # Start button area
    start_button = button_font.render("Start", True, cst.WHITE)
    start_button_pos_x = cst.WIDTH / 2 - start_button.get_width() / 2
    start_button_pos_y = cst.HEIGHT / 2
    start_button_rect = start_button.get_rect(topleft=(start_button_pos_x, start_button_pos_y))
    window.blit(start_button, start_button_rect)

    # Quit button area
    quit_button = button_font.render("Quit", True, cst.WHITE)
    quit_button_pos_x = cst.WIDTH / 2 - start_button.get_width() / 2
    quit_button_pos_y = cst.HEIGHT / 2 + quit_button.get_height() * 2
    quit_button_rect = quit_button.get_rect(topleft=(quit_button_pos_x, quit_button_pos_y))
    window.blit(quit_button, quit_button_rect)


    # Update window
    pygame.display.update()
    pygame.display.flip()

    selection_not_made = True

    while selection_not_made:
        for event in pygame.event.get():
            # Quitting the game
            if event.type == pygame.QUIT:
                run = False
                selection_not_made = False

            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Set mouse click
            left_click, middle_click, right_click = pygame.mouse.get_pressed()

            # If click on Start
            if start_button_rect.collidepoint(mouse_x, mouse_y):
                if event.type == pygame.MOUSEBUTTONDOWN and left_click:
                    run = True
                    selection_not_made = False

            # If click on Quit
            if quit_button_rect.collidepoint(mouse_x, mouse_y):
                if event.type == pygame.MOUSEBUTTONDOWN and left_click:
                    run = False
                    selection_not_made = False
    return run