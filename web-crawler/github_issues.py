from bs4 import BeautifulSoup
import requests

input_url = input("Enter GitHub Repository: ") or 'https://github.com/freeCodeCamp/chapter/'
res = ''
count = 1
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
    tags = soup.find_all('span')

    # Contents from the <span> tags.
    for tag in tags:
        # if class attribute is the issue title
        if tag.get('class') == ['js-issue-title']:
            res = tag.text.strip()
    print('Issue# ' + str(count) + ' - ' + res)
    if res == '':
      break
    res = ''
    count += 1
