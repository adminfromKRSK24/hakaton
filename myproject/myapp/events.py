from bs4 import BeautifulSoup
import sqlite3

def get_event(database: str):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    
    query = f'SELECT * FROM Events ORDER BY id DESC LIMIT 1'
    cursor.execute(query)
    events = cursor.fetchone()

    connection.close()

    return list(events) if events else []


def add_event_for_calendar(html_page: str, event: list[str]):
    date = event[1]
    start_time = event[2]
    end_time = event[3]
    name_event = event[4]
    city = event[5]
    tags = event[6]
    location = event[9]

    with open(html_page, 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')

    old_tag = soup.body
    new_tag = soup.new_tag("div", class_="event")
    event_html = f"""
        <b><h3>{date}</h3></b>
        <p>Мероприятие {name_event} будет проходить в городе {city}</p>
        <p>Место проведения: {location}</p>
        <p>Начало мероприятия: {start_time}</p>
        <p>Конец мероприятия: {end_time}</p>
        <p>Интересы: {tags}</p>
        <hr/>
    """
    parced_html = BeautifulSoup(event_html, 'html.parser')
    new_tag.append(parced_html)
    old_tag.insert(-2, new_tag)
    with open(html_page, 'w', encoding='utf-8') as file:
        file.write(str(soup))




if __name__ == '__main__':
    
    database = './bd/DB1.db'
    event = get_event(database)
    page = './event_list.html'

    add_event_for_calendar(page, event)


