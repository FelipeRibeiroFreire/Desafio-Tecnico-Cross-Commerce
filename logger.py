import logging

logger = logging.getLogger("")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fh = logging.FileHandler("app.log")
fh.setFormatter(formatter)

std = logging.StreamHandler()
std.setFormatter(formatter)

# add handler to logger object
logger.addHandler(fh)
logger.addHandler(std)

logger.setLevel(logging.INFO)

class ResponseLoggerMiddleware(object):
    def process_response(self, req, resp,a,b):
        logger.info('{0} {1} {2}'.format(req.method, req.relative_uri, resp.status[:3]))


