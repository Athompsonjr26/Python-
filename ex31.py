print "you enter a dark room with two doors. Do you go through #1 or door #2"

door = raw_input("> ")

if door == "1":
    print "Theres a giant bear here eating a cheese cake."
    print "1. Take the cake"
    print "2. Scream at the bear"

    bear = raw_input("> ")

    if bear == "1":
        print "the bear eats face off"
    elif bear == "2":
        print "the bear eats you legs off"
    else:
        print "well doing %s is probably better. bear runs away." % bear

elif door == "2":
        print "you stare into the endless abyss at cthuulhu retina"
        print "1. blueberries"
        print "2. yellow jacket clothespins"
        print "3. understanding revolvers yelling melodies"

        instanity = raw_input("> ")

        if instanity == "1" or instanity == "2":
            print "your body survies"
        else:
            print "The instanity rots"

else:
    print "you stumble around"
