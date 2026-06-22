import pygame
pygame.init()

screen = pygame.display.set_mode ((600,400))
pygame.display.set_caption('Vowel Checker')

font = pygame.font.Font(None, 21)
empty_text = ('The text box is empty.')
instructions = font.render('Welcome! Type a word, then I\'ll detail everything about it! Press enter once done.', True, (255, 255, 255))
border = font.render('..............................................................................................................................................', True, (255, 255, 255))
your_word_here = font.render(' Your word here: ', True, (255, 255, 255))
reset_button_text = font.render('Reset', True, (255, 255, 255))
reset_button_centered = reset_button_text.get_rect(center=(300, 200))


button_left_edge = 240
button_right_edge = 360
button_top_edge = 175
button_bottom_edge = 225



warning = ""
text =  ""
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

        
        elif event.type == pygame.KEYDOWN:
             #start of keydown block
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
                        
                   
                    if letter in consonants:
                        
                        consonant_count += 1
                        length += 1
                        consonants_found += letter
                    
                    if letter in vowels or letter in consonants:
                        warning = ""
                    
                    else: 
                        warning = " ERROR: Only letters A-Z are allowed."
            
                vowels_result = f" Number of vowels: {vowel_count}"
                vowels_displayed = f" Vowels: {vowels_found}"   
                consonants_result = f" Number of consonants: {consonant_count}"
                consonants_displayed = f" Consonants: {consonants_found}"
                length_of_word= f" Length: {length}"

                if text == "":
                    warning = (' ERROR: The text box is empty! Please type a word.')
                    vowels_result = (' Number of vowels: 0')
                    consonants_result = (' Number of consonants: 0')
                    consonants_displayed = (" Consonants: None ")
                    vowels_displayed = " Vowels: None "
                    length_of_word = " Length: 0"
            else:
                text += event.unicode
                #end of keydown block
                

        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            if button_left_edge <= mouse_x <= button_right_edge and button_top_edge <= button_bottom_edge <= 225:
                 vowels_result = (' Number of vowels: 0')
                 consonants_result = (' Number of consonants: 0')
                 consonants_displayed = (" Consonants: None ")
                 vowels_displayed = " Vowels: None "
                 length_of_word = " Length: 0"
                 text  =""
               
             
                
                
              
                
                
                    
                


            

    screen.fill ((40, 50, 65))
    
    pygame.draw.rect(screen, (255,0,10), (240, 175, 120, 50))
    
    typed = font.render(text, True, (255, 255, 255))
    
    length_of_word_displayed = font.render(length_of_word, True, (255, 255, 255))
    vowel_output = font.render(vowels_result, True, (255, 255, 255))
    warning_text = font.render(warning, True, (255, 255, 255))
    vowels_found_surface = font.render (vowels_displayed, True, (255, 255, 255))
    consonants_found_surface = font.render (consonants_displayed, True, (255, 255, 255))
    consonant_output = font.render(consonants_result, True, (255, 255, 255))
    
    
    screen.blit(reset_button_text,reset_button_centered)
    screen.blit (your_word_here, (10,40))
    screen.blit(instructions, (10, 10))
    screen.blit(typed, (124, 40))
    screen.blit(vowels_found_surface, (10, 80))
    screen.blit(vowel_output, (10, 100))
    screen.blit(consonants_found_surface, (10, 120))
    screen.blit(consonant_output, (10, 140))
    screen.blit(length_of_word_displayed, (10, 160))
    screen.blit(warning_text, (10, 240 ))
    screen.blit(border, (10,15))

    pygame.display.update()

