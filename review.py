from customer_order import customer_name

class Review:
    def __init__(self, rating, comment):
        self.rating = rating
        self.comment = comment

    def display_review(self):
        print(f"Customer: {self.customer_name}")
        print(f"Rating: {self.rating}")
        print(f"Comment: {self.comment}")
      
        
        
        # Create a review object
customer_review = Review("Jirani", 3.5, "Great quality fruits and vegetables!")

# Display the review details
customer_review.display_review()
        
        
