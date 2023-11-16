---
title: People
layout: single
permalink: /people/
classes: wide
author_profile: true
---

Current and past lab members.

<!-- get lists of people -->
{% assign current_list = site.people | where: "current", true %}
{% assign alum_list = site.people | where: "current", false %}

{% assign masters_list = current_list | where_exp: "item", "item.categories contains 'Masters'" %}
{% assign phd_list = current_list | where_exp: "item", "item.categories contains 'PhD'" %}
{% assign postdoc_list = current_list | where_exp: "item", "item.categories contains 'PostDoc'" %}



<!-- make grids of people in different categories -->

<!-- ### PostDocs -->

{% include sub-grid.html entries=postdoc_list sort_by=page.sort_by sort_order=page.sort_order type="grid" %}

{% if phd_list.size > 0 %}
### PhD Students

{% include sub-grid.html entries=phd_list sort_by=page.sort_by sort_order=page.sort_order type="grid" %}

{% endif %}

{% if masters_list.size > 0 %}
### Masters Students

{% include sub-grid.html entries=masters_list sort_by=page.sort_by sort_order=page.sort_order type="grid" %}

{% endif %}

### Alumni

{% include sub-grid.html entries=alum_list sort_by=page.sort_by sort_order=page.sort_order type="grid" %}
