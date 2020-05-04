import http.client
import urllib.parse


def call_get():
    conn = http.client.HTTPSConnection("www.python.org")
    conn.request("HEAD", "/")
    res = conn.getresponse()
    print(res.status, res.reason)
    data = res.read()
    print(data)
    conn.close()


def call_post():
    params = urllib.parse.urlencode(
        {'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = http.client.HTTPConnection("bugs.python.org")
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data)
    conn.close()


def call_put():
    BODY = "***filecontents***"
    conn = http.client.HTTPConnection("localhost", 8080)
    conn.request("PUT", "/file", BODY)
    response = conn.getresponse()
    print(response.status, response.reason)
    conn.close()
