import urllib.request
def main():
    url = 'http://ipecho.net/plain'
    url2 = 'http://ifconfig.me'
    try:
        f = urllib.request.urlopen(url)
        html = f.read().decode()
        f.close()
    except:
        try:
            f = urllib.request.urlopen(url2)
            html = f.read().decode()[:-1]
            f.close()
        except:
            html = 'Could not resolve external IP\nCheck network connection'
    return(html)
