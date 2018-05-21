'''
testing module for scale_zip
photos from "filename.zip" will be in unzipped-filename
'''
from zip_processor import ZipProcessor
from scale_zip import ScaleZip


scale = ScaleZip('photos.zip')
unziper = ZipProcessor('photos.zip', scale )
unziper.process_zip()