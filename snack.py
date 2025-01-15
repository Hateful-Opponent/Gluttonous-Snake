import pygame
import random

start = False
starting = False  #控制游戏是否开始

# 初始化 Pygame
pygame.init()

# 分数
score = 0
score1 = 0

# 设置游戏界面大小、背景颜色和游戏标题
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('贪吃蛇')

# 插入背景图片
a = pygame.image.load(r"package\PHOTO.jpg")
b = pygame.transform.scale(a, (1280, 720))


c = pygame.image.load(r"package\屏幕截图 2023-12-23 010955.png")
d = pygame.transform.scale(c, (1280, 720))
# 设置文字颜色和字体
font_size = 32
font = pygame.font.Font(None, font_size)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

purple = (255,0,255)
# 定义蛇的初始位置、大小和速度
snake_x = 800
snake_y = 300
snake_size = 20
snake_speed = 10
x = 20
# 定义蛇1的初始位置、大小和速度
snake1_x = 100
snake1_y = 300
snake1_size = 20
snake1_speed = 10
x1 = 20

# 是否暂停
is_pause = False

# 定义食物的初始位置和大小
food_x = random.randrange(0, screen_width - snake_size, 20)
food_y = random.randrange(0, screen_height - snake_size, 20)
food_size = 20

# 扣分的食物
shit_x = random.randrange(0, screen_width - snake_size, 20)
shit_y = random.randrange(0, screen_height - snake_size, 20)
shit_size = 20

#墙
wall_x = random.randrange(0, screen_width - snake_size, 20)
wall_y = random.randrange(0, screen_height - snake_size, 20)
wall_size = 20

if ((wall_y <= food_y+120 and food_y>= wall_y) and wall_x == food_x )or ((wall_y <= snake_y+120 and snake_y>= wall_y) and wall_x == snake_x) or ((wall_y <= snake1_y+120 and snake1_y>= wall_y) and wall_x == snake1_x):
    wall_x = random.randrange(0, screen_width - snake_size, 20)
    wall_y = random.randrange(0, screen_height - snake_size, 20)
    wall_size = 20
# 定义蛇的移动方向
snake_direction = 'right'
snake1_direction = 'right'

# 定义一个列表来保存蛇的身体坐标
snake_body = []
snake1_body = []

# 定义一个计时器来控制蛇的移动速度
clock = pygame.time.Clock()

#暂停正在播放的音乐
def pause_music():
    pygame.mixer.music.pause()

#恢复播放暂停的音乐
def unpause_music():
    pygame.mixer.music.unpause()


# 定义一个函数来绘制
def draw(snake_x, snake_y, snake1_x, snake1_y, snake_body, snake1_body, food_x, food_y, shit_x, shit_y, wall_x, wall_y):
    screen.blit(b, (0, 0))
    # 绘制蛇
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, [pos[0], pos[1], snake_size, snake_size])

    for pos in snake1_body:
        pygame.draw.rect(screen, YELLOW, [pos[0], pos[1], snake1_size, snake1_size])
    # 绘制食物
    pygame.draw.rect(screen, RED, [food_x, food_y, food_size, food_size])
    pygame.draw.rect(screen, BLUE, [shit_x, shit_y, shit_size, shit_size])

    #绘制墙
    pygame.draw.rect(screen, purple, [wall_x, wall_y, wall_size, wall_size+120])

    # 绘制文字
    text = font.render(
        "score1:" + str(score1) + "                            press M to listen music.                              score: " + str(score),
        True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (650, screen_height - 20)
    screen.blit(text, text_rect)
    pygame.display.update()


# 更新蛇的身体坐标
def update_snake(snake_x, snake_y):
    snake_body.insert(0, [snake_x, snake_y])
    if len(snake_body) > 1:
        snake_body.pop()
def update_snake1(snake1_x, snake1_y):
    snake1_body.insert(0, [snake1_x, snake1_y])
    if len(snake1_body) > 1:
        snake1_body.pop()


# 判断游戏是否结束
def Game_isEnd(snake_x, snake1_x, screen_width, snake_size, snake_y, snake1_size, snake1_y, screen_height, snake_body,snake1_body):
    if ((snake_x < 0 or snake_x > screen_width - snake_size or snake_y < 0 or snake_y > screen_height - snake_size or [snake_x, snake_y] in snake_body[1:])
            or (snake1_x < 0 or snake1_x > screen_width - snake1_size or snake1_y < 0 or snake1_y > screen_height - snake1_size or [snake1_x, snake1_y] in snake1_body[1:])
            or ([snake_x, snake_y] in snake1_body[0:] or [snake1_x, snake1_y] in snake_body[0:])):
        global start
        start = False

    return start


# 主循环
while True:

    for event in pygame.event.get():

        # 右上角关闭键生效
        if event.type == pygame.QUIT:
            quit()
        #按1开始
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            if starting!=True:
                start = True
                starting = True
        # 处理按键事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'down':
                snake_direction = 'up'
            elif event.key == pygame.K_DOWN and snake_direction != 'up':
                snake_direction = 'down'
            elif event.key == pygame.K_LEFT and snake_direction != 'right':
                snake_direction = 'left'
            elif event.key == pygame.K_RIGHT and snake_direction != 'left':
                snake_direction = 'right'

            if event.key == pygame.K_w and snake1_direction != 'down':
                snake1_direction = 'up'
            elif event.key == pygame.K_s and snake1_direction != 'up':
                snake1_direction = 'down'
            elif event.key == pygame.K_a and snake1_direction != 'right':
                snake1_direction = 'left'
            elif event.key == pygame.K_d and snake1_direction != 'left':
                snake1_direction = 'right'
            #按ESC退出
            elif event.key == pygame.K_ESCAPE:
                quit()

            #监听：按空格暂停
            elif event.key == pygame.K_SPACE:
                if is_pause == False and start == True:
                    is_pause = True
                    font = pygame.font.Font(None, 50)
                    text3 = font.render('press SPACE to continue game', True, WHITE)
                    screen.blit(text3,
                                ((screen_width - text3.get_width()) / 2, (screen_height - text3.get_height()) / 2))
                    pygame.display.update()
                    font = pygame.font.Font(None, 32)
                    # 音乐暂停
                    pause_music()
                else:
                    is_pause = False
                    # 音乐继续
                    unpause_music()
            #监听：R重启
            elif event.key == pygame.K_r:
                if start == False and starting == True:
                    score = 0
                    start = True
                    snake_x = 800
                    snake_y = 300
                    snake_direction = 'right'
                    snake_body = []
                    snake1_x = 100
                    snake1_y = 300
                    snake1_direction = 'right'
                    snake1_body = []
                    score1 = 0

            # 插入音乐
            elif event.key == pygame.K_m:
                pygame.mixer.music.load(r"package\One more night.mp3")
                pygame.mixer.music.play()


            # 扩展2:贪吃蛇手动加速
            elif event.key == pygame.K_LSHIFT:
                x = 60
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                x = 20

    # 按1开始游戏
    if starting == False:
        screen.blit(d, (0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render("Press 1 to start the game", True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (screen_width / 2, screen_height / 2)
        screen.blit(text, text_rect)
        pygame.display.update()
        font = pygame.font.Font(None, 32)

    # 结束游戏
    if start == False and starting == True:
        font = pygame.font.Font(None, 50)
        text1 = font.render('Game Over!', True, WHITE)
        screen.blit(text1, ((screen_width - text1.get_width()) / 2, (screen_height - text1.get_height()) / 2 - 50))
        text = font.render('Score1: ' + str(score1), True, WHITE)
        screen.blit(text, ((screen_width - text.get_width()) / 2, (screen_height - text.get_height()) / 2))
        text3 = font.render('Score: ' + str(score), True, WHITE)
        screen.blit(text3, ((screen_width - text3.get_width()) / 2, (screen_height - text3.get_height()) / 2 + 50))
        text2 = font.render('press R to restart or press ESC to quit', True, WHITE)
        screen.blit(text2, ((screen_width - text2.get_width()) / 2, (screen_height - text2.get_height()) / 2 + 100))
        pygame.display.update()
        font = pygame.font.Font(None, 32)

    # 重新开始（刷新墙）
    if start == False:
        pygame.time.wait(100)
        wall_x = random.randrange(0, screen_width - snake_size, 20)
        wall_y = random.randrange(0, screen_height - snake_size-100, 20)
        wall_size = 20
        continue
    if is_pause == True:
        pygame.time.wait(100)
        continue

    # 移动蛇的方向
    if is_pause == False or start == True:
        if snake_direction == 'up':
            snake_y -= snake_speed
        elif snake_direction == 'down':
            snake_y += snake_speed
        elif snake_direction == 'left':
            snake_x -= snake_speed
        elif snake_direction == 'right':
            snake_x += snake_speed
        if snake1_direction == 'up':
            snake1_y -= snake1_speed
        elif snake1_direction == 'down':
            snake1_y += snake1_speed
        elif snake1_direction == 'left':
            snake1_x -= snake1_speed
        elif snake1_direction == 'right':
            snake1_x += snake1_speed

    # 判断是否吃到食物
    if (snake_x == food_x and snake_y == food_y) or (snake_x == food_x and abs(snake_y - food_y) < snake_size) or (
            snake_y == food_y and abs(snake_x - food_x) < snake_size):
        food_x = random.randrange(0, screen_width - snake_size, 10)
        food_y = random.randrange(0, screen_height - snake_size, 10)
        snake_body.append([snake_x, snake_y])
        score += 1
    if (snake_x == shit_x and snake_y == shit_y) or (snake_x == shit_x and abs(snake_y - shit_y) < snake_size) or (
            snake_y == shit_y and abs(snake_x - shit_x) < snake_size):
        shit_x = random.randrange(0, screen_width - snake_size, 10)
        shit_y = random.randrange(0, screen_height - snake_size, 10)
        snake_body.append([snake_x, snake_y])
        score -= 1

    if (snake1_x == food_x and snake1_y == food_y) or (snake1_x == food_x and abs(snake1_y - food_y) < snake1_size) or (
            snake1_y == food_y and abs(snake1_x - food_x) < snake1_size):
        food_x = random.randrange(0, screen_width - snake1_size, 10)
        food_y = random.randrange(0, screen_height - snake1_size, 10)
        snake1_body.append([snake1_x, snake1_y])
        score1 += 1
    if (snake1_x == shit_x and snake1_y == shit_y) or (snake1_x == shit_x and abs(snake1_y - shit_y) < snake1_size) or (
            snake1_y == shit_y and abs(snake1_x - shit_x) < snake1_size):
        shit_x = random.randrange(0, screen_width - snake1_size, 10)
        shit_y = random.randrange(0, screen_height - snake1_size, 10)
        snake1_body.append([snake1_x, snake1_y])
        score1 -= 1

    # 撞墙
    if (snake1_y >= wall_y-10 and snake1_y <=wall_y+130 ) and (  snake1_x>=wall_x-10  and snake1_x<= wall_x+10 ):
            start = False
    if (snake_y >= wall_y - 10 and snake_y <= wall_y + 130) and (snake_x >= wall_x - 10 and snake_x <= wall_x + 10):
        start = False

    # 更新蛇的身体坐标
    update_snake(snake_x, snake_y)
    update_snake1(snake1_x, snake1_y)

    # 判断游戏是否结束
    a = Game_isEnd(snake_x, snake1_x, screen_width, snake_size, snake_y, snake1_size, snake1_y, screen_height,
                   snake_body, snake1_body)
    if a == False:
        start = a

    # 绘制开始界面
    if starting == True:
        draw(snake_x, snake_y, snake1_x, snake1_y, snake_body, snake1_body, food_x, food_y, shit_x, shit_y, wall_x, wall_y)

    # 控制蛇的移动速度
    clock.tick(x)