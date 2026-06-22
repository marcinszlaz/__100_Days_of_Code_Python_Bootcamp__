# commands in venv:

* `export FLASK_APP=mainproject.py` - adding variable (main file)
* `flask run --host=0.0.0.0 --port=5005 --debug` - launch  WSGI server
* `flask routes` - runs in venv, display available routes
* `flask shell` after that `app.config` - same but better xD
* `FLASK_RUN_HOST=0.0.0.0` `FLASK_RUN_PORT=5005` - put it inside .flaskenv file

# some commands in vim

*.`:9,18norm.i#`.-.this.way.you.can.handle.multiline.comments.in.vim
*.`:9,18norm.x`.-.delete.one.char.(#),.you.can.use.visual.too
* `:9,21s/^#/`.-.this.also.remove.(substitiute).#.to.`.`
* `v.-.visual.:s/^#//` .equal.this.above
* `^` it means "first char" like in xpath / css selectors
* ctrl.-.y.means.YES.for.chosen.tips.from.plugins.in.vim
