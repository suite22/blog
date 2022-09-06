---
layout: post
title: Random Walk
---

Hello.[^1]

<canvas id="randomWalk" width="600" height="600">
current stock price: $3.15 + 0.15
</canvas>
<script>
const canvas = document.getElementById('randomWalk');
if (canvas.getContext) {
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = 'rgb(200, 0, 0)';
    ctx.fillRect(10, 10, 50, 50);

    ctx.fillStyle = 'rgba(0, 0, 200, 0.5)';
    ctx.fillRect(30, 30, 50, 50);
}
</script>

[^1]: Footnote test one.