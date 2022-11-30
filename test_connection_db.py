import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://andresone64:Scrufyharp09@votaciones.ioxdkga.mongodb.net/votaciones_db?retryWrites=true&w=majority",
    tlsCAFile=ca
)
db = client.test
# print("\n", db)

data_base = client['votaciones_db']
# print(data_base.list_collection_names())
