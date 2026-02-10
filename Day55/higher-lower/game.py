from flask import Flask
import random
app = Flask(__name__)

num = random.randint(0,9)

def home_page_decorator(func):
    def wrapper(*args, **kwargs):
        return "<h1 style='text-align: center;'>" + func(*args, **kwargs) + "</h1>"\
        "<div style='text-align: center;'>"\
        "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"\
        "</div>"
    return wrapper

def guess_game_decorator(func):
    def wrapper2(*args, **kwargs):
        guess = func(*args, **kwargs)
        if guess > num:
            return"<h1 style='text-align: center; color: red;'>Too high, try again!</h1>"\
            "<div style='text-align: center;'>"\
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'"\
            "</div>"
        elif guess < num:
            return"<h1 style='text-align: center; color: purple;'>Too low, try again!</h1>"\
            "<div style='text-align: center;'>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'"\
            "</div>"
        else:
            return"<h1 style='text-align: center; color: green;'>You guessed correctly!</h1>"\
            "<div style='text-align: center;'>"\
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'"\
            "</div>"
    return wrapper2



@app.route('/')
@home_page_decorator
def home_page():
    return "Guess a number between 0 and 9"

@app.route('/<int:guess>')
@guess_game_decorator
def guess_game(guess):
    print(num)
    print(guess==num)
    return guess


if __name__ == "__main__":
    app.run(debug=True, port=5001)