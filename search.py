from AnilistPython import Anilist
import os

anilist = Anilist()

### CLASSES
class Anime:
    def __init__(self, name):
        data = anilist.get_anime(name)
        self.name_romaji = data['name_romaji']
        self.name_english = data['name_english']
        self.genres = data['genres']
        self.episodes = data['airing_episodes']
        self.desc = data['desc']

    def display(self):
        print('Name (Romaji): ' + str(self.name_romaji))
        print('Name (English): ' + str(self.name_english))
        print('Genres: ' + str(self.genres))
        print('Episodes: ' + str(self.episodes))
        print('Description: ' + str(self.desc).replace('<br>', '\n').replace('<i>', '').replace('</i>', ''))

class Manga:
    def __init__(self, name):
        data = anilist.get_manga(name)
        self.name_romaji = data['name_romaji']
        self.name_english = data['name_english']
        self.genres = data['genres']
        self.release_format = data['release_format']
        self.release_status = data['release_status']
        self.volumes = data['volumes']
        self.chapters = data['chapters']
        self.desc = data['desc']
    
    def display(self):
        print('Name (English): ' + str(self.name_english))
        print('Name (Romaji): ' + str(self.name_romaji))
        print('Genres: ' + str(self.genres))
        print('Format: ' + str(self.release_format))
        print('Status: ' + str(self.release_status))
        print('Volumes: ' + str(self.volumes))
        print('Chapters: ' + str(self.chapters))
        print('Description: ' + str(self.desc).replace('<br>', '\n').replace('<i>', '').replace('</i>', ''))

class Character:
    def __init__(self, name):
        data = anilist.get_character(name)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.native_name = data['native_name']
        self.desc = data['desc']
        self.image = data['image']

    def display(self):
        print('First name: ' + str(self.first_name))
        print('Last name: ' + str(self.last_name))
        print('Native name: ' + str(self.native_name))
        print('Description: ' + str(self.desc).replace('<br>', '\n').replace('<i>', '').replace('</i>', ''))
        print('Image: ' + str(self.image))


### USER INTERACTION

# Input
def input_checker(text, options):
    option = int(input(text))
    if option not in options:
        print('Invalid input!')
        return input_checker(text, options)
    else:
        return option

# Creates the list of possible options
def create_list(options):
    options_list = []
    for i in range(len(options)):
        options_list.append('[%s] %s' % (i, options[i]))
    return options_list

# Menu
def menu(options_list):
    correct_options = []
    print("<Rift's Weeb Search>\n")
    options = create_list(options_list)
    for i in range(len(options)):
        correct_options.append(i)
        print(options[i])
    option = input_checker('Your choice: ', correct_options)
    return option

def run():
    option = menu(['Anime', 'Manga', 'Character'])
    os.system('cls' if os.name == 'nt' else 'clear')

    print("<Rift's Weeb Search>\n")
    search = input('Name: ')
    os.system('cls' if os.name == 'nt' else 'clear')

    print("<Rift's Weeb Search>\n")

    if option == 0:
        o = Anime(search)
    elif option == 1:
        o = Manga(search)
    elif option == 2:
        o = Character(search)
    o.display()

run()