import random

fruits_list = ["apple","lemon"]
i = fruits_list[random.randint(0,1)]

link_fruits = "pictures/fruits/" + i + ".png"
# fruits = pygame.image.load(link_fruits)

print(i)
print(link_fruits)