import pygame 

pygame.init()

screen = pygame.display.set_mode ((600 , 600))
pygame.display.set_caption('Key detector')

font = pygame.font.Font(None, 40)
text = font.render('Press a key', True, (255, 255, 255))

exit_font = pygame.font.Font(None, 40 )
exit_text = exit_font.render('You pressed the X. Goodbye!' , True, (255, 0, 0) )




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen.fill((0, 0 , 0))
            screen.blit(exit_text,(0,15))
            pygame.display.update()
            pygame.time.wait(3000)
            running = False 
          
        
        elif event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            text = font.render (f'You pressed: {key_name} ', True, (255,255,255) )

    screen.fill((0, 0 , 255))
    screen.blit(text,(0,15))
    pygame.display.update()



pygame.quit()
 