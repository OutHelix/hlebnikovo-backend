from datetime import datetime
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')


def get_connection():
    return psycopg2.connect(database=DATABASE_NAME,
                            user=DATABASE_USER,
                            password=DATABASE_PASSWORD,
                            host=DATABASE_HOST,
                            port=DATABASE_PORT)

def getInfo(namehorse):
    conn = get_connection()
    cur = conn.cursor()
    command = '''
    SELECT horsename, text1, text2, text3, pic_url 
    FROM horsesinfo 
    WHERE horsename = '{namehorse}'
    LIMIT 1
    '''
    cur.execute(command.format(namehorse = namehorse))
    horseinfo = cur.fetchone()
    cur.close()
    conn.close()
    return horseinfo
def writeQ(username, phone, qtext):
    #Подключение к базе данных
    conn = get_connection()
    cur = conn.cursor()
    # Запись данных в таблицу questions
    command = '''
    INSERT INTO questions (username, phone, question) 
    VALUES ('{username}','{phone}','{qtext}')
    '''
    cur.execute(command.format(username=username, phone=phone, qtext = qtext))
    conn.commit()
    cur.close()
    conn.close()


horsename = "Мальчик"


def writePeople(date, time, fullname, phone, numofpeople):
    global horsename
    horse = horsename
    condates = datetime.strptime(date, "%d.%m.%Y").strftime("%Y-%m-%d")
    conn = get_connection()
    cur = conn.cursor()
    command =f'''
    INSERT INTO userinfo (fullname, phone, numofpeople)
VALUES ('{fullname}', '{phone}', '{numofpeople}')
ON CONFLICT (fullname) DO NOTHING
RETURNING user_id;
WITH horse_data AS (
    SELECT horse_id FROM horsesinfo WHERE horsename = '{horse}'
), date_data AS (
    SELECT date_id FROM datetable WHERE date_value = '{condates}'
), time_data AS (
    SELECT time_id FROM timetable WHERE time_value = '{time}'
)
INSERT INTO orders (horse, dateoforder, timeoforder, orderuser)
VALUES (
    (SELECT horse_id FROM horse_data),
    (SELECT date_id FROM date_data),
    (SELECT time_id FROM time_data),
    (SELECT user_id FROM userinfo WHERE fullname = '{fullname}')
)

    '''
    cur.execute(command)
    conn.commit()
    cur.close()
    conn.close()


def getDateList():
    conn = get_connection()
    cur = conn.cursor()
    command = '''
    SELECT date_value
    FROM datetable
    '''
    cur.execute(command)
    dates = cur.fetchall()
    cur.close()
    conn.close()
    for i in range(11):
        original_date = dates[i]
        date_value = original_date[0]
        formatted_date = date_value.strftime("%d.%m.%Y")
        dates[i] = formatted_date
    return dates


def getTimeList():
    conn = get_connection()
    cur = conn.cursor()
    command = '''
    SELECT time_value
    FROM timetable
    '''
    cur.execute(command)
    times = cur.fetchall()
    cur.close()
    conn.close()
    fixed_time = [item[0] for item in times]
    return fixed_time


def getDataTime(dates):
    global horsename
    conn = get_connection()
    cur = conn.cursor()
    command = '''
    SELECT datetable.date_value, timetable.time_value
    FROM orders
    INNER JOIN datetable ON dateOfOrder = datetable.date_id
    INNER JOIN timetable ON timeOfOrder = timetable.time_id
    INNER JOIN horsesinfo ON horse = horsesinfo.horse_id
    WHERE horsesinfo.horsename = '{horsename}'
    '''
    cur.execute(command.format(horsename = horsename))
    subnumber = cur.fetchall()
    cur.close()
    conn.close()
    number = [[1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1]]
    formsubnumber = [(date.strftime("%d.%m.%Y"), time) for date, time in subnumber]
    # Проходим полностью матрицу
    for j in range(10):
        for i in range(11):
            date = dates[i] if i > 0 else dates[0]
            time = "10:00-11:00" if j == 0 else f"{10 + j}:00-{11 + j}:00"
            # Проверяем, есть ли соответствующие данные в subnumber
            if (str(date), str(time)) in formsubnumber:
                number[j][i] = 2
    return number