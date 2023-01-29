from bs4 import BeautifulSoup
import requests

my_file_address = 'home.html'

with open(my_file_address, 'r') as my_file_contents:
    content = my_file_contents.read()

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.findAll('div', class_='card')

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')



