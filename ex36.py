# search "# placeholder text" for spots where narration still needs to be added.

from sys import exit

def start():
    print '''After the grueling savagery of the trials, you're close to finding a lusus at
last. Now you just need to track down a beast appropriate to your hemotype.
What IS your hemotype, anyway?
(acceptable answers include rust, brown, yellow, arsenic, jade, teal, cerulean,
blue, indigo, violet, fuschia)'''
    hemotype = raw_input("> ")
    landtypes = ["rust", "brown", "yellow", "arsenic", "jade", "teal", "cerulan", "blue", "indigo"]
    
    if hemotype == "violet" or hemotype == "fuschia":
        print "A seadweller! Into the pool you go."
        print "You splash into the pool and swim out of the caverns, into the sea."
        print "Ah, the sea. Your rightful heritage!"
        seastart()
    elif hemotype in landtypes:
        print "A landdweller. Shoo, out through the caves with you."
    elif "red" in hemotype or "crimson" in hemotype or "scarlet" in hemotype:
        print "Oh dear. How did the auxiliatrices miss a mutant?"
        dead("The quick jab of a culling fork corrects that problem.")
    else:
        print "Ugh, how did something else sneak its way in with the proper trolls?"
        dead("At least you'll make a nice snack for the Mother Grub.")

def dead(why):
    print why, "Whoops."
    exit(0)

## SEADWELLER PATH starts here ##

def seastart():
    print "Will you swim up or down?"
    next = raw_input("> ")

# Here and later, most of the descriptive text occurs before moving to the next function/
# node; that way if the player inputs an answer that causes a repeat of the node, only 
# the prompt displays again, not all the flavor text.
    
    if "up" in next and not "down" in next:
        print "You swim up nearer to the surface."
        print "The water is sparkling and clear, this close to the surface."
    	print "Light filters down from above and illuminates tiny particles in the water."
        near_surface()
    elif "down" in next and not "up" in next:
        print "You swim down into the darker waters below."
        print "There's much less light down here, but you can make your way by other means."
        print "There is a cave here, and beyond that the water grows still deeper."
        darkwater()
    elif "up" in next and "down" in next:
        dead("You swim up and down in pointless circles until you attract the attention of a large and hungry fish.")
    else:
        print "Indecisiveness is hardly befitting royalty."
        seastart()

# Seadweller shallow-water path

def near_surface():
    print "Will you poke your head up above the surface, or explore the shallows?"
    next = raw_input("> ")
    
    if "surface" in next:
        dead("You peek out above the waves and are snatched up immediately by a hungry seagull.")
    elif "explore" in next:
        print "You swim further through the shimmering water. Your domain is beautiful."
        print "What's that? Up ahead you can see two great beasts engaged in combat."
        approach()
    else:
        print "At this rate all the good lusii will be taken by the time you decide."
        near_surface()

def approach():
    print "Obviously you want to get a closer look. But how close? Give me a number."
    next = raw_input("> ")
    
    try:
        how_close = float(next)
    except ValueError:
        print "Try again. A NUMBER."
        approach()
    
    if how_close <= 5:
        print "You dart in close, only %d feet from the action!" % how_close
        dead("A lashing tentacle whips out of the fray and shatters your little carapace.")
    elif how_close <= 20:
        print "At a comfortable distance of %d feet, you watch the combatants." % how_close
        print "The white seal at last emerges triumphant! It does a victory flip,"
        print "then notices you observing. It swims over to nose at you gently."
        print "You feel a sense of warmth and instinctive delight in its presence, and"
        print "latch on to one flipper. The seal will be a great lusus! You'll have"
        print "such fun together. Congratulations!"
        exit(0)
    elif how_close <= 40:
    #placeholder text
        print "Octopus ending"
        exit(0)
    else:
        print "That was exciting, but it would have been better if you'd been able to see more."
        print "Better get back on the hunt!"
        sea_start()

# Seadweller deeper-water path

def darkwater():
    print "Explore the cave, or swim deeper?"
    next = raw_input("> ")
    
    if "deeper" in next:
        print "Undeterred by the forbidding darkness, you swim still deeper."
        print "Down here it gets really, REALLY dark. But there's a glimmering light"
        print "over there in the distance."
        abyss()
    elif "explore" in next or "cave" in next:
        print "You can't resist exploring the cave. What if there's treasure?"
        print "Or monsters?"
        print "Or monster treasure?"
        eelcave()
    else:
        print "You haven't got all night, you know."
        darkwater()

def eelcave():
    print "To the left, you see something fluttering in an alcove. To the right, you"
    print "see something white tucked behind a rock. What will you do? Press 1 to"
    print "investigate the fluttering thing. Press 2 to investigate the white thing."
    print "Press 3 to leave the cave and seek your fortune elsewhere."
    next = raw_input("> ")
    
    if next == "1":
        print "The way it flutters is just so mesmerizing. You have to go look."
        print "You swim up into the alcove, drawn toward that flicker, fascinated."
        dead("...And an eel lunges out of hiding, gulping you down in one bite.")
    elif next == "2":
    #placeholder text
        print "Eel lusus ending"
        exit(0)
    elif next == "3":
        print "You decide to go back and rethink your strategy a bit."
        seastart()
    else:
        print "You never even see what it is that rushes up behind you. You barely"
        print "have time to feel it chomp down."
        dead("Probably a tasty morsel like you shouldn't have dawdled so much.")

def abyss():
    print "Should you rush to find out what it is?"
    next = raw_input("y/n> ")
    
    if next == "n":
    #placeholder text
        print "Benthic ending"
        exit(0)
    elif next == "y":
        dead("You rush toward the angler's lure. By the time you see teeth, it's too late.")
    else:
        print "Nobody is entirely sure what happened to you down in the deeps."
        dead("But you were never heard from again.")

## LANDDWELLER PATH starts here ##


## end of defs ##

start()