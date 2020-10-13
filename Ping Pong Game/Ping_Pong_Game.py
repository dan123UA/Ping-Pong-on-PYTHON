import pygame,sys,random
pygame. init( )
clock = pygame.time.Clock()


screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

ball = pygame.Rect((screen_width/2 - 10, screen_height/2 - 10 ,20,20))

player = pygame.Rect(screen_width-20,screen_height/2 - 70, 10, 140)
enemy = pygame.Rect(10,screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey8')
white = (200,200,200)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
enemy_speed = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame. quit ( )
            sys. exit()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_DOWN:
                player_speed += 7

        if event.type == pygame.KEYUP :
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_w:
                enemy_speed -= 7
            if event.key == pygame.K_s:
                enemy_speed += 7

        if event.type == pygame.KEYUP :
            if event.key == pygame.K_w:
                enemy_speed += 7
            if event.key == pygame.K_s:
                enemy_speed -= 7

        

        

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y = -ball_speed_y
    if ball.left <= 0 or ball.right >= screen_width:
        ball.center = (screen_width/2, screen_height/2)
        ball_speed_y *= random.choice((1,-1))
        ball_speed_x *= random.choice((1,-1))

    if ball.colliderect(player) or ball.colliderect(enemy) :
        ball_speed_x = -ball_speed_x
        

    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

    enemy.y += enemy_speed
    if enemy.top <= 0:
        enemy.top = 0
    if enemy.bottom >= screen_height:
        enemy.bottom = screen_height

    screen.fill(bg_color)
    pygame.draw.rect(screen,white,player)
    pygame.draw.rect(screen,white,enemy)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (screen_width/2,0), (screen_width/2,screen_height))

    pygame.display.flip()
    clock.tick(60)
