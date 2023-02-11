from Library import Library
import datetime


def make_library():
    while True:
        library_name = input('Enter your library name: ')
        library = Library(library_name)