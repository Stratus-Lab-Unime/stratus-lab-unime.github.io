---
layout: page
title: Research
permalink: /research/
---

At STRATUS, we investigate how intelligent cyber-physical systems can become more secure,
verifiable, and autonomous, while operating across increasingly distributed and heterogeneous
computing environments.

Our research is organized around four complementary pillars, connecting foundational research
with experimental applications in robotics, autonomous mobility, industrial systems, and
ubiquitous computing.

<style>
/* Riquadri e colori arrivano da /assets/css/stratus.css */
.research-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.2em;
  margin: 2em 0;
}

.research-header {
  display: flex;
  align-items: center;
  gap: 0.8em;
  margin-bottom: 1em;
}

.research-header i {
  font-size: 2.2em;
  width: 44px;
  text-align: center;
}

.research-header h3 {
  margin: 0;
  font-size: 1.1em;
  line-height: 1.2;
}

.research-item p {
  font-size: 0.9em;
  line-height: 1.6;
  margin: 0;
}

@media (max-width: 600px) {
  .research-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="research-grid">
{%- comment -%}
I quattro riquadri non sono scritti qui: vengono da _data/areas.yml, come le
quattro sezioni della pagina delle tesi. Lì ogni area porta due descrizioni, e
questa pagina legge `research_en`, quella in registro scientifico.
{%- endcomment -%}
{%- for a in site.data.areas %}
  <div class="research-item">
    <div class="research-header">
      {% include icon.html name=a.icon %}
      <h3>{{ a.label }}</h3>
    </div>
    <p>{{ a.research_en }}</p>
  </div>
{%- endfor %}

</div>
