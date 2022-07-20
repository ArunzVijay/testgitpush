import pymongo
client = pymongo.MongoClient("mongodb+srv://arunzvijay07:12Sweety34@cluster0.wvslu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "aruna",
    "email" : "arunzvijay07@gmail.com",
    "surname" : "vijay"
}
d = {
    "name" : "aruna",
    "email" : "arunzvijay07@gmail.com",
    "surname" : "vijay"
}

d = {
    "name" : "aruna",
    "email" : "arunzvijay07@gmail.com",
    "surname" : "vijay"
}
d = {
    "name" : "aruna",
    "email" : "arunzvijay07@gmail.com",
    "surname" : "vijay"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)