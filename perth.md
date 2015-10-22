---
layout: page
title: Perth
menu: yes
---
## Contact

* Twitter: [SecTalks](https://twitter.com/sectalks)
* Email: [perth@sectalks.org](mailto:perth@sectalks.org)

## Organising team

* [@nanomebia](https://twitter.com/nanomebia)

## Location

Perth CBD (available to members only)

## Date & Time

Second last Thursday of each month at 5:30pm.

## Upcoming meetup

Details will be sent to the members mailing list.

## How to join

We always like to get more awesome people in.
We have an entry qualification challenge that you need
to solve to show us your degree of awesomeness.

#### What is the entry challenge?

1. Follow [sectalks](https://twitter.com/sectalks) on Twitter.
1. Tweet "@sectalks, V jnaan wbva...".
1. The challenge details will be DMed to you.
1. Have fun and email us the flag.

*Note: Twitter doesn't allow for DM, if you don't follow @sectalks.*

#### But I am new to security, can I still join?

SecTalks is always open to anyone who is keen to learn infosec.
Ask a member to refer you (see our twitter followers) or email us and
lets us know why you wanna join and we will be in touch.

## Past meetups

{% for post in site.posts %}
{% if post.categories contains "meetup" and post.categories contains "perth" %}
* <a href="{{ post.url | prepend: site.baseurl | prepend: site.url }}">{{ post.title }}{% if post.summary %} - {{ post.summary }}{% endif %}</a>
{% endif %}
{% endfor %}
