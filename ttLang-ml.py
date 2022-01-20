# coding: utf-8

import sys
import signal


def exec_script():
    file = sys.argv[1]
    with open(file, encoding='UTF-8') as file_obj:
        content = file_obj.read()

    py_code = replace_content(content)
    exec(py_code)


def replace_content(content):
    maps = {
        'func main():': "if __name__ == '__main__':",
        '//': '#',
        'include': 'import',
        'srclib': 'from',
        'func': "def",
        '_construct_': "__init__",
        'this': "self",
        ':=': "=",
        'elseif': "elif",
        '主函数():': "if __name__ == '__main__':",
        '包含': 'import',
        '源库': 'from',
        '定义方法': "def",
        '构造函数': "__init__",
        '类成员': "self",
        '当': "while",
        '打印': "print",
        '整型': "int",
        '定义类': "class",
    }

    for old in maps:
        new = maps[old]

        content = content.replace(old, new)

    return content


# 自定义信号处理函数
def my_handler(signum, frame):
    global stop
    stop = True
    print("进程被终止")


# 设置相应信号处理的handler
signal.signal(signal.SIGINT, my_handler)
signal.signal(signal.SIGTERM, my_handler)
stop = False

try:
    while True:
        if len(sys.argv) > 1:
            exec_script()
            break

        if stop:
            print("Exit!")
            break

        try:
            x = input("ttLang-ml>")
        except Exception as err:
            print("in error")
            continue

        if x == "exit" or x == "退出":
            print("Exit!")
            break

        if x in globals().keys():
            continue
        try:
            py_code = replace_content(x)
            exec(py_code)
        except Exception as err:
            print("error 1")
except Exception as err:
    print("error 0")
