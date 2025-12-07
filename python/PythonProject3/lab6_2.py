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
            'workouts': [],
                'total_trains':0,
                'total_calories': 0,
                'total_time': 0

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


def populate_user_worcouts(users,workouts):
    for u in users:
        for w in workouts:
            if u['user_id'] == w['user_id']:
                u['workouts'].append(w)
    return


def analyze_user_activity(users):

    for u in users:
        w1 = u['workouts']
        total_trains = 0
        total_calories = 0
        total_time = 0
        for w in w1:
            total_trains=  total_trains + 1
            total_calories = total_calories + w['calories']
            total_time = total_time+ w['duration']
        u['total_trains'] = total_trains
        u['total_calories'] = total_calories
        u['total_time'] = total_time

    sorted_users = sorted(users, key=lambda x: (x['total_trains'], x['total_calories'],  x['total_time']), reverse=True)
    print('ТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:')
    n = 0
    for u in sorted_users:
        n = n + 1
        if n > 3:
            return
        print(n,'.', u['name'])
        print('Тренировок: ', u['total_trains'])
        print('Калорий: ',  u['total_calories'])
        print('Время: ', round(u['total_time']/60, 1), 'часов')
        print('')
    return

u = load_users_data()
w = load_workouts_data()
populate_user_worcouts(u,w)

analyze_user_activity(u)
