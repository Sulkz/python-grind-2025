class Product:
    def __init__(self, sku, name, quantity, unit_price, category):
        self.sku = sku
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
        self.category = category
        
class InventoryManager:
    def __init__(self):
        self.stock = dict()
        
    def add_product(self, sku, name, quantity, unit_price, category):
        if sku in self.stock:
            return " sku already exists"
        if not isinstance(name, str) or name.strip() != "":
            return "name has to be string"
        if not isinstance(category, str) or category.strip() != "":
            return "category has to be string"
        if not isinstance(quantity, int):
            return "quantity has to be an int"
        if not isinstance(unit_price, float):
            return "unit_price has to be a float"
        product = Product(sku, name, quantity, unit_price, category)
        self.stock[sku] = product
        return "product added"
    
    def remove_product(self, sku):
        if sku in self.stock:
            del self.stock[sku]
            return "product removed"
        return "product doesnt exist"
    
    def update_stock(self, sku, quantity_change):
        if not isinstance(quantity_change, int):
            return "quantity_ change has to be int"
        
        if sku in self.stock:
            product = self.stock[sku]
            new_quantity = product.quantity + quantity_change
            if new_quantity < 0 :
                product.quantity = 0
                return "product is out of stock"
            product.quantity = new_quantity
            return f"product: {sku}, quantity: {product.quantity}"
        return "sku not in does not exist"
            
    def get_product(self, sku):
        if sku.lower() in self.stock:
            product = self.stock[sku]
        return {
                "product": {product.sku},
                "name": {product.name},
                "quantity": {product.quantity},
                "unit_price": {product.unit_price},
                "category": {product.category}
                }
        
        
    def list_products(self):
        for _, prod_obj in self.stock.items():
            return f"product: {prod_obj.sku},{prod_obj.name},{prod_obj.quantity},{prod_obj.unit_price},{prod_obj.category}"
        
    def list_low_stock(self, threshold):
        
        for _, product_object in self.stock.items():
            if product_object.qauntity <= threshold:
                return f"product: {product_object.sku}, quantity: {product_object.quantity}"
            else:
                return "no products quantity is lower than {threshold}"

            
            
    def total_value(self):
        total = 0
        for _, product_object in self.stock.items():
            total += product_object.quantity * product_object.unit_price
        return float(total)