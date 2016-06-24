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

## 関数

### docstirng

### ramda

## モジュール

# 参考文献

 * http://qiita.com/Kodaira_/items/feadfef9add468e3a85b
 * http://docs.python.jp/3.5/tutorial/index.html


