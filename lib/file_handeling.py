import sys
import os
import subprocess

class File:
    def __init__(self) -> None:
        pass

    def get_filename(self, file_path) -> str:
        list_of_files = os.path.split(file_path)
        return list_of_files[-1]

    def save_file(self, content):
        export_path = self.ask_filepath(save=True)
        file = open(export_path, 'w')
        for line in content:
            file.writelines(line)
        file.close()

    def ask_text(self):
        try:
            text = subprocess.check_output(["zenity", "--entry"]).decode("utf-8").strip()
        except subprocess.CalledProcessError:
            sys.exit('A critical error occoured. The programm will close itself now.')
        return text

    def ask_filepath(self, save=False):
        if save:
            try:
                filename = subprocess.check_output(["zenity", "--file-selection", "--save"]).decode("utf-8").strip()
            except subprocess.CalledProcessError:
                sys.exit('A critical error occoured. The programm will close itself now.')
            return filename
        else:
            try:
                filename = subprocess.check_output(["zenity", "--file-selection"]).decode("utf-8").strip()
            except subprocess.CalledProcessError:
                sys.exit('A critical error occoured. The programm will close itself now.')
            return filename
