from pathlib import Path
from PIL import Image


class ScaleZip:
    def __init__(self, zipname):
        '''
        inits variable
        '''
        self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))

    def process_files(self, filename):
        """ Scale each image in the directory to the given by user size"""
        size = input('Enter image size divided by /(ex: 240/480): ')
        a, b = size.split('/')
        a, b = int(a), int(b)
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((a, b))
            scaled.save(str(filename))


