from flask import Flask, render_template, request
from operator import itemgetter
import csv




app = Flask(__name__)



def get_data():
    # open data file, filter for in_office,
    # add fullname field
    # then return list of dicts
    with open('./static/data/legislators.csv', 'r') as f:
        newrows = []
        for row in csv.DictReader(f):
            if row['in_office'] == '1':
                row['fullname'] = ' '.join([row['firstname'], row['middlename'], row['lastname']])
                newrows.append(row)
        return newrows

def filter_data(lastname='', sortby=None):
    # first, select only peeps that match by a name, then sort them
    lowname = lastname.lower()
    rows = [d for d in get_data() if lowname in  d['lastname']]
    if sortby == 'oldest':
        return sorted(rows, key=itemgetter('birthdate'), reverse=True)
    elif sortby == 'youngest':
        return sorted(rows, key=itemgetter('birthdate'))
    else:
        # i.e. 'alpha' or any value...just sort by last name, first name
        return sorted(rows, key=itemgetter('lastname'))



@app.route("/")
def homepage():
    html = render_template('index.html')
    return html

@app.route("/results")
def results():
    _sortby =  request.args.get('sortby')
    _lastname =  request.args.get('lastname')
    peeps = filter_data(lastname=_lastname, sortby=_sortby)
    html = render_template('results.html', lastname=_lastname,
                           legislators=peeps, sortby=_sortby)
    return html

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
