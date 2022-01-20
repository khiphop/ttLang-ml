[English](./README.md) | 中文

> 学习自 **Enaium**@bilibili.com

### Step 1 编写

创建 ttLang-ml.py 并编写代码

```python
while True:
    x = input(":ttLang-ml >>>")
    if x in globals().keys():
        print(globals()[x])
        continue
    try:
        exec(x)
    except Exception as err:
        print(err)
```



### Step 2 运行

```
pip install pyinstaller
pyinstaller -F ttLang-ml.py
./dist/ttLang-ml.exe
```



### Step 3 使用

##### 3.1 输出 "hello world"

```
:ttLang-ml >>>print("hello world")
```

> 以下开始省略 :ttLang-ml >>>



##### 3.2 加法

```
a=1;b=2;print(a+b)
```



##### 3.3 打印love拼成的心形

```
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30,30)]) for y in range(30, -30, -1)]))
```



```
              veLoveLov           veLoveLov
            eLoveLoveLoveLove   eLoveLoveLoveLove
          veLoveLoveLoveLoveLoveLoveLoveLoveLoveLov
         veLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveL
        veLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLov
        eLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
        LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveL
        oveLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLo
        veLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLov
        eLoveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
         oveLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
          eLoveLoveLoveLoveLoveLoveLoveLoveLoveLove
          LoveLoveLoveLoveLoveLoveLoveLoveLoveLoveL
            eLoveLoveLoveLoveLoveLoveLoveLoveLove
             oveLoveLoveLoveLoveLoveLoveLoveLove
              eLoveLoveLoveLoveLoveLoveLoveLove
                veLoveLoveLoveLoveLoveLoveLov
                  oveLoveLoveLoveLoveLoveLo
                    LoveLoveLoveLoveLoveL
                       LoveLoveLoveLov
                          LoveLoveL
                             Lov
                              v
```



##### 3.4 打印九九乘法表

```
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)])for x in range(1, 10)]))
```



```
1*1=1
1*2=2  2*2=4
1*3=3  2*3=6  3*3=9
1*4=4  2*4=8  3*4=12 4*4=16
1*5=5  2*5=10 3*5=15 4*5=20 5*5=25
1*6=6  2*6=12 3*6=18 4*6=24 5*6=30 6*6=36
1*7=7  2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49
1*8=8  2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64
1*9=9  2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81
```



##### 3.5 打印斐波那契数列

```
print([x[0] for x in [(a[i][0], a.append([a[i][1], a[i][0]+a[i][1]])) for a in([[1, 1]], ) for i in range(30)]])
```



```
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]
```



##### 3.6 打印 base64 解密内容

```
bytes = base64.b64decode(b'SSBsb3ZlIHlvdQ==');print(bytes.decode())
```



```
I love you
```



##### 3.7 执行base64 解密内容

制作加密内容

```
import base64

fun = """
def hello():
    print("hello world")

if __name__ == '__main__':
    hello()
"""

encode = base64.b64encode(fun.encode(encoding="utf-8"))

print(encode)
```

执行加密内容

```
import base64;decode = base64.b64decode(b'CmRlZiBoZWxsbygpOgogICAgcHJpbnQoImhlbGxvIHdvcmxkIikKCgppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOgogICAgaGVsbG8oKQo=');print(decode);print('====');exec(decode)
```



```
b'\ndef hello():\n    print("hello world")\n\n\nif __name__ == \'__main__\':\n    hello()\n'
====
hello world
```

