def getUrlList(str):
    urls = []
    if str:
        urls = str.split(',')
        if '' in urls:
            urls.remove('')
    return urls
