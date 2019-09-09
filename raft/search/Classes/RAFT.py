class RAFT:
    
    def __init__(self, name, rating, num_reviews, location, categories, price):
        self.name = name
        self.rating = rating
        self.num_reviews = num_reviews

        self.price = price
        
        self.address = ' '.join(location['display_address'])
        self.city = location['city']
        self.state = location['state']
        self.zip_code = location['zip_code']
        
        self.categories = []
        for category in categories:
            self.categories.append(category['title'])