from model.model import data_list
from http import HTTPStatus
from flask_restful import Resource
from model.model import Numbers
from logger import logger
import copy

class ModelResource(Resource):
    def get(self):
        copy_data_list =copy.deepcopy(data_list)
        logger.info('GET data_list')
        data = Numbers()
        data.order_data_list(copy_data_list, 0, len(copy_data_list) - 1)

        if data_list:
            response = {
                'total_items': len(copy_data_list),
                'numbers': copy_data_list}
        else:
            response = {'message': 'empty data list'}

        return response, HTTPStatus.OK






