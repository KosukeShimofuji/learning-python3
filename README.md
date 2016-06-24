# Python3の学習

CTFのWriteupをみるとexploitはpythonで書かれていることが多いし、機会学習の分野でもpythonを利用していることが多いし、OpenStackのsdkもpythonを推しているのでpythonを学ぶ必要性を感じる。Python2系の最終バージョンであるpython2.7も2020年で保守が打ち切られるみたいなので、これからpython2.7を学ぶ必要性は薄そうだ。よってpython3を学ぶこととする。

# Pythonの開発環境を整える

## pyenv

pyenvはpythonの特定のバージョンのインストールとバージョンの切り替えを手軽に行えるようにしてくれるツールです

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

 * python3系の最新版をインストールする

```
$ pyenv install 3.5.1
```

 * システム全体で最新版のpythonを利用する

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

```
$ pyenv virtualenv 3.5.1 learning-3.5.1
$ pyenv global learning-3.5.1
```

# 参考文献

 * http://qiita.com/Kodaira_/items/feadfef9add468e3a85b
 * http://docs.python.jp/3.5/tutorial/index.html


