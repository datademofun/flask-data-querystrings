from helpers import get_legislators, get_ziplookups
from helpers import filter_by_state, filter_by_zipcode, sort_by_criteria


# store the datarows in memory
legislators = get_legislators()
ziplookups = get_ziplookups()


# this function is the only one that app.py needs to know about
def just_do_it(state="", zipcode="", sortby="alpha"):
    matched_rows = []
    datarows = legislators
    # first, filter
    if zipcode:
        filteredrows = filter_by_zipcode(zipcode, legislators, ziplookups)
    else:
        # by default, search by state abbreviation
        filteredrows = filter_by_state(state, legislators)
    # then, sort and return the result
    # remember to pass in filteredrows, not legislators
    return sort_by_criteria(sortby, filteredrows)



def print_record_count():
    print("There are", len(legislators), 'rows.')
