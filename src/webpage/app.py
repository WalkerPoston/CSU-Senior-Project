from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__, static_url_path='/static')

client = MongoClient('localhost', 27017)

db = client.GPS_Coordinates
coords = db.coords

#if __name__ == '__main__':
#    app.run(host="0.0.0.0", debug=True)


@app.route('/update', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        lat = request.form['lat']
        lng = request.form['lng']   
        coords.insert_one({'latitude': lat, 'longitude': lng})
        #print(coords.find())
        return redirect(url_for('index'))
        # return 'Success'

    all_coords = coords.find()
    return render_template('index.html', coords=all_coords)


@app.route('/', methods=['GET'])
def show_map():
    return render_template('map.html')

@app.route('/share.html', methods=['GET'])
def show_share():
    return render_template('share.html')

@app.route('/MissingItem.html', methods=['GET'])
def show_MI():
    return render_template('MissingItem.html')

@app.route('/map.html', methods=['GET'])
def Back_to_Map():
    return render_template('map.html')
