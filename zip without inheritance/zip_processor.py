import os
import shutil
import zipfile
from zip_replace import ZipReplace
from scale_zip import ScaleZip

class ZipProcessor:
    def __init__(self, zipname, scale, replace = None):
        """
        called when initing a new instance of ZipProcessor class
        creates attributes zipname, temp_directory, scale, replace
        """
        self.zipname = zipname
        self.scale = scale
        self.replace = replace

    def process_zip(self):
        """
        unzips the given zip, calls process_file method  and zips
        processed files back
        """
        self.unzip_files()
        self.scale.process_files(self.zipname)
        self.zip_files()

    def unzip_files(self):
        """
        unzips files of given zip file
        """
        self.scale.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.scale.temp_directory))

    def zip_files(self):
        """
        zips files of given zip file
        """
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.scale.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        # shutil.rmtree(str(self.temp_directory))