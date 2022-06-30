from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.sumbhxu.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# Quiz 1.
db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})