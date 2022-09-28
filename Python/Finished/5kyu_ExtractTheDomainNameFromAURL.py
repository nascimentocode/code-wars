from urllib.parse import urlparse

def domain_name(url):
    if urlparse(url)[1] != '':
        host = urlparse(url)[1].split('.')
        if host[0] == 'www':
            return host[1]
        return host[0]
    else:
        host = urlparse(url)[2].split('.')
        if host[0] == 'www':
            return host[1]
        return host[0]