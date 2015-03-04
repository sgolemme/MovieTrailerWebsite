import nominee
import fresh_tomatoes

#Create best picture category
americanSniper = nominee.Movie("American Sniper",
	"https://www.youtube.com/watch?v=99k3u9ay1gs",
	"http://ia.media-imdb.com/images/M/MV5BMTkxNzI3ODI4Nl5BMl5BanBnXkFtZTgwMjkwMjY4MjE@._V1_SX640_SY720_.jpg",
    False,
    "Clint Eastwood, Robert Lorenz, Andrew Lazar, Bradley Cooper and Peter Morgan",
    "Navy SEAL sniper Chris Kyle's pinpoint accuracy saves countless lives on the battlefield and turns him into a legend. Back home to his wife and kids after four tours of duty, however, Chris finds that it is the war he can't leave behind."
    )
birdman = nominee.Movie("Birdman",
	"https://www.youtube.com/watch?v=uJfLoE6hanc",
	"http://ia.media-imdb.com/images/M/MV5BODAzNDMxMzAxOV5BMl5BanBnXkFtZTgwMDMxMjA4MjE@._V1_SX640_SY720_.jpg",
	True,
	"Alejandro G. Iñárritu, John Lesher and James W. Skotchdopole",
	"A washed up actor, who once played an iconic superhero, battles his ego and attempts to recover his family, his career and himself in the days leading up to the opening of a Broadway play."	
	)
boyhood = nominee.Movie("Boyhood",
	"https://www.youtube.com/watch?v=Ys-mbHXyWX4",
	"http://ia.media-imdb.com/images/M/MV5BMTYzNDc2MDc0N15BMl5BanBnXkFtZTgwOTcwMDQ5MTE@._V1_SX640_SY720_.jpg",
	False,
	"Richard Linklater and Cathleen Sutherland",
	"The life of a young man, Mason, from age 5 to age 18.",
	)
grandBudapest = nominee.Movie("The Grand Budapest Hotel",
	"https://www.youtube.com/watch?v=1Fg5iWmQjwk",
	"http://ia.media-imdb.com/images/M/MV5BMzM5NjUxOTEyMl5BMl5BanBnXkFtZTgwNjEyMDM0MDE@._V1_SX214_AL_.jpg",
	False,
	"Wes Anderson, Scott Rudin, Steven Rales and Jeremy Dawson",
    "The adventures of Gustave H, a legendary concierge at a famous hotel from the fictional Republic of Zubrowka between the first and second World Wars, and Zero Moustafa, the lobby boy who becomes his most trusted friend."
    )
imitationGame = nominee.Movie("The Imitation Game",
	"https://www.youtube.com/watch?v=S5CjKEFb-sM",
	"http://ia.media-imdb.com/images/M/MV5BNDkwNTEyMzkzNl5BMl5BanBnXkFtZTgwNTAwNzk3MjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
	False,
	"Nora Grossman, Ido Ostrowsky and Teddy Schwarzman",
    "During World War II, mathematician Alan Turing tries to crack the enigma code with help from fellow mathematicians."
    )
selma = nominee.Movie("Selma",
	"https://www.youtube.com/watch?v=x6t7vVTxaic",
	"http://www.impawards.com/intl/uk/2014/posters/selma.jpg",
	False,
	"Christian Colson, Oprah Winfrey, Dede Gardner and Jeremy Kleiner",
    "A chronicle of Martin Luther King's campaign to secure equal voting rights via an epic march from Selma to Montgomery, Alabama in 1965."
    )
theoryOfEverything = nominee.Movie("The Theory of Everything",
	"https://www.youtube.com/watch?v=Salz7uGp72c",
	"http://ia.media-imdb.com/images/M/MV5BMTAwMTU4MDA3NDNeQTJeQWpwZ15BbWU4MDk4NTMxNTIx._V1_SX640_SY720_.jpg",
	False,
	"Tim Bevan, Eric Fellner, Lisa Bruce and Anthony McCarten",
    "The relationship between the famous physicist Stephen Hawking and his wife."
    )
whiplash = nominee.Movie("Whiplash",
	"https://www.youtube.com/watch?v=7d_jQycdQGo",
	"http://a.oscar.go.com/service/image/index/id/6fd3106f-6f2a-4afb-bda6-30c30716ecd1/dim/261x417.jpg",
	False,
	"Jason Blum, Helen Estabrook and David Lancaster",
    "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential."
    )

bestPicture = nominee.Category("Best Picture", [americanSniper, birdman, boyhood, grandBudapest, imitationGame, selma, theoryOfEverything,whiplash])

#Create lead actor category
carell = nominee.Actor("Steve Carell",
	"https://www.youtube.com/watch?v=qfaOOC4q5lQ",
	"http://a.oscar.go.com/service/image/index/id/bf50ea28-6b22-46c4-8b41-1643a75e4d37/dim/261x417.jpg",
	False,
	"Foxcatcher",
	"As John du Pont, Steve Carell plays an eccentric millionaire who invites an Olympic wrestler to live and train at his estate.",
	"This is the first Academy Award nomination for Steve Carell.")
cooper = nominee.Actor("Bradley Cooper",
	"https://www.youtube.com/watch?v=DPriqlw8KB8",
	"http://a.oscar.go.com/service/image/index/id/a59ee529-30fd-43d1-a21c-7b9f0adb969b/dim/261x417.jpg",
	False,
	"American Sniper",
	"Bradley Cooper plays Chris Kyle, a military marksman dealing with the stress and personal toll caused by his deployment as a sniper.",
	"Including his nomination this year as a Producer of Best Picture nominee AMERICAN SNIPER, this is the fourth Academy Award nomination for Bradley Cooper.")
cumberbatch = nominee.Actor("Benedict Cumberbatch",
	"https://www.youtube.com/watch?v=qu9ImFMLYxw",
	"http://a.oscar.go.com/service/image/index/id/bc69879a-8911-409a-9073-403f4d3dbe40/dim/261x417.jpg",
	False,
	"The Imitation Game",
	"Benedict Cumberbatch portrays Alan Turing, a brilliant mathematician working on a top secret project to crack the Nazis' encryption code.",
	"This is the first Academy Award nomination for Benedict Cumberbatch.")
keaton = nominee.Actor("Michael Keaton",
	"https://www.youtube.com/watch?v=VlQEuXIZyQ0",
	"http://a.oscar.go.com/service/image/index/id/41df1a31-b900-4edd-8706-7e48d36b6090/dim/261x417.jpg",
	False,
	"Birdman or (The Unexpected Virtue of Ignorance)",
	"Michael Keaton plays Riggan, an actor preparing to appear in a Broadway play, although he is best known for his portrayal of a popular superhero.",
	"This is the first Academy Award nomination for Michael Keaton.")
redmayne = nominee.Actor("Eddie Redmayne",
	"https://www.youtube.com/watch?v=mhSDcgdWam0",
	"http://a.oscar.go.com/service/image/index/id/9702ebba-504c-4b20-a161-04adb1dfb5f8/dim/261x417.jpg",
	True,
	"The Theory of Everything",
	"Eddie Redmayne plays Stephen Hawking, a brilliant young cosmologist who learns that he is suffering from a progressive motor neuron disease.",
	"This is the first Academy Award nomination for Eddie Redmayne.")

leadActor = nominee.Category("Actor - in a Leading Role", [carell, cooper, cumberbatch, keaton, redmayne])

#Create lead actress category
cotillard = nominee.Actor("Marion Cotillard",
	"https://www.youtube.com/watch?v=HWCaiIcN6lE",
	"http://a.oscar.go.com/service/image/index/id/23cc0c4d-1216-476f-8eb1-34be0fc7edd0/dim/261x417.jpg",
	False,
	"Two Days, One Night",
	"As Sandra, Marion Cotillard portrays a factory worker who has two days to convince her colleagues to forgo their bonuses so that she can keep her job.",
	"This is the second Academy Award nomination for Marion Cotillard.")
jones = nominee.Actor("Felicity Jones",
	"https://www.youtube.com/watch?v=EsrhiHij_Zg",
	"http://a.oscar.go.com/service/image/index/id/0c806fea-d35d-4906-9df8-c0ec497e0e56/dim/261x417.jpg",
	False,
	"The Theory of Everything",
	"Felicity Jones portrays Jane Hawking, a young woman whose love for a brilliant scientist helps him to defy the dire prognosis he has received.",
	"This is the first Academy Award nomination for Felicity Jones.")
moore = nominee.Actor("Julianne Moore",
	"https://www.youtube.com/watch?v=WuFjzAD4ank",
	"http://a.oscar.go.com/service/image/index/id/9d3edece-17f4-4f02-8f19-4dad945fc037/dim/261x417.jpg",
	True,
	"Still Alice",
	"As Alice Howland, Julianne Moore plays a college professor who learns that she is suffering from early-onset Alzheimer's disease.",
	"This is the fifth Academy Award nomination for Julianne Moore.")
pike = nominee.Actor("Rosamund Pike",
	"https://www.youtube.com/watch?v=8Ov7j9Ajnxk",
	"http://a.oscar.go.com/service/image/index/id/24cc7d59-8433-4664-ade3-77e77d24d2f6/dim/261x417.jpg",
	False,
	"Gone Girl",
	"Rosamund Pike plays Amy Dunne, a young wife whose disappearance causes suspicion to fall on her husband.",
	"This is the first Academy Award nomination for Rosamund Pike.")
witherspoon = nominee.Actor("Reese Witherspoon",
	"https://www.youtube.com/watch?v=vXmE_V5nS1g",
	"http://a.oscar.go.com/service/image/index/id/011c092c-c536-48f2-a3b1-736a7d3e6554/dim/261x417.jpg",
	False,
	"Wild",
	"Reese Witherspoon plays Cheryl, a young woman who attempts to reclaim control of her life by undertaking a thousand-mile hike along the Pacific Crest Trail.",
	"This is the second Academy Award nomination for Reese Witherspoon.")

leadActress = nominee.Category("Actress - in a Leading Role", [cotillard, jones, moore, pike, witherspoon])

#Create supporting actor category
duvall = nominee.Actor("Robert Duvall",
	"https://www.youtube.com/watch?v=mq1NUy_OrEM",
	"http://a.oscar.go.com/service/image/index/id/8e868466-f773-445c-8207-5912f886c3c7/dim/261x417.jpg",
	False,
	"The Judge",
	"As Joseph Palmer, Robert Duvall plays a self-righteous judge who finds he needs the help of his son, a ruthless defense attorney.",
	"This is the seventh Academy Award nomination for Robert Duvall.")
hawke = nominee.Actor("Ethan Hawke",
	"https://www.youtube.com/watch?v=wu-yKaX1ZDY",
	"http://a.oscar.go.com/service/image/index/id/b00a32e8-79da-4949-8980-8af40c22bacd/dim/261x417.jpg",
	False,
	"Boyhood",
	"Ethan Hawke plays a divorced father whose free-spirited lifestyle conflicts with his responsibility to his children.",
	"This is the fourth Academy Award nomination for Ethan Hawke.")
norton = nominee.Actor("Edward Norton",
	"https://www.youtube.com/watch?v=u26tUeVITCU",
	"http://a.oscar.go.com/service/image/index/id/7a302b32-69a8-49e5-a7b7-aa20584f98bb/dim/261x417.jpg",
	False,
	"Birdman or (The Unexpected Virtue of Ignorance",
	"Edward Norton plays Mike, an egotistical movie star who is cast in a Broadway play opposite a faded actor desperate for a comeback.",
	"This is the third Academy Award nomination for Edward Norton.")
ruffalo = nominee.Actor("Mark Ruffalo",
	"https://www.youtube.com/watch?v=tylVqa-NGeQ",
	"http://a.oscar.go.com/service/image/index/id/bb807168-d58f-4841-a487-ed8aeb5a1b52/dim/261x417.jpg",
	False,
	"Foxcatcher",
	"Mark Ruffalo portrays David Schultz, an Olympic wrestling champion and a devoted husband and father.",
	"This is the second Academy Award nomination for Mark Ruffalo.")
simmons = nominee.Actor("J.K. Simmons",
	"https://www.youtube.com/watch?v=xCRgTSak8o4",
	"http://a.oscar.go.com/service/image/index/id/d3091bd4-e8e6-4e2b-a64e-74a1b24c23e6/dim/261x417.jpg",
	True,
	"Whiplash",
	"As Fletcher, J.K. Simmons plays a music teacher who motivates his students through fear and humiliation.",
	"This is the first Academy Award nomination for J.K. Simmons.")

supportingActor = nominee.Category("Actor - in a Supporting Role", [duvall, hawke, norton, ruffalo, simmons])

#Create supporting actress category
arquette = nominee.Actor("Patricia Arquette",
	"https://www.youtube.com/watch?v=fxVRZ2Z2wR4",
	"http://a.oscar.go.com/service/image/index/id/a067093c-a928-4c2e-9a5c-747fd60588d0/dim/261x417.jpg",
	True,
	"Boyhood",
	"Patricia Arquette portrays a divorced mother struggling to make a life for herself and her two children.",
	"This is the first Academy Award nomination for Patricia Arquette.")
dern = nominee.Actor("Laura Dern",
	"https://www.youtube.com/watch?v=C856fNvsgCo",
	"http://a.oscar.go.com/service/image/index/id/55b25595-57ee-4d53-b344-5620faa593a1/dim/261x417.jpg",
	False,
	"Wild",
	"Laura Dern plays Bobbi, a single mother whose love for life becomes an inspiration for her troubled daughter.",
	"This is the second Academy Award nomination for Laura Dern.")
knightley = nominee.Actor("Kiera Knightley",
	"https://www.youtube.com/watch?v=g6HgVcNI2NA",
	"http://a.oscar.go.com/service/image/index/id/3f194410-5eaf-48d6-a20f-bd0be153146b/dim/261x417.jpg",
	False,
	"The Imitation Game",
	"As Joan Clarke, Keira Knightley plays a young woman with a talent for ciphers who finds herself part of a top secret group of code breakers during the Second World War.",
	"This is the second Academy Award nomination for Keira Knightley.")
stone = nominee.Actor("Emma Stone",
	"https://www.youtube.com/watch?v=tn48hUyFrKQ",
	"http://a.oscar.go.com/service/image/index/id/39dcb24e-9882-412d-804a-ce0cc5806055/dim/261x417.jpg",
	False,
	"Birdman or (The Unexpected Virtue of Ignorance",
	"Emma Stone portrays Sam, the sarcastic daughter of a movie star who mocks him for his efforts to be taken seriously as an actor.",
	"This is the first Academy Award nomination for Emma Stone.")
streep = nominee.Actor("Meryl Streep",
	"https://www.youtube.com/watch?v=hkNwYWN6BKc",
	"http://a.oscar.go.com/service/image/index/id/df89dd59-71b9-4141-9bb7-24bc76beb20c/dim/261x417.jpg",
	False,
	"Into the Woods",
	"Meryl Streep plays the Witch, a powerful sorceress who has placed a curse on a baker's family, yet cares tenderly for the child she once stole and keeps locked in a tower.",
	"This is the nineteenth Academy Award nomination for Meryl Streep.")

supportingActress = nominee.Category("Actress - in a Supporting Role", [arquette, dern, knightley, stone, streep])

#Create animated feature film 
bigHero6 = nominee.Movie("Big Hero 6",
	"https://www.youtube.com/watch?v=z3biFxZIJOQ",
	"http://a.oscar.go.com/service/image/index/id/78122228-1eeb-48e5-bf62-33036cdfb68f/dim/261x417.jpg?cb=112323",
    True,
    "Don Hall, Chris Williams and Roy Conli",
    "Fourteen-year-old science prodigy Hiro spends his time developing fighting robots for underground competitions until his older brother introduces him to an eccentric group of young inventors. When the talented misfits band together to fight a dangerous villain."
    )
boxtrolls = nominee.Movie("The Boxtrolls",
	"https://www.youtube.com/watch?v=Q2dFVnp5K0o",
	"http://a.oscar.go.com/service/image/index/id/52b60953-f99d-440e-8fed-ec8204fd58e3/dim/261x417.jpg?cb=6641364",
    False,
    "Anthony Stacchi, Graham Annable and Travis Knight",
    "In the city of Cheesebridge, a community of shy trolls lives in hiding, emerging only at night to scavenge anything the humans have left outdoors. When they take a human baby and raise him as one of their own."
    )
howToTrain = nominee.Movie("How to Train Your Dragon 2",
	"https://www.youtube.com/watch?v=Z9a4PvzlqoQ",
	"http://a.oscar.go.com/service/image/index/id/6f359c5b-7fce-4a57-ba27-0aec448d912c/dim/261x417.jpg",
    False,
    "Dean DeBlois and Bonnie Arnold",
    "Viking dragon tamer Hiccup is now a young man, but he retains his longing for new experiences and his bond with his beloved dragon, Toothless. After Hiccup and his girlfriend Astrid uncover a hidden dragon paradise."
    )
songSea = nominee.Movie("Song of the Sea",
	"https://www.youtube.com/watch?v=HgbXWt8kM5Q",
	"http://a.oscar.go.com/service/image/index/id/2c48f44b-a865-4727-8506-a7e876267195/dim/261x417.jpg?cb=54423",
    False,
    "Tomm Moore and Paul Young",
    "Saoirse and Ben live with their father, a lighthouse keeper, on a small island. Ben, who blames his sister for their mother's death, is unaware that Saoirse, like their mother, is a mythical sea creature known as a Selkie and is now the last of her kind."
    )
princessKaguya = nominee.Movie("The Tale of the Princess Kaguya",
	"https://www.youtube.com/watch?v=tM6hcHp0_kU",
	"http://a.oscar.go.com/service/image/index/id/c5363b96-ea57-407d-853b-b52beb0a9759/dim/261x417.jpg",
    False,
    "Isao Takahata and Yoshiaki Nishimura",
    "When a bamboo cutter named Okina finds a miniature infant inside a cane stalk, he brings her home to his wife, Ona, and she grows immediately to the size of a human baby. Called Princess by her adoptive parents."
    )

animatedFeature = nominee.Category("Animated Feature Film", [bigHero6, boxtrolls, howToTrain, songSea, princessKaguya])

#collection of all of the categories
oscars = [bestPicture, leadActor, leadActress, supportingActor, supportingActress, animatedFeature]
#generate the html page
fresh_tomatoes.open_movies_page(oscars)
