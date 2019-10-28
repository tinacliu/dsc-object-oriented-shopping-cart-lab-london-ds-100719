class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None, total=0):
      self.total = total
      self.employee_discount = emp_discount
      self.items = []

    def add_item(self, name, price, quantity=1):
      self.total += price * quantity
      for q in range(quantity):
        self.items.append({'name': name, 'price': price})
      return self.total

    def mean_item_price(self):
      return self.total/len(self.items)

    def median_item_price(self):
      prices = []
      for item in self.items:
        prices.append(item['price'])

      prices.sort()
      med = int((len(prices)-1)/2)
      if len(prices)%2:
        return prices[med]
      else:
        return (prices[int(len(prices)/2)] + prices[int(len(prices)/2-1)])/2

    def apply_discount(self):
      if self.employee_discount == None:
        return 'Sorry, there is no discount to apply to your cart :('
      else:
        disc_total = self.total * (1 - self.employee_discount/100)
        return disc_total

    def void_last_item(self):
      if self.items:
        rm_item = self.items.pop()
        self.total -= rm_item['price']
      else:
        'sorry, no more item in your basket'

