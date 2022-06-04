# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
#
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

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