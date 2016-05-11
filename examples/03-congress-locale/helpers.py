from operator import itemgetter
import csv
LEGS_FNAME = './static/data/legislators.csv'
ZIPLOOKUP_FNAME = './static/data/districts.csv'


def get_legislators():
    # open data file, filter for in_office,
    # add fullname field
    # then return list of dicts
    with open(LEGS_FNAME, 'r') as f:
        newrows = []
        for row in csv.DictReader(f):
            if row['in_office'] == '1':
                row['fullname'] = ' '.join([row['firstname'], row['middlename'], row['lastname']])
                newrows.append(row)
        return newrows


def get_ziplookups():
    with open(ZIPLOOKUP_FNAME, 'r') as f:
        # the zip/districts file doesn't have headers,
        # so we need to manually add them ourselves
        c = csv.DictReader(f, fieldnames=['zipcode', 'state', 'district'])
        return list(c)




def filter_by_state(state, datarows):
    matches = []
    for c in datarows:
        # find all house members
        # that match given z['district'] and z['state']
        if c['title'] == 'Rep' or c['title'] == 'Sen':
            if state.upper() == c['state']: # upcase the state, so that `ca` resolves to `CA`
                matches.append(c)
    return matches



def filter_by_zipcode(zipcode, datarows, ziplookups):
    matches = []
    zrows = [z for z in ziplookups if z['zipcode'] == zipcode]
    for z in zrows:
        for c in datarows:
            # find all house members
            # that match given z['district'] and z['state']
            if c['title'] == 'Rep':
                if c['district'] == z['district'] and c['state'] == z['state']:
                    matches.append(c)
            # find all senators that match z['state']
            elif c['title'] == 'Sen':
                if c['state'] == z['state']:
                    matches.append(c)
    return matches





def sort_by_criteria(criteria, datarows):
    if criteria == 'oldest':
        rows = sorted(datarows, key=itemgetter('birthdate'))
    elif criteria == 'youngest':
        # we have to 'reverse' the sort because younger ages correspond to
        # "bigger" (i.e. later) birthdates
        rows = sorted(datarows, key=itemgetter('birthdate'), reverse=True)
    else:
        # i.e. 'alpha' or any value...just sort by last name, first name
        rows = sorted(datarows, key=itemgetter('lastname'))
    return rows
