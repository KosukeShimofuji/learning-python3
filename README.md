# Python3の学習

CTFのWriteupをみるとexploitはpythonで書かれていることが多いし、機会学習の分野でもpythonを利用していることが多いし、OpenStackのsdkもpythonを推しているのでpythonを学ぶ必要性を感じる。Python2系の最終バージョンであるpython2.7も2020年で保守が打ち切られるみたいなので、これからpython2.7を学ぶ必要性は薄そうだ。よってpython3を学ぶこととする。

# Pythonの開発環境を整える

## pyenv

pyenvはpythonの特定のバージョンのインストールとバージョンの切り替えを手軽に行えるようにしてくれるツールです。

 * pyenvの初期設定を行う

```
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
$ cat >> .bashrc
export PYENV_ROOT=$HOME/.pyenv
export PATH=$PYENV_ROOT/bin:$PATH
eval "$(pyenv init -)"
^C
$ sudo apt-get install libbz2-dev zlib1g-dev libssl-dev libreadline-dev libsqlite3-dev
```

 * python3系の最新版をインストールする。

```
$ pyenv install 3.5.1
```

 * システム全体で最新版のpythonを利用する。

```
$ pyenv global 3.5.1
$ python --version
Python 3.5.1
```

## virtualenv

virtualenvは同じversionのpythonで異なる環境を作成するためのツールです。

```
$ git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
$ cat >> .bashrc
eval "$(pyenv virtualenv-init -)"
^C
```

python 3.5.1の別の環境を作成する。

```
$ pyenv virtualenv 3.5.1 learning-3.5.1
$ pyenv global learning-3.5.1
```

# python3 チュートリアル

## PEP8 

[PEP8](http://pep8-ja.readthedocs.io/ja/latest)という推奨されるコーディング規約が存在する。

 * タブではなく4文字の空白を利用する
 * 79文字の範囲内に収まるようにコーディングを行う

## print

 * 区切り文字変更(改行なし)

python3のみで使える模様。

```
print("Hello", end="")
```

## 引数の受け渡し

pythonの引数の受け渡しはsys.argvを通して行うためsysモジュールをインポートする必要がある。

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

for i in sys.argv:
    print i
```

```
$ python argv.py 1 2 3
argv.py
1
2
3
```

## データ構造

### 文字列型(String)

```
>>> s = "string"
>>> s
'string'
>>> s[1]
't'
>>> s[1] = 'b'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

文字列型はindexやスライスで参照可能だが、immutableなデータ構造であり変更ができない。

### リスト

```
>>> l = [1,2,3,4,5]
>>> l
[1, 2, 3, 4, 5]
>>> l[3]
4
>>> l[3] = 400
>>> l
[1, 2, 3, 400, 5]
```

リストはindexやスライスで参照可能であり、mutableなデータ構造なのでも要素の修正もできる。
リストはタプルと違い、インデックスよりイテレータにより参照されることが多い。

### タプル

```
>>> t = 1,2,"hoge"
>>> t
(1, 2, 'hoge')
>>> t2 = t, 3, 4
>>> t2
((1, 2, 'hoge'), 3, 4)
>>> t2[1]
3
>>> t2[1] = 3000
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

リストと似ているがimmutableな型なので要素の変更はできない。

### 集合型

```
>>> g = {'hoge', 'foo', 'bar', 'hoge'}
>>> g
{'bar', 'foo', 'hoge'}
```

集合は重複する要素を持たない、順序付けられていない要素の集まりです。

### 辞書型

```
>>> dic = {'january': 1, 'February': 2}
>>> dic['january']
1
```

Perlのハッシュなどと同じデータ構造です。

## 制御構造

### if文

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = int(input("plese enter an integer: "))
if x < 0:
    print ("Negative integer")
elif x == 0:
    print ("Zero")
elif x==1:
    print ("Single")
else:
    print("More")
```

elseifではなくてelifとさらに短くなっている。

```
kosuke@chaos ~/learning-python3 $ python if.py
plese enter an integer: 10
More
kosuke@chaos ~/learning-python3 $ python if.py
plese enter an integer: 1
Single
kosuke@chaos ~/learning-python3 $ python if.py
plese enter an integer: -10
Negative integer
```

### for文

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

words = ['cat', 'window', 'defensetrate']
for w in words:
    print (w, len(w))
```

CやPerlのfor文とは違いpythonのfor文はリストや文字列などのシーケンス型にわたって反復処理を行う。

```
('cat', 3)
('window', 6)
('defensetrate', 12)
```

### range関数

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

for i in range(5):
    print(i)
```

数列に対して処理を行いたい場合はrange関数を使うのが便利です。

```
0
1
2
3
4
```

rangeには開始値、最大値、増加値を指定することができます。

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

for i in range(-10, 10, 3):
    print(i)
```

-10から初めて最大値10まで増加値を3に設定して実行してみます。

```
$ python range.py
-10
-7
-4
-1
2
5
8
```

リストにindexでアクセスする際にもrangeを使用することができます。


```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print (i, a[i])
```

```
$ python range.py
(0, 'Mary')
(1, 'had')
(2, 'a')
(3, 'little')
(4, 'lamb')
```

## break文とcontinue文とループのelse節

break文とcontinue文の挙動はCと同じです。注目すべきはpythonはfor文などの繰り返し文にelse節を持てるということです。else節は繰り返し条件の終了時に呼ばれますが、breakなどで抜けた場合には実行されません。

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals',  x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
```

このコードのelse節はif文ではなくfor文にかかっていることに注目してください。

```
(2, 'is a prime number')
(3, 'is a prime number')
(4, 'equals', 2, '*', 2)
(5, 'is a prime number')
(6, 'equals', 2, '*', 3)
(7, 'is a prime number')
(8, 'equals', 2, '*', 4)
(9, 'equals', 3, '*', 3)
```

### pass文

pass文は何もしません。構文上ステートメントが必要だが、実装の内容はきまっていないときにとりあえず何もしない処理を書いておくときに便利です。

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    pass
```

何もせず、ただずっと繰り返すスクリプトは上記のようにかけます。

## 関数

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib2(n):
        """Retrun a list containg the Fibonacci series up to n """
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a,b = b, a+b
        return result

print (fib2(100))
```

関数はdefキーワードで始まり、()内に引数を受け取るリストを指定しなければなりません。
"""で囲まれた文字列はdoc
stringであり、ドキュメンテーション文字列を使ったツールなどで出力されます。

関数の中の変数はすべてローカル変数であり、関数の終了とともに削除されます。(シンボルテーブルから除去される)
グローバル変数の参照は可能ですが、ローカル変数と名前が一致していた場合、ローカル変数の値が優先されます。
関数内でグローバル変数に値を代入するにはglobal文で明示しなければなりません。

関数の引数の受け取り方にはデフォルト引数の指定や、キーワード引数、可変引数を設定することができます。

## lambda

lambdaを使えば名前のない関数を定義することができます。

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = lambda a,b:a+b
print(f(2,3))
```

```
$ python lambda.py
5
```

## モジュール

拡張子pyのファイルはすべてモジュールです。モジュールはそれぞれシンボルを持つため、同じ変数名を使っていたとしても名前空間が衝突することは通常ありません。

 * a.py

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = ['hoge', 'foo', 'bar']

def hello():
    print("Hello World")

def name():
    print(__name__)

if __name__ == '__main__':
    print "Run as a script"
```

 * run.py

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import a

a.hello()
a.name()
```

 * run.pyの実行

```
$ python run.py
Hello World
a
```

 * a.pyの実行

```
$ python a.py
Run as a script
```

特定のシンボルだけを取り出すこともできます。

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from a import hello

hello()
```

モジュールはsys.pathに格納されるディレクトリの順で検索されます。

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
print(sys.path)
```

```
$ python sys_path.py
['/home/kosuke/learning-python3/module', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages']
```

# 参考文献

 * http://qiita.com/Kodaira_/items/feadfef9add468e3a85b
 * http://docs.python.jp/3.5/tutorial/index.html


