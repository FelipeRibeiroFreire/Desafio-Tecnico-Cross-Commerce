from logger import logger
import threading
import requests
import json

data_list = list()

class Numbers():

    page = 1
    url = (f"http://challenge.dienekes.com.br/api/numbers?page")

    def get_data_url(self):
        logger.info({'message': 'get data initiated'})
        while self.page:

            data_reponse = requests.get(f"{self.url}={self.page}")
            json_data = json.loads(data_reponse.content.decode('utf-8'))

            if json_data.get('numbers') == []:
                break
            try:
                data_list.extend(json_data.get('numbers'))

            except TypeError:
                logger.info({'message': f'page: {self.page} -> {json_data.get("error")}'})

                continue
            self.page += 1



    def partition_data_list(self, data, first, last):
        pivot = data[first]
        pivot_index = first

        last_index = last
        less_pivot_index = last_index

        greater_pivot_index = first+1

        while True:
            while data[greater_pivot_index] < pivot and greater_pivot_index < last:
                greater_pivot_index +=1

            while data[less_pivot_index] > pivot and less_pivot_index >= first:
                less_pivot_index -=1

            if greater_pivot_index < less_pivot_index:
                temp = data[greater_pivot_index]
                data[greater_pivot_index] = data[less_pivot_index]
                data[less_pivot_index] = temp
            else:
                break

        data[pivot_index] = data[less_pivot_index]
        data[less_pivot_index] = pivot
        return less_pivot_index

    def order_data_list(self,data_list, first, last):

        if last - first <= 0:
            return

        else:
            partition_point = self.partition_data_list(data_list, first, last)
            self.order_data_list(data_list, first, partition_point-1)
            self.order_data_list(data_list, partition_point+1, last)




numbers = Numbers()
threading_get_dados = threading.Thread(target = numbers.get_data_url)
