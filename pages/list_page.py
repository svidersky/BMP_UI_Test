from internal_page import InternalPage


class ListPage(InternalPage):

    @property
    def add_product_field(self):
        return self.driver.find_element_by_id("input_product")

