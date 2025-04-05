import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.mixer.init()
done = False

playlist = ["track1.mp3", "track2.mp3", "track3.mp3"]
index = 0

def play(index):
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()

play(index)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # PLAY/PAUSE
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  # SToP
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:  # NEXT IN QUEUE
                index = (index + 1) % len(playlist)
                play(index)
            elif event.key == pygame.K_b:  # PREVIOUS IN QUEUE
                index = (index - 1) % len(playlist)
                play(index)

    screen.fill((0, 0, 0))
    pygame.display.flip()
