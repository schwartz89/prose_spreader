def pspread(file):
    f = open(file, 'r')
    content = f.read()
    content = content.replace('. ', '. \n')
    content = content.replace('! ', '! \n')
    content = content.replace('? ', '? \n')
    f = open(file, 'w')
    f.write(content)
#pspread('test.txt')

# functionality to add:
# add support for other filetypes (markup, word) through conditional read statements
# ?make it a toggleable function. (add a second binary arg as to whether you are switching it on or off. Paragraphs are an issue here)
