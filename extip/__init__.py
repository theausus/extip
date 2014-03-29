import urllib.request
def main():
    url = 'http://ipecho.net/plain'
    url2 = 'http://ifconfig.me'
    try:
        f = urllib.request.urlretrieve(url)[0]
        f = open(f)
        html = f.read()
        f.close()
    except:
        try:
            f = urllib.request.urlretrieve(url2)[0]
            f = open(f)
            html = f.read()[:-1]
            f.close()
        except:
            html = 'Could not resolve external IP\nCheck network connection'
    return(html)
