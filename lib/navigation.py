class Navigate:
    def __init__(self) -> None:
        self.file_map = []
        self.line_size = []
        self.cursor_pos = [0, 0]

    def initialize(self, file):
        '''Initializes the class by generating a map of the current file.\n This may not be efficient enough for larger files though.\n If that is the case then i have to rewrite everything to use a generator.'''
        for line in file:
            for character in line:
                self.line_size.append(character)
            self.file_map.append(self.line_size)
            self.line_size = []
        print(self.file_map)
        self.cursor_pos = [0, 0]

    def get_cursor_pos(self):
        '''Gets the current cursor position in the file.'''
        return self.cursor_pos

    def get_current_content(self):
        return self.file_map

    def mv_up(self):
        '''Moves cursor up.'''
        if self.cursor_pos[0] != 0:
            self.cursor_pos[0] -= 1
        else:
            pass

    def mv_down(self):
        '''Moves cursor down.'''
        if self.cursor_pos[1] != len(self.file_map):
            self.cursor_pos[0] += 1
        else:
            self.cursor_pos[0] = 0
            self.cursor_pos[1] = 0

    def mv_left(self):
        '''Moves cursor down.'''
        if self.cursor_pos[1] != 0:
            self.cursor_pos[1] -= 1
        else:
            self.cursor_pos[0] -= 1
            self.cursor_pos[1] = len(self.file_map[self.cursor_pos[0]])

    def mv_right(self):
        '''Moves cursor right.'''
        if self.cursor_pos[1] != len(self.file_map[self.cursor_pos[0]]):
            self.cursor_pos[1] += 1
        else:
            self.cursor_pos[0] += 1
            self.cursor_pos[1] = 0

    def del_character(self):
        '''Delets a charater from the file.'''
        #check if every character in a line is a '' if so remove that line
        self.file_map[self.cursor_pos[0]][self.cursor_pos[1]] = ''

    def write_character(self, character):
        '''Writes the given character to the file.'''
        self.file_map[self.cursor_pos[0]][self.cursor_pos[1]] = str(character)
        if character != '\n':
            self.cursor_pos[1] += 1
        else:
            self.cursor_pos[0] += 1
            self.cursor_pos[1] = 0
