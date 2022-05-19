from AnilistPython import Anilist

anilist = Anilist()

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
    print("<Rift's Weeb Search>/n")
    options = create_list(options_list)
    for i in range(len(options)):
        correct_options.append(i)
        print(options[i])
    option = input_checker('Your choice: ', correct_options)


# Main Menu
def main_menu():
    menu(['Anime', 'Manga', 'Character'])

main_menu()