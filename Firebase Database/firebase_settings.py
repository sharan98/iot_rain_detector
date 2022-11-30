"""
https://github.com/thisbejim/Pyrebase/blob/master/README.md
^^pyrebase 
"""
import pyrebase

#url of the database
firebase_url = "https://raincheck-2aeb6.firebaseio.com/"

config = {
    "apiKey": "AIzaSyC4nv3eGXd3f0OikXSnsWrtFNVjfIFz_uQ",
    "authDomain": "raincheck-2aeb6.firebaseapp.com",
    "databaseURL": firebase_url,
    "projectId": "raincheck-2aeb6",
    "storageBucket": "raincheck-2aeb6.appspot.com",
    "messagingSenderId": "640500222516"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

#if __name__ == '__main__':
#    print ("Firebase")