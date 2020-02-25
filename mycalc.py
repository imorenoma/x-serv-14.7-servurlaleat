#!/usr/bin/python3

import random
import webapp
import operator

dic={"sumar":operator.add,
     "restar": operator.sub}

class Calc(webapp.webApp):

    def parse(self, request):

        resource = request.split('/')[1]
        _, operador, op1, op2 = resource.split('/')
        return operador, op1, op2

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
        operador, op1, op2 = parsedRequest
        result = dic[operador](float(op1), float(op2))

        return ("200 OK", "<html><body><h1><a href = '" + str(result)
                + "'>Dame Otra</h1></body></html>")


if __name__ == "__main__":
    tetsWebApp = Calc("localhost", 1234)
