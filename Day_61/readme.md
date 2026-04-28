# how to use pip for install dependencies

## instaling dependencies
- On Windows type:
python -m pip install -r requirements.txt
- On MacOS type:
pip3 install -r requirements.txt

## create file with dependencies
- On Windows type:
python -m pip freeze > requirements.txt

## create file with dependencies
* in case when you operate in one virtual
environment with multiple projects:
  - Its useful solution if you have multiple projects inside one virtual environment
  - `pip install pipreqs`
  - `pipreqs --use-local --ignore templates,static --savepath requirements.txt;`
* or just:
  * pipreqs --force --savepath requirements.txt (be careful, its overwrite existing requirements file)

- _HINT_
- if you have a lot of projects without requirements.txt file
- you can use my program project folder => *req_adder*
- 