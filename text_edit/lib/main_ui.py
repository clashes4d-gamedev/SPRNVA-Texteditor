import pygame
import lib.colors
import lib.text_renderer

class Ui():
    def __init__(self):
        pass

    def display_filename(self, color, font, font_size, filename, width, height):
        '''Creates a Surface that displays the name of the current file.'''
        file_name_surf = pygame.Surface((width, height))
        file_name_surf.fill(lib.colors.GREY)
        text_rect = lib.text_renderer.Render().render(file_name_surf, width//2 , height - font_size, color, font, font_size, filename, render=False)
        lib.text_renderer.Render().render(file_name_surf, width//2 - text_rect.width//2, height - font_size, color, font, font_size, filename)
        return file_name_surf