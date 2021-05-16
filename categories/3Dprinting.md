---
layout: post
title: "3D Printing"
date: 2019-02-25
image: '/assets/img/'
description: 'and CAD Design'
twitter_text: ' '
---

This will be filled up with more information and pictures at a later stage

### Molecules and Proteins
- [RLP30 + NLP](https://www.youmagine.com/designs/rlp30-nlp-protein-models) - Ectodomain of the RLP30 receptor and its ligand NLP

### Labequipment
- [Glass Vial Rack](https://www.youmagine.com/designs/glass-vial-racks) - Simple rack for glass vials
- [Base for Measuring Cylinder](https://www.youmagine.com/designs/base-for-measuring-cylinder) - Base for a measuring cylinder
- [NMR Tube Rack](https://www.youmagine.com/designs/nmr-tube-rack) - Rack for 3 or 5 mm NMR tubes

### Functional Prints
- [Workbench Tool Holder](https://www.youmagine.com/designs/different-holders-for-your-work-bench-equipment) - Collection of simple tool holder
- [Shelf Holder](https://www.youmagine.com/designs/shelf-holder-for-table-foot) - Simple shelf holder for a standard IKEA table foot
- [Windshield Wiper Repair](https://www.youmagine.com/designs/windshield-wiper-repair-nissan-micra-k11-2001) - Replacement for windshield wiper part in a Nissan Micra


{% comment %}

{% for category in site.categories %}
  {% if category[0] == "3Dprinting" %}
    <h3>{{ category[0] }}</h3>
    <ul>
      {% for post in category[1] %}
      <div class="user-projects">
        <div class="images-left-page">
          <img src="{{ post.image | prepend: site.baseurl }}"/>
        </div>
        <div class="contents-right-page">
          <h3> {{ post.title }}: {{ post.description }} </h3>
          <p>  {{ post.long_description }} </p>
          <a class="project-link" href="{{ post.url }}">Tell me more!</a>
        </div>
      </div>
      {% endfor %}
    </ul>
  {% endif %}
{% endfor %}

<br>
#### This is a growing list of projects which is updated once in a while


{% for category in site.categories %}
  {% if category[0] == "3Dprinting" %}
    <h3>{{ category[0] }}</h3>
    <ul>
      {% for post in category[1] %}

        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
        <img src= "{{ post.image | prepend: site.baseurl }}">
        {{ post.description }}
        {% endfor %}
    </ul>
  {% endif %}
{% endfor %}
{% endcomment %}
