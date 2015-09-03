__author__ = 'fbidu'

BASE_URL = "https://github.com/github/gitignore/blob/master/"
GITIGNORE_URL = ""

def has_gitignore():
    import os
    return os.path.isfile("./.gitignore")


def get_https_response(host, path):
    import httplib
    conn = httplib.HTTPSConnection(host)
    conn.request('HEAD', path)
    response = conn.getresponse()
    conn.close()
    return response


def check_exists(url):
    from urlparse import urlparse
    response = get_https_response(urlparse(url).netloc, urlparse(url).path)
    return response.status == 200


def find_gitignore(language):
    if check_exists(BASE_URL+language+".gitignore"):
        global GITIGNORE_URL
        GITIGNORE_URL= BASE_URL+language+".gitignore"
        return True
    else:
        return False


def download_gitignore(url):
    import urllib
    print("Downloading " + url)
    retriever = urllib.URLopener()
    retriever.retrieve(url, ".gitignore")


def main():
    import sys
    print "Looking for .gitignore for " + str(sys.argv[1]) + "..."
    found = find_gitignore(str(sys.argv[1]))

    if found:
        print("Found gitignore!")

    print("Looking for a local .gitignore file...")
    has_local_gitignore = has_gitignore()

    if has_local_gitignore:
        print("Local .gitignore file found! Appending new file at the bottom")
    else:
        print("No local .gitignore file was found, creating a new one")
        download_gitignore(GITIGNORE_URL)


if __name__ == '__main__':
    main()