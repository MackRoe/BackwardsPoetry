poem = """If you are a dreamer, come in,
If you are a dreamer, a wisher, a liar,
A hope-er, a pray-er, a magic bean buyer…
If you’re a pretender, come sit by my fire
For we have some flax-golden tales to spin.
Come in!
Come in!"""


def lines_printed_backwards(lines):
    '''This function takes in a list of strings containing the lines of your
    poem as arguments and will print the poem lines out in reverse with the
    line numbers reversed. '''
    lines.reverse()
    for line in lines:
        print(line)


def lines_printed_random(lines):
    '''randomly select lines from a list of strings and print them out in
    random order. Repeats are okay and the number of lines printed should be
    equal to the original number of lines in the poem (line numbers don't need
    to be printed). Hint: try using a loop and randint()'''

    random_lines = []
    while len(lines) < 0:
        line = random.choice(lines)
        lines.pop(line)
        random_lines.append(line)
        lines = random_lines
    for line in lines:
        print(line)


def my_own_rearrange():
    pass

# TODO: GET A LIST OF STIRNGS THAT CONTAINS LINES OF POEM


lines = poem.split("\n")

# make prettier output by seperating lines
for line in lines:
    print(line)

# testing Code
print("Backwards Poem:")
lines_printed_backwards(lines)

# print("Randomized Poem:")
# lines_printed_random(lines)
