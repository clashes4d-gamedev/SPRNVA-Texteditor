import pygame

class Render:
    def __init__(self) -> None:
        pygame.font.init()
        self.font = None

    def init(self, font, size):
        self.font = self.create_font(font, size)

    def create_font(self, font, size):
        self.font = pygame.font.SysFont(font, size)
        return self.font

    def create_txt(self, color, font, size, text):
        self.font = self.create_font(font, size)
        return self.font.render(text, True, color)

    def get_character_size(self, character):
        return pygame.font.Font.size(self.font, character)
        #return self.font.size(character)

    def render(self, win, posx, posy ,color, font, size, text, render=True):
        '''Creates a TextObject and displays it to the screen.\n Also returns the Bounding box of the Text as a pygame.Rect object.'''
        txt_surf = self.create_txt(color, font, size, text)
        if render:
            win.blit(txt_surf, (posx, posy))
        return txt_surf.get_rect()
