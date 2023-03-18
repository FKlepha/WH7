import pygame
import sys
import time
import random

difficulty = 10
WIN_quantity = 20
frame_size_x = 720
frame_size_y = 480

pygame.display.set_caption('Snake v1.0')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
orange = pygame.Color(255, 128, 0)

fps_controller = pygame.time.Clock()

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
wall_body = [[100, 50], [90, 50], [80, 50]]


food_pos_1 = [random.randrange(1, (frame_size_x // 10)) * 10,
              random.randrange(1, (frame_size_y // 10)) * 10]
food_spawn_1 = False

food_pos_2 = [random.randrange(1, (frame_size_x // 10)) * 10,
              random.randrange(1, (frame_size_y // 10)) * 10]
food_spawn_2 = False

food_pos_3 = [random.randrange(1, (frame_size_x // 10)) * 10,
              random.randrange(1, (frame_size_y // 10)) * 10]
food_spawn_3 = False

wall_pos_1 = [random.randrange(1, (frame_size_x // 10)) * 10,
              random.randrange(1, (frame_size_y // 10)) * 10]
wall_spawn_1 = False

wall_pos_2 = [random.randrange(1, (frame_size_x // 10)) * 10,
              random.randrange(1, (frame_size_y // 10)) * 10]
wall_spawn_2 = False

wall_pos_3 = [random.randrange(1, (frame_size_x // 10)) * 10,
              random.randrange(1, (frame_size_y // 10)) * 10]
wall_spawn_3 = False

direction = 'RIGHT'
change_to = direction

score = 0
pygame.init()


def game_over():
    my_font = pygame.font.SysFont('arial', 60)

    game_over_surface = my_font.render('GAME OVER', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(1)

    game_over_surface = my_font.render('FATLLIYT', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 2)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(1)

    my_font = pygame.font.SysFont('arial', 40)
    game_over_surface = my_font.render(f'SCORE: {score}', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 1.5)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(1)
    pygame.quit()
    sys.exit()


def WIN_over():
    my_font = pygame.font.SysFont('arial', 60)

    game_over_surface = my_font.render('CONGRATULATION', True, green)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(1)

    game_over_surface = my_font.render('YOU WIN!!!', True, green)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 2)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(1)

    my_font = pygame.font.SysFont('arial', 40)
    game_over_surface = my_font.render(f'SCORE: {score}', True, green)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x / 2, frame_size_y / 1.5)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(1)
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if change_to == 'UP' and direction != 'DOWN':
        direction = change_to
    if change_to == 'DOWN' and direction != 'UP':
        direction = change_to
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = change_to
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = change_to

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos_1[0] and \
            snake_pos[1] == food_pos_1[1]:
        score += 1
        difficulty += 1
        food_spawn_1 = False

    elif snake_pos[0] == food_pos_2[0] and \
            snake_pos[1] == food_pos_2[1]:
        score += 1
        difficulty += 1
        food_spawn_2 = False

    elif snake_pos[0] == food_pos_3[0] and \
            snake_pos[1] == food_pos_3[1]:
        score += 1
        difficulty += 1
        food_spawn_3 = False
    else:
        snake_body.pop()

    if snake_pos[0] == wall_pos_1[0] and \
       snake_pos[1] == wall_pos_1[1]:
        game_over()

    elif snake_pos[0] == wall_pos_2[0] and \
         snake_pos[1] == wall_pos_2[1]:
        game_over()

    elif snake_pos[0] == wall_pos_3[0] and \
         snake_pos[1] == wall_pos_3[1]:
        game_over()

    if score == WIN_quantity:
        WIN_over()

    if not food_spawn_1:
        food_pos_1 = [random.randrange(1, (frame_size_x // 10)) * 10,
                      random.randrange(1, (frame_size_y // 10)) * 10]
        food_spawn_1 = True
    if not food_spawn_2:
        food_pos_2 = [random.randrange(1, (frame_size_x // 10)) * 10,
                      random.randrange(1, (frame_size_y // 10)) * 10]
        food_spawn_2 = True
    if not food_spawn_3:
        food_pos_3 = [random.randrange(1, (frame_size_x // 10)) * 10,
                      random.randrange(1, (frame_size_y // 10)) * 10]
        food_spawn_3 = True

    game_window.fill(black)
    pygame.draw.rect(game_window, green, pygame.Rect(food_pos_1[0], food_pos_1[1], 10, 10))
    pygame.draw.rect(game_window, green, pygame.Rect(food_pos_2[0], food_pos_2[1], 10, 10))
    pygame.draw.rect(game_window, green, pygame.Rect(food_pos_3[0], food_pos_3[1], 10, 10))

    pygame.draw.rect(game_window, blue, pygame.Rect(wall_pos_1[0], wall_pos_1[1], 10, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(wall_pos_2[0], wall_pos_2[1], 10, 10))
    pygame.draw.rect(game_window, blue, pygame.Rect(wall_pos_3[0], wall_pos_3[1], 10, 10))

    my_font = pygame.font.SysFont('arial', 20)
    game_score_surface = my_font.render(f'score: {score}', True, orange)
    game_score_rect = game_score_surface.get_rect()
    game_score_rect.midtop = (frame_size_x / 15, frame_size_y / 100)
    game_window.blit(game_score_surface, game_score_rect)

    my_font = pygame.font.SysFont('arial', 10)
    game_score_surface = my_font.render(f'fps: {difficulty}', True, orange)
    game_score_rect = game_score_surface.get_rect()
    game_score_rect.midtop = (frame_size_x / 1.05, frame_size_y / 100)
    game_window.blit(game_score_surface, game_score_rect)


    my_font = pygame.font.SysFont('arial', 10)
    game_score_surface = my_font.render('Design by F_Klepcha', True, red)
    game_score_rect = game_score_surface.get_rect()
    game_score_rect.midtop = (frame_size_x / 1.1, frame_size_y / 1.05)
    game_window.blit(game_score_surface, game_score_rect)

    for pos in snake_body:
        pygame.draw.rect(game_window, white, pygame.Rect(pos[0], pos[1], 9, 9))

    if snake_pos[0] < 0:
        game_over()

    if snake_pos[0] > frame_size_x - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y - 10:
        game_over()

    for block in snake_body[3::]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    pygame.display.update()
    fps_controller.tick(difficulty)