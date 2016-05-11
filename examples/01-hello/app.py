from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    html = render_template('index.html')
    return html

@app.route("/result")
def goodbye():
    x =  request.args.get('stuff')
    html = render_template('results.html', target=x)

    return html

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
