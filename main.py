import requests
from website import create_app
from flask import Flask, render_template

response = requests.get('https://randomuser.me/api')

gender = response.json()['results'][0]['gender']
print(gender)

title = response.json()['results'][0]['name']['title']

first_name = response.json()['results'][0]['name']['first']


last_name = response.json()['results'][0]['name']['last']

print(f'{title}. {first_name} {last_name}')

age = response.json()['results'][0]['dob']['age']
print(f'Age: {age}')


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'The quick brown fox jumps over the lazy dog'



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

