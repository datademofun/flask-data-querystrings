# Search Congressmembers by zipcode

Source: [examples/03-congress-locale](examples/03-congress-locale)

Live-demo [on Heroku (for now)](https://mysterious-gorge-91285.herokuapp.com)

There's not much to this besides more data-munging. Whereas the [previous example](lesson-02.md) had a search box that allowed users to search by last name, this variation allows entry of ZIP code, which is even easier since you don't have to worry about matching upper/lowercase. To make this a little tricker, I've designed the form to also accept state abbreviation, if a user can't remember their zip code.

The only tricky part is that the data-wrangling code has to traverse two datasets: the legislators listing and a [lookup table that matches zip codes to congressional districts](examples/03-congress-names/static/data/districts.csv).

The structure of the table is so simple that there aren't even any table headers (which means I have to supply them manually when I parse the CSV):

|-------|----|---|
| 55784 | MN | 8 |
| 56688 | MN | 8 |
| 55786 | MN | 8 |
| 54479 | WI | 7 |
| 56680 | MN | 8 |
| 54654 | WI | 3 |


When a user supplies a zip code, the first step is to read the [districts.csv]((examples/03-congress-names/static/data/districts.csv) data (which I've stuffed into the variable `ziplookups`) and get the rows in which the zipcode column matches the user's input.

*Then*, we match against [legislators.csv](examples/03-congress-names/static/data/legislators.csv), the relevant part of which looks like this:

| party | state |   district  |
|-------|-------|-------------|
| D     | HI    | 1           |
| D     | NY    | 5           |
| R     | AL    | 4           |
| D     | HI    | Junior Seat |
| R     | CO    | Senior Seat |
| D     | NJ    | 1           |
| D     | ME    | 1           |
| R     | MO    | 2           |


House members have a `state` and `district`. To get a user's Senators, we simply match on `state`.


## Separation of concerns

I think the most notable part of this example is how I've removed the data-wrangling code out of [__app.py__](examples/03-congress-locale/app.py) and split it into [__foo.py__](examples/03-congress-locale/foo.py) and [__helpers.py__](examples/03-congress-locale/helpers.py).

Why two files? It could've just been `foo.py`...but I wanted `app.py` to only worry about calling one function -- `foo.just_do_it()`. All the functions for reading and filtering the datasets are hidden away in `helpers.py`. My approach isn't more right than a less fractured one...I sometimes just like shuffling things up for variety's sake.

The upshot is that I can also run `foo.just_do_it()` on its own in iPython:

~~~py
from foo import just_do_it
peeps = just_do_it(zipcode='90210')
print(len(peeps))
# 9
~~~

