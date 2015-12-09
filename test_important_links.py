"""
Test important links status codes
"""


import urllib, socket
 
site_urls = [
    'http://buymeapie.com/ru/',
    'http://buymeapie.com/en/',
    'http://buymeapie.com/zh/',
    'http://buymeapie.com/ja/',
    'http://buymeapie.com/de/',
    'http://buymeapie.com/fr/',
    'http://buymeapie.com/nl/',
    'http://buymeapie.com/es/',
    'http://buymeapie.com/pt/',
    'http://buymeapie.com/da/',
    'http://buymeapie.com/sv/',
    'http://buymeapie.com/it/',
    'http://buymeapie.com/lists',
    'http://buymeapie.com/about',
    'http://buymeapie.com/press',
    'http://buymeapie.com/contacts',
    'http://buymeapie.com/blog/en/',
    'http://buymeapie.com/blog/',
    'http://buymeapie.com/terms-of-use',
    'http://buymeapie.com/privacy',
    'http://buymeapie.com/ru/job',
    'http://m.buymeapie.com/lists',
    'http://m.buymeapie.com/authorization',
    'http://m.buymeapie.com/signup',
    'http://m.buymeapie.com/remember_pin',
    'http://m.buymeapie.com/ru/',
    'http://m.buymeapie.com/en/',
    'http://m.buymeapie.com/zh/',
    'http://m.buymeapie.com/ja/',
    'http://m.buymeapie.com/de/',
    'http://m.buymeapie.com/fr/',
    'http://m.buymeapie.com/nl/',
    'http://m.buymeapie.com/es/',
    'http://m.buymeapie.com/pt/',
    'http://m.buymeapie.com/da/',
    'http://m.buymeapie.com/sv/',
    'http://m.buymeapie.com/it/',
    'http://m.buymeapie.com/ru/about',
    'http://m.buymeapie.com/ru/job',
    'http://m.buymeapie.com/de/press'
]
 

def check_pages(pages):
    '''
    Check specified urls status codes
    :param pages:
    :return:
    :exception: if status code is not 200 and 301
    '''
    try:
        for page_url in pages:
            code = urllib.urlopen(page_url).getcode()
            print "{0} - {1}".format(page_url, code)
            assert code in [200, 301]
    except socket.error, e:
        print "Connection Error: ", e
 
check_pages(site_urls)