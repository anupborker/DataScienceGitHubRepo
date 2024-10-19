import random

# Sample reviews for different sentiments
positive_reviews = [
    "The product was excellent! I am very happy with my purchase.",
    "I had a fantastic experience with customer service.",
    "This is the best thing I've ever bought!",
    "Absolutely wonderful! Highly recommend to everyone.",
    "I'm so pleased with the results, will definitely buy again."
]

neutral_reviews = [
    "The product is okay, nothing special.",
    "Service was average and met my expectations.",
    "The item arrived on time.",
    "It's a decent product, neither good nor bad.",
    "I have no complaints, but nothing to rave about."
]

negative_reviews = [
    "I'm really disappointed with this purchase.",
    "The product broke after a week of use.",
    "Terrible customer service experience, will not return.",
    "This was a waste of money, I regret buying it.",
    "The item did not match the description at all."
]

# Combine all reviews
all_reviews = (
    random.sample(positive_reviews, 5) + 
    random.sample(neutral_reviews, 5) + 
    random.sample(negative_reviews, 5)
)

# Shuffle the reviews to mix sentiment types
random.shuffle(all_reviews)

# Write to the input.txt file
with open('input.txt', 'w') as file:
    for review in all_reviews:
        file.write(review + '\n')

print("input.txt has been created with sample reviews.")
