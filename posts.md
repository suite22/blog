---
layout: default
title: Posts
---

# Posts By Time

{% assign postsByYearMonth = site.posts | group_by_exp: "post", "post.date | date: '%B %Y'" %}
{% for yearMonth in postsByYearMonth %}
  <h2>{{ yearMonth.name }}</h2>
  <ul>
    {% for post in yearMonth.items %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}

---

# Posts By Topic
{% for tag in site.tags %}
  {% assign tagnames = tag[0] %}
  
  <h2>{{ tagnames | capitalize }}</h2>
  <ul>
  {% assign topicposts = tag[1] %}
  {% for post in topicposts %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
  </ul>
{% endfor %}