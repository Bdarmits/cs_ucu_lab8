'''
testing module for scale_zip
photos from "filename.zip" will be in unzipped-filename
'''
from scale_zip import *

unziper = ScaleZip('photos.zip')
unziper.process_zip()