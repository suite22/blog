---
layout: post
title: The Cover Oregon Failure
---

If we've met in person you've probably heard me try to steer the conversation towards the [Cover Oregon website failure](https://en.wikipedia.org/wiki/Cover_Oregon#Website_failure). If only the site worked as well as the ["violently adorable" TV ads](https://www.youtube.com/watch?v=Dh9munYYoqQ)! To me it's a software disaster as stunning as the [Hindenburg](https://en.wikipedia.org/wiki/Hindenburg_disaster) and it happened right here in my own backyard. The blank stares after talking about it for 10 (or more) minutes tell me that not everyone shares my level of fascination. In particular, I find that people who work in software are the _least_ surprised, "Oh of course it failed! I bet the code was a mess!"  But why do we view the failure of massive software projects like this as almost inevitable? 

<a title="Sam Shere (1905–1982), Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Hindenburg_disaster.jpg"><img alt="Hindenburg disaster" src="https://upload.wikimedia.org/wikipedia/commons/1/1c/Hindenburg_disaster.jpg"></a>

Co-worker's aren't wrong about the odds of success, most large software projects tend to fail not just government projects. But we don't talk about other types of engineering like this. Bridges rarely collapse even though civil engineers in the United States issue dire reports. Even rockets, AKA literal rocket science, launch _and land_ without much fanfare these days. Yet core parts of our state infrastructure can fail to deliver unemployment insurance correctly and the reporting focuses mostly on the high level political characters - as if it's their fault the mainframes running COBOL can't handle the crisis. 

In an obvious sense it is a failure in leadership to let core systems fail through mismanagement and neglect. But that's not the story of the Cover Oregon failure. The State and (mostly) Federal government spent over $300M for a new website that never launched. We didn't even get to see a rocket explode during testing. Nothing. Any number greater than a dollar for _nothing_ seems like a bad deal. 

## What happened? 

Again if you've ever worked in software you can probably guess most of the root causes [listed in the reporting](https://github.com/suite22/oregon-healthcare-website-retro): poor planning, terrible communication, lots of political CYA'ing, shoddy work, etc... And yet how can we have nothing to show for it all beyond lawsuits between the State and Oracle? Where is the code? What were the details of some of the terrible decisions? 

## What did we learn?

That's the core of the question that has kept me interested in this story. With the Hindenburg we stopped flying around in massive explode-y ships. We [built bridges differently](https://practical.engineering/blog/2019/3/9/why-the-tacoma-narrows-bridge-collapsed) after the Tacoma Narrows bridge collapsed. After the Challenger disaster [the commission named names](https://www.washingtonpost.com/archive/politics/1986/06/10/challenger-disaster-blamed-on-o-rings-pressure-to-launch/6b331ca1-f544-4147-8e4e-941b7a7e47ae/) and made significant changes to prevent another shuttle from exploding (the [Netflix series](https://www.space.com/challenger-final-flight-netflix-docuseries.html) is great!). Complex problems and projects [fail for complex reasons](https://how.complexsystems.fail) but after reading through the newspaper reporting, TV segments, lawsuits, and Congressional report it seems most of us (residents of the state and software engineers) learned next to nothing from the $300M+. 

I plan to highlight the best portions in later posts from the Congressional report and lawsuits about the Cover Oregon failure, but there's no [memorable Feynman-level insight](http://www.feynman.com/science/the-challenger-disaster/) that I've uncovered. There's also been no major reform in how the State does business with Oracle. The lawsuits were ultimately settled and Oracle still sells software that is [critical to core operations in the State](https://patch.com/oregon/portland/oregon-settles-oracle-over-cover-oregon-fiasco). We're talking about a project failure that ultimately required [daily updates to Larry Ellison](https://pamplinmedia.com/pt/9-news/294405-171739-documents-oracle-doesnt-want-you-to-read-) - the co-founder and head of Oracle at the time. Lots of political fallout was [placed on Governor Kitzhaber](https://www.oregonlive.com/business/2014/08/oracle_cover_oregon_lawsuit.html) after he left office from unrelated scandals. But are they the only satisfying characters to blame as the figureheads at the top?

## How do we prevent another disaster?

Beyond the specifics of the Oregon Cover failure, how and what should we change so we actually learn from the past? Talking with other smart folks I want to write about how we can improve - building software inside and outside government.

In future posts my hope is to find a way to tell you a story worth sticking around for - what happened, what did we learn, and how do we prevent another disaster.

My (rough) outline ahead is:

### 1. What is code?
How do we talk about a software project failure in a way that everyone can follow along? What analogies or comparisons can we make to understand the scale? What does a bridge project cost? How much have other major software project failures cost? Paul Ford's legendary 38K word article ["What is code?"](https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/) is a wonderful prompt for further exploration.

### 2. Reporting on Software
I've spent hours reading and watching through the wonderful reporting done by newsrooms across the state: [Jeff Manning](https://twitter.com/JeffmanningOre) at The Oregonian, [Nick Budnick](https://twitter.com/NickBudnick) at the Portland Tribune, and [Chelsea Kopta](https://twitter.com/ChelseaKopta) at KATU in particular spent endless hours reporting the various angles of the story. The technical specifics of the project though are largely buried in source materials. How should technical failures be reported? Do people care about the details? Professionally, I still have questions about the high level architecture and a serious fascination with minutiae like: burn-down charts, team structures, source code, etc.

### 3. Software as Infrastructure
The analogy of software to roads and bridges is popular, but is it useful in this case? We grade the health of bridges in the State but do we grade the health of software used by the State? What is the state of our software infrastructure?

### 4. Crash Investigators
When a plane crashes the NTSB is responsible for determining a root cause and making recommendations to improve overall safety for air travel. Should we have something like the NTSB for failed software projects?

### 5. Software _Engineering_?
Is the field of engineering the best comparison for writing software? In the early days of the field people  had to fight for the title of "Software **Engineer**" so that they would be taken as seriously as the other engineering disciplines. But is there a better analogy? Is writing software on a large team more like writing a novel together - software _novelists_? Martin Fowler said that maybe a lawyer is a better comparison because what is software if not contracts between systems? 

### 6. State Mishandling vs Corporate Fraud?
Did the State fail to properly manage the project? Did Oracle set out to rip the State off from the start? Who is ultimately responsible? Much of the reporting on the failure centered on these questions, and I'm not certain I will be the one to establish any new insights but I hope that a thorough review of the technical details can bring more satisfying answers.

--- 

If you also find this topic interesting I have an open-source [repo on Github](https://github.com/suite22/oregon-healthcare-website-retro) where I've been collecting source material and notes. If you have insights you would like to share please [reach out on Twitter](https://twitter.com/suite22). I've spent a long time thinking this story and I'm excited to finally start sharing more of my findings here.