# Flask Apps with Query Strings

A set of lessons and examples in which a __ is presented to the user to allow search/filtering by freeform text, radio buttons, and/or checkboxes.

# Lessons

- [lesson-01.md](lesson-01.md) - How to add the most basic of web forms and how to extract the key-value pair from a URL string.
  - source: [examples/01-hello](examples/01-hello)
- [lesson-02.md](lesson-02.md) - How to search and sort Congressional data using inputs from a web form that include text-search and radio buttons.
  - source: [examples/02-congress-names](examples/02-congress-names)
- [lesson-03.md](lesson-03.md) - Same subject as the previous lesson, but includes a lookup dataset to allow a user to search by zipcode (which requires writing a lookup function).
  + source: [examples/03-congress-locale](examples/02-congress-locale)
  + demo: [on heroku](https://mysterious-gorge-91285.herokuapp.com)





# Code concepts in general

So far in our Flask apps, we've dealt two kinds of simple Flask apps:

#### Single-page Flask apps

These's apps consist of a single page of data results:

- [Introduction to Simple Web Applications with Flask](http://www.compjour.org/lessons/flask-single-page/)
- [Introduction to Simple News Apps based on CSPC Recall Data](http://www.compjour.org/lessons/flask-recalls/)
- Earthquake listings: [simple](https://github.com/datademofun/heroku-flask-quakes-simple) and [not-as-simple](https://github.com/datademofun/heroku-flask-quakes-lesssimple)



#### Multi-page Flask apps

Apps that can generate multiple pages based on named route paths and variables:

- [Flask documentation on routing and variable rules](http://flask.pocoo.org/docs/0.10/quickstart/#variable-rules)
- [First News App with LA Riots Data](http://first-news-app.readthedocs.io/en/latest/)
- [Flask app with Spotify data](https://github.com/datademofun/spotify-flask)


## URL query strings

The iteration here is not too complicated. Instead of generating variable routes like:

        /senators/state/CA

We'll be specifying variables in the __query string__; the below key-value pair is roughly the same effect as the path shown above:

       /senators?state=CA        


Using query strings allows for greater flexibility in passing variables:

       /senators?state=CA&sort_by=age



## About webforms

How do we pass in those different key-value pairs? In our HTML view, we render a __web form__ that contains input fields for `'state'` and `'sort_by'` -- or whatever key-value pairs you want.

A web form, in its most basic variation, consists of a `<form>` tag that:

- has an `action` attribute, typically corresponding to a route string
- has a `method` attribute -- for now, we'll just assume it's good 'ol `get` for [a simple HTTP GET request](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods)
- wraps at least one `<input>` tag: [w3schools (whom I'd almost never recommend) as a straightforward list](http://www.w3schools.com/html/html_form_input_types.asp)
- wraps a "button", typically another `<input>` tag that has the `type='submit'`



## About the Flask Request object

The Flask documentation has a section on the [Request object](http://flask.pocoo.org/docs/0.10/api/#flask.request), which is the data object that the Flask application exposes to a given view function after matching based on an endpoint and query parameters.

For example, if we have an endpoint with a route path of `/results` and two key-value pairs of: 
  
  - `'id`  and `42`
  - `name` and `mary`

The resulting  a URL path and query string will be:

      /results?id=42&name=mary

The Flask application will serialize the __parameters__  as part of an object named __request__ (which has nothing to do with the [Requests library](http://docs.python-requests.org/en/master/)).

Specifically, the __request__ object will have an attribute named `args`, which is a dictionary of keyvalue pairs, i.e.:

~~~py
      {'id': '42', 'name': 'mary'}
~~~
