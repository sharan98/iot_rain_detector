import firebase_settings as firebase    #the database --->> firebase.db

db = firebase.db
    
#counts number of children in firebase_url/location
#location ==>> 'DateTime' or 'DateTime/3/age'...
def count(location = None):
    if location == None:
        all_children = db.get()
    else:
        all_children = db.child(location).get()
    if all_children.val() == None:
        print("Empty")
        return None
    return len([x for x in all_children.val() if x != None])

#prints all children in firebase_url/location
def printChildren(location = None):
    if location == None:
        all_children = db.get()
    else:
        all_children = db.child(location).get()
    if all_children.val() == None:
        print("Empty")
        return None
    if isinstance(all_children.val(), list):
        for i in (x for x in all_children.val() if x != None):
            print(i)
    elif isinstance(all_children.val(), dict):
        for key, value in all_children.val().items():
            print (key, value)
    else:
        print(all_children.val())

def pushToDb(location, id, data):
    nodes = db.child(location).get()
    if (nodes.val() == None):
        print ('No such location')
        return
    try:
        print(nodes.val())
        r = db.child(location).child(id).set(data)
    except:
        print('Some Error')