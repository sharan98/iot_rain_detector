"""
https://github.com/thisbejim/Pyrebase/blob/master/README.md
^^pyrebase 
"""


import pyrebase, time

#url of the database
firebase_url = "https://raincheck-2aeb6.firebaseio.com/"

# old...ignore the following comment, but dont delete
"""
    data = {'time': time.strftime("%H:%M:%S"),\
            'date': time.strftime('%d/%m/%y')}

    print (data)
    result = requests.post(firebase_url + '/DateTime.json', data = json.dumps(data))

    print ('Record inserted: ' + str(result.status_code) + ', ' + result.text)


    data = requests.get('https://raincheck-2aeb6.firebaseio.com/DateTime/-LMuZbfQ1z2JOPOAXpsu')

    print (data.status_code)
    print (data.json)
    print (data)
"""
"""
config = {
    "apiKey": "raincheck-2aeb6",
    "authDomain": "raincheck-2aeb6.firebaseapp.com",
    "databaseURL": "https://raincheck-2aeb6.firebaseio.com/",
    "storageBucket": "gs://raincheck-2aeb6.appspot.com"
}
"""
config = {
    "apiKey": "AIzaSyC4nv3eGXd3f0OikXSnsWrtFNVjfIFz_uQ",
    "authDomain": "raincheck-2aeb6.firebaseapp.com",
    "databaseURL": "https://raincheck-2aeb6.firebaseio.com",
    "projectId": "raincheck-2aeb6",
    "storageBucket": "raincheck-2aeb6.appspot.com",
    "messagingSenderId": "640500222516"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

data = {'time': time.strftime("%H:%M:%S"), 'date': time.strftime('%d/%m/%y')}



"""
#the func returns dict with current time and date
def now_time():
    return {'time': time.strftime("%H:%M:%S"), 'date': time.strftime('%d/%m/%y')}

#inserts 3 records into the database
for i in range(3):
    r = db.child("DateTime").child(str(i)).set(now_time())
    time.sleep(10)

"""



