import pygame, datetime

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect)

pygame.init()
screen = pygame.display.set_mode((600, 500))
clock = pygame.time.Clock()
done = False

center = (300, 250)

mickey = pygame.image.load("clock.jpg")
right_hand = pygame.image.load("right-hand.png").convert_alpha()
left_hand = pygame.image.load("left-hand.png").convert_alpha()

mickey_rect = mickey.get_rect(center=center)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    screen.fill((255, 255, 255))

    screen.blit(mickey, mickey_rect)

    min_angle = -minutes * 6
    sec_angle = -seconds * 6

    topleft_min = (center[0] - right_hand.get_width() // 2, center[1] - right_hand.get_height() // 2)
    topleft_sec = (center[0] - left_hand.get_width() // 2, center[1] - left_hand.get_height() // 2)

    blitRotateCenter(screen, right_hand, topleft_min, min_angle)
    blitRotateCenter(screen, left_hand, topleft_sec, sec_angle)

    pygame.display.flip()
    clock.tick(60)
