import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Заголовок и иконка окна
pygame.display.set_caption("Simple")
icon = pygame.image.load("img/download.JPG.jpg")
pygame.display.set_icon(icon)

# Загрузка изображения цели
target_img = pygame.image.load("img/target.png")
target_width = 150
target_height = 150

# Начальная позиция цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Начальный цвет экрана
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Имена и очки игроков
player_names = ["Игрок 1", "Игрок 2"]
player_scores = [0, 0]
current_player = 0

# Шрифт для отображения счета и имен игроков
font = pygame.font.SysFont(None, 36)

# Основной игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Перемещение цели при попадании
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                # Изменение цвета экрана
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                # Увеличение счета текущего игрока
                player_scores[current_player] += 1
                # Переключение на следующего игрока
                current_player = (current_player + 1) % len(player_names)

    # Заполнение экрана новым цветом
    screen.fill(color)

    # Отображение цели
    screen.blit(target_img, (target_x, target_y))

    # Отображение имен и очков игроков
    y_offset = 10
    for i, name in enumerate(player_names):
        score_text = font.render(f"{name}: {player_scores[i]}", True, (255, 255, 255))
        screen.blit(score_text, (10, y_offset))
        y_offset += 40  # Смещение для следующего игрока

    # Обновление экрана
    pygame.display.update()

    # Ограничение кадров в секунду
    clock.tick(30)

# Завершение работы Pygame
pygame.quit()

