guestList = ['seebass', 'sarkany', 'zest']
message = "To " + guestList[0].title() + ", want to eat something?...there be ice cream too!"
print(message)
message = "Hi " + guestList[1].title() + ", I'm making a fud, wanna join?"
print(message)
message = "Oi " + guestList[2].title() + ", making food, theres chicken nuggies if you want them?"
print(message)

message = "Unfortuntely " + guestList[2].title() + " can't make it, obviously MFF is more important than Chicken Nuggies!"
print(message)

guestList.remove('zest')
guestList.append('pixel')

message = "Hey " + guestList[2].title() + ", how do you fancy something to eat?"
print(message)
print()
print("Just letting everyone know, theres a bigger table available, so expect 3 more people coming to eat!")

guestList.insert(0, 'Mika')
guestList.insert(2, 'Fen')
guestList.append('Sanderson')
print(guestList)

message = "To " + guestList[0].title() + ", want to eat something?"
print(message)
message = "To " + guestList[1].title() + ", want to eat something?...there be ice cream too!"
print(message)
message = "To " + guestList[2].title() + ", want to eat something?"
print(message)
message = "To " + guestList[3].title() + ", want to eat something?"
print(message)
message = "To " + guestList[4].title() + ", want to eat something?"
print(message)
message = "To " + guestList[5].title() + ", want to eat something?"
print(message)
print()
print("Due to a fuck up, I can only invite 2 people")
