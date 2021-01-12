---
layout: page
title: Complex Systems
---

1. [Modeling](#modeling)
2. [Reducing Failures](#failures)
3. [Chaos Engineering](#chaos)
4. [General Architecture](#architecture)

## <a id="modeling"></a>Modeling
### "[Seeing Whole Systems](https://longnow.org/seminars/02017/aug/07/seeing-whole-systems/)" by [Nicky Case](https://ncase.me), Talk 2017

> We all know every map is simplified. Few people understand that maps are not useful despite being simplified, they're useful precisely because they're simplified.
~ [15:40](https://youtu.be/PCwtsK_FhUw?t=940)

### "[Visualizing software architecture with the C4 model](https://www.youtube.com/watch?v=x2-rSnhpw0g)" by [Simon Brown](http://simonbrown.je), Conference Talk 2019

#### [C4 Model](https://c4model.com/)

He basically advocates UML diagrams at 4 layers of details:
1. Context (dependent systems and overview for newcomers)
2. Containers (not like Docker, more like each deployable software system) 
3. Components (think modules or core features within a software system) 
4. Code (more traditional class model)

### "[Technical leadership and the balance with agility](https://leanpub.com/software-architecture-for-developers)" by Simon Brown, ebook

> Imagine that you need to create a network between two offices located at different ends of the country. One option is to find the largest reel of network cable that you can, plug it in at one office, and start heading to the other in a straight line. Assuming that you had enough cable, this could potentially work. In reality though, there are a number of environmental constraints (real-world obstacles such as rivers, lakes, roads, cities, etc) and service-level agreements (performance, bandwidth, security, etc) that you need to consider in order to actually deliver something that satisfies the original goal. This is where the process of architecting is important. One single long piece of cable is certainly one approach, but it?s not a very good one because of the real- world constraints. For this reason, networks are typically much more complicated, requiring a collection of smaller building blocks that collaborate together in order to satisfy the goal. ~ P. 5

I like the simplicity and visual nature of that example.

## <a id="failures"></a>Reducing Failures 
### [How Complex Systems Fail](https://how.complexsystems.fail)

> Improved safety depends on providing operators with calibrated views of the hazards. It also depends on providing calibration about how their actions move system performance towards or away from the edge of the envelope.
~ [https://how.complexsystems.fail/#18](https://how.complexsystems.fail/#18)

### "[How Complex Systems Fail](https://www.youtube.com/watch?v=2S0k12uZR14)" by Richard Cook, Conference Talk 2012

He's taking the alternate approach and asking "why don't we have more failures?"
Why do we have so much success? Is it because of or in spite of the designs?
Systems as imagined versus systems as found.

He mentioned [FUNCTIONAL RESONANCE ANALYSIS METHOD](https://functionalresonance.com).

Mental simulation of what happens when actions are taken on the system. Expose controls so that operators can make things more resilient.

### "[Resilience In Complex Adaptive Systems](https://www.youtube.com/watch?v=PGLYEDpNu60)" by Richard Cook, Conference Talk 2013

> "Any meeting where you have to get people together to tell them how important something is - you've failed." ~ 10:45
  
### [Complex Systems](https://snafucatchers.github.io/), group write-up referenced by Dr. Cook 
Reading more from Dr. Cook on making complex systems more resilient. 

> A full understanding of how experts cope with the complexity confronting them is essential to engineering the processes to be more resilient. Doing this often requires some form of process tracing

Great quote from one of the underlying sources (Process tracing methods for the study of cognition outside the experimental psychology laboratory):
> to be successful in unlocking the doors concealing nature's secrets, a person must have ingenuity. If he does not have the key for the lock, he must not hesitate to pick it, to climb in a window, or even kick in a panel. If he succeeds, it is more by ingenuity and determination than by method. (Hildebrand, 1957, p. 26)

#### Situational surprise vs fundamental surprise
1. situational surprise is compatible with previous beliefs about 'how things work'; fundamental surprise refutes basic beliefs;
2. it is possible to anticipate situational surprise; fundamental surprise cannot be anticipated;
3. situational surprise can be averted by tuning warning systems; fundamental surprise challenges models that produced
success in the past;
4. learning from situational surprise closes quickly; learning from fundamental surprise requires model revision and changes
that reverberate.
Information technology anomalies are frequently fundamental surprises. This is due to the difficulty in maintaining adequate mental models of what is below the line, understanding how this connects to what is above the line -- crossing the line, as software systems grow in complexity and continuously change.

## <a id="chaos"></a>Chaos Engineering
### [Chaos Engineering](https://learning.oreilly.com/library/view/chaos-engineering/9781492043850/preface03.html), Book 2020

I started exploring chaos engineering as it relates to understanding complex systems because one of the recommendations from Dr. Cook is that the best way for operators to under how the complex system they're managing works is to continuously interact with it.

## <a id="architecture"></a>General Architecture
Recommended [game programming book](https://gameprogrammingpatterns.com/contents.html) with architecture examples.

### [Amazon's Builders' Library](https://aws.amazon.com/builders-library/?cards-body.sort-by=item.additionalFields.customSort&cards-body.sort-order=asc), video collection

#### "[Failing Successfully](https://www.youtube.com/watch?v=yQiRli2ZPxU)", conference talk 2019
