hangman0 = './hangman0.png'
hangman1 = './hangman1.png'
hangman2 = './hangman2.png'
hangman3 = './hangman3.png'
hangman4 = './hangman4.png'
hangman5 = './hangman5.png'

hangman_list = [hangman0, hangman1, hangman2, hangman3, hangman4, hangman5]

word_dict = {
	"animals":'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),

	"countries":'Afghanistan Albania Algeria Andorra Angola Argentina Armenia Australia Austria Azerbaijan Bahamas Bahrain Bangladesh Barbados Belarus Belgium Belize Benin Bhutan Bolivia Botswana Brazil Brunei Bulgaria Burma Burundi Cambodia Cameroon Canada Chad Chile China Cambodia Comoros Congo Croatia Cuba Cyprus Denmark Djibouti Dominica Ecuador Egypt Eritrea Estonia Ethiopia Fiji Finland France Gabon Georgia Germany Ghana Greece Grenada Guatemala Guinea Guyana Haiti Honduras Hungary Iceland India Indonesia Iran Iraq Ireland Israel Italy Jamaica Japan Jordan Kazakhstan Kenya Kiribati Kuwait Kyrgyzstan Laos Latvia Lebanon Lesotho Liberia Libya Liechtenstein Lithuania Luxembourg Macedonia Madagascar Malawi Malaysia Maldives Mali Malta Mauritania Mauritius Mexico Micronesia Moldova Monaco Mongolia Montenegro Morocco Mozambique Namibia Nauru Nepal Netherlands Nicaragua Niger Nigeria Norway Oman Pakistan Palau Panama Paraguay Peru Philippines Poland Portugal Qatar Romania Russia Rwanda Samoa Senegal Serbia Seychelles Singapore Slovakia Slovenia Somalia Spain Sudan Suriname Swaziland Sweden Switzerland Syria Tajikistan Tanzania Thailand Togo Tonga Tunisia Turkey Turkmenistan Tuvalu Uganda Ukraine Uruguay Uzbekistan Vanuatu Venezuela Vietnam Yemen Zambia Zimbabwe'.split(),

	"feelings":'acceptance admiration adoration affection afraid agitation agreeable aggressive aggravation agony alarm alienation amazement amusement anger angry anguish annoyance anticipation anxiety apprehension assertive assured astonishment attachment attraction awe beleaguered bewitched bitterness bliss blue boredom calculating calm capricious caring cautious charmed cheerful closeness compassion complacent compliant composed contempt conceited concerned content contentment crabby crazed crazy cross cruel defeated defiance delighted dependence depressed desire disappointment disapproval discontent disenchanted disgust disillusioned dislike dismay displeasure dissatisfied distraction distress disturbed dread eager earnest easy-going ecstasy ecstatic elation embarrassment emotion emotional enamored enchanted enjoyment enraged enraptured enthralled enthusiasm envious envy equanimity euphoria exasperation excited exhausted extroverted exuberant fascinated fatalistic fear fearful ferocity flummoxed flustered fondness fright frightened frustration furious fury generous glad gloating gloomy glum greedy grief grim grouchy grumpy guilt happiness happy harried homesick hopeless horror hostility humiliation hurt hysteria infatuated insecurity insulted interested introverted irritation isolation jaded jealous jittery jolliness jolly joviality jubilation joy keen kind kindhearted kindly laid back lazy like liking loathing lonely longing loneliness love lulled lust mad merry misery modesty mortification naughty neediness neglected nervous nirvana open optimism ornery outgoing outrage panic passion passive peaceful pensive pessimism pity placid pleased pride proud pushy quarrelsome queasy querulous quick-witted quiet quirky rage rapture rejection relief relieved remorse repentance resentment resigned revulsion roused sad sadness sarcastic sardonic satisfaction scared scorn self-assured self-congratulatory self-satisfied sentimentality serenity shame shock smug sorrow sorry spellbound spite stingy stoical stressed subdued submission suffering surprise sympathy tenderness tense terror threatening thrill timidity torment tranquil triumphant trust uncomfortable unhappiness unhappy upset vain vanity venal vengeful vexed vigilance vivacious wary watchfulness weariness weary woe wonder worried wrathful zeal zest'.split(),

	"shapes":'annulus arc asymmetry bipyramid cardioid circle cone crescent cube cuboid curve cylinder decagon disc dodecahedron dot ellipse ellipsoid gnomon heart helix heptagon hexaflexagon hexagon hexahedron hyperboloid hypersphere icosahedron interval kite line lozenge nonagon octagon octahedron orb oval paraboloid parallelepiped parallelogram pentagon plane point polygon polyhedra prism pyramid quadrilateral ray rectangle rhombus round sector semicircle shape shapeless sphere spheroid square star symmetry tetrahedron tesseract torus trapezium trapezoid triangle wedge'.split(),

	"sports":'aerobics archery badminton baseball basketball biathlon bicycling billiards bowling boxing canoeing crew cricket croquet cycling darts discus diving dodgeball fencing football frisbee golf gymnastics handball hanggliding hockey horseriding hurdle iceskating javelin jogging judo jumprope karate kayaking kite lacrosse luge netball orienteering paddling parasailing parkour pickleball pingpong polo pool racing racquetball rafting rockclimbing rollerskating rowing rugby running sailing scubadiving skating skiing sledding snorkling snowboarding snowshoeing soccer softball squash surfing swimming taekwondo tag tennis throwing toboggan track trampoline triathlon ultramarathon unicycle vault volleyball wakeboarding walking waterskiing weightlifting windsurfing wrestling'.split()
}

def guess_check(magic_word, guess, correct_guesses, wrong_guesses):
	if guess in (correct_guesses + wrong_guesses):
		return
	if guess in magic_word:
		for i in range(len(correct_guesses)):
			if magic_word[i] == guess:
				correct_guesses[i] = guess
	else:
		wrong_guesses.append(guess)