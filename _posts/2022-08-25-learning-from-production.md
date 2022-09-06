---
layout: post
title: Learning from What We Build
image: $$ Use something from Midjourney $$
published: false
---
Build measure fix - cite the actual model that people use. 
This article is valuable because we're going to show examples of why you can learn faster and better through better telemetry.

Imagine that we can simplify the range of states that the application be in by representing it as a 2D grid like Minesweeper. 
Find the bug 
$$ minesweeper with emoji tiles $$
One of the cells contains a bug. If you manually click through to find it you have some clicking to do.
Now expand our imagined grid. Your application is likely vastly more complex.
We can improve our odds with testing but fundamentally there are more states you can imagine in advance or reason about.
Chess is constrained but there are even more possible variations of chess games than there are atoms in the observable universe.
If your code is doing more than a game of chess then there are potentially even more states. The point is that the number of possible states is beyond the limits of your limited attention span while coding.
$$ expanded interactive grid $$
We don't have time to search ourselves as the grid grows. We actually only need to know about the bugs that impact the business and our customers. In an ecommerce app checkout is more important than the precise pixels in rounded buttons. We can use engineering Telemetry to light flares to guide us. We can now look out across the landscape from our watch tower to see the flares early. Now we know when we need to big deeper into a system and learn about what's not working as expected.

Could include a section in the middle about QA and other developers wandering around blindly. 
Also a brief discussion about black box testing as our model for discussion in this case.
We want to constrain the possible states based on one of my favorite articles. 

KEEP the simulation part from Nicky Case and make it where the bugs are introduced as new versions release. Then we can see how the telemetry we add helps reduce the bug rate or at least the time to remediate. 