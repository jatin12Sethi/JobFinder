from flask import Flask, render_template

app = Flask(__name__)

Jobs=[
    {
        'id': 1,
        'title': 'Software Developer',
        'company': 'Google',
        'location': 'Mountain View, CA',
        'salary': '20 LPA',
        'description': 'Develop software for Google'
    },
    {
        'id': 2,
        'title': 'Junior Developer',
        'company': 'Google',
        'location': 'Mountain View, CA',
        'salary': '30 LPA',
        'description': 'Develop software for Google'
    },
    {
        'id': 3,
        'title': 'Senior Analyst Developer',
        'company': 'Google',
        'location': 'Mountain View, CA',
        'salary': '40 LPA',
        'description': 'Develop software for Google'
    }
]

@app.route('/')

def hello_world():
    return render_template('home.html', jobs=Jobs,app_name='Job Board')

if __name__ == '__main__':
    app.run()
