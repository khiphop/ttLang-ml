import base64

fun = """
def hello():
    print("hello world")

if __name__ == '__main__':
    hello()
"""

encode = base64.b64encode(fun.encode(encoding="utf-8"))

print(encode)
