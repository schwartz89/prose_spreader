def pspread(file):
    f = open(file, 'r')
    content = f.read()
    scontent = content.replace('. ', '. \n')
    f = open(file, 'w')
    f.write(scontent)