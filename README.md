# Kindling
Kindling is an online dating app that allows users to practice online dating without knowing the race of their partners. This way, users get to know more about their matches' personalities instead of rejecting them solely based on race.
Inspiration
After we realized how racially bias popular online dating apps were such as Tinder, we were inspired to create this app. Most online dating apps take into account race -whether it is an inputted race from the user or an underlying race from the profile picture- in their matchmaking algorithm. As a result, you are more likely to match with a certain race depending on your previous match history. Our goal was to create an app where people were able to judge others based on character and personality instead of rejecting them instantly based on superficial looks or ethnicity.

What it does
Kindling is an online dating app that allows users to practice online dating without knowing the race of their partners. This way, users get to know more about their matches' personalities instead of rejecting them solely based on race.

How we built it
Our app mainly makes use of two features. The first being a text filter for bios and messaging. We use the GLoVe python library to help train for word similarity and this allows us to determine which words are similar with ethnicity. We take those words and filter them out of the bios and messages. We use this same feature for bio similarity to determine how likely two users would be a good match.

The second feature is an image/video filter. It uses a large test data set in conjunction with neural networks to create an AI model for determining which part of the image is skin. We then take that part of the image and change its color so that it is impossible to determine which race that person is. We will use this feature for profile pictures, sending pictures, and video calls.

Challenges we ran into
One challenge we ran into was creating the neural network for the skin filter. Finding a good training dataset was hard but we eventually opted out of a clothing segmentation dataset. Afterward, we realized that the program would run for very long without producing great results. We decided to lower the resolution of our images for the model to train quicker.

Accomplishments that we're proud of
We were very proud of the image recognition program actually working despite all of the challenges we faced.

What we learned
We spent countless hours researching how word similarity and sentence similarity worked. It consisted of large vectors of different topics each word had associated with it. We also spent countless hours finding a dataset and running our neural network program. However, we believe that the time was well spent as we learned a lot about NLP or natural language processing and image recognition.

What's next for Kindling (online dating app)
We were mainly focused on the functionality of the program but not as much on its design and usability. We hope to improve on aspects of that in the future.
