# Write code below 💖

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Answer the following question using the number related to your choose")

q1 = int(input("""Do you like Dawn or Dusk?
    (1) Dawn
    (2) Dusk
    Choise: """))

if q1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif q1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input")

q2 = int(input("""When I’m dead, I want people to remember me as:
    (1) The Good
    (2) The Great
    (3) The Wise
    (4) The Bold
    Choise: """))

if q2 == 1:
    hufflepuff += 1
elif q2 == 2:
    slytherin += 1
elif q2 == 3:
    ravenclaw += 1
elif q2 == 4:
    gryffindor += 1
else:
    print("Wrong input")

q3 = int(input("""Which kind of instrument most pleases your ear?
    (1) The violin
    (2) The trumpet
    (3) The piano
    (4) The drum
    Choise: """))

if q3 == 1:
    slytherin += 1
elif q3 == 2:
    hufflepuff += 1
elif q3 == 3:
    ravenclaw += 1
elif q3 == 4:
    gryffindor += 1
else:
    print("Wrong input")


print("Gryffindor: " + str(gryffindor))
print("Ravenclaw: " + str(ravenclaw))
print("Hufflepuff: " + str(hufflepuff))
print("Slytherin: " + str(slytherin))

house_assigned = max(gryffindor, ravenclaw, hufflepuff, slytherin)

print("You have been assigned to : " )

if gryffindor == house_assigned:
    print('🦁 Gryffindor!')
elif ravenclaw == house_assigned:
    print('🦅 Ravenclaw!')
elif hufflepuff == house_assigned:
    print('🦡 Hufflepuff!')
else:
    print('🐍 Slytherin!')

