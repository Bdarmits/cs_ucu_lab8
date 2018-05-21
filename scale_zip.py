from zip_processor import *
import os
import sys
from PIL import Image


class ScaleZip(ZipProcessor):
    def __init__(self, filename):
        """
        inherit init from ZipProcessor, change filename
        """
        super().__init__(filename)

    def process_files(self):
        """ Scale each image in the directory to the given by user size """
        size = input('Enter image size divided by /(ex: 240/480): ')
        a, b = size.split('/')
        a, b = int(a), int(b)
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((a, b))
            scaled.save(str(filename))


