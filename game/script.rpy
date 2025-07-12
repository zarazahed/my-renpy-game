define c = Character('Coco', color="#310075")
define minu = Character('Minu', color="#310075")
define m = Character('Me', color="#00750c")
define r = Character('Raspberry', color="#920f5e")
define s = Character('Strudel', color="#753d0a")
image bg forest = "images/forest.png"

label start:

    scene bg forest with fade

    "It's been a bit of a slow day."

    "As a cat in Pumpkinville, I guess most days tend to be fairly quiet."

    "But today I feel a bit more bored than usual."

    "Yawn... and a bit tired."

    show testing with dissolve

    c "Good morning, Lily!"

    m "Oh, hello! This is a pleasant surprise!"

    "Hmm... when was the last time I saw Coco?"

    "Wow, it really has been a while."

    c "I was visiting the area looking for potion ingredients, so I wanted to drop by for a visit."

    m "Come in and have some tea! We have a lot to catch up on."

    jump teascene

label teascene:

    scene bg forest with fade

    "Hm, Cupcake said she wanted twilight green tea. I would have some too... but I'm afraid that's the last one."
    
    "Oh well. Which tea should I choose for myself?"

menu: 
    
    "Enchanted herbal mix: gives energy boost for the rest of the day":
        jump herbal

    "Fairydew brew: gives you extra sprinkles of luck for the rest of the day":
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

    m "Well, it's a good thing you told me! I'll be sure to send a letter to her."

    c "Hey, I'm going there too today! We should go together."

    c "Anyways, a bunch of her friends are planning a surprise party! We're going to decorate my place this evening and hang out."
    
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

    "Guess I'll never know whether today would be fun."

    return

label market:

    c "Yay! Let's go to the market after we've finished the tea."

    scene black with fade

    pause 1.0

    scene bg forest with fade

    m "Wow, so many new stalls have popped up since I last visited."

    c "I know, right? Cookies... mushrooms... poisons... eek, I'll get distracted. Stay on track. Present for Strudel."

    c "Hm.. I think I see a vase that she would love."

    c "Do you want to get that for Strudel? I think we can afford it if we split the cost."

    "Wow, that's a tough choice. She would definitely love that vase, but I heard her talking about wanting a new hat the other day."

menu:

    "Buy the vase and split the cost. If Cupcake can't afford it, it'll be nice to help out.":
        jump vasesplit
    
    "Say no and get your own present. It's not your problem anyways.":
        jump berude

    "Tell Cupcake about what you heard. "
        jump surprisedcupcake

label vasesplit:

    c "Awesome!"

    scene black with fade

    pause 1.0

    scene bg forest with fade

    m "It looks gorgeous."

    c "I know, right?"

    c "Ahh! I didn't even notice! We have to hurry. They're going to start decorating soon!"

    jump partyprep

label berude:

    c: 

label surprisedcupcake:

    c "Whoa! I didn't know that.
    
    c "Let's both get her hats! I'm sure she'll love them."

    scene black with fade

    pause 1.0

    scene bg forest with fade

    c "Haha, this one looks nice."

    c "Ahh! I didn't even notice! We have to hurry. They're going to start decorating soon!"

    jump partyprep

label partyprep:

    r "Hello!"

