# Service Pad Backend Developer Technical Test API REST

## Run locally

- Install requirements. (This step might not work, i didn't knew how to create the file I just copy pasted the names of the library that I needed to install.)

```
pip install -r requirements.txt
```

- Create your `.env`, `.env example` is provided for the needed fields.
- Run the app with:

```
export FLASK_APP='main.py'

python3 -m flask run
# or
flask run
```

## Logic test

- Logic test files are provided inside the `logic test` folder, to run them:

```
python3 fibonacci.py 7 #Needs argument.
python3 fizz_buzz.py
python3 word_counter
```
