import pygame

pygame.init()






#surfaces 
font = pygame.font.Font(None, 30)
white = (255, 255, 255)
text = ""
word = ""
enter_a_word_font = pygame.font.Font(None, 40)
surface_enter_a_word = font.render('Enter a word below: ', True, (255, 255, 255))


screen = pygame.display.set_mode((600 , 400))
pygame.display.set_caption('Word Math Analyzer')

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                    text = text [:-1]
            
            elif event.type == pygame.K_RETURN:
                word = text

                word_length = len(word)
                middle_letter = word_length //2
                first_half = word[:middle_letter]
                second_half = word[middle_letter:]
                
                length_surface = font.render(f'Length: {word_length}', True, white )
                middle_surface = font.render(f'Middle letter: {middle_letter}', True, white )
                first_surface = font.render(f'First half: {first_half}', True, white )
                last_surface = font.render(f'Second half: {second_half}', True, white )

                screen.blit(length_surface, (50,100))
                screen.blit(middle_surface, (50,150))
                screen.blit(first_surface, (50,200))
                screen.blit(last_surface, (50,250))
            else:
                text += event.unicode
                
    screen.fill((100,100, 255))
    
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(surface_enter_a_word, (50, 40))
    pygame.display.update()
    
pygame.quit()