import pygame

vec = pygame.math.Vector2


class TextBox:
    def __init__(self, x, y, width, height, bg_color=(125, 125, 125), active_color=(255, 255, 255), text_size=24,
                 text_color=(0, 0, 0), border=0, border_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pos = vec(x, y)
        self.size = vec(width, height)
        self.image = pygame.Surface((width, height))
        self.bg_color = bg_color
        self.active_color = active_color
        self.active = False
        self.text = ""
        self.text_size = text_size
        self.font = pygame.font.SysFont("Times New Roman", self.text_size)
        self.text_color = text_color
        self.border = border
        self.border_color = border_color
        self.numbers = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 1073741913, 1073741914, 1073741915, 1073741916,
                        1073741917, 1073741918, 1073741919, 1073741920, 1073741921, 1073741922]
        self.special = [8, 32]

    def update(self):
        pass

    def draw(self, window):
        if not self.active:
            if self.border == 0:
                self.image.fill(self.bg_color)
            else:
                self.image.fill(self.border_color)
                pygame.draw.rect(self.image, self.bg_color, (
                    self.border, self.border, self.width - self.border * 2, self.height - self.border * 2))
            # rendering text to image
            text = self.font.render(self.text, False, self.text_color)
            # getting size attributes
            text_height = text.get_height()
            # text_width = text.get_width()
            self.image.blit(text, (self.border * 2, (self.height - text_height) // 2))
        else:
            if self.border == 0:
                self.image.fill(self.active_color)
            else:
                self.image.fill(self.border_color)
                pygame.draw.rect(self.image, self.active_color, (
                    self.border, self.border, self.width - self.border * 2, self.height - self.border * 2))

            # rendering text to image
            text = self.font.render(self.text, False, self.text_color)
            # getting size attributes
            text_height = text.get_height()
            text_width = text.get_width()
            if text_width < self.width - self.border * 2:
                self.image.blit(text, (self.border * 2, (self.height - text_height) // 2))
            else:
                self.image.blit(text, (
                    (self.border * 2) + (self.width - text_width - self.border * 4), (self.height - text_height) // 2))

        window.blit(self.image, self.pos)

    def add_text(self, key):

        try:
            # adding numbers
            if key in self.numbers:
                text = list(self.text)
                if key < 100:
                    text.append(str(key - 48))
                elif key == 1073741922:
                    text.append(str(0))
                else:
                    text.append(str(key - 1073741912))
                self.text = ''.join(text)
            # Backspace
            elif key == 8:
                text = list(self.text)
                text.pop()
                self.text = ''.join(text)
            # space bar
            elif key == 32:
                text = list(self.text)
                text.append(' ')
                self.text = ''.join(text)
            # adding letters
            elif chr(key).isalpha():
                text = list(self.text)
                text.append(chr(key))
                self.text = ''.join(text)
                print(self.text)
            else:
                print(key)
        except:
            print(key)

    def check_click(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                self.active = True
            else:
                self.active = False
        else:
            self.active = False

    def return_value(self):
        return self.text
