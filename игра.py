import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 500, 680
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Взырвные лестницы")

# Цвета
WHITE = (102, 255, 178)
GREEN = (51, 0, 102)
RED = (255, 255, 0)
BLUE = (119, 38, 226)

# Настройки
FPS = 30
player_width, player_height = 50, 50
player_velocity = 5
is_jumping = False
jump_count = 10
score = 0
lives = 3

# Генерация платформ
def create_platforms(num_platforms):
    platforms = []
    last_y = HEIGHT - 50  # Начинаем с нижней части окна
    min_height_between_platforms = 80  # Минимальное расстояние между платформами
    max_height = HEIGHT - 100  # Максимальная высота для платформ (не выше 100 пикселей от верхнего края)

    for _ in range(num_platforms):
        x = random.randint(50, WIDTH - 150)

        # Генерация новой платформы ниже последней, но не выше max_height
        if last_y > max_height + min_height_between_platforms:
            y = random.randint(max_height, last_y - min_height_between_platforms)
        else:
            y = last_y - min_height_between_platforms  # Устанавливаем платформу на максимальной высоте

        platform = pygame.Rect(x, y, 100, 10)
        platforms.append(platform)
        last_y = y  # Обновляем y для следующей платформы
    
    platforms.sort(key=lambda p: p.y)  # Сортируем платформы по Y-координате
    return platforms

def create_coins(platforms):
    coins = []
    for platform in platforms:
        for _ in range(2):  # Создаем 2 монетки на платформе
            x = platform.x + random.randint(0, 90)
            y = platform.y - 20  # Генерация монет на высоте выше платформы
            coin_rect = pygame.Rect(x, y, 20, 20)

            # Проверяем, не пересекается ли монета с другими платформами
            if y > 0 and not any(coin_rect.colliderect(p) for p in platforms):
                coins.append(coin_rect)
    return coins

def draw_window(player_rect, platforms, coins, score, lives, win=False):
    WIN.fill(WHITE)

    # Рисуем платформы и монетки
    for platform in platforms:
        pygame.draw.rect(WIN, GREEN, platform)
    for coin in coins:
        pygame.draw.circle(WIN, RED, (coin.x + 10, coin.y + 10), 10)

    # Рисуем игрока
    pygame.draw.rect(WIN, BLUE, player_rect)

    # Рисуем очки и жизни
    font = pygame.font.SysFont('comicsans', 30)
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    WIN.blit(score_text, (10, 10))
    lives_text = font.render(f'Lives: {lives}', True, (0, 0, 0))
    WIN.blit(lives_text, (WIDTH - 150, 10))

    # Показать сообщение о выигрыше
    if win:
        win_text = font.render("You Win! Press R to restart", True, (0, 0, 0))
        WIN.blit(win_text, (WIDTH // 2 - 150, HEIGHT // 2))

    pygame.display.update()

def main():

    global is_jumping, jump_count, score, lives

    run = True
    clock = pygame.time.Clock()
    player_x = WIDTH // 2
    player_y = HEIGHT // 2
    platforms = create_platforms(10)  # Начальные платформы
    coins = create_coins(platforms)  # Создаем монеты на каждой платформе

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    win = False
    collected_platforms = set()  # Для отслеживания собранных платформ

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and player_rect.x - player_velocity > 0:
            player_rect.x -= player_velocity
        if keys[pygame.K_RIGHT] and player_rect.x + player_velocity < WIDTH - player_width:
            player_rect.x += player_velocity

        if not is_jumping:
            if keys[pygame.K_SPACE]:
                is_jumping = True
            if keys[pygame.K_v]:  # Проваливание через платформу (с помощью V)
                for platform in platforms:
                    if player_rect.colliderect(platform) and player_rect.bottom <= platform.bottom:
                        player_rect.y += 20  # Увеличьте значение, чтобы провалиться через платформу
                        break
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                player_rect.y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                is_jumping = False
                jump_count = 10

        # Проверка столкновения с платформами
        on_platform = False

        for index, platform in enumerate(platforms):
            if player_rect.colliderect(platform) and player_rect.bottom - player_rect.height <= platform.top:
                player_rect.bottom = platform.top  # Перемещение игрока на верх платформы
                if index not in collected_platforms:  # Проверяем, что платформа ещё не была собрана
                    score += 100  # Увеличиваем счет при приземлении
                    collected_platforms.add(index)  # Добавляем в собранные платформы
                on_platform = True

        # Проверка на падение вниз
        if player_rect.y > HEIGHT:
            lives -= 1  # Уменьшаем количество жизней
            player_rect.y = HEIGHT // 2  # Возвращаем игрока в стартовую позицию
            player_rect.x = WIDTH // 2

        # Если игрок не на платформе, применяем гравитацию
        if not on_platform:
            player_rect.y += 7  # Применяем гравитацию

        # Проверка на сбор монеток
        for coin in coins[:]:
            if player_rect.colliderect(coin):
                coins.remove(coin)
                score += 50  # Очки за сбор монетки

        # Если монетки собраны, создаем новые платформы и монеты
        if len(coins) == 0:
            platforms.clear()  # Удаляем все старые платформы
            platforms = create_platforms(10)  # Генерируем новые платформы
            coins = create_coins(platforms)  # Создаем новые монеты на новых платформах

        draw_window(player_rect, platforms, coins, score, lives, win)

        # Проверка на выигрыш
        if score >= 10000 and not win:
            win = True

        # Если игра окончена, проверка на перезапуск
        if win and keys[pygame.K_r]:
            score = 0
            lives = 3
            player_rect.x = WIDTH // 2
            player_rect.y = HEIGHT // 2
            platforms = create_platforms(10)  # Начальные платформы
            coins = create_coins(platforms)  # Создаем новые монеты на каждой платформе
            win = False
            collected_platforms.clear()  # Сброс собранных платформ

        # Если жизни исчерпаны, игра заканчивается
        if lives <= 0:
            run = False  # Остановка игры при нулевых жизнях

    pygame.quit()

if __name__ == "__main__":
    main()
# Пример игры с таблицей лидеров
def play_game():
    """Функция, представляющая основную игровую логику."""
    player_name = input("Введите ваше имя: ")

    print(f"{player_name}, вы набрали {score} очков!")
if __name__ == "__main__":
    play_game()
