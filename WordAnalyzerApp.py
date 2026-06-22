import pygame
pygame.init()

screen = pygame.display.set_mode ((600,400))
pygame.display.set_caption('Vowel Checker')

font = pygame.font.Font(None, 21)
empty_text = ('The text box is empty.')

instructions = font.render('Welcome! Type a word, then I\'ll detail everything about it! Press enter once done.', True, (255, 255, 255))
border = font.render('..............................................................................................................................................', True, (255, 255, 255))
your_word_here = font.render(' Your word here: ', True, (255, 255, 255))




warning = ""
text = ""
vowels_result = " Number of vowels: 0"
consonants_result = " Number of consonants: 0"
vowels = "aeiouyAEIOUY"
vowels_displayed = " Vowels: None"
consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
consonants_displayed = " Consonants: None"
length_of_word = " Length of word: 0"



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event. type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text [:-1]
        
            elif event.key == pygame.K_RETURN:
                length = 0
                vowels_found = ""
                consonants_found = ""
                vowel_count = 0
                consonant_count = 0 
                
                for letter in text:
                    if letter in vowels :
                       
                        vowel_count += 1
                        length += 1
                        vowels_found += letter
                   
                    vowels_result = f" Number of vowels: {vowel_count}"
                    vowels_displayed = f" Vowels: {vowels_found}"

                    
                    if letter in consonants:
                        length += 1
                        consonant_count += 1
                        consonants_found += letter
                    
                    
                    
                    consonants_result = f" Number of consonants: {consonant_count}"
                    consonants_displayed = f" Consonants: {consonants_found}"
                    
                    length_of_word= f" Length: {length}"

                if text == "":
                    warning = ('The text box is empty! Please type a word.')
                    vowels_result = (' Number of vowels: 0')
                    consonants_result = (' Number of consonants: 0')
                    consonants_displayed = " Consonants: None " 
                    vowels_displayed = " Vowels: None "
                    length_of_word = " Length: 0"
                
                elif text == " ":
                    warning = (' ERROR: Spacebar is an invalid input. Backspace a few times and type a word.')
                    vowels_result = (' Number of vowels: 0')
                    consonants_result = (' Number of consonants: 0')
                    consonants_displayed = " Consonants: None"
                    vowels_displayed = " Vowels: None"
                    length_of_word = " Length: 0 "
                    
                
                else:
                    warning = ""
                    
                


            else:
                text += event.unicode

    screen.fill ((40, 50, 65))
    typed = font.render(text, True, (255, 255, 255))
    
    length_of_word_displayed = font.render(length_of_word, True, (255, 255, 255))
    vowel_output = font.render(vowels_result, True, (255, 255, 255))
    warning_text = font.render(warning, True, (255, 255, 255))
    vowels_found_surface = font.render (vowels_displayed, True, (255, 255, 255))
    consonants_found_surface = font.render (consonants_displayed, True, (255, 255, 255))
    consonant_output = font.render(consonants_result, True, (255, 255, 255))
    
    
    screen.blit (your_word_here, (10,40))
    screen.blit(instructions, (10, 10))
    screen.blit(typed, (124, 40))
    screen.blit(vowels_found_surface, (10, 80))
    screen.blit(vowel_output, (10, 100))
    screen.blit(consonants_found_surface, (10, 120))
    screen.blit(consonant_output, (10, 140))
    screen.blit(length_of_word_displayed, (10, 160))
    screen.blit(warning_text, (10, 210 ))
    screen.blit(border, (10,15))

    pygame.display.update()

