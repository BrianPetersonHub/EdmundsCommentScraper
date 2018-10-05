# 9/23/18
# Brian Peterson
# This program scrapes comment data from edmunds.com
# and outputs a json file

# To use, specify the discussion category as the index_url

import requests
from bs4 import BeautifulSoup
import re
import json

# URL to Tire forum
index_url = "https://forums.edmunds.com/discussions/tagged/x/tires-wheels"

# get the html for the index page
index_page = requests.get(index_url)

# grab the number of pages of forums
soup1 = BeautifulSoup(index_page.content, 'html.parser')
index_page_number_tags = soup1.find_all(class_=re.compile('Pager-p'))

if index_page_number_tags != []:
    index_last_page_number = int(index_page_number_tags[-1].getText())
else:
    index_last_page_number = 1

print("There are " + str(index_last_page_number) + " pages of forums")

data_by_page_by_forum_by_page = {}

# from each page
for i in range(1, index_last_page_number+1):
    # grab all of the URLs on the page
    index_page_num = requests.get(index_url + "/p" + str(i))
    soup2 = BeautifulSoup(index_page_num.content, 'html.parser')
    data_list_tags = soup2.find(class_="DataList Discussions")
    title_tags = data_list_tags.find_all(class_='Title')

    forum_urls = []
    for tag in title_tags:
        href_tag = tag.find('a')
        forum_urls.append(href_tag['href'])

    print(
        "    Collected " + str(len(forum_urls))
        + " urls from page number " + str(i)
        )

    data_by_forum_by_page = {}

    numberofforums = 0
    # for each forum
    for j in range(len(forum_urls)):
        # get number of pages in forum
        forum_index_url = forum_urls[j]
        forum_index_page = requests.get(forum_index_url)

        soup3 = BeautifulSoup(forum_index_page.content, 'html.parser')
        page_number_tags = soup3.find_all(class_=re.compile('Pager-p'))

        if page_number_tags != []:
            last_forum_page_num = int(page_number_tags[-1].getText())
        else:
            last_forum_page_num = 1

        print("        Forum " + str(j+1) + " has " + str(last_forum_page_num) + " pages")

        data_by_page = {}

        # for each page in a forum
        for k in range(1, last_forum_page_num+1):
            forum_page = requests.get(forum_index_url + "/p" + str(k))

            # collect the comments on this page
            soup = BeautifulSoup(forum_page.content, 'html.parser')
            user_content_tags = soup.find_all(class_="Message userContent")

            data_by_comment = {}
            num_of_comments = 0
            for tag in user_content_tags:

                # extracts text from block quotes
                comment = ''
                if tag.find('blockquote'):
                    try:
                        comment += tag.contents[2].strip()
                    except:
                        comment += ''
                else:
                    comment += tag.contents[0].strip()

                # if no blockquote, extract the text normally
                if comment == '':
                    comment = tag.getText()
                data_by_comment["comment" + str(num_of_comments+1)] = comment
                num_of_comments += 1

            data_by_page["page" + str(k)] = data_by_comment

            print(
                "            Collected " + str(num_of_comments)
                + " comments from Forum " + str(j+1)
                + ", page " + str(k)
                )

        data_by_forum_by_page["forum"+str(j+1)] = data_by_page

        print(
            "        Collected all comments from forum "
            + str(j+1) + " on page " + str(i)
            )

    data_by_page_by_forum_by_page["indexpage"+str(i)] = data_by_forum_by_page

    print("    Collected all forum message data for page " + str(i) + "\n")

print("Finished collecting data")
print("Exporting to JSON...")

with open("edmunds_comment_data.json", 'w') as out:
    json.dump(data_by_page_by_forum_by_page, out)
print("Export finished! :)")