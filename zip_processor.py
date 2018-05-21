import os
import shutil
import zipfile
from pathlib import Path

class ZipProcessor:
    def __init__(self, zipname):
        """
        called when initing a new instance of ZipProcessor class
        creates attributes zipname, temp_directory
        """
        self.zipname = zipname
        self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))

    def process_zip(self):
        """
        unzips the given zip, calls process_files method  and zips
        processed files back
        """
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        """
        unzips files of given zip file
        """
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        """
        zips files of given zip file
        """
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        # shutil.rmtree(str(self.temp_directory))