from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime
import bisect

def get_event(database: str):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    
    query = f'SELECT * FROM Events ORDER BY id DESC LIMIT 1'
    cursor.execute(query)
    events = cursor.fetchone()

    connection.close()

    return list(events) if events else []


def sort_event(html_page: str):
    with open(html_page, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')

    all_dates = soup.find_all('h3', class_='date')
    dates = [datetime.strptime(elem.text.strip(), '%Y-%m-%d') for elem in all_dates]

    # sorted_dates = sorted(dates, key=lambda date: datetime.strptime(date, '%Y-%m-%d'))
    return sorted(dates)



def add_event_for_calendar(html_page: str, event: list[str]):
    date = event[1]
    month = date.split('-')[1]
    start_time = event[2]
    end_time = event[3]
    name_event = event[4]
    city = event[5]
    tags = event[6]
    location = event[9]

    sorted_dates = sort_event(html_page)
    new_date_obj = datetime.strptime(date, '%Y-%m-%d')
    bisect.insort(sorted_dates, new_date_obj)
    sorted_dates_str = [date_obj.strftime('%Y-%m-%d') for date_obj in sorted_dates]
    # print(sorted_dates_str)
    month_dates = [date for date in sorted_dates_str if date[5:7] == month]
    index = month_dates.index(date)

    with open(html_page, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')

    old_tag = soup.find(id=month)
    new_tag = soup.new_tag("div", class_="event")
    event_html = f"""
        <b><h3 class="date">{date}</h3></b>
        <p>Мероприятие {name_event} будет проходить в городе {city}</p>
        <p>Место проведения: {location}</p>
        <p>Начало мероприятия: {start_time}</p>
        <p>Конец мероприятия: {end_time}</p>
        <p>Интересы: {tags}</p>
        <hr/>
    """
    parced_html = BeautifulSoup(event_html, 'html.parser')
    new_tag.append(parced_html)
    old_tag.insert(index, new_tag)
    with open(html_page, 'w', encoding='utf-8') as file:
        file.write(str(soup))




if __name__ == '__main__':
    
    database = './db/DB1.db'
    event = get_event(database)
    page = './calendar.html'

    add_event_for_calendar(page, event)
    # sort_event(page)


