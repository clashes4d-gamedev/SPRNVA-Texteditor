import pygame
import lib
import sys
import os
pygame.init()

class MainWin:
    def __init__(self) -> None:
        self.win_size = (1280, 720)
        self.win = pygame.display.set_mode(self.win_size, vsync=1, flags=pygame.RESIZABLE)
        pygame.display.set_caption(lib.constants.WINDOWCAPTION)
        self.clock = pygame.time.Clock()

        # Replace this with tk filepath dialog THIS IS TEMPORARY
        self.file_path = os.path.join('res', 'sample_file.txt')
        self.file_name = lib.file.get_filename(self.file_path)

        self.current_file = open(self.file_path)
        self.current_file_lines = self.current_file.read().splitlines()

        self.text_win = pygame.Surface((self.win_size[0], self.win_size[1]))
        self.text_surf = pygame.Surface((self.text_win.get_width(), self.text_win.get_height()))
        self.text_surf.set_colorkey(lib.colors.BLACK)
        self.text_coords = [0, lib.constants.FILENAMEHEIGHT]

    def update(self) -> None:
        lib.navigation.initialize(self.current_file_lines)
        lib.text.init(lib.constants.FONT, lib.constants.FONTSIZE)
        while 1:
            self.win.fill(lib.colors.BLACK)
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4  and not self.text_coords[1] >= lib.constants.FILENAMEHEIGHT + 2:
                        self.text_coords[1] += lib.constants.SCROLLSPEED
                    
                    elif event.button == 5 and not self.text_coords[1] <= -(self.text_surf.get_height() - lib.constants.TEXTREADABILITYBUFFER):
                        self.text_coords[1] -= lib.constants.SCROLLSPEED

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_o and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                        #pass
                        self.file_path = lib.file.ask_filepath()
                        self.current_file = open(self.file_path)
                        self.current_file_lines = self.current_file.read().splitlines()
                        self.file_name = lib.file.get_filename(lib.file.ask_filepath())

                    if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_LCTRL and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                        lib.file.save_file(lib.navigation.get_current_content())
                        #pass

                    if event.key == pygame.K_UP:
                        lib.navigation.mv_up()

                    if event.key == pygame.K_DOWN:
                        lib.navigation.mv_down()

                    if event.key == pygame.K_LEFT:
                        lib.navigation.mv_left()

                    if event.key == pygame.K_RIGHT:
                        lib.navigation.mv_right()

                    # if ctrl and plus is pressed make the text larger
                    if event.key == pygame.K_PLUS and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                        lib.constants.FONTSIZE += 1

                    # if ctrl and minus is pressed make the text smaller
                    if event.key == pygame.K_MINUS and pygame.key.get_mods() & pygame.KMOD_LCTRL:
                        lib.constants.FONTSIZE -= 1

                if event.type == pygame.VIDEORESIZE:
                    self.win_size = (event.w, event.h)
                    self.win = pygame.display.set_mode(self.win_size, vsync=1, flags=pygame.RESIZABLE)
                    self.text_win = pygame.Surface((self.win_size[0], self.win_size[1]))

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            curr_pos_in_txt = lib.navigation.get_cursor_pos() # This will not work you either have to get a font with the same glyph size for each character or get the glyp size for each character dynamically
            current_content = lib.navigation.get_current_content()
            current_character = current_content[curr_pos_in_txt[0]][curr_pos_in_txt[1] - 1]
            pygame.draw.rect(self.text_surf, lib.colors.WHITE,
                            (curr_pos_in_txt[1] * lib.text.get_character_size(current_character.lower())[0],
                             curr_pos_in_txt[0] * lib.constants.FONTSIZE, 2, lib.constants.FONTSIZE))

            file_name_surf = lib.ui.display_filename(lib.colors.WHITE, lib.constants.FONT, 20, self.file_name, self.text_win.get_width(), lib.constants.FILENAMEHEIGHT)

            # enumerates over every line in the given file and then renders it to the screen
            for line_number, line in enumerate(self.current_file_lines):
                lib.text.render(self.text_surf, 0, line_number * lib.constants.FONTSIZE, lib.colors.WHITE, lib.constants.FONT, lib.constants.FONTSIZE, line)

            self.text_win.blit(self.text_surf, (self.text_coords[0], self.text_coords[1]))
            self.text_win.blit(file_name_surf, (0,0))
            self.text_surf.fill(lib.colors.BLACK)

            self.win.blit(self.text_win, (0,0))
            self.text_win.fill(lib.colors.BLACK)

            pygame.display.flip()
            self.clock.tick(lib.constants.FPS)
        self.current_file.close()

if __name__ == '__main__':
    MainWin().update()