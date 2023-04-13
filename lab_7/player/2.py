import pygame
pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player")
background = pygame.transform.scale(pygame.image.load('image/player.jpg'), (WIDTH, HEIGHT))
sound = [
    pygame.mixer.Sound("image/These Are The Times.mp3"),
    pygame.mixer.Sound("image/Ring.mp3"),
    pygame.mixer.Sound("image/Sting - Shape Of My Heart.mp3")
]
sound_name = [
    "These Are The Times",
    "Ring",
    "Shape Of My Heart"
]
sound_cnt = 0

myfont = pygame.font.SysFont("Times New Roman", 30)

playmusic = myfont.render("Press Space to play music", True, ('Red'))
nextmusic = myfont.render("Press C to play next music", True, ('Red'))
stopmusic = myfont.render("Press Z to stop music", True, ('Red'))
previousmusic = myfont.render("Press X to play previous music", True, ('Red'))


musis_on = False

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(playmusic, (50, 0))
    screen.blit(nextmusic, (50, 100))
    screen.blit(stopmusic, (50, 200))
    screen.blit(previousmusic, (50, 300))
    screen.blit(myfont.render(f"Music name : {sound_name[sound_cnt]}", True, ('Red')), (50, 400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not musis_on:
                musis_on = True
                sound[sound_cnt].play()
            elif event.key == pygame.K_c:
                musis_on = True
                sound[sound_cnt].stop()
                sound_cnt += 1
                if sound_cnt >= len(sound):
                    sound_cnt = 0
                sound[sound_cnt].play()
            elif event.key == pygame.K_z:
                musis_on = False
                sound[sound_cnt].stop()
            elif event.key == pygame.K_x:
                musis_on = True
                sound[sound_cnt].stop()
                sound_cnt -= 1
                if sound_cnt < 0:
                    sound_cnt = len(sound) - 1
                sound[sound_cnt].play()

    pygame.display.flip()