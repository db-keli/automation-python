#! /usr/bin/env python3

# multidownloadXkcd.py - Downloads XKCD comics using multiple threads

import requests
import os
import bs4
import threading

os.makedirs('xkcd', exist_ok=True)


def downloadxkcd(startcomic, endcomic):
    for urlNumber in range(startcomic, endcomic):
        print('Downloading page http://xkcd.com/%s...' % urlNumber)
        res = requests.get('http://xkcd.com/%s' % urlNumber, 'lxml')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'lxml')

        comic_elem = soup.select('#comic img')

        if not comic_elem:
            print('Could not find image')

        else:
            comic_url = comic_elem[0].get('src')
            comic_url = f"https:/{comic_url}"
            print('Downloading Image')
            res = requests.get(comic_url)
            res.raise_for_status()

            # saving image to ./xkcd

            image = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image.write(chunk)
            image.close()
            
downloadxkcd(1, 2)
# download_threads = []
# for i in range(0, 1400, 100):
#     download_thread = threading.Thread(target=downloadxkcd, args=(i, i+99))
#     download_threads.append(download_thread)
#     download_thread.start()

# for download_thread in download_threads:
#     download_thread.join()

print('Done')
