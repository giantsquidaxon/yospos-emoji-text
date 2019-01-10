import sys, getopt
from random import choice
sanics = [":sonicrun1:", ":sonicrun2:", ":sonicrun3:", ":sonicrun4:", ":sonicrun5:", ":sonicrun6:", ":sonicrun7:", ":sonicrun8:"]
emojis = {" " : ["**SPACE**"],
"A" : [":afc:", ":afx:", ":a:"],
"AC" : [":ac:"],
"AT" : [":aplus:"],
"B" : [":nhl-bos:", ":mlb-bos:", ":bengals:"],
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
"K" : [":kde-bw:"],
"KC" : [":royals:"],
"L" : [":aslol:"],
"LA" : [":mlb-lad:", ":nhl-la:"],
"M" : [":graph:", ":motorola:", ":tori:", ":eminem:"],
"N" : [":butt:", ":n:"],
"NY" : [":giants:"],
"O" : [":0:", ":amiga:", ":awesome:", ":bloomin:", ":nhl-wpg:"],
"OO" : [":lemniscate:", ":eyes:"],
"OWO" : [":owo:"],
"P" : [":p:", ":pinterest:"],
"Q" : [":quicktime:"],
"R" : [":r:", ":buffering:", ":rainier:"],
"REAL" : [":realplayer:", ":real:"],
"S" : [":s:"],
"SN" : [":gettin:"],
"T" : [":test3:", ":shroom:", ":timbers:", ":tronc:", ":rippepperonis:", ":titans:"],
"U" : [":u:", ":colts:", ":hanukkah:"],
"UK" : [":cayuts:"],
"V" : [":bong:"],
"W" : [":kenwood:", ":wutang:"],
"X" : [":x:"],
"Y" : [":louise:", ":y:"],
"Z" : [":zilog:"]}

def process(s):
	solutions = []
	def process(accumulated, remaining):
		if len(remaining) == 0:
			solutions.append(accumulated)
			return

		def symbolicate(letters):
			if remaining.startswith(letters):
				process(accumulated + [choice(emojis[letters])], remaining[len(letters):])

		for emoji in emojis.keys():
			symbolicate(emoji)

	process([], s.upper())

	shortest = min([len(x) for x in solutions])
	solutions = [x for x in solutions if len(x) == shortest]
	if len(solutions) > 0:
		return choice(solutions)

def main(argv):
	sanic = False
	options, remainder = getopt.gnu_getopt(sys.argv[1:],"",["gofast"])
	for opt, arg in options:
		if opt == "--gofast":
			sanic = True
	text = " ".join(remainder)
	emojis = process(text)
	if sanic:
		for i in range(0,len(emojis)):
			if emojis[i]=="**SPACE**":
				emojis[i] = sanics[i % len(sanics)]
	else:
		emojis = [":nbsp:" if x=="**SPACE**" else x for x in emojis]
	print "".join(emojis)

if __name__ == '__main__':
    main(sys.argv[1:])
