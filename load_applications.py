#!/usr/bin/python3

import webbrowser

# opens chrome browser with urls specified in url_list
def open_browser():
    chrome_path = '/usr/bin/google-chrome'
    url_list = [ 'https://www.youtube.com',
        'https://www.hackerearth.com/challenges/',
        'https://github.com/johnythomas' ]

    for url in url_list:
        webbrowser.get(chrome_path).open(url)

def main():
    open_browser()

if __name__ == '__main__':
    main()
