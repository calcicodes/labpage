---
layout: single
title:  JOB TITLE
excerpt: SHORT DESCRIPTION
categories: job
people_category: CATEGORY  # OPTIONAL TO MAKE PEOPLE APPEAR AT THE BOTTOM
toc: true
toc_sticky: true
header:
  teaser: /assets/images/posts/leverhulme-pdra2-teaser.png  # ADD IMAGE
open: true
apply_url: LINK TO APPLICATION PAGE
apply_deadline: APPLICATION DEADLINE
interview_period: WHEN WILL INTERVIEWS BE HELD
---

BRIEF DESCRIPTION OF THE JOB AND WHAT I'M LOOKING FOR

**Applications:**
{% if page.open %}
{: .notice--info}
The deadline for applications is **{{ page.apply_deadline }}**. See [below](#logistical-details) for more details.
{% else %}
{: .notice--warning}
**Applications for this position are now closed.** Please see our [jobs page](/jobs) for other opportunities.
{% endif %}

## Project Scope

DESCRIBE THE PROJECT

## What sort of person am I looking for?

WHO AM I LOOKING FOR?

## How do I find out more?

FIND OUT MORE

## Logistical Details

ANYTHING LOGISTICAL

{% if page.open %}

{: .notice--info}
The deadline for applications is **{{ page.apply_deadline }}**. We anticipate that interviews will be held in {{ page.interview_period }}.

[Apply Here]({{ page.apply_url }}){: .btn .btn--info}

{% else %}

{: .notice--warning}
**Applications for this position are now closed.**

{% endif %}
