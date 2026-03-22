# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Raniya", color = "#E10072")
define p = Character("Penelope", color = "#FF5400")

transform smallright:
    zoom 0.7  # scale down to 40% of original size
    xalign 1.8  # right edge
    yalign 1.0  # bottom edge
transform smallleft:
    zoom 0.7
    xalign -0.7
    yalign 1.0

label scene_loop:
    # Loop through scenes 1-5 with 0.1 second pauses
    $ i = 0
    while i < 6:
        scene sleep
        pause 0.25
        scene open
        pause 0.25
        $ i += 1
    return
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
   
    scene sleep with fade
    play music "snoring-71560.mp3" volume 8.5
    pause 3.0
    play sound "magic-03-278824.mp3"
    scene cat with fade
    pause 1.5
    scene kitty
    play sound "cat-meow-401729.mp3"
    pause 0.9
    scene cat
    pause 1.5
    play music "sweet-acoustic-guitar-music-311691.mp3" fadein 1.5
    call scene_loop
    scene yawn 
    play sound "yawning-6096.mp3" volume 8.5
    pause 4.0
    show glad
    play sound "aw-86103.mp3"
    r "Aww, what an adorable dream about cats!"
    scene bu
    r "Though, in the end, it was just a dream..."
    play sound "no-96018.mp3"
    r "Nooooo! My cute kitties!"
    r "I want to pet them so much!"
    show scared
    r "Wait..."
    r "I couldn't get a kitty before because my mom was allergic to them."
    show confident
    play sound "sound-effects-finger-snap-with-reverb-113861.mp3" volume 9.9
    r "But now that I have my own dorm, I can finally go buy one!"
    show believe 
    play sound "sad.mp3" volume 19.5
    r "The only problem is, I'm just a college student and don't have much money..."
    scene bu
    r "Plus, I know so little about cat breeds and their pros and cons!"
    show believe
    r "So if I want to find the perfect kitty that matches my interests and financial situation, I'll need to do a lot of reaserch."
    scene bu
    play sound "girl-oh-no-150550.mp3" volume 3.0
    r "Oh no! But I don't want to do work!!!"
    play sound "ding-idea-40142.mp3"
    show glad
    r "Oh wait! My best friend Penelope works at the pet store across the street!"
    play sound "chuckle.mp3" volume 2.0
    r "She can definitely help me!"
    show yes
    r "Then I can finally have a pet of my own!"
    show believe
    r "But I really need to think about how much money I should spend on a cat."
    r "Do you think I should just go for a common cat sice I'm a only collede student and it's my first time trying to raise one?"
    hide believe
    show glad
    r "Or maybe I should aim for apedigree or purebred cat while I'm living alone and have the time to take care of it -- who knows, maybe I'll become an expert!"
    show confident 
    r "Or... Should I take a risk, go all in, and spend ll my current money on an exotic or rare breed?"

    menu:
        "Common cats, spend $50 to $200":
            jump common
        "Purebred cats, spend $500 to $2,000":
            jump purebred
        "Rare breeds, spend $3,000 to $5,000... Or even higher!":
            jump rare
    
    label common:
        hide confident
        show glad
        r "Yeah! I feel like this is the most reasonable choice."
        r "I'm just a student and I have limited money and time to take care of the cat."
        r "And cheaper cats are still cute, right?"
        r "Let's stick with that idea!"
        r "{i}I'm so excited!{/i} Let's go!"
        hide glad
        jump store


    label purebred:
        hide confident 
        show yes
        r "Yes! If I'm going to buy a cat, it should be a purebred!"
        r "I'm so excited! Yeah!"
        r "Let's go right now!"
        hide yes
        jump store

    label rare:
        hide confident
        show yes
        r "Yeah! Let's go all in!"
        r "Since my parents aren't around, it's the perfect time to do something wild!"
        r "I'm so excited! Let's go right now!"
        hide yes
        jump store
        

    label store:
        play music "meow-meow-give-me-milk-version-1-317260.mp3"
        scene room with fade
        play sound "store-entrance-bell-188054.mp3" volume 1.5
        pause 1.0
        show yes at smallleft with fade 
        play sound "hello-278029.mp3" volume 5.5
        r "Hello!"
        show smile at smallright with fade
        play sound "why-hello-there-103596.mp3" volume 5.5
        p "Why hello there!"
        p "What brings you here to the pet store Raniya?"
        hide yes
        show confident at smallleft
        r "Haha! Penelope, what do you think? I'm here to buy a pet, of course!"
        hide smile
        show hap at smallright
        p "Really, Raniya? That's a surprise!"
        p "What animal are you planing to buy?"
        hide confident
        show glad at smallleft
        r "A cat! I just had a dream anout them, and I'm eager to buy one!"
        hide glad
        show believe at smallleft
        r "But I literally kno wnothing about cat breeds or how to take care of them, so..."
        hide believe
        show yes at smallleft 
        r "Here I am, at my best friend's pet store!"
        r "You can help me with this, right, Penelope?"
        hide hap
        show smile at smallright
        p "Of course! That's my job!"
        p "I can help you anything related to it!"
        hide smile
        show normal at smallright
        p "First, though, I need to know what type of cat you're planing to buy."
        p "Rescue cats? Mid-range breeds? Or... High-end breeds?"
        hide yes
        show confident at smallleft
        r "Oh! I actually thought of that at home!"
        r "I choose..."
        menu:
            "Affordable Cats":
                jump affordable
            "Mid-Range Breeds":
                jump mid
            "High-End Breeds":
                jump high

        label affordable:
            r "I choose affordable cats."
            hide confident
            show yes at smallleft
            r "As my best friend, you know my financial situation."
            hide normal
            show smile at smallright 
            p "Yes, of course!"
            p "I was expecting you to say that!"
            hide smile
            show normal at smallright
            p "Just because they're cheaper doesn't mean they're not cute!"
            hide normal
            show smile at smallright
            p "There are so many adorable mixed-breed and domestic cats!"
            p "I want to introduce you to two of my favourites."
            hide smile
            show hap at smallright
            p "As your best friend, I know you'll love them too!"
            scene tabby with fade
            play sound "cat-meow-sound-383823.mp3" volume 3.3
            hide hap
            show normal at smallright
            p "So this cute cat you're seeing is a grey tabby cat."
            p "A tabby cat isn't a breed, but a coat pattern defined by an M marking on the forehead, stripes by its eyes, cheeks, along its back, and around its legs and tail."
            p "Common personality traits often reported by tabby owners include affectionate, playful and curious, intelligent, vocal, and adaptable."
            p "In our pet store, a tabby cat ranges from around $50 to $200 for a domestic short-hair tabby."
            hide yes
            show confident at smallleft
            play sound "aw-86103.mp3"
            r "Aw! That's so wonderful!"
            hide confident
            show yes at smallleft with fade
            r "What's the next one you wanted to introduce?"
            scene dragon li with fade
            play sound "cat-meow-14536.mp3" volume 9.9
            show normal at smallright
            p "The next one I want to introduce to you is the Dragon Li or Li Hua Mao."
            show glad at smallleft with dissolve
            r "Oh! Sounds like a Chinese breed!"
            p "Yeah! It's know for its striking golden-brown, broken-mackerel tabby coat."
            p "Li Hua is an intelligent, loyal, playful, and athletic natural breed."
            p "In our store, they cost about $140 to $280."
            r "Cool!"
            scene room with fade
            r "I think I want..."
            stop music fadeout 2.0
            menu:
                "Tabby Cat":
                    play sound "end.mp3"
                    hide glad
                    show confident at smallleft
                    r "I think I want a tabby cat!"
                    pause 2.05
                    return

                "Li Hua Mao":
                    play sound "end.mp3"
                    hide glad
                    show confident at smallleft
                    r "I think I want Li Hua Mao!"
                    pause 2.05
                    return

        label mid:
            r "I choose mid-range breeds."
            hide confident
            show yes at smallleft
            r "I don't want a mixed-breed cat, but I also don't want to spend too mucg on an expensive one, so I pick the middle option."
            hide normal
            show smile at smallright 
            p "Yes, of course! That's totally your style!"
            play sound "chuckle.mp3" volume 2.0
            p "Haha, and let me introduce you a breed I absolutely love-"
            hide smile
            show hap at smallright
            p "The Russian Blue!!!"
            hide hap
            show smile at smallright
            p "As your best friend, I know you'll love them too!"
            scene russian blue with fade
            play sound "cat-meow-sound-383823.mp3" volume 3.3
            hide hap
            show normal at smallright
            p "Russian Blue is a pedigreed cat breed with solid blue colours that vary from a light shimmering silver to a darker, slare grey."
            p "The short, dense coat, which stands out from the body, has been the breed's hallmark for more than a century."
            p "The Russian Blue has bright green eyes, pinkish lavender or mauve paw pads."
            p "They have teo layers of short thick fur in a solid blue-grey colour with a silver sheen."
            hide yes
            show confident at smallleft
            play sound "aw-86103.mp3"
            r "Aw! That's so wonderful!"
            hide confident
            show yes at smallleft with fade
            r "Tell me more about their personalities!!!"
            hide normal
            show smile at smallright
            p "They are generally considered to be a quiet breed but there are always exceptions!"
            show glad at smallleft with fade
            r "Oh! Cool!"
            p "Yeah! They are normally reserved around stranders, unless they are brought up in an active household."
            p "Russian Blue kittens are energetic and require adequate playmates or toys as they can become mischievous if bored."
            p "In our store, they cost about $800 to $2000."
            r "Great!"
            hide glad
            show believe at smallleft
            r "It's a bit pricey for me..."
            hide believe
            show glad at smallleft
            r "But I really love teh Russian Blue's personality and traits!"
            stop music fadeout 2.0
            play sound "end.mp3"
            hide glad
            show confident at smallleft
            r "I think I'm getting a Russian Blue!"
            pause 2.05
            return
            
        label high:
            r "I choose high-end breeds."
            hide confident
            show yes at smallleft
            r "As my best friend, you know my personality -- I always want the best!"
            hide normal
            show smile at smallright 
            p "Yes, of course!"
            p "Althought they can be really expensive, I respect your choice, Raniya."
            hide smile
            show normal at smallright
            p "But since you choose the rare and high-end breeds, you should really take extra care of them -- seriously!"
            hide yes
            show believe at smallleft
            r "Okay... you're making me nervous. Why should I take extra care of them?"
            hide normal
            show smile at smallright
            p "Well, since the rare and high-end breeds are more delicate and require specific care, it's important to give them extra attention."
            p "I want to introduce you to two of my favourites."
            hide smile
            show hap at smallright
            p "As your best friend, I know you'll love them too!"
            scene sphynx with dissolve
            play sound "cat-meow-sound-383823.mp3" volume 3.3
            hide hap
            show normal at smallright
            p "So this unique cat you're seeing is a sphynx."
            p "They are also known as the Canadian Sphynx."
            p "It's a breed of cat known for its lack of fur."
            p "Hairlessness in cats is naturally occurring genetic mutation, and the Sphynx was developed through selective breeding of these animals, starting in the 1960s."
            hide normal
            show smile at smallright
            p "Sphynx are known for their extroverted behavior. They display a high level of energy, intelligence, curiosity and sffection for their owners."
            p "They are one of the more dog-like breeds of cats, frequently greeting their owners at the door and are friendly when meeting strangers."
            p "Care should be taken to limit the Sphynx cat's exposure to outdoor sunlight at length, as they can develop sunburn and skin damage similar to that of humans."
            p "But yes, Sphynx cats tend to be highly attached to their owners!"
            hide yes
            show confident at smallleft
            play sound "aw-86103.mp3"
            r "Aw! That's so sweet!"
            hide confident
            show believe at smallleft
            r "How much does it cost?"
            p "In our store, a Sphynx cat costs between $1,500 and $5,000."
            hide believe
            show yes at smallleft with fade
            r "Ok. What's the next one you wanted to introduce?"
            scene savannah with dissolve
            play sound "cat-meow-7-fx-306186.mp3" volume 9.9
            show normal at smallright
            p "The next one I want to introduce to you is the Savannah."
            hide yes
            show glad at smallleft with fade
            r "Oh! Looks so tall!"
            p "Yeah! Savannahs can be very large, and in 2016 an F2 male attained a world record for tallest cat at 48.4 centimetres!"
            p "This hybridization typically produces large and lean offspring, with the serval's characteristic large ears and markedly brown-spotted coats."
            r "Cool!"
            p "Savannah cats are known for their loyalty."
            p "And they will follow their owners around the house."
            p "They can also be trained to walk on a leash and to fetch!"
            r "Cool!"
            r "I know many Savannah cats do not fear water, and will play in or even immerse themselves in water!"
            p "That's true! But there are some health considerations and ownership laws..."
            p "Savannah cats are more likely to develop hypertrophic cardiomyopathy (HCM) than other domestic breeds."
            p "The Savannah Cat Association recommends cats are screened for HCM, as well as progressive retinal atrophy and pyruvate kinase deficiency, which can cause blindness and anemia, respectively."
            p " And you would need to know some laws that govern ownership of Savannah cats."
            hide glad
            show believe at smallleft
            r "That's pretty challenging..."
            hide believe
            show yes at smallleft
            r "But they look so elegant and sleek!"
            hide yes
            show confident at smallleft
            r "And I LOVE their unique characteristics!!!"
            p "A Savannah cat in our store costs around $1,000 to over $20,000"
            hide confident
            show glad at smallleft
            scene room with fade
            r "So, I think I'll choose..."
            stop music fadeout 2.0
            menu:
                "Sphynx Cat":
                    play sound "end.mp3"
                    hide glad
                    show confident at smallleft
                    r "I think I want a Sphynx!"
                    pause 2.05
                    return

                "Savannah":
                    play sound "end.mp3"
                    hide glad
                    show confident at smallleft
                    r "I think I want a Savannah!"
                    pause 2.05
                    return

    return
