from flask import Flask, render_template, request
from foo import just_do_it
app = Flask(__name__)

@app.route("/")
def homepage():
    html = render_template('index.html')
    return html

@app.route("/results")
def results():
    reqargs = request.args
    _sortby =  reqargs.get('sortby')
    _zipcode = reqargs.get('zipcode')
    _state = reqargs.get('state')


    # return an error if there is no state or zipcode
    if not _zipcode and not _state:
        return """
            <h1>Error</h1>
            <p>Must have either a state abbreviation or zipcode value</p>
            <p>Go <a href="{url}">back</a></p>
        """.format(url=request.referrer)


    elif request.args.get('zipcode'):
        search_type = 'zipcode'
        search_val = request.args.get('zipcode')
        peeps = just_do_it(zipcode=search_val, sortby=_sortby)
    elif request.args.get('state'):
        search_type = 'state'
        search_val = request.args.get('state')
        peeps = just_do_it(state=search_val, sortby=_sortby)

    html = render_template('results.html', legislators=peeps, sortby=_sortby,
                            search_type=search_type, search_value=search_val)
    return html

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
