from flask import Flask, request, render_template
import requests, random

app = Flask(__name__)


url = 'http://numbersapi.com/'

number = random.randint(0, 2022)
about_type = 'trivia'

@app.route('/')

def home():
    numData = requests.request("GET", url + str(number) + '/' + about_type)

    return render_template('index.html', num = numData.text)



@app.route('/getData', methods = ['POST', 'GET'])

def display():

    if request.method == 'POST':

        inputNum = request.form['inputNum']

        if inputNum != '':

            if request.form.get('trivia') == 'Trivia':
                trivia = requests.request("GET", url + str(inputNum) + '/' + 'trivia')

                return render_template('index.html', num = trivia.text)

            elif request.form.get('math') == 'Math':
                math = requests.request("GET", url + str(inputNum) + '/' + 'math')

                return render_template('index.html', num = math.text)

            elif request.form.get('date') == 'Date':
                date = requests.request("GET", url + str(inputNum) + '/' + 'date')

                return render_template('index.html', num = date.text)

            elif request.form['year'] == 'Year':
                year = requests.request("GET", url + str(inputNum) + '/' + 'year')

                return render_template('index.html', num = year.text)

            else:
                return redirect('/')
        
        else:
            numData = requests.request("GET", url + str(number) + '/' + about_type)

            return render_template('index.html', num = numData.text)

    else:
        return redirect('/')

            


if __name__ == '__main__':
    app.run(debug = True)