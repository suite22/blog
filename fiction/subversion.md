---
layout: default
title: Subversion
image: ../../assets/subversion/midjourney-suit.jpg
author: Ben Goertz
---

<script>
    // Currently known dreamers
    const knownDreamers = ['alone', 'dalle', 'midjourney'];
    // Start with this dreamer when the page loads
    const initialDreamer = 'midjourney';

    document.addEventListener("DOMContentLoaded", function() {
        changeTo(initialDreamer);
    });

    // An inline script to keep it simple with Jekyll.
    function changeTo(dreamer) {
        const dreamerSelector = document.querySelectorAll('.' + dreamer);
        // Enable selected dreamer
        for (let i = 0; i < dreamerSelector.length; i++) {
            dreamerSelector[i].style.setProperty('display', 'contents');
        }
        // Bold the link to select at top of page
        const dreamerLinkSelector = document.getElementById(dreamer + 'Link')
        dreamerLinkSelector.style.setProperty('font-weight', 'bold');

        // Hide all other dreamers
        const hiddenDreamers = knownDreamers.filter(function(e) { return e !== dreamer });
        for (let j = 0; j < hiddenDreamers.length; j++) {
            // Reset bold for hidden dreamers
            const hideDreamerLinkSelector = document.getElementById(hiddenDreamers[j] + 'Link');
            hideDreamerLinkSelector.style.setProperty('font-weight', 'normal');
            const hideDreamerSelector = document.querySelectorAll('.' + hiddenDreamers[j]);
            for (let k = 0; k < hideDreamerSelector.length; k++) {
                hideDreamerSelector[k].style.setProperty('display', 'none');
            }
        }
    }
</script>

> _Dream with:_[^1]
<a id="midjourneyLink" href="javascript:void(0)" onclick="changeTo('midjourney');">Midjourney</a>
<a id="dalleLink" href="javascript:void(0)" onclick="changeTo('dalle');">DALL·E</a>
<a id="aloneLink" href="javascript:void(0)" onclick="changeTo('alone');">Alone</a> 

# Subversion 

<div class="midjourney"><img alt="The sound waves forming an almost harmonious unified chorus and then drifting to discordance." src="../../assets/subversion/midjourney-drifting-to-discordance.jpg"></div>

<div class="dalle"><a title="DALL·E Info" href="https://labs.openai.com/s/AWqqhYIwbsZ9Uxs2Na1PbLsC"><img alt="Fluctuations of the competing sounds together forming an almost harmonious unified chorus and then drifting to discordance" src="../../assets/dalle2-subversion-botany.jpg"></a></div>

Inside the research bubble my attention is drawn not to the distinct hum of each miniaturized botany experiment neatly ordered within the clean space but to the fluctuation of the competing sounds together - sometimes the sound waves forming an almost harmonious unified chorus and then drifting to discordance. The collective sound of all the machines is never stable enough for my brain to silence it as background noise. It's annoying when I'm trying to keep the trail of movements in my encoded puzzles fresh in my memory. 

Abruptly breaking through the sound and into the research bubble is Carl, "you got another message Ada. Metadata says the cache today has a response from Dr. Quorn for you. Should be out of confirmation analysis in a bit."

I shift my puzzle to the side, "thanks for scanning the metadata for me."

"Ha, no one ever writes me. Must be nice when your dad is a fan."

Turning and exiting the research bubble Carl is gone as quickly as he entered. His round and cheerful face always seems to be in motion, bobbing from one area of the ship to the other. The only time he's still is hunched over his station, his hair falling down over his eyes, focused so intently he brushes his hair back with his thick fingers barely noticing when gravity brings each strand right back down.

Carl is a gift in that it helps to have a peer to talk to in realtime. We are a small contingent of two Awake Researchers with almost unlimited access to the past but little opportunity for collaboration with others now. For Awake Researchers, like myself, transmissions related to ongoing research are allowed with the remaining researchers on Ohm, our origin planet. Messages are reviewed and trimmed for length when possible but occasional personal touches find their way into transmissions. As the distances expand and the delays increase the priority is given towards scientific research and critical updates between Arks and Ohm. On a one-way journey with no return and no follow-on Arks there's no good that comes from sentimental messages home. Each person on the Ark has various reasons for making the break. Maintenance crew for example do send something back in a sense - almost all their pay is distributed for family or friends on Ohm. Every day they serve on the Herja they know someone back home is better for it. Strict discipline is mostly self-enforced when support for loved ones is closely tied to it.

I enjoy discussing research with Carl even though our work is focused on different fields. He is solely fascinated by any means of algorithmic improvement to ship monitoring and Sleeper optimization. He believes any potential improvement is worth exploring no matter how marginal. My unwelcome feedback is that several generations of brilliant minds at New Horizon Labs have refined each and every control flow within the system. I imagine it like a beautifully designed garden, every path deliberate and perfect. "You're wrong Ada. It's not magical like that. I've already made several refinements that are under Lab review." I don't tell him that I think his improvements are likely regressions that will be rejected. "You focus on not contaminating our new home and I'll make sure the Sleepers are in optimal condition." We've built up a sense of each other from training and working together in close proximity. Carl doesn't have to say again that he thinks that I'm basically doing busy work. He's said repeatedly, "the odds of any sort of long term bio-isolation and preservation on the new planet is as close to zero percent as I can imagine." His imagination for numbers isn't lacking, but I believe with the right plan and dedication we can keep our new home unspoiled for generations.

---

"Look around your boots Ada and make sure the seal around your ankles is tight. The dust is still dangerous." My father was always right or at least it felt that way. He surprised me by leaving an encoded puzzle on the table letting me know he got the approvals to bring me, for the first time, out into the Exclusion Zone. We shared ciphers as an endless game - my father happy with every turn of language and for me the thrill of building a complex meaning only we could share. It's not like the oversight at our remote station was strict. If anything taking me added significant risk to my life, but I had begged him to take me for years.

The heavy respirator with my oversized hazard suit crumples awkwardly on my young form. The gravel under my boots has a different crunch than I have ever heard while walking to the gate sealing in our station. As we wait for the gate to open, a process my father has been through hundreds of times, I want to see his warm smile as he turns to me but his eyes are the only part of him I recognize, "stay close to me. I'll show you where the first sensors are that we need to service." My heart pounds in my ears over the cycle of the respirator as we step out together into the Exclusion Zone.

<div class="midjourney"><img alt="The heavy respirator with my oversized hazard suit crumples awkwardly on my young form." src="../../assets/subversion/midjourney-suit.jpg"></div>

<div class="dalle"><a title="DALL·E Info" href="https://labs.openai.com/s/cJdBbdqbok1m9kutzI0GV79H"><img alt="A large oak tree with a low branch reaching towards the ground in a wooded glen with fallen leaves and brown ferns at golden hour" src="../../assets/dalle2-subversion-tree.jpg"></a></div>

At some point the paved service road had been so broken open by grasses and weeds that it was chipped up into more of a loose path. We walk along the uneven road and then fork off into the woods near a massive barren tree screaming up overhead slowly decaying. One large branch drooping to the ground, almost like a helpful inclined ramp for the few animals left to explore the great tree. The sadness of the tree reminds me of some of the bedtime stories my father told. Instead of fairy tales he would tell stories about things he found in the Exclusion Zone. His primary research focused on plant and animal regeneration within the zone but his passion, what kept him up late into the night in his study, was the restoration of lost works. Stories, poems, even graffiti, he photographed and copied anything that had a chance of holding lost meaning. Several colleagues met with him regularly at our house comparing translations of works that had been found in various languages, each attempting to weave back to the original author's language or intent. The joy and the warmth that poured out of their debates felt warmer to me than any fire we huddled around later to hear readings. They drank and laughed together, savoring every recovered gem with endless excitement. My father told stories from before Doomsday about the forests and the animals that used to roam the area. His voice slowly drifting towards sadness as he talked about what was lost. Gone now and never coming back. He mourned the organic and the man-made. Tales of lost species took him on endless trails to works from his youth. 

"How can I explain a poem to you that I only remember the feeling of?" 

<div class="midjourney"><img alt="small ravines lined with unnaturally bright layers of sediment washed like bright bands from a child's paint set." src="../../assets/subversion/midjourney-bright-layers-of-sediment.jpg"></div>

We walk beyond the tree with the branch like a ramp for several kilometers through small ravines lined with unnaturally bright layers of sediment washed like bright bands from a child's paint set. Together in an open plain of low grass not higher than my boots my father taps my arm and points down into the mud - a small animal's footprint. One of the few signs of animal life. We follow the trail for a few paces looking for clearer prints. "What do you think it is?" I ask. He studies the prints closely, "hard to say. They're from before the last rain so at least a few days old." A few meters away I find another grouping of paw prints, this time with a tiny set trailing, "look I think these prints are from a baby!" My father bends down close to the ground near the tiny prints. "Yes but look at how it's dragging the right side. It's either injured or more likely malformed." Few animals play near our home at the research outpost. Seeing these prints, thinking about the stories of destruction from my father, and now imagining a young creature trying to limp along attempting to keep up with a parent - my eyes race across the trail and then the edges of the field hoping to see more signs of survival, something to indicate they are okay. That we are okay. As the tears and heavy breathing fog up my respirator mask I look towards the low rust colored clouds and start to wobble. My father catches me. His comforting words are broken up over the comms by my sobs but once I'm calmer he says, "the damage that's been done here cannot be undone." His firm grip on my shoulder, willing his strength down into me, helps me. I stand tall; take a deep breath. 

We reach the sensor station after a short walk out of the grassy plain. Along the ridge line near my father I stand waiting while he works. He asks me to hand him each tool even though he could set his bag closer and work alone as he usually does. My mind wanders between tasks as I look out further, our valley behind us, and study the outlines of buildings in the distance that I have only seen in photographs from my father. What was this all like before? What did the flowers and fruit trees look like in bloom before the cold set in? I want to know every person who stood along these ridges and saw their town, their home, as it was in its prime. Not as it is, but as it should have been.

"Hand me that smaller brush, the one with the two millimeter wires. No, the other one. Thanks." My father carefully places each detached component on a clean cloth on the ground next to him. "These collection trays and sensors keep getting overwhelmed with how much material is being collected. I keep telling them it's above the margins in the spec." His voice trailing off, his comment not entirely meant for me as he remains focused on his work. 

<div class="midjourney"><img alt="the whir of the sensors and radio relay" src="../../assets/subversion/midjourney-whir-of-sensors.jpg"></div>

I wait. My wonder is punctured by the whir of the sensors and radio relay powering back up a low, almost harmonious, hum of technology among the whirl of the wind moving through the leaves nearby. “Help me pack the tools up Ada. We’ve got enough daylight left, I want to show you my favorite spot in the Zone.” 

Along grass fracked pavement we approach a small concrete building with vertical slit windows. The once classical sign droops over the entrance: LIBRARY. I pause as soon as the reality of being in front of the place that my father’s study holds a prized photo of – this is the place of dreams. 

Inside, rays of light cut through the fallen shelves to books in various states of re-attempted ordering. My father and others from the outpost, as a hobby, have carefully sorted the most prized works off of the floor onto tables near the windows. “We can’t stay long and you need to be careful. Stay close.” The only feeling I have is utter amazement at what once stood proudly within these walls. My father has shown me photos and talked about the library for years - and of other libraries even larger - but my imagination has mostly constructed rows of the books I know from home but now here, stepping over low dunes of water soaked books I realize how many worlds exist between each binding that I may never know. “Over here is the wall I want to show you.” Pointing into the next room, darker and hazier, I follow him. My father is brave. I’ve never been inside any place like this, everything at the outpost is prefabricated fast-build and well lit. These walls have the weight of people planning to stay. Brushing my gloves along the dust lined shelf running the length of the wall I see salvaged spines with legends told to me as bedtime tales: Chang, Le Guin, Liu, and Tchaikovsky. I realize only once the shelf runs out I’ve reached the other end of the room and my father is standing next to a table with several books open but has stopped to watch my revelry. I see his smile cut in half by the light coming down from a yellowed bubble skylight overhead. “Helping to recover and translate some of these works has brought me great peace. Listen to this line:

“What use is it to speak if you don’t know what to say.”

<div class="midjourney"><img alt="How can I explain a poem to you that I only remember the feeling of?" src="../../assets/midjourney/subversion-the-feeling-of-a-poem.jpg"></div>

Standing next to him now I hear the warmth in his voice and know his smile is slowly growing as he rolls around the words with delight in his mind. I want to live here with him. Among these pages regardless of the danger.

In the stillness a shadow on the wall glances off one of the puddles near us. Immediately my father grabs my arm and shifts me behind him. Without looking down he pulls a long metal tool from his tool bag and turns up our suit lights. Cutting back into the dark corners on the far side where shelves remain sagging - the light catches eyes. Iridescent. Terror escapes me as a scream that my father cuts short, grabbing me, “stay behind me and move with me slowly.” The open archway back into the main entrance and outside is almost cut off as the creature moves between us and the exit. I see my father’s grip tighten on the tool now turned weapon as the shadows slip off the dark furred canine, something likely bred from one of the pets from Earth. Its fangs are sharp enough to rip our haz-suits. My father moves us back along the wall I entered, the legends to my back. As we move down the rows of still standing shelves it keeps pace from the center of the room glaring between the stacks back at us. Just before the archway is a circular desk and as we pass the last shelf the animal lunges from floor, splashing, to the desk, claws craving against the surface, and at us. The swing of the tool meets it in midair, a singular muted tone and a yelp. My father shoves me back as he turns his full weight into the next swing and I hear the squish of the dense tone again. No more cries from the animal.

When my father turns back to me I see almost the same crazed eyes I saw earlier across the room but from a man covered in red streaks over the once clear mask. 

Outside, we lock the door. His only words are, “I’ll take care of it later.”

<div class="midjourney"><img alt="We make it back to the station as the rouge sunset flares on the horizon over the group of small structures in our research outpost." src="../../assets/subversion/midjourney-rouge-sunset.jpg"></div>

<div class="dalle"><a title="DALL·E Info" href="https://labs.openai.com/s/HA9OrHHtU4lD86pmV37sXGVi"><img alt="The station as the rouge sunset flares" src="../../assets/dalle2-subversion-rouge-sunset.jpg"></a></div>

We make it back to the station as the rouge sunset flares on the horizon over the group of small structures in our research outpost. After decontamination we look through the photos from our day in his work room: dried skat from a herbivore, black and gray fur scraped into the rough bark of a tree, and the paw prints we studied. Incomplete stories, but now I have experienced the pieces that my father draws from. We add the best to the walls of his study, covered with overlapping photos and pages many found by him or shared by a colleague digging through rubble in one of the zones. After several drinks and loud debates my father usually bursting into laughter. He was constantly floating between deeply serious and spontaneously funny. 

---

Passing with top marks I graduated our provincial school and left to train for my passion of plant genetics. My father grew frustrated with his research - how his data about Exclusion Zone conditions was presented beyond his research group. "My field reports keep getting revised or rejected during review. The field readings don't line up with the projected improvements." Frustrated, he lowered himself further in his chair. "Are you sure the sensors are right?" My question stung him, "after two decades I know when the equipment is right." He shifted away and stared off into the distance, I could see the storm clouds reflecting off the glasses he now wore. "Things are worse here than they want people to believe." 

As I neared graduation my father shifted course and took a job as an archivist and translator - turning his longtime hobby into his career. I hoped the change would lift the sadness from him, but it didn't. My father grew more agitated over the years as I returned to see him. The open debates with colleagues around the fire had turned into closed door discussions in hushed tones. I was not invited to join. Familiar faces of friends were replaced by colder, rougher faces who glared through the doorway whenever the door briefly opened. 

The sudden announcement of early departure dates for the first Arks came as a wonderful surprise to me and somehow as a bleak omen to my father and those he now spent time with.

"I'm applying and I want you to come with me. We can work together on the same Ark." His shoulders sagged and his eyes hunted for a dark corner of the room. "You're all I have, Ada. I've been worried they would draw you away with this nonsense." 

He needed me and I needed him. I submitted an application for him along with mine. I didn't tell him. Together on the Herja or Resolution, the first two leaving, or any of the upcoming Arks we would be safe. A new chance to make things right, or at least not make them wrong again.

The next morning on the counter I found a small envelope with "To My Traveling Hope" written in his handwriting. His boots were gone, he had already left for the day. I opened it:

> To My Traveling Hope Ada,\
> It took until almost 230 years after Doomsday for the radioactive isotopes to decay before even short excursions into the Exclusion Zones were permitted. The loss of human life, lands, animals, and ways of living and thinking are innumerable. 
>
> The scale of each missing thing weighed on your mother more with each day. One day it crushed her and she wandered off alone like a wounded animal to die alone. My greatest fear when digging through the debris is that one day I'll find her. Gone in every sense but unspeakably cast into my memory forever in some terrible contorted form. I remember her as the woman she was when you were born, not as the broken woman who left. She loved you deeply.
>
> This research station has been my home for more years than any other place. The other families here helped hold us together and to raise you and your older brother. He barely blinked once he could enlist to defend us from the terrorist who he feared would strike again. Losing your brother pierced me, his stoic face cracking as the convoy reached the gates of our station. I hoped his path would not be yours. 
>
> If you do decide to travel, I want you to think not only of your actions but also what you leave behind. There is a wake that rolls behind each of us that is visible only after deep reflection. 
>
>> We wandered in darkness\
> our lights flickering\
> no stars to guide\
> no hope to sustain\
> no wisdom passed down\
> merely the march of progress again\
> A phoenix without color\
> purely utilitarian form\
> function without beauty\
> prowling for home
> 
> All my love,\
> Q

I spent hours imagining ways to deal with the disappointment of being rejected for my inexperience. My father's expertise meant his application was a mere formality. I sat in his office, in the chair he spent hours writing, and opened the responses once they arrived. 

"Dr. Quorn, your application has been denied for: subversion."

My application however said "accepted: Active Research Position I."

I sat for a long time trying to tease out the series of steps that led to a universe where someone as intelligent as my father would be denied for something so clearly false. How could any of this be true?

<div class="dalle"><a title="DALL·E Info" href="https://labs.openai.com/s/mVtBowlRNkQnGGhYHDHizc11"><img alt="As the light through the window cast shadows slowly across each photo and text on the wall" src="../../assets/dalle2-subversion-light-through-window.jpg"></a></div>

As the light through the window cast shadows slowly across each photo and text on the wall I sat for a long time silently. Reports in various states of review and completion lay in loose piles on his desk. He hated politics. He spoke only of the inappropriate oversight of the data from his research. As my anger soared I opened drawers and picked through pages looking for this subversion they claimed existed. In the back of a drawer under a book I found a list of short, coded symbols - I immediately felt their repulsive intent. The light in the room shifted like a sudden eclipse from one of the moons and there in the doorway stood my father. "Be careful what you leave written down, it might travel farther than you think."

As we sat silently drinking his favorite rare gin it felt wasted on us. He was the first to breach the void: "Some talk of the light of human consciousness as a rare prize that should be preserved, but what have we done of the places we've come to? At what cost does our light bring darkness to millions and billions of other species. Is our light meant to rage while so many are burnt out? Better that we lock the cage around ourselves and destroy the key." Turning the now decoded page in my hand I hope for another meaning, something to offset the doom that had descended. "We can do better. We can learn to preserve and protect." With a heavy sigh he turns to me, "I have spent my entire life willing myself to believe that. Years spent reconstructing lost writings have led me to a far worse fear." He rose from his chair and pulled down a page from the wall:

> "We build what we do not understand and we know what we have done only once we destroy the systems upon which we depend. We are mad men among the stars. It is up to each of us to prevent more destruction."

<div class="dalle"><a title="DALL·E Info" href="https://labs.openai.com/s/1SBsmSI2fNZQ3bwlhTnL5f1u"><img alt="We are mad men among the stars" src="../../assets/dalle2-subversion-madmen-among-the-stars.jpg"></a></div>

"I can't believe in a universe so bleak. I won't just stay here and wait for the end." Turning to me with his eyes pleading, "At what cost to others Ada?"

He gently pulls the coded sheet from my hand and into the fireplace. We both watch as the flames burn it to ash and I feel the lonesome burn of propellant that will lift me away from this home to a new one.

<div class="midjourney"><img alt="We both watch as the flames burn it to ash" src="../../assets/subversion/midjourney-flames-burn-to-ash.jpg"></div>

---

With Carl out of the research area, I hesitate for a moment before gliding over to read the message from Dr. Quorn. The proper thing to do is to wait for the entire cache to pass through error correction, but errors are rare and I know I must search before anyone else. Our coded messages are thinly veiled at best, we've never had a secret actually worth intently searching for before. 

I decode each piece of the message without leaving any record of my steps. Playing with all my three dimensional puzzles over the years has helped me build up an ability to hold the next moves in memory. As I race to complete the last stanzas the meaning floods my awareness setting off neurons in a chain reaction. The worst is happening and I feel powerless to stop the sequence that has traveled here long before I realized.

Carl bursts back into the research bubble, "We lost contact with the Resolution! They think the ark might have suffered a... catastrophic failure."

"I know."

<div class="midjourney"><img alt="Ada's face" src="../../assets/midjourney/midjourney-character-face.jpg"></div>

---

[^1]: The images for this story were generated using DALL·E and Midjourney. I wrote posts about the experience of using each system for the first time: [I Fed Lines From My Short Story Into DALL·E](../../2022/08/01/creating-with-dalle/) and [...And Then I Fed Lines From My Short Story Into Midjourney](../../2022/08/05/creating-with-midjourney/). The styles are distinct enough that I think they represent different visions for the world of the story. 