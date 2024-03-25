import requests
from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import openpyxl
from time import sleep
import base64

# Your proxy key
'''
api_key = ''

response = requests.get(
    url='https://proxy.scrapeops.io/v1/',
    params={
        'api_key': api_key,
        'url': 'https://quotes.toscrape.com/',
    },
)

print('Response Body: ', response.content)
'''

# File name
workbook = openpyxl.load_workbook('house_list.xlsx')
# Page name
sheet_data = workbook['data']
# Column
house_list = []
# Row (iterate over the column = min_col1 to max_col1 and over the row min_row2 to max_row11)
for line in sheet_data.iter_rows(min_col=1, max_col=1, min_row=2, max_row=11):
    for cell in line:
        house_list.append(cell.value)


def start_driver():
    chrome_options = Options()

    arguments = ['--lang=en-us',
                 '--window-size=1920,1080', '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    prefs = {
        'profile.default_content_setting_values': {
            'cookies': 2,
            'notifications': 2,
            'automatic_downloads': 1
        }
    }

    chrome_options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = start_driver()

for house_list in house_list:
    driver.get(f'https://www.century21global.com/en/p/{house_list}')
    sleep(3)
    base64_string = driver.print_page()
    pdf_in_bytes = base64.b64decode(base64_string)

    # Formatting CNPJ
    format_house_list = house_list.replace(
        '.', ',').replace('-', '').replace('/', '')

    with open(f'./company data/{format_house_list}.pdf', 'wb') as file:
        file.write(pdf_in_bytes)
