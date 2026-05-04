import os,pathlib

basedir = pathlib.Path.cwd()
print('basedir: ',basedir)
basedir_ = pathlib.Path.cwd() / 'zupa.txt'
print('basedir_: ',basedir_)
_basedir_ = 'sqlite:///' + os.getcwd() + 'movie.db'
print('_basedir_: ',_basedir_)
