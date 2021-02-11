print('Blake is going to be a fucking millionare')

def say_hi():
    print('Hi!')

say_hi()

def say_hi(name = 'there'):
    print('Hi {}!'.format(name))

say_hi()
say_hi('Jason')

def say_hi(first, last):
    print('Hi {} {}!'.format(first, last))

say_hi('Jane', 'Doe')

def say_hi(first, last):
    print('Hi {} {}!.'.format(first, last))

say_hi(first = 'Jane', last = 'Doe')
say_hi(last = 'Doe', first = 'John')

def get_name():
    """Get and return a name"""
    name = input('What is your name')
    return name

def say_name(name):
    """Say a name"""
    print('Yourname is {}.'.format(name))

def get_and_sayname():
    """Get and display name"""

name = get_name()

say_name(name)
get_and_sayname()


def get_word(word_type):
    """Get a word from a user and return that word."""
    if word_type.lower() == 'adjective':
        a_or_an = 'an'
    else:
        a_or_an = 'a'
    return input(f'Enter a word that is {a_or_an} {word_type}')

def fill_in_the_blanks(noun,verb,adjective):
    """Fills in the blanks and returns a completed story."""
    story = f'In this book you will learn how to {verb} its so easy a {noun} can do it. Trust me, it will be very {adjective}'
    return story

def display_story(story):
    """Displays a story."""
    print()
    print('Here is the story you created. Enjoy!')
    print()
    print(story)



def create_story():
    """Creates a story by capturing the input and displaying a finished story."""
    noun = get_word('noun')
    verb = get_word('verb')
    adjective = get_word('adjective')

    the_story = fill_in_the_blanks(noun, verb, adjective)
    display_story(the_story)

create_story()
