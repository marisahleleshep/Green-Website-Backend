class Review:
    def __init__(self, customer_name, rating, comment):
        self.customer_name = customer_name
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
        
        
