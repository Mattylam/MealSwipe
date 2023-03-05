import pandas as pd
import numpy as np
import random
from sklearn.metrics.pairwise import cosine_similarity
# Load the dataset
data = pd.read_csv('fooddata2.csv', index_col=0)

# Encode the attributes of each dish as feature vectors
features = data

# Compute the similarity matrix
similarity_matrix = cosine_similarity(features)

# Define a function to recommend similar dishes
def recommend_dishes(liked_dishes, n=5):
    # Compute the average feature vector of the liked dishes
    liked_dishes_vectors = np.stack([features.loc[dish] for dish in liked_dishes])
    avg_vector = np.mean(liked_dishes_vectors, axis=0)

    # Compute the similarity scores between the average vector and all other dishes
    similarity_scores = list(enumerate(cosine_similarity([avg_vector], features)[0]))

    # Sort the dishes by their similarity scores
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Select the top n most similar dishes
    top_dishes = similarity_scores[1:n+1]

    # Return the names of the top n most similar dishes
    return [data.iloc[i[0]].name for i in top_dishes]

# Example usage: recommend similar dishes to a set of liked dishes
#liked_dishes = ['Kung Pao Chicken', 'Hot Pot', 'Ramen', 'Bibimbap', 'Nasi Goreng']
#recommendations = recommend_dishes(liked_dishes)

# create the display scene for demonstrative purposes

# create the list of food and randomly generate until user likes 5 dishes
food = data.index.values.tolist()
def displayfood(food):
    random_element = random.choice(food)
    print("Randomly selected element:", random_element)
    food.remove(random_element)

count = 0
liked_dishes = []

while count < 5:
    random_element = random.choice(food)
    print("Displaying food:", random_element)
    response = input("Do you like this dish? (yes/no) ")
    if response == "yes":
        count += 1
        print("Your choice is recorded")
        liked_dishes.append(random_element)
        food.remove(random_element)
    else:
        print("dislike")
        food.remove(random_element)

    print("You have chosen:", count)

print("5 count reached. Calculating your preference.")
recommendations = recommend_dishes(liked_dishes)
print(recommendations)


