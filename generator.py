import motor.motor_asyncio
import random

client = motor.motor_asyncio.AsyncIOMotorClient("localhost", 27017)
db = client.Cameras

surname_male = ["Иванов", "Петров","Сидоров","Каменев","Попов","Тимашенко"]
surname_female = ['Иванова', 'Петрова','Сидорова','Каменева','Попова','Кубикова','Петренко' ]
name_male = ["Алексей", "Сергей","Андрей","Олег","Игорь","Петр","Тимофей"]
name_female = ["Арина", "Марина","Карина","Полина","Ирина","Мальвина","Малина"]
cities = ["Волгоград", "Москва", "Санкт-Петербург", "Казань"]
NAME_C = ["EOS 850D", "D850", "ZV-1F", "X-T4"]
TYPE_F = ["Зеркальная", "Цифровая", "Беззеркальная"]
TYPE_MATRIX = ["CMOS", "BSI CMOS", "X-Trans CMOS 4"]
ISO = ["100-25600", "64-3200", "80-12800"]


async def do_insert_many_users(surname_male, surname_female, name_male, name_female, cities):
    collection = db.users
    n = await collection.count_documents({})
    for i in range(n, 2000):
        if i % 2 == 0:
            result = await collection.insert_many([{"i": i, "Name": random.choice(name_male), "Surname":
            random.choice(surname_male), "City": random.choice(cities)}])
        else:
            result = await collection.insert_many([{"i": i, "Name": random.choice(name_female), "Surname":
            random.choice(surname_female), "City": random.choice(cities)}])
async def do_insert_many_cameras(NAME_C, TYPE_F, TYPE_MATRIX, ISO):
    collection = db.cameras
    n = await collection.count_documents({})
    for i in range(n, 2000):
        result = await collection.insert_many([{"i": i, "NAME_C": random.choice(NAME_C), "TYPE_F":
        random.choice(TYPE_F), "TYPE_MATRIX": random.choice(TYPE_MATRIX), "ISO": random.choice(ISO)}])
loop = client.get_io_loop()
loop.run_until_complete(do_insert_many_users(surname_male, surname_female, name_male, name_female, cities))
loop = client.get_io_loop()
loop.run_until_complete(do_insert_many_cameras(NAME_C, TYPE_F, TYPE_MATRIX, ISO))
