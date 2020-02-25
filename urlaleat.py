#!/usr/bin/python3

import random
import webapp


class urlAleatApp(webapp.webApp):

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
        aleat = random.randint(0, 1000000)
        return ("200 OK", "<html><body><h1><a href = '" + str(aleat)
                + "'>Dame Otra</h1></body></html>")


if __name__ == "__main__":
    tetsWebApp = urlAleatApp("localhost", 1234)
