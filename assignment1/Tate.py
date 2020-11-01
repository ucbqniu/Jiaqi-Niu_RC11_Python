# Imports:
# use python --version to check what version of python your standard installation is
# if this is 2.x you will have to use pip3 install otherwise pip install

import csv
import requests
# pip install pillow
from PIL import Image
from io import BytesIO

# Define the ArtTate class, with all attributes that you find usefull
class ArtTate:
    # Define the initialise function accordingly
    def __init__(self, id, width, depth, height, imageUrl, artist):
        # delete pass when you start editing, this is a placeholder keyword to say that nothing happens
        self.id = id
        self.width = width
        self.depth = depth
        self.height = height
        self.imageUrl = imageUrl
        self.artist = artist
        self.imagePath = ''

        if self.width:
            self.width = str(self.width)
        else:
            self.width = 10

        if self.height:
            self.height = str(self.height)
        else:
            self.height = 10

        if self.depth:
            self.depth = str(self.depth)
        else:
            self.depth = 10

    # Define a function that prints a description
    def describe(self):
        # delete pass when you start editing, this is a placeholder keyword to say that nothing happens
        print("artist:" + self.artist, "id:" + self.id, "width:" + str(self.width), "depth:" + str(self.depth), "height:" + str(self.height))

    # implement the get image function that saves the image to the specified folder
    def getImageFile(self):
        # delete pass when you start editing, this is a placeholder keyword to say that nothing happens
        if self.imageUrl:
            response = requests.get(self.imageUrl)
            try:
                im = Image.open(BytesIO(response.content))
            except OSError:
                return None
            path = "Artworks/" + self.artist + "_" + self.id + ".jpg"
            self.imagePath = path
            im.save(path, "JPEG")

artPieces = []
with open("CSVFiles/artwork_data.csv", encoding = 'utf-8-sig') as artFile:
    artReader = csv.DictReader(artFile)

    for row in artReader:
        id = row['id']
        width = row['width']
        height = row['height']
        depth = row['depth']
        imageUrl = row['thumbnailUrl']
        artist = row['artist']
        if width or depth or height:
            artPiece = ArtTate(id, width, depth, height, imageUrl, artist)
            artPieces.append(artPiece)
            print(artist)

for art in artPieces:
    if "Pollock" in art.artist:
        art.getImageFile()


# Read in the rows of the artwork_data.csv file into a list of ArtTate objects

# write a loop that saves all artwork thumbnails of an artist to a specific folder
