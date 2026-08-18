# Simple Movie Recommender

print("Answer yes or no:")

likes_action = input("Do you like action movies? ").lower() == "yes"
likes_comedy = input("Do you like comedy movies? ").lower() == "yes"

if likes_action:
    print("You might enjoy: John Wick or Mad Max.")
elif likes_comedy:
    print("You might enjoy: The Mask or Superbad.")
else:
    print("Try something new: Forrest Gump.")
