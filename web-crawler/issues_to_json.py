from bs4 import BeautifulSoup
import requests
import datetime
from datetime import datetime
import json

def days_between(d1, d2):

    d1 = datetime.strptime(d1, '%b %d, %Y')
    d2 = datetime.strptime(d2, '%b %d, %Y')
    return abs((d2 - d1).days)

my_dict = {}
input_url = input("Enter GitHub Repository: ") or 'https://github.com/freeCodeCamp/chapter/'
res = ''
count = 270
while True:
    has_no_content = False
    url = "{}/issues/{}".format(input_url, count)

    # Getting the webpage, creating a Response object.
    response = requests.get(url)

    # Extracting the source code of the page.
    data = response.text

    # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
    soup = BeautifulSoup(data, 'lxml')

    # Extracting all the <span> tags into a list.
    spans = soup.find_all('span')

    # Contents from the <span> tags.
    for span in spans:
        # if class attribute is the issue title
        if span.get('class') == ['js-issue-title']:
            res = span.text.strip()
    if res == '':
      break
    divs = soup.find_all('div')
    for div in divs:
        if div.get('class') == ['TableObject-item']:
            status = div.text.strip()
            print(status)
    relative_times = soup.find_all('relative-time')
    days = str(days_between(relative_times[0].text,relative_times[-1].text))
    print('Issue# ' + str(count) + ' - ' + res)
    print('Opened at ' + relative_times[0].text)       # output: mmm-dd-yyyy i.e. Oct 15, 2019
    print('Last comment at ' + relative_times[-1].text)
    print('Running days: ' + str(days))
    print('status: ' + status)
    # dictionary not working currently
    if str(count) not in my_dict:
        my_dict[str(count)] = {
            'title': res,
            'start': relative_times[0].text,
            'end': relative_times[-1].text,
            'days': days,
            'status': status
        }
    elif my_dict[str(count)].status != status or my_dict[str(count)].status == '':
        my_dict[str(count)].status = status
        my_dict[str(count)].end = relative_times[-1].text
        my_dict[str(count)].days = days
    res = ''
    count += 1

filename = input_url.split('/')[-2]
with open(filename+'.json', 'w') as f:
    json.dump(my_dict, f, ensure_ascii=False, indent=4)
