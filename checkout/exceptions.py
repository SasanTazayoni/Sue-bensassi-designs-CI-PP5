class InsufficientStock(Exception):
    """ Raised when a product has insufficient stock to fulfil an order. """

    def __init__(self, product):
        self.product = product
        super().__init__(
            f'Insufficient stock for product {product.id} ({product.name}).'
        )
