"""
This is a improved URL shortener
It takes the 140000 characters of Unicode to encode original urls to short urls
It can reduce the length of the urls to only 3 characters
Author: David Zhang
Version: 0.1
Date: October 20, 2020
"""

# use the entire unicode data
import unicodedata

class urlShortener:
    # This is the order number of new url for encoding in the class
    counter = 0
    currentUrl = ''
    # use six dictionaries for storing the data
    # first dictionary is for one character url, the keys are original urls
    data1 = {}
    # the partner of data1, the keys are short urls
    coData1 = {}
    # for two character url, the keys are original urls
    data2 = {}
    # the partner of data2, the keys are short urls
    coData2 ={}
    # for three character url, the keys are original urls
    data3 = {}
    # the partner of data3, the keys are short urls
    coData3 = {}
    # total usable characters
    LIMIT = 140000

    # initialize
    def __init__(self, url):
        # remove the spaces at the beginning and at the end of the url
        url = url.strip()
        # if url is a long string, convert it to a short one
        if len(url.strip())>3:
            self.originalUrl = url
            self.shortUrl = self.encode(url)
        # if url is a short one, find its original form
        else: 
            self.shortUrl = url
            self.originalUrl= self.decode(url)
        

    # encode function
    def encode(self, url):
        # one character for the first 140000 urls
        if urlShortener.counter < urlShortener.LIMIT:
            if url not in urlShortener.data1:
                if urlShortener.counter == 0:
                    newShortUrl = '!'
                else:
                    currentU = urlShortener.currentUrl
                    currentShortU = urlShortener.data1[currentU]
                    newShortUOrder = ord(currentShortU)+1
                    while not chr(newShortUOrder).isprintable():
                        newShortUOrder += 1
                    newShortUrl = chr(newShortUOrder)
                urlShortener.counter += 1
                urlShortener.data1[url] = newShortUrl
                urlShortener.coData1[newShortUrl] = url
                urlShortener.currentUrl = url
            return urlShortener.data1[url]

        # two characters for the second 14000~14000**2
        elif urlShortener.counter < urlShortener.LIMIT**2:
            # check if a reused url
            if url not in urlShortener.data2:
                if urlShortener.counter == LIMIT:
                    newShortUrl = '!!'
                else:
                    currentU = urlShortener.currentUrl
                    currentShortU = urlShortener.data2[currentU]
                    c1, c2 = currentShortU[0], currentShortU[1]
                    c1Order = ord(c1)
                    c2Order = ord(c2)
                    if ord(c2) < urlShortener.LIMIT:
                        c2Order += 1
                        while not chr(c2Order).isprintable():
                            c2Order += 1
                    else:
                        c2Order = 33
                        c1Order += 1
                        while not chr(c1Order).isprintable():
                            c1Order += 1
                    newShortUrl = chr(c1Order) + chr(c2Order)
                urlShortener.data2[url] = newShortUrl
                urlShortener.counter += 1
                urlShortener.coData2[newShortUrl] = url
                urlShortener.currentUrl = url
            return urlShortener.data2[url]

        elif urlshortener.count < urlshortener.LIMIT**3:
            # check if a reused url
            if url not in urlShortener.data3:
                if urlShortener.counter == LIMIT**2:
                    newShortUrl = '!!!'
                else:
                    currentU = urlShortener.currentUrl
                    currentShortU = urlShortener.data3[currentU]
                    c1, c2, c3 = currentShortU[0], currentShortU[1], currentShortU[2]
                    c1Order = ord(c1)
                    c2Order = ord(c2)
                    c3Order = ord(c3)
                    if c3Order < urlShortener.LIMIT:
                        c3Order += 1
                        while not chr(c3Order).isprintable():
                            c3Order += 1
                    else:
                        c3Order = 33
                        if c2Order < urlShortener.LIMIT:
                            c2Order += 1
                            while not chr(c2Order).isprintable():
                                c2Order += 1
                        else:
                            c2Order = 33
                            c1Order += 1
                            while not chr(c1Order).isprintable():
                                c1Order += 1
                    newShortUrl = chr(c1Order) + chr(c2Order) + chr(c3Order)
                urlShortener.data3[url] = newShortUrl
                urlShortener.counter += 1
                urlShortener.coData3[newShortUrl] = url
                urlShortener.currentUrl = url
            return urlShortener.data3[url]
        
        
    # decode function
    def decode(self, url):
        # find the original url in the first dictionary with one character url
        if len(url) == 1:
            return urlShortener.coData1[url]
        # find the original url in the second dictionary with two character url
        elif len(url) == 2:
            return urlShortener.coData2[url]
        # find the original url in the third dictionary with three character url
        elif len(url) == 3:
            return urlShortener.coData3[url]

