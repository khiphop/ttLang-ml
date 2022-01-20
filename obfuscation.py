import sys

file = sys.argv[1]


def create_tt(content):
    maps = {
        'func main():': "if __name__ == '__main__':",
        '//': '#',
        'include': 'import',
        'srclib': 'from',
        'func': "def",
        '_construct_': "__init__",
        'this': "self",
        ':=': "=",
        'elseif': "elif"
    }

    for tt in maps:
        py = maps[tt]

        content = content.replace(py, tt)

    with open('main.tt', 'w') as fw:
        fw.seek(0)
        fw.write(content)


f = open(file, 'r')
content = f.read()

try:
    create_tt(content)
finally:
    f.close()
