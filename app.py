import random

poem = """If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!"""

poem2 = []


def load_poem():
    f = open('poem1.txt', 'r')
    poem1 = f.readlines()
    f.close()
    # testing
    # print(poem1)
    lines = poem1  # .split("\n")
    return lines


def lines_printed_backwards(lines):
    '''This function takes in a list of strings containing the lines of your
    poem as arguments and will print the poem lines out in reverse with the
    line numbers reversed. '''
    lines.reverse()
    numbering = len(lines)
    for i in range(len(lines)):
        line = lines[i]
        print(str(numbering) + " " + line)
        numbering -= 1


def lines_printed_random(lines):
    '''randomly select lines from a list of strings and print them out in
    random order. Repeats are okay and the number of lines printed should be
    equal to the original number of lines in the poem (line numbers don't need
    to be printed). Hint: try using a loop and randint()'''
    # test function is being called correctly
    # print("-lines_printed_random function called-")
    random_lines = []
    # initialize random_lines list
    list_length = len(lines)
    # set list_length as an integer representing the length of the list
    # print("List length is: " + str(list_length))
    # test list_length is set correctly
    while list_length >= 0:
        line = random.choice(lines)
        # test that random choice has been made and assigned
        # print("Randomly chosen line is:" + line)
        random_lines.append(line)

        for line in random_lines:
            print(line)
            list_length -= 1


def my_own_rearrange():
    pass

# TODO: GET A LIST OF STIRNGS THAT CONTAINS LINES OF POEM


lines = poem.split("\n")
more_lines = load_poem()
# make prettier output by seperating lines
# for line in lines:
#     print(line)



# testing Code
def print_backwards_poem(lines):
    print("")
    print("Backwards Poem:")
    lines_printed_backwards(lines)


def print_randomized_poem(lines):
    print("")
    print("Randomized Poem:")
    lines_printed_random(lines)


def get_user_poem(use_own_poem, poem2):
    if use_own_poem:
        # boolean conditional default is True
        number_of_lines = input("How many lines is your poem? ")
        count_lines = 0
        poem_done = None
        while count_lines != number_of_lines:
            if count_lines == 0:
                poem_line = input("Enter the 1st line of your poem: ")
                poem2.append(str(poem_line))
                count_lines += 1
            elif count_lines == int(number_of_lines) - 1:
                poem_line = input("Enter last line of your poem: ")
                poem2.append(poem_line)
                count_lines += 1
                poem_done = True
            elif not poem_done:
                poem_line = input("Enter next line of your poem: ")
                poem2.append(poem_line)
                count_lines += 1
            else:
                print("Your poem is complete.")
                count_lines = number_of_lines
        return poem2

def display_user_poem(poem2):
    for line in poem2:
        print(line)


def use_own_poem():
    get_poem = input("Want to try this with your own poetry?[Y or N] ")
    if get_poem == "Y":
        return True


def poem_check(poem2, use_own_poem):
    print("*** YOUR POEM ***")
    display_user_poem(poem2)
    poem_check = input("How does it look? [A for awesome or X for Oops] ")
    while poem_check != "A" or "X":
        poem_check = input("How does it look? [A for awesome or X for Oops] ")
        if poem_check == "X":
            print("Let's try again")
            get_user_poem(use_own_poem)
        elif poem_check == "A":
            print(" ")
            print("Sweet!")
            return True



print("** Poetry Fun **")
print_backwards_poem(lines)
print_randomized_poem(lines)
print("")
see_next = input("Would you like to see another poem? [Y for yes]")
while see_next != "Y":
    see_next = input("Would you like to see another poem? [Y for yes]")
else:
    load_poem()
    print_backwards_poem(more_lines)
    print_randomized_poem(more_lines)

# allow user to enter their own poetry
use_own_poem()
get_user_poem(use_own_poem, poem2)
poem_check(poem2, use_own_poem)
print_backwards_poem(poem2)
print_randomized_poem(poem2)
