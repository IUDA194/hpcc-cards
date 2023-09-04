import pymongo

# Устанавливаем соединение с MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Выбираем базу данных
db = client["khpcc"]

# Выбираем коллекцию "groups_P"
collection = db["groups_p"]

# Ключ, по которому будем искать
search_key = "П-21"

# Выполняем поиск по ключу "group_name"
cursor = collection.find({"group_name": search_key})


for record in cursor:
    print(record)
# if result:
#     print("Найдена группа:")
#     print(result)
# else:
#     print(f"Группа с ключом '{search_key}' не найдена.")
