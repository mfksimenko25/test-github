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
        print(n,'.', u['name'], '('+ u['fitness_level']+')')
        print('Тренировок: ', u['total_trains'])
        print('Калорий: ',  u['total_calories'])
        print('Время: ', round(u['total_time']/60, 1), 'часов')
        print('')
    return


def  analyze_workout_types(workouts):
    workouts_stat = {}
    print("РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:")
    for w in workouts:
        if w['type'] not in workouts_stat:
            workouts_stat.update([(w['type'], [])])
        workouts_stat[w['type']].append(w)

    for key in workouts_stat:
        a = workouts_stat[key]
        n = 0
        d = 0
        c = 0
        for w in a:
            n = n + 1
            d = d + w['duration']
            c = c + w['calories']
        print(key.capitalize() + ':', n, 'тренировок', '(', round(n*100/len(workouts), 1), '%)')
        print('  Средняя длительность:', round(d/n, 0), 'мин')
        print('  Средние калории:', round(c/n, 0), 'ккал')
    return

def  find_user_workouts(users, user_name):
    for u in users:
        if u['name'] == user_name:
            return u['workouts']
    print("пользователь не найден")
    return []

def find_user(users, user_name):
    for u in users:
        if u['name'] == user_name:
            return u
    print("пользователь не найден")
    return []

def analyze_user(user, workouts):
    print('ДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ:', user['name'])
    print('=============================================')
    print('Возраст:', user['age'], 'лет,', 'Вес:', user['weight'],'кг')
    print('уровень:', user['fitness_level'])

    n = 0
    c = 0
    t = 0
    dist = 0
    workouts_stat = {}
    for w in user['workouts']:
        if w['type'] not in workouts_stat:
            workouts_stat.update([(w['type'], [])])
        workouts_stat[w['type']].append(w)
        n = n +1
        c = c + w['calories']
        t = t + w['duration']
        dist = dist + w['distance']
    max1 = 0
    key_max =' '
    for key in workouts_stat:
        a = workouts_stat[key]
        if len(a) > max1:
            key_max = key
            max1 = len(a)



    print('Тренировок:',n )
    print('Сожжено калорий:', c)
    print('Общее время:', round(t/60, 1), 'часов')
    print('Пройдено дистанции:', round(dist, 1), 'км')
    print('Средние калории за тренировку:', round(c/n, 0))
    print('Любимый тип тренировки:', key_max)


u = load_users_data()
w = load_workouts_data()
populate_user_worcouts(u,w)

analyze_user_activity(u)
analyze_workout_types(w)
find_user_workouts(u, 'Борис')
analyze_user(find_user(u, 'Борис'), w)