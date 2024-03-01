#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status using urlib package """

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html_content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(html_content)))
        print("\t- content: {}".format(html_content))
        print("\t- utf8 content: {}".format(html_content.decode('utf-8')))
