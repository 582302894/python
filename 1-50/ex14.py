from sys import argv

script, user_name = argv
propmt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(propmt)

print "Where do you live %s" % user_name
lives = raw_input(propmt)

print "What kind of computer do you have?"
computer = raw_input(propmt)

print """
Alaright,so you said %s about liking me.
You live in %r, Not sure where that is.
And you have a %r coumputer. Nice.
""" % (likes, lives, computer)
