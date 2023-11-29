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
         return list(set([review.restaurant().name() for review in self.reviews]))

    
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
                return customer.full_name()
        return None
      
    
    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_customers = [customer.full_name() for customer in cls.customers if customer.given_name() == given_name]
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
    
    def display_reviews(self):
        return [f"Review for {self.name()} by {review.customer().full_name()} - Rating: {review.rating()}" for review in self._reviews]

    def customers(self):
        return list(set([review.customer().full_name() for review in self._reviews]))
    
    
    
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
        self._restaurant.reviews().append(self)
        Review.add_rating(self)
       

    def rating(self):
        return self._rating
    
    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    @classmethod
    def add_rating(cls, rating):
        cls.reviews.append(rating)

    @classmethod
    def all_ratings(cls):
        print([rating.rating for rating in cls.reviews])

   

    @classmethod
    def show_all_reviews(cls):
      print([(review._customer.full_name(), review._restaurant.name(), review._rating) for review in cls.reviews])



print("....................Customer Concatenated Names ........................")   
customer1=Customer("Angela","Mithi")
print(customer1.full_name())
customer2=Customer("Natasha","Koskei")
print(customer2.full_name())
customer3=Customer("Natalie","Jerotich")
print(customer3.full_name())
customer4=Customer("Angela","Wangechi")
print(customer4.full_name())
print("....................All Customers.......................")
Customer.show_all_customers()
print("                                 ")
print(".............All Restaurant Names.........................")
restaurant1=Restaurant("Grand Regency")
print(restaurant1.name())
restaurant2=Restaurant("The Hilton")
print(restaurant2.name())
restaurant3=Restaurant("Sarova")
print(restaurant3.name())
print("                                 ")
print("...................All reviews..........................")
review1 = Review(customer1, restaurant1, 7)
review2 = Review(customer2, restaurant2, 9)
review3 = Review(customer3, restaurant1, 4)
review4 = Review(customer1, restaurant1, 8)
review5 = Review(customer1, restaurant2, 4)
review6 = Review(customer3, restaurant1, 5)
review7 = Review(customer1, restaurant3, 10)
review8 = Review(customer3, restaurant3, 6)

print(restaurant1.display_reviews())
print(restaurant2.display_reviews())
print(restaurant3.display_reviews())
print("                                 ")
print("..........Unique lists of all customers who have reviewed each restaurant..............")
print(restaurant1.name() + f" customers:", restaurant1.customers())
print(restaurant2.name() + f" customers:",restaurant2.customers())
print(restaurant3.name() + f" customers:",restaurant3.customers())
print("                                 ")
print("..............unique list of all restaurants a customer has reviewed.....................")
customer1.add_review(restaurant1, 7)
customer2.add_review(restaurant2, 9)
customer3.add_review(restaurant1, 4)
customer1.add_review(restaurant1, 8)

customer1.add_review(restaurant2, 3)
customer3.add_review(restaurant1, 10)
customer1.add_review(restaurant3, 10)
customer3.add_review(restaurant3, 6)

print(f"Restaurants reviewed by {customer1.full_name()}: {customer1.restaurants()}")
print(f"Restaurants reviewed by {customer2.full_name()}: {customer2.restaurants()}")
print(f"Restaurants reviewed by {customer3.full_name()}: {customer3.restaurants()}")

print("                                 ")
print('..............No of Reviews for each customer...................')
print(f"No of reviews for customer1 ", customer1.num_reviews())
print(f"No of reviews for customer2 ", customer2.num_reviews())
print(f"No of reviews for customer3 ", customer3.num_reviews())
print("                                 ")
print("..............Matching Names..................")
print(f"First Full Name that matches with (Angela Mithi):", Customer.find_by_name("Angela Mithi"))
print(f"First Full Name that matches with (Natasha Koskei):", Customer.find_by_name("Natasha Koskei"))
print(f"All customers with given name i.e.(Angela):", Customer.find_all_by_given_name("Angela"))
print("                                 ")
print("................Average rating for all restaurants...................")
print(f"Average Star Rating for Restaurant1", restaurant1.average_star_rating())
print(f"Average Star Rating for Restaurant2", restaurant2.average_star_rating())
print(f"Average Star Rating for Restaurant3", restaurant3.average_star_rating())


