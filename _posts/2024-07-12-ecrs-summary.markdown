---
layout: single
title:  "A Considerably Constructive Coral Conference: ECRS 2024"
excerpt: "Presenting early-stage PhD work at Europe's largest coral conference"
categories: conference
toc: false

---

Eight trains, five countries, and a few days after leaving Cambridge I found myself in Naples, Italy, for the 2024 [European Coral Reef Symposium (ECRS)](https://ecrs2024.eu/). The European chapter of the international society, [ICRS](https://coralreefs.org/) (no prizes for guessing the acronym!), the ECRS pops up somewhere in Europe once every four years, offset by two years from ICRS. Considering timing within my PhD, location, and keynotes, it was clear that it’d be an experience to write home about.

I attended ECRS to fill in the coral-loving world on my work [*predicting where coral will survive best in futures experiencing the environmental conditions caused by anthropogenic climate change*](https://orlando-code.github.io/research.html). The objective here is to guide our precious reef conservation efforts to those areas where corals are most likely to survive under climate change. This requires robust predictions of environmental suitability at spatial scales relevant to these conservation projects.

While it’s quite the challenge, initial results look promising. In short, a fairly simple machine learning model is able to nicely recreate the distribution of reefs that it would expect to see, given only information about depth, and how warm, how salty, how fast-moving, how sunny (et cetera et cetera) the oceans off Australia have been over the last ~150 years. 

<figure style="width: 100%" class="align-center">
  <img src="/assets/images/posts/ecrs_summary/GBR_predicted.png" alt="Prediction of reef distribtuion by machine learning model (similar to observed)." style="width:49%">
  <img src="/assets/images/posts/ecrs_summary/GBR_true.png" alt="Observed present-day reef distribution (similar to predicted)." style="width:49%">
  <figcaption>
  <strong> Model prediction of Great Barrier Reef.</strong> Left: Model prediction of coral density based on historic environmental timeseries. Right: Observed geographical distribution of the present-day reef.
  </figcaption>
</figure>

<figure style="width: 100%" class="align-center">
  <img src="/assets/images/posts/ecrs_summary/zGBR_predicted.png" alt="Prediction of reef distribtuion by machine learning model (similar to observed)." style="width:49%">
  <img src="/assets/images/posts/ecrs_summary/zGBR_true.png" alt="Observed present-day reef distribution (similar to predicted)." style="width:49%">
  <figcaption>
  <strong> Zooming in on the model prediction of Great Barrier Reef.</strong> Left: Model shies away from predicting the highest-density coral areas, and edges of coral patches. Right: Observed geographical distribution of the present-day reef.
  </figcaption>
</figure>

How do we know this information? Climate models! The beauty of being able to learn the conditions favoured by corals from these is that these models also contain our best guess as to what these conditions will look like far into the future as a result of various different roadmaps of greenhouse gas emissions. The ability to predict present-day coral coverage from this data therefore indicates that we can predict (under certain assumptions) where conditions will be favourable in the coming century. Longtermist conservation projects here we come! 

If you’re interested in learning more (or just enjoy animation), check out [my website](https://orlando-code.github.io/research.html) for slide decks and more detail. You can also use the site to get in touch: I’d love to hear from you!

Of course, my presentation was just one of many at ECRS. While the three jam-packed days contained too many excellent talks to count, a few particularly resonated: [Christian Voolstra](https://x.com/reefgenomics?lang=en) ([University of Konstanz](https://www.uni-konstanz.de/en/), President of ICRS) on the optimism and reef conservation best-practices imparted by a small island community in Indonesia (in press); [Andrew Baker](https://coralreeffutures.earth.miami.edu/people/lab-members/andrew-baker/index.html) ([University of Miami Coral Reef Futures Lab](https://coralreeffutures.earth.miami.edu/index.html)) on the prophetic [devastation of corals in the Florida Keys and the practice of ex-situ rescue](https://www.climate.gov/news-features/event-tracker/future-coral-restoration-florida-keys-after-unprecedented-marine-heat) and translocation of species; and [Michael Sweet](https://twitter.com/DiseaseMatters?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor) ([University of Derby](https://www.derby.ac.uk/)) on the need to curb emissions decades ago and what can still be done (and [is being done](https://www.coralspawninglab.org/)) to scale conservation efforts. 

Michael’s talk also highlighted the disconnect between the number of scientists who fly great distances (or perhaps worse, short distances) to attend events and their ongoing work to safeguard the future of our precious ecosystems. This continues to be a major friction point in the community, and hopefully one which will be addressed by greater awareness, virtual networking options, and better low-carbon transport infrastructure…

All in all, ECRS was an excellent place to get feedback on the approaches and objectives of my ongoing and future PhD work. Its prime value came from being able to meet (both casually and in response to presentations) people from all over Europe and the world to share our ideas, buoying both our passions and ambitions. Within hours of arriving at the conference I had a list of novel insights about things to explore, and was more excited than ever to get back to the keyboard and code!

So what’s next? Really useful conferences seem to generate more work than they demanded: contacting (and being contacted by) people to continue exchanging ideas and discuss collaborations, responding to feedback to wrap up the presented work into a paper, and exchanging photos! Given that I’m writing this from a plane bound for Bermuda – where I’ll be spending the next four months at the [Bermuda Institute of Ocean Sciences (BIOS)](https://bios.asu.edu/) taking courses on coral reef ecology and scientific diving while interning to improve our maps of the world’s reefs – there’s certainly a lot to look forward to. In the longer-term, bring on [ICRS 2026](https://www.icrs2026.nz/): coming to an Auckland, NZ, near you…