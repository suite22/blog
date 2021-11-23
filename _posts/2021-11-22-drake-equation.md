---
layout: post
title: Exploring the Drake Equation
---

There's a beautiful scene in [Five Billion Years of Solitude](https://bookshop.org/books/five-billion-years-of-solitude-the-search-for-life-among-the-stars/9781617230165) that I keep returning to where the author is touring [Frake Drake](https://en.wikipedia.org/wiki/Frank_Drake)'s greenhouses filled with orchids:

<blockquote class="quoteback" darkmode="true" data-title="Five Billion Years of Solitude, page 37-38" data-author="Lee Billings" cite="https://bookshop.org/books/five-billion-years-of-solitude-the-search-for-life-among-the-stars/9781617230165">
<div>
<p>He opened the door to the nearest one, and the hum of ventilation fans and a blast of humid, loamy air flowed out over the grass. Stepping inside, he let out a peaceful sigh. Like the other two greenhouses alongside it, this one was filled with orchids.</p>
[...]
<p>Drake turned to what he said was his current favorite, a single orange bloom with three angular petals
that tapered to sharp, blood-red points. They looked like fangs. 'This one's a hybrid of two different genuses [... ] No one's seen one like this before, with this red. It wasn't blooming yesterday. Some of these only blossom one day out of the year, and the next day they're gone. You're lucky to be here right now – the flowers aren't long for this world.' He touched the petals with reverence.</p>
[...]
<p>I told Drake his orchids made me think of <i>L</i>, a technological civilizations longevity, the greatest uncertainty in his equation. If it was too low, our galaxy could give birth to millions, even billions, of civilizations over its eons-long life, but each one, isolated on a lonely planet, would wither and fall unseen with no chance for cross-pollination. If <i>L</i> was high, then in-bloom civilizations could linger and eventually intermingle, hybridizing their cultures across the light-years. Stability could set in; some would perhaps gain a sort of immortality.</p>
<p>Drake smiled and nodded. The similarity had not escaped his notice.</p>
</div>
<footer>Lee Billings<cite> <a href="https://bookshop.org/books/five-billion-years-of-solitude-the-search-for-life-among-the-stars/9781617230165">https://bookshop.org/books/five-billion-years-of-solitude-the-search-for-life-among-the-stars/9781617230165</a></cite></footer>
</blockquote><script src="https://cdn.jsdelivr.net/gh/Blogger-Peer-Review/quotebacks@1/quoteback.js"></script>

The book has many other fantastic moments but this scene has lodged that _L_, longevity, in my mind as something worth thinking deeply about. Essays from [The Clock of the Long Now](https://bookshop.org/books/the-clock-of-the-long-now-time-and-responsibility/9780465007806) pair well with this. 

### Drake Equation 

_N_ = _R_<sub>∗</sub> &bull; _f_<sub>p</sub> &bull; _n_<sub>e</sub> &bull; _f_<sub>l</sub> &bull; _f_<sub>i</sub> &bull; _f_<sub>c</sub> &bull; _L_

It's hard to understand exactly what the range of possible values in the [Drake Equation](https://en.wikipedia.org/wiki/Drake_equation) (above) produce, so I made a small [explorable](https://explorabl.es) version to play with below. Each of the underlined values is interactive and draggable like a slider.

<span id="interactive-article-anchor"></span>

<script src="/assets/idyll-embed.min.js"></script>
<script>
    // From https://en.wikipedia.org/wiki/Drake_equation
    // The Drake equation is: N = R∗ ⋅ fp ⋅ ne ⋅ fl ⋅ fi ⋅ fc ⋅ L
    // N = the number of civilizations in our galaxy with which communication might be possible
    // R∗ = the average rate of star formation in our Galaxy
    // fp = the fraction of those stars that have planets
    // ne = the average number of planets that can potentially support life per star that has planets
    // fl = the fraction of planets that could support life that actually develop life at some point
    // fi = the fraction of planets with life that actually go on to develop intelligent life (civilizations)
    // fc = the fraction of civilizations that develop a technology that releases detectable signs of their existence into space
    // L = the length of time for which such civilizations release detectable signals into space

    // Find the element where Idyll will inject content.
    var articleAnchor = document.getElementById('interactive-article-anchor');

    // Get your markup.
    var idyllMarkup = '\
    [var name:"R" value:3 /] \
    [i]R[/i][sub]∗[/sub] = [Dynamic value:R min:0 max:25 format:"d" /] the average rate of star formation in our Galaxy. \
    [br /] \
    [var name:"fp" value:0.95 /] \
    [i]f[/i][sub]p[/sub] = [Dynamic value:fp min:0 max:1 step:"0.01" format:"0.0%" /] the fraction of those stars that have planets. \
    [br /] \
    [var name:"ne" value:5 /] \
    [i]n[/i][sub]e[/sub] = [Dynamic value:ne min:0 max:100 format:"d" /] the average number of planets that can potentially support life per star that has planets. \
    [br /] \
    [var name:"fl" value:0.5 /] \
    [i]f[/i][sub]l[/sub] = [Dynamic value:fl min:0 max:1 step:"0.01" format:"0.0%" /] the fraction of planets that could support life that actually develop life at some point. \
    [br /] \
    [var name:"fi" value:0.5 /] \
    [i]f[/i][sub]i[/sub] = [Dynamic value:fi min:0 max:1 step:"0.01" format:"0.0%" /] the fraction of planets with life that actually go on to develop intelligent life (civilizations). \
    [br /] \
    [var name:"fc" value:0.5 /] \
    [i]f[/i][sub]c[/sub] = [Dynamic value:fc min:0 max:1 step:"0.01" format:"0.0%" /] the fraction of civilizations that develop a technology that releases detectable signs of their existence into space. \
    [br /] \
    [var name:"L" value:1000 /] \
    [i]L[/i] = [Dynamic value:L min:0 max:1000000 step:"100" format:"d" /] the length of time for which such civilizations release detectable signals into space. \
    [br /] \
    [derived name:"N" value:`R * fp * ne * fl * fi * fc * L` /] \
    [i]N[/i] = [Display value:N format:"d" /] the number of civilizations in our galaxy with which communication might be possible.';

    // Instantiate the Idyll runtime.
    Idyll.render(idyllMarkup, articleAnchor);
</script>

## How I Made This
I used [idyll-embed](https://github.com/idyll-lang/idyll-embed) and a simple inline script. The tiny scale of this explorable reminds me of being back in high school tinkering around on the internet. Puttering aimlessly, except here I've found a question I want to think more about.