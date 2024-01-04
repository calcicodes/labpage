---
layout: single
title:  "New Paper: Kgen!"
excerpt: "Kgen: reducing inconsistencies in seawater carbon calculations."
categories: research paper
chatgpt: false
toc: true
toc_sticky: true
header:
  teaser: /assets/images/software/kgen-teaser.png
---

We've just released [Kgen](https://palaeocarb.github.io/Kgen/), a software package for calculating stoichiometric equilibrium constants (**K*'s**) for calculating carbon chemistry in seawater... so what does that mean?

K\*'s are used to calculate the state of dissolved carbon in seawater. This is a big deal because this sets the relationship between ocean carbon concentration, pH and CO<sub>2</sub> in the atmosphere, so it's *really* important to get them right. The issue here is that many different people have their own favourite methods of doing these calculations using multiple software platforms and packages, and there's no consistent cross-checking to make sure everyone is using the same numbers. This has caused problems in the past, when typos and inconsistencies have led to calculating different results for the same calculations. This has been a particular problem in palaeo reconstructions, where the composition of seawater changes, and **this is the problem that Kgen solves**.

Kgen to provides consistent K\* values across three different computing platforms (Python, R, and Matlab). This allows researchers to confidently use K\* values in their calculations, knowing that someone else using different software will get exactly the same result. It also integrates a pitzer model for calculating the influence of changing seawater composition on K\* values, which is particularly important for palaeo reconstructions.

## Find out more

 - [Read the preprint](https://doi.org/10.22541/essoar.170421455.50048580/v1)
 - [Check out the software](https://palaeocarb.github.io/Kgen/)
