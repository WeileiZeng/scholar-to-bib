import urllib
url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'


import urllib.request

with urllib.request.urlopen(url) as url:
    s = url.read()
    # I'm guessing this would output the html source code ?
    print(s)
