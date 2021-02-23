from flask import Flask, render_template, redirect, url_for, request
import logic
import file_handler

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        inputString = ''
        # print('--------', request.form)
        if len(request.form['inputFile']) != 0:
            inputfile = request.form['inputFile']
            inputString = file_handler.handler(
                inputfile[len(inputfile)-3: len(inputfile)], inputfile)
        else:
            inputString = request.form['inputText']
        # print(inputString)
        sentiment = logic.sentiment_analyze(inputString)
        print(sentiment)
        if sentiment == 'Positive Sentiment':
            return render_template('output.html', Positive=sentiment)
        elif sentiment == 'Negative Sentiment':
            return render_template('output.html', Negative=sentiment)
        else:
            return render_template('output.html', Neutral=sentiment)
    else:
        return render_template('base.html')


@ app.route('/')
def output():
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
