class NewString(str):

    def len(self):
        return len(self)

    def reverse(self):
        return self[::-1]

class Pizza:
    def __init__(self, size, ingredients, dough):
        self.size = size
        self.ingredients = ingredients
        self.dough = dough

    def cost(self):
        ingredient_cost = 1
        size_cost = {'small': 10, 'medium': 15, 'large': 20}
        dough_cost = {'normal': 0, 'gluten free': 3}
        total_cost = 0

        total_cost += size_cost[self.size]
        total_cost += dough_cost[self.dough]
        total_cost += len(self.ingredients * ingredient_cost)

        return total_cost
