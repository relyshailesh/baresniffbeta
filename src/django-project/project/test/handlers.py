from icetea.handlers import BaseHandler

class TestHandler(BaseHandler):
    read = True

    def read(self, request, *args, **kwargs):
        return "Hello world!"


