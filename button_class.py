import pygame
from pygame.locals import *
pygame.init()
vec = pygame.math.Vector2

pygame.display.init()
clicked = False

class Button:
    def __init__(self,  x, y, width, height, color=(0, 0, 0),
                 hover_color= (0,0,0), border=True, border_width=2, border_color=(0, 0, 0,),
                 text='', val = 0, font_name='freesansbold.ttf', text_size=20, text_color=(0, 0, 0), bold_text= False, click_color = (0,0,0)):
        self.val = val
        self.x = x
        self.y = y
        self.pos = vec(x,y)
        self.width = width
        self.height = height
        #self.surface = surface
        self.image = pygame.Surface((width,height))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        #self.state = state
        #self.function = function
        self.color = color
        self.hover_color = hover_color
        self.border = border
        self.border_width = border_width
        self.border_color = border_color
        self.text = text
        self.text_size = text_size
        self.font_name = pygame.font.Font(font_name, self.text_size)

        self.text_color = text_color
        self.bold_text = bold_text
        self.hovered = False
        self.click_color = click_color


    def add_point(self):
        self.val = self.val + 1
        self.text = str(self.val)
       # self.show_text()
        print("point added: ", self.text)

    def get_point(self):
        return  str(self.val)

    def get_num(self):
        return int(self.val)

    def update(self, mouse):
        '''if self.mouse_hovering(pos):
            self.hovered = True
        else:
            self.hovered= False'''
        if self.rect.collidepoint(mouse):
            self.hovered = True
        else:
            self.hovered = False



    def draw(self, window):
        global clicked
        action = False
        #font = pygame.font.Font('freesansbold.ttf', 25)
        font = self.font_name
        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(window, self.click_color, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(window, self.hover_color, button_rect)
        else:
            pygame.draw.rect(window, self.color, button_rect)



        # add shading to button
        white = (255, 255, 255)
        black = (0, 0, 0)
        pygame.draw.line(window, white, (self.x, self.y), (self.x + self.width, self.y), 3)
        pygame.draw.line(window, white, (self.x, self.y), (self.x, self.y + self.height), 3)
        pygame.draw.line(window, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 3)
        pygame.draw.line(window, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 3)

        # add text to button
        text_img = font.render(self.text, True, self.text_color)
        text_len = text_img.get_width()
        text_height = text_img.get_height()
        window.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + int(self.height / 2) - int(text_height / 2)))

        return action





    def show_text(self, text):
        font= pygame.font.SysFont(self.font_name, self.text_size, bold=self.bold_text)
        text = font.render(self.text, False, self.text_color)
        size = text.get_size()

        self.image.blit(text, self.pos)

    def mouse_hovering(self, pos):
        if pos[0] > self.pos[0] and pos[0] < self.pos[0]+self.width:
            if pos[1] > self.pos[1] and pos[1] < self.pos[1]+self.height:
                return True
        return False

