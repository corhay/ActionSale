import flask
import sqlite3
from flask import jsonify, request, render_template
from flask_caching import Cache
from datetime import date
from datetime import timedelta
from datetime import datetime

#create flask app
app = flask.Flask(__name__)
#configure app
config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300,
}
app.config.from_mapping(config)
#set caching
cache = Cache(app)

stores = ("coop", "mig", "denn")

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def getWeek(curDate=date.today()):
    if isinstance(curDate, str):
        curDate = datetime.strptime(curDate, '%d.%m.%Y')

    dow = int(curDate.strftime("%w"))
    weekStartDiff = (dow - 2) % 7
    #start of week (tuesday)
    sw = curDate - timedelta(days=weekStartDiff)
    #end of week (monday)
    ew = sw + timedelta(days=6)
    #format like ActCoop
    return sw.strftime("%d") + "." + sw.strftime("%m") + "." + sw.strftime("%Y") + " - " + ew.strftime("%d") + "." + ew.strftime("%m") + "." + ew.strftime("%Y")

@app.route('/', methods=['GET'])
@cache.cached(timeout=3600)
def home():
    return render_template('home.html')

@app.route('/v1/products/categories', methods=['GET'])
def api_categories():
    categories = {
        'Bières' : ('Bière', 'Lager'),
        'Vins' : ('AOC', 'DOC', '2014', '2015', '2016', '2018', '2019', 'Vin', ''),
        'Cigarettes' : ('cigarette', 'tabac', 'Cigar', 'Smoking', 'OCB'),
        'Viandes' : ('poulet', 'boeuf', 'bœuf', 'steak', 'émincé', 'escalope', 'porc', 'lard', 'agneau', 'cheval', 'viande', 'lapin'),
        'Fromages' : ('Tomme', 'Gruyère', 'Vacherin', 'emmental', 'edammer', 'mozzarella', 'cheddar', 'Fromage', 'Cheese', ''),
        'Snacks' : ('Chip', 'Popcorn', 'Flûte', 'Cacahuète', 'Pistache', 'Snack', 'Biscuit', 'Apéro', 'Flip'),
        'Chocolats' : ('Chocolat', 'Lindt', 'Cailler', 'Frey', 'Munz', 'Mikado', 'Nutella'),
        'Pizzas' : ('Pizza', 'Buitoni'),
        'Pâtes' : ('Spaghetti', 'Farfalle', 'Fusilli', 'Orecchiette', 'Lasagne', 'Ravioli', 'Macaroni', 'Penne', 'Tagliatelle', 'Tortellini', 'Rigatoni', 'Linguine', 'Spätzli', 'Gnocchi', 'Trofie', 'Gemelli', 'Conchiglie' ),
    }

    response = jsonify(categories)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/v1/discounts/current', methods=['GET'])
#@cache.cached(timeout=3600*24, key_prefix='current_discounts')
def api_all():
    conn = sqlite3.connect('actions.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    currentDate = '%' + getWeek()[:10] + '%'
    #currentDate = '%01.06.2020%'
    all_discounts = {}
    for store in stores:
        query = "SELECT DISTINCT * FROM " + store + "_discounts INNER JOIN " + store + "_categories ON " + store + "_discounts.Title = " + store + "_categories.Title WHERE date LIKE ?"
        all_discounts[store] = cur.execute(query, [currentDate]).fetchall()

    response = jsonify(all_discounts)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/v1/discounts/all', methods=['GET'])
def api_filter():
    #get params cleanly
    query_parameters = request.args
    
    store = query_parameters.get('store')
    search = query_parameters.get('search')
    date = query_parameters.get('date')

    #check params
    if not (store or search or date):
        return bad_request(400)
    
    #open connection to db
    conn = sqlite3.connect('actions.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    results = {}

    #build queries

    #get searches
    if search:
        search = search.split()

    #get stores desired
    if store:
        filterStores = store.split()
    else:
        filterStores = stores
        
    #loop through each desired store
    for filterStore in filterStores:

        filterStore = filterStore.lower()

        if filterStore in stores:
            query = 'SELECT DISTINCT * FROM ' + filterStore + '_discounts WHERE'

            searchTerms = []
            if search:
                for word in search:
                    keyword = '%' + word + '%'
                    searchTerms.append(keyword)
                    query += ' Title LIKE ? OR'
                query = query[:-3]
            else:
                query += ' Title=Title'
            if date:
                #check value
                try:
                    query += ' AND date LIKE ' + '\'%' + getWeek(date)[:10] + '%\''
                except ValueError:
                    return bad_request(ValueError)

            query += ';'
            results[filterStore] = cur.execute(query, searchTerms).fetchall()
            #results[filterStore] = query
        else:
            return bad_request(400)

    return results

@app.errorhandler(404)
@cache.cached(timeout=3600*24)
def page_not_found(e):
    return render_template("errors/page_not_found.html")

@app.errorhandler(400)
#@cache.cached(timeout=3600*24)
def bad_request(e):
    return render_template("errors/bad_request.html")

if __name__ == '__main__':
    app.run(threaded=True, port=5000)