# MealSwipe
Goal: Using ML to help you discover new meals that you like

## Inspiration 

The inspiration of Meal swipe came because one of our members had an argument with his partner over choosing what to eat. Our team really connected with the struggle of picking the right restaurant and the right meal. What if instead of looking restaurant we could just pick the right meal before even tasting it. 

Trying new things and choosing the right meal can be difficult. Can we create an algorithm that introduces different meal options based on individual taste? 

## What it does 

Borrowing it's intuitive swipe interface from Tinder, MealSwipe allows users to decide what to eat quicker than ever without compromising on quality. With a simple swipe left or right, users can quickly browse through personalized recipe and restaurant recommendations and choose the ones that catch their eye, allowing MealSwipe to learn a user's taste to provide even better recommendations next time. 

The concept of MealSwipe is simple. Each meal can be boiled down into raw data, we can then compare meals to see if they have similar ingredients or taste based on ML techniques. Through swiping, we build a profile of the preferences of individual users and give out recommendations on meals.  

## How we built it 

We created a meal dataset using web scrapping techniques. For the prototype, we have separated the meal features into 13 features. 

MealSwipe uses item-based k-Nearest Neighbors (k-NN) algorithm to compare meals.
The item-based k-NN algorithm is a simple but effective way to make personalized recommendations based on item ratings. 

We also spent a lot of time experimenting with different algorithms to see which ones would work best for making personalized meal recommendations. The item-based k-Nearest Neighbors algorithm was ultimately chosen because of its simplicity and effectiveness, but we also considered other algorithms like collaborative filtering and matrix factorization.

In addition to using web scraping techniques to create the meal dataset and applying the item-based k-Nearest Neighbors algorithm to compare meals, we took other important steps to ensure that the MealSwipe project was a success. For example, we spent a lot of time researching the best tools and techniques for web scraping, data cleaning, and data analysis. This allowed us to create a high-quality dataset that was well-suited for the needs of the project.

Since we lacked front-end skills and experience, we looked for tools that were easy to use and beginner-friendly. As a result, we used Figma, a collaborative interface design tool. We are proud that our first-year students and first-time hackathon participants were able to pick up the interface quickly and produce a prototype in the time we had.



## Challenges we ran into 

We could not find the correct dataset containing the information that we can use in the ML algorithm. We had to web scape and clean multiple datasets.
In addition, our team does not have any experience in front-end app development.

Overall, building the MealSwipe project was a challenging but rewarding experience. We had to navigate technical challenges, design considerations, and user feedback, but we ultimately created a project that we are proud of and that has the potential to help people make healthier and more enjoyable meal choices.


## Accomplishments that we're proud of 

Not only did we create our own unique dataset, but we also created a ML algorithm

Apart from that, new members that entered UniHack this year without prior experience were able to learn new skills and technology and contribute in a meaningful way. 

## What we learned 

Different web scrapping techniques and different ML algorithms. 

## What's next for MealSwipe

The next step is to expand the dataset and do some user research.  
