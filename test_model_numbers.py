from model.model import Numbers, data_list

class TestModelNumbers:
    numbers = Numbers()
    def test_get_data_url(self):
        self.numbers.get_data_url()
    def test_order_data_list(self):
        self.numbers.order_data_list(data_list,0,len(data_list)-1)
