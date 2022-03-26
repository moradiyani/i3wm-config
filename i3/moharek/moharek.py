from urllib.request import urlretrieve
from random import choice
from sys import argv
from os.path import isfile

def random_print(a):
    with open(a) as file:
        text_list = []
        for line in file:
            text_list.append(line.partition('#')[0])
        text_list = [x for x in text_list if x != '']
        text_list = [x for x in text_list if x != '\n']
        print(choice(text_list))
if len(argv) == 1:
    if isfile('/tmp/all'):
        random_print('/tmp/all')
    else:
        try:
            urlretrieve('https://raw.githubusercontent.com/sys113/moharek/main/files/all', '/tmp/all')
            random_print('/tmp/all')
        except:
            print("error , network connection error!")
elif len(argv) == 2:
    try:
        random_print(argv[1])
    except FileNotFoundError:
        print("error , '{0}' file not found!".format(argv[1]))
    except IndexError:
        print("error , please set file in tweo argument and set value to file , simple : python3 moharek.py file!")

else:
    print("error , please send only a argument , simple : python3 moharek.py all ")
