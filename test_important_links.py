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
]
 

def check_pages(pages):
    try:
        for page_url in pages:
            code = urllib.urlopen(page_url).getcode()
            print "{0} - {1}".format(page_url, code)
            assert code in [200, 301]
    except socket.error, e:
        print "Connection Error: ", e
 
check_pages(site_urls)