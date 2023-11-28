class Customer:
    customers = []
    

    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name
        self.reviews=[]
        Customer.add_customer_to_all(self)

    def given_name(self):
        return self.first_name

    def familyName(self):
        return self.family_name

    def full_name(self):
        return f"{self.first_name} {self.family_name}"
    
    def restaurants(self):
        return list(set([review.restaurant() for review in self.reviews]))
    
    def add_review(self, restaurant, rating):
          new_review = Review(self, restaurant, rating)
          self.reviews.append(new_review)
          restaurant.reviews().append(new_review)
          return new_review

    def num_reviews(self):
        return len(self.reviews)
    
    @classmethod    
    def find_by_name(cls,name):
        for customer in cls.customers:
            if customer.full_name()==name:
                return customer
            else:
                return None
      
    
    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_customers = [customer for customer in cls.customers if customer.given_name() == given_name]
        return matching_customers


    @classmethod
    def add_customer_to_all(cls, customer):
        cls.customers.append(customer)

    @classmethod
    def show_all_customers(cls):
        print([customer.full_name() for customer in cls.customers])


class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews = []

    def name(self):
        return self._name

    def reviews(self):
        return self._reviews

    def customers(self):
        return [review.customer() for review in self._reviews]
    
    def average_star_rating(self):
        if not self._reviews:
            return None  

        total_rating = sum(review.rating() for review in self._reviews)
        average_rating = total_rating / len(self._reviews)
        return average_rating
  



class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.add_rating(self)

    def rating(self):
        return self._rating

    @classmethod
    def add_rating(cls, rating):
        cls.reviews.append(rating)

    @classmethod
    def all_ratings(cls):
        print([rating.rating for rating in cls.reviews])

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant
    
customer1=Customer("Angela","Mithi")
print(customer1.full_name())
customer2=Customer("Natasha","Koskei")
print(customer2.full_name())
customer3=Customer("Natalie","Jerotich")
print(customer3.full_name())
Customer.show_all_customers()
restaurant1=Restaurant("Grand Regency")
print(restaurant1.name())
restaurant2=Restaurant("The Hilton")
print(restaurant2.name())

