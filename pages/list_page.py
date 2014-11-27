from internal_page import InternalPage


class ListPage(InternalPage):

    @property
    def add_product_field(self):
        return self.driver.find_element_by_id("input_product")


    @property
    def test_product(self):
        return self.driver.find_element_by_id("//div[contains(@class,'product-item-title') and contains(text(),'Test')]")

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