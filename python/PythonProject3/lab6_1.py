import xml.etree.ElementTree as ET
import datetime
#import matplotlib.pyplot as plt
def load_users_data():
    try:
        users_tree = ET.parse("D:\\коля\\users.xml")
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
            'user_id': int(user_elem.find('user_id').text),
            'name': user_elem.find('name').text,
            'age': int(user_elem.find('age').text),
            'weight': int(user_elem.find('weight').text),
            'fitness_level': user_elem.find('fitness_level').text,
            'workouts': []
                }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден")
        return []


def load_workouts_data():
    try:
        users_tree = ET.parse("D:\\коля\\workouts.xml")
        users = []
        for user_elem in users_tree.getroot().findall('workout'):
            user = {
            'workout_id': int(user_elem.find('workout_id').text),
            'user_id': int(user_elem.find('user_id').text),
            'date': datetime.datetime.strptime(user_elem.find('date').text,'%Y-%m-%d'),
            'type': user_elem.find('type').text,
            'duration': int(user_elem.find('duration').text),
            'distance': float(user_elem.find('distance').text),
            'calories': int(user_elem.find('calories').text),
            'avg_heart_rate': int(user_elem.find('avg_heart_rate').text),
            'intensity': user_elem.find('intensity').text
                            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден")
        return []

def get_stats(users,workouts):
    for u in users:
        for w in workouts:
            if u['user_id'] == w['user_id']:
                u['workouts'].append(w)

    train_count = 0
    users_count = 0
    calories = 0
    totaltime = 0
    distance = 0


    for u in users:
        users_count = users_count + 1
        w1 = u['workouts']
        for w in w1:
            train_count = train_count + 1
            calories = calories + w['calories']
            totaltime = totaltime + w['duration']
            distance = distance + w['distance']
    print('ОБЩАЯ СТАТИСТИКА')
    print(' ===================================')
    print('Всего тренировок:',  train_count)
    print('Всего пользователей:',  users_count)
    print('Сожжено калорий:', calories)
    print('Общее время:', round(totaltime/60, 1), 'часов')
    print('Пройдено дистанции:', round(distance, 1),'км')
    return

u = load_users_data()

w = load_workouts_data()

get_stats(u, w)