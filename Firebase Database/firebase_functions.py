import firebase_settings as firebase    #the database --->> firebase.db

db = firebase.db
    
#counts number of children in firebase_url/location
#location ==>> 'DateTime' or 'DateTime/3/age'...
def count(location = None):
    if location == None:
        all_children = db.get()
    else:
        all_children = db.child(location).get()
    try:
        return len([x for x in all_children.val() if x != None])
    except TypeError as e:
        print ("%s doesn't exist" % location)
        print (e)
        return None

#prints all children in firebase_url/location
def printChildren(location = None):
    if location == None:
        all_children = db.get()
    else:
        all_children = db.child(location).get()
    if all_children.val() == None:
        print("Location doesn't exist")
        return None
    if isinstance(all_children.val(), list):
        for i in (x for x in all_children.val() if x != None):
            print(i)
    elif isinstance(all_children.val(), dict):
        for key, value in all_children.val().items():
            print (key, value)
    else:
        print(all_children.val())


#pushToDb(loc, 3, {data})...inserts into db if the loc already exists
def pushToDb(location, id, data):
    nodes = db.child(location).get()                #get the data at location
    if (nodes.val() == None):               
        print ('No such location')                  #don't insert into db if the location is non-existent
        return
    try:
        print(nodes.val())
        r = db.child(location).child(id).set(data)
    except Exception as e:
        print('Some Error' + str(e))


#retrieve data in an ordered dictionary
#eg getOrdered(loc, 'mon', 1) ----> gives data ordered by month starting from January
#startAt parameter is absolutly necessary for data to be ordered
#the startAt value need not exist in the database, the above example works, even if no entries were made in january
def getOrdered(location, orderBy = None, startAt = None):
    #print ("l : %s  o: %s  e: %s" % str(location) )
    print (f'l : {location}  o: {orderBy} e: {startAt}')                #debugging
    try:
        if startAt != None:
            d = db.child(location).order_by_child(orderBy).start_at(startAt).get()
        elif orderBy != None:
            d = db.child(location).order_by_child(orderBy).get()
        else:
            d = db.child(location).get()
        values = d.val()#[x for x in d.val() if x != None] #d.val()
        return values
    except IndexError as i:
        print ( str(i))
    except:
        print ('err, check location: ' + str(location) + ' and orderby: ' + str(orderBy) + "  "+ str(e))
    return


#use this to retrieve data matching a key 'equalTo'
# for eg, getEqualTo(loc, 'mon', 12) gives all records made in december
#don;t bohter using this if only passing orderBy Value: doesnt work
def getEqualTo(location, orderBy = None, equalTo = None):
    print (f'l : {location}  o: {orderBy} e: {equalTo}')        #for debugging
    try:
        if equalTo != None:
            d = db.child(location).order_by_child(orderBy).equal_to(equalTo).get()
        elif orderBy != None:
            d = db.child(location).order_by_child(orderBy).get()
        else:
            d = db.child(location).get()
        values = d.val()#[x for x in d.val() if x != None] #d.val()
        return values
    except IndexError as i:
        print ('equalTo: ' + str(equalTo) + " not found " + str(i))
    except Exception as e:
        print ('err, check location: ' + str(location) + ' and orderby: ' + str(orderBy) + "  "+ str(e))
    return



