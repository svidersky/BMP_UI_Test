from internal_page import InternalPage
from model.elements_ids import *

class ListPage(InternalPage):
    """
    Elements' ids that are located in lists' management section
    """
    @property
    def field_add_product(self):
        return self.driver.find_element_by_id(input_product_id)

    @property
    def button_delete_list(self):
        return self.driver.find_element_by_id("button_delete_list")

    @property
    def button_add_list(self):
        return self.driver.find_element_by_id("button_add_list")

    @property
    def button_add_list(self):
        return self.driver.find_element_by_id("button_add_list")

    @property
    def button_edit_list(self):
        return self.driver.find_element_by_id("button_edit_list")

    @property
    def input_edit_list(self):
        return self.driver.find_element_by_id("input_edit_list")