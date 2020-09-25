"""
This is an improved URL shortener
It takes the entire 140000 characters of Unicode to encode the short urls
It can reduce the length of the short urls to only 3 characters
"""

class urlShortener:
    # This is the counter of new url for encoding
    counter = 0
    # the latest one in the dictionary
    currentUrl = ''
    # use three dictionaries for storing the data
    # for one character url
    data1 = {}
    # for two character url
    data2 = {}
    # for three character url
    data3 = {}
    # total usable characters
    LIMIT = 140000
    
    # initialize
    def __init__(self, url):
        self.url = url
        self.shortUrl = self.encode(url)
        urlShortener.counter += 1
        urlShortener.currentUrl = url
        
    
    # encode function
    def encode(self, url):
        # one character for the first 140000 urls
        if urlShortener.counter < urlShortener.LIMIT:
            # check if a reused url
            if url not in urlShortener.data:
                # retrieve the current url data from the class
                currentU = urlShortener.currentUrl
                currentShortU = urlShortener.data[currentU]
                # if this is the first url in the one character dictionary
                if currentShortU == '':
                    newShortUrl = '!'
                # update the order of url from the current url data in the dictionary
                else:
                    newShortUOrder = ord(currentU)+1
                    # check if is readable
                    while not chr(newShortUOrder).isprintable():
                        newShortUOrder += 1
                    # get a new short url
                    newShortUrl = chr(newShortUOrder)
                # write the new url into the dictionary
                urlShortener.data1[url] = newShortUrl
            # return the new short url
            return urlShortener.data1[url]
        
        # two characters for the second 14000~14000**2
        elif urlShortener.counter < urlShortener.LIMIT**2:
            # check if a reused url
            if url not in urlShortener.data2:
                # retrieve the current url data from the class
                currentU = urlShortener.currentUrl
                currentShortU = urlShortener.data2[currentU]
                # if this is the first url in the two character dictionary
                if currentShortU == '':
                    newShortUrl = '!!'
                # update the order of url from the current url data in the dictionary
                else:
                    c1, c2 = currentShortU[0], currentShortU[1]
                    c1Order = ord(c1)
                    c2Order = ord(c2)
                    # check if the last character is under the limit
                    if ord(c2) < urlShortener.LIMIT:
                        # update the last character
                        c2Order += 1
                        while not chr(c2Order).isprintable():
                            c2Order += 1
                    # otherwise, need to update the first character and set the last character to 33
                    else:
                        c2Order = 33
                        c1Order += 1
                        while not chr(c1Order).isprintable():
                            c1Order += 1
                    # get the new short url
                    newShortUrl = chr(c1Order) + chr(c2Order)
                # write it into the dictionary
                urlShortener.data2[url] = newShortUrl
            # return the new short url
            return urlShortener.data2[url]
        
        # three character dictionary
        elif urlshortener.count < urlshortener.LIMIT**3:
            # check if a reused url
            if url not in urlShortener.data3:
                # retrieve the url data from the class
                currentU = urlShortener.currentUrl
                currentShortU = urlShortener.data3[currentU]
                # check if this is the first url in the three character dictionary
                if currentShortU == '':
                    newShortUrl = '!!!'
                # update the order of url from the current url data in the dictionary
                else:
                    c1, c2, c3 = currentShortU[0], currentShortU[1], currentShortU[2]
                    c1Order = ord(c1)
                    c2Order = ord(c2)
                    c3Order = ord(c3)
                    # check if the last character is under the limit
                    if c3Order < urlShortener.LIMIT:
                        # update the last character
                        c3Order += 1
                        while not chr(c3Order).isprintable():
                            c3Order += 1
                    # otherwise need to check the second character
                    else:
                        c3Order = 33
                        if c2Order < urlShortener.LIMIT:
                            # update the second character
                            c2Order += 1
                            while not chr(c2Order).isprintable():
                                c2Order += 1
                        # update the first character if both the last one and second one reach limit
                        else:
                            c2Order = 33
                            c1Order += 1
                            while not chr(c1Order).isprintable():
                                c1Order += 1
                    # get the new short url
                    newShortUrl = chr(c1Order) + chr(c2Order) + chr(c3Order)
                # write the new short url into the dictionary
                urlShortener.data3[url] = newShortUrl
            # return the new short url
            return urlShortener.data3[url]
        
