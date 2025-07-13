define c = Character('Coco', color="#310075")
define minu = Character('Minu', color="#309117")
define m = Character('Me', color="#00750c")
define r = Character('Raspberry', color="#920f5e")
define s = Character('Strudel', color="#753d0a")
image bg forest = "images/forest.png"
image bg doorclosed = im.Scale("images/doorclosed.png", 1920, 1080)
image bg dooropen = im.Scale("images/dooropen.png", 1920, 1080)
image bg teacounter = im.Scale("images/teacounter.png", 1920, 1080)
image bg market = im.Scale("images/market.png", 1920, 1080)
image bg strudelhouse = im.Scale("images/strudelhouse.png", 1920, 1080)
image bg cocohouse = im.Scale("images/cocohouse.png", 1920, 1080)
image bg yarn = im.Scale("images/yarn.png", 1920, 1080)

default present = ""
default teaboost = ""

label start:

    stop music fadeout 1.0

    scene bg doorclosed with fade

    "It's been a bit of a slow day."

    "As a cat in Pumpkinville, I guess most days tend to be fairly quiet."

    "But today I feel a bit more bored than usual."

    "Yawn... and a bit tired."

    play sound "audio/door.mp3"

    scene bg dooropen

    show cocosmile with dissolve

    c "Good morning, Lily!"

    play music "audio/nicesong.mp3"

    m "Oh, hello! This is a pleasant surprise!"

    "Hmm... when was the last time I saw Coco?"

    "Wow, it really has been a while."

    c "I was visiting the area while shopping, so I wanted to drop by for a visit."

    m "Come in and have some tea! We have a lot to catch up on."


    jump teascene

label teascene:

    stop music fadeout 1.0

    scene bg teacounter with fade

    "Hm, Coco said she wanted twilight green tea. I would have some too... but I'm afraid that's the last one."
    
    "Oh well. Which tea should I choose for myself?"

menu: 
    
    "Enchanted herbal mix: gives random energy boosts for a couple of days":
        $ teaboost = "energy"
        jump herbal
        
    "Fairydew brew: gives you extra sprinkles of luck for the rest of the day":
        $ teaboost = "luck"
        jump fairydew

    "Suspicious tea bag: who doesn't like a good surprise?":
        jump poison

label herbal:

    scene bg forest with fade

    m "Here's your tea!"

    c "Thank you!"

    m "*sips the tea*"

    "I'm feeling a bit more energetic already!"

    c "This is amazing!"

    "Wow, I'm glad she likes it so much!"

    jump invitation

label fairydew:

    scene bg forest with fade

    m "Here's your tea!"

    c "Thank you!"

    m "*sips the tea*"

    "Ha, who knows? Maybe something lucky will happen today."

    c "This is amazing!"

    "Wow, I'm glad she likes it so much!"

    jump invitation

label poison:

    scene bg forest with fade

    m "Here's your tea!"

    c "Thank you!"

    c "Are you feeling okay? You don't look too well."

    m "For some reason I feel a bit... drained."

    c "Um, what's that you're drinking?"

    m "Just some tea I found."

    c "Can I see it?"

    m "Yeah."

    c "*sniff*"

    c "Hey! This is Somnus Chamomile! Isn't that the strong sleep-inducing..."

    scene black with fade

    c "Uh, you awake?"

    m "Zzz... Zzz... Zzz..."

    c "Um... I guess I'll be on my way..."

    "..."

    "Well, you just had to go and choose the suspicious teabag, didn't you?"

    return

label invitation:

    c "Hey, did you know Strudel's birthday is tomorrow?"

    m "Wait, really? Oh no... I had it marked a week later in my calendar."

    m "Well, it's a good thing you told me!"

    c "We should go to the market together to get presents!"

    c "Oh yeah - a bunch of her friends are planning a surprise party too! We're going to decorate my place this evening and hang out."
    
    c "Do you want to join?"

menu:

    "Say yes.":
        jump market

    "Decline.":
        jump boringday


label boringday:

    scene bg forest with fade

    "Well, Coco left to buy a present."

    "Now, should I read that book I've been saying I'll read for a year?"

    "Or maybe paint something... or bake... or polish my wand..."

    scene black with fade

    pause 1.0

    scene bg forest with fade

    "There! I did everything I wanted to do."

    "I wonder if Coco and the others are having fun. I'm starting to regret saying no..."

    "Guess I'll never know whether today would've been fun."

    return

label market:

    c "Yay! Let's go to the market after we've finished the tea."

    scene black with fade

    pause 1.0

    scene bg market with fade

    m "Wow, so many new stalls have popped up since I last visited."

    c "I know, right? Cookies... mushrooms... poisons... eek, I'll get distracted. Stay on track. Present for Strudel."

    c "Hm.. I think I see a vase that she would love."

    c "Do you want to get that for Strudel? I think we can afford it if we split the cost."

    "Wow, that's a tough choice. She would definitely love that vase, but I heard her talking about wanting a new hat the other day."

menu:

    "Buy the vase and split the cost. If Coco can't afford it, it'll be nice to help out.":
        $ present = "vase"
        jump vasesplit
    
    "Say no and get your own present. It's not your problem anyways.":
        $ present = "hat"
        jump berude

    "Tell Coco about what you heard.":
        $ present = "hat"
        jump surprisedcoco

label vasesplit:

    c "Awesome!"

    scene black with fade

    pause 1.0

    scene bg market with fade

    m "It looks gorgeous."

    c "I know, right?"

    c "Ahh! I didn't even notice! We have to hurry. They're going to start decorating soon!"

    jump partyprep

label berude:

    m "Um, I think I'm good. I'll get my own present."

    c "Oh, okay."

    scene black with fade

    pause 1.0

    scene bg market with fade

    c "You got her a hat? Cool!"

    c "Ahh! I didn't even notice! We have to hurry. They're going to start decorating soon!"

    jump partyprep

label surprisedcoco:

    c "Whoa! I didn't know that."
    
    c "Let's both get her hats! I'm sure she'll love them."

    scene black with fade

    pause 1.0

    scene bg market with fade

    c "Haha, this one looks nice."

    c "Ahh! I didn't even notice! We have to hurry. They're going to start decorating soon!"

    jump partyprep

label partyprep:

    scene black with fade

    pause 1.0

    scene bg cocohouse with fade

    "Wow, all of her closest friends showed up!"

    r "Hello, Lily! I didn't know you were coming!"

    m "Hi!"

    r "I'm so glad to see you here! Everyone is so excited for Strudel's surprise tomorrow."

    m "Me too!"

    r "Hey, wait a minute... are you free tomorrow?"

    m "Well, yeah. Why?"

    r "Perfect! Could you be the one to bring Strudel to the surprise party?"

    m "Sure! That sounds like a load of fun."

    r "Perfect! Because everyone else mysteriously vanished when I asked."

    m "Ah. So I’m the backup backup plan. Got it."

    r "Hey! Everyone! We have a volunteer to help bring Strudel here."

    scene black with fade

    pause 1.0

    scene bg forest with fade

    r "Haha, everyone is super happy you could do it. Strudel really likes you."

    m "I'm happy to help too."

    scene black with fade

    "You help decorate and prepare for the party."

    jump yarnscene

label yarnscene:

    if teaboost == "luck":

        scene bg yarn with fade
        
        "Hm? What's this?"

        "Whoa, you found a magic yarnball on your way back home."

        "Guess a bit of extra luck really never hurts!"

        jump nextday

    elif teaboost == "energy":

        jump nextday

label nextday:

    scene bg doorclosed with fade

    m "Alright... time to get Strudel to the party without making her suspicious."

    m "Man, I feel kind of bad having to pretend that I forgot it was her birthday."

    m "Maybe cookies will help."

    scene black with fade

    pause 1.0

    scene bg strudelhouse with fade

    s "Oh! Lily! What brings you here so early?"

    m "Just out for a walk. Thought I’d stop by."

    s "A walk? At sunrise? Who are you and what have you done with Lily?"

    m "It’s not that weird! Just... clearing my head. Here, I brought cookies."

    s "You did? Huh. Alright, you're forgiven."

    m "Want to walk with me to the meadow? I heard something fun might be happening there today."

    "Uh oh, hope I didn't just ruin everything. Why did I say something fun?"

    "Okay, she doesn't seem to have caught on. Phew."

    s "Are we talking fun like last time? Because chasing enchanted squirrels is not my idea of fun."

    m "Less squirrels this time. I promise."

    s "Alright, alright. Lead the way, cookie-bringer."

    "Just act normal. Don’t ruin the surprise. Just act normal..."

    jump partyreveal

label partyreveal:
    s "Wait... why are we walking this way? I thought we were going to the meadow?"

    m "Uh... shortcut! Yeah. This way is faster."

    s "You're acting weird."

    m "No, I'm acting totally normal. So normal. Extremely normal."

    s "Now I know something’s up."

    m "Surprise!!!"

    r "Happy birthday, Strudel!"

    c "We decorated all morning!"

    minu "And we got your favorite cake!"

    s "Wait, what?! You all..."

    s "You planned this whole thing?!"

    m "We wanted it to be special."

    s "I can’t believe this... You really caught me off guard. I was worried everyone forgot my birthday. Thank you!"

    r "Group hug!!!"

    c "Speech! Speech!"

    s "As much as I'd love to deliver a speech, I'd say that birthday cake looks way more appetizing."

    c "Yayy! Cake time!"

    scene black with fade

    pause 1.0

    scene bg forest with fade

    c "I'm... stuffed, to be honest."

    c "Burp. Excuse me."

    s "Same. Yaaawn."

    s "I hate to say it, but I'm a tiny bit tired."

    minu "I might just fall asleep... right... here..."

    if teaboost == "energy":

        c "Lily still looks pretty jumpy, though."

        m "Do I?"

        "Must be the tea kicking in!"

        c "Wish I could say the same."

    elif teaboost == "luck":
        m "Me too."

    r "Hey, hey, hey. No falling asleep yet! We need to open presents!"

    s "That many? You guys didn't have to!"

    c "How could we not? I still use that mug you gifted me every day. Hey, are you crying?"

    s "Allergies. Anyways, let me open this one..."

    if present == "vase":
        s "I LOVE the vase!"
        
        "Wow, she must really like it... she put flowers in it right away."

    elif present == "hat":
        s "A hat? I've been wanting a new one for such a long time!! This is my favourite style, too!"
        
        "I knew it! Strudel put it on right away."
    
    r "Here's mine, hehe."

    s "Wow! Is this Mysticnip?!"

    r "Haha, yup."

    minu "I made you these pistachio cookies!"

    s "You know how much I love those!!! Minu, you're the best!"

    if teaboost == "luck":

        m "Oh yeah, I also found this yesterday! It's a magic yarn ball. I wanted to give it to you."

        c "A magic yarn ball? Sweet mother of pearl, that sounds epic."

        m "I tested it out. This thing glows when you pounce on it! And it always rolls just out of reach! It's the best."

        s "Lily! This is awesome!!! Thank you so much!"

    elif teaboost == "energy":

        jump partyaftermath


label partyaftermath:

    scene black with fade

    pause 1.0

    scene bg forest with fade

    c "Wow, I'm exhausted!"

    m "Yeah, me too."

    s "You really outdid yourselves with the decorations!"

    r "It was worth it! Today was, like, the best birthday party ever."

    minu "I know, right?"

    s "I'm so grateful to have such nice felines for friends."

    c "Right back to you, Strudel!"

    "Today really was an amazing day, wasn't it?"

    "I'm glad I made the choices I did!"

    scene black with fade

    play music "audio/ending.mp3"

    "THANK YOU FOR PLAYING!"

    pause 1.0

    return