import sys
from random import choice
emojis = {" " : [":sonicrun1:", ":sonicrun2:", ":sonicrun3:", ":sonicrun4:", ":sonicrun5:", ":sonicrun6:", ":sonicrun7:", ":sonicrun8:"],
"A" : [":afc:", ":afx:", ":a:"],
"AC" : [":ac:"],
"B" : [":nhl-bos:"],
"C" : [":cuecat:", ":cubs:", ":bears:", ":nhl-cgy:", ":numbermuncher:"],
"CR" : [":rockies:"],
"D" : [":broncosd:"],
"DC" : [":dc:"],
"E" : [":google:", ":erlang:", ":e:"],
"ERE" : [":ere:"],
"F" : [":falcons:"],
"F" : [":fortnite:", ":F:"],
"FC" : [":fcc:"],
"G" : [":googleg:", ":packers:"],
"GAY" : [":gay:"],
"H" : [":hilldawg:"],
"HP" : [":hpsauce:"],
"HUT" : [":hut:"],
"I" : [":bolt:", ":guillotine:", ":middle_finger:"],
"J" : [":jalopnik:"],
"KC" : [":royals:"],
"L" : [":aslol:"],
"M" : [":graph:", ":motorola:", ":tori:"],
"N" : [":butt:", ":n"],
"NY" : [":giants:"],
"O" : [":0:", ":amiga:", ":awesome:", ":bloomin:", ":nhl-wpg:"],
"OO" : [":lemniscate:"],
"OWO" : [":owo:"],
"Q" : [":quicktime:"],
"R" : [":r:", ":buffering:", ":rainier:"],
"S" : [":s:"],
"SN" : [":gettin:"],
"T" : [":test3:", ":shroom:", ":timbers:", ":tronc:"],
"U" : [":u:", ":colts:", ":hanukkah:"],
"UK" : [":cayuts:"],
"V" : [":bong:"],
"W" : [":kenwood:", ":wutang:"],
"X" : [":x:"],
"Y" : [":louise:", ":y:"]}

def process(s):
	solutions = []
	def process(accumulated, remaining):
		#print "accumulated:" + str(accumulated)
		#print "remaining:" + str(remaining)
		if len(remaining) == 0:
			solutions.append(" ".join(accumulated))
			return

		def symbolicate(letters):
			if remaining.startswith(letters):
				return process(accumulated + [choice(emojis[letters])], remaining[len(letters):])

		for emoji in emojis.keys():
			symbolicate(emoji)

	process([], s.upper())

	shortest = min([len(x) for x in solutions])
	solutions = [x for x in solutions if len(x) == shortest]
	if len(solutions) > 0:
		return choice(solutions)

print process(sys.argv[1])
