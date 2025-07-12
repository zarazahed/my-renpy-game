define c = Character('Cupcake', color="#310075")
define minu = Character('Minu', color="#310075")
define m = Character('Me', color="#00750c")
define r = Character('Raspberyy', color="#920f5e")
image bg forest = "images/forest.png"

label start:

    scene bg forest with fade

    "It's been a bit of a slow day."

    "As a cat in Pumpkinville, I guess most days tend to be fairly quiet."

    "But today I feel a bit more bored than usual."

    "Yawn... and a bit tired."

    show testing with dissolve

    c "Good morning!"

    m "Oh, hello! This is a pleasant surprise!"

    "Hmm... when was the last time I saw Cupcake?"

    "Wow, it really has been a while."

    c "I was visiting the area looking for potion ingredients, so I wanted to drop by for a visit."

    m "Come in and have some tea! We have a lot to catch up on."

    jump teascene

label teascene:

    scene bg forest with fade

    "Hm, Cupcake said she wanted twilight green tea. Which tea should I choose for myself?"

menu: 
    
    "Enchanted herbal mix: gives energy boost for the rest of the day":
        jump herbal

    "Fairydew brew: gives you extra sprinkles of luck for the rest of the day":
        jump fairydew

    "Suspicious tea bag"
        jump poison

label poison:

    scene bg forest with fade

label herbal:

    scene bg forest with fade

    "Wow, I'm feeling a bit more energetic already!"

    m ""

    c ""

    "Wonder if that was the right choice."

    return

label fairydew:

    scene bg forest with fade

    m "Sure!"

    return