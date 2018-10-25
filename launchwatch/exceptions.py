""" LaunchWatch exceptions. """


class BotError(Exception):
    """ Exception to handle all scraping errors. """
    def __init__(self, response):
        """ Initialize BotError.

        Takes a requests.Response object, breaks into url, status code,
        text, etc. (everything useful)

        Arguments:
            response -- a requests.Response object
        
        """
        self.url = response.url
        self.status = response.status_code
        self.content = response.text

    @property
    def content(self):
        return str(self.content)

    @property
    def status(self):
        return int(self.status)


class ParseError(Exception):
    """ Exception to handle all parsing errors. """
    def __init__(self, response):
        """ Initialize ParseError.

        Takes a requests.Response object, breaks into url, status code,
        text, etc. (everything useful)

        Arguments:
            response -- a requests.Response object
        
        """
        self.url = response.url
        self.status = response.status_code
        self.content = response.text

    @property
    def content(self):
        return str(self.content)

    @property
    def status(self):
        return int(self.status)