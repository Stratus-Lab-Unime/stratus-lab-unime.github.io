---
layout: page
title: Teaching
permalink: /teaching/
---

<style>
/* Riquadri, pillole e colori stanno in /assets/css/stratus.css */
.teaching-section h2 {
  font-size: 0.9em;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--muted);
  margin: 2.2em 0 1.2em;
}

.teaching-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.2em;
}

.course-card {
  padding: 1.2em 1.4em;
}

.course-head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.6em;
  margin-bottom: 0.4em;
}

.course-title {
  font-weight: bold;
  font-size: 1.05em;
  color: var(--ink);
}

.course-programme {
  font-size: 0.9em;
  font-style: italic;
  color: var(--body-text);
  margin-bottom: 0.6em;
}

.course-role {
  font-size: 0.78em;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--body-text);
  margin-bottom: 0.3em;
}

.course-meta {
  font-size: 0.8em;
  color: var(--muted);
  margin: 0;
}

@media (max-width: 700px) {
  .teaching-grid {
    grid-template-columns: 1fr;
  }
}
</style>

Courses taught by Francesco Longo at the Department of Engineering of the University of Messina, and at the other departments and doctoral schools that draw on the group's subject area.

<div class="teaching-section">
{% assign current = site.data.teaching | where: "status", "current" %}
{% assign past = site.data.teaching | where: "status", "past" %}

  <h2>Currently taught</h2>
  <div class="teaching-grid">
{% for c in current %}
    <div class="course-card" id="{{ c.id }}">
      <div class="course-head">
        <span class="course-title">{{ c.title }}</span>
        <span class="course-badge">{{ c.level }}</span>
      </div>
      <div class="course-programme">{{ c.programme }}</div>
      <div class="course-role">{{ c.role }}</div>
      <p class="course-meta">
        {%- if c.credits != "" %}{{ c.credits }} CFU, {% endif -%}
        {{ c.hours }} hours &middot; taught in {{ c.language }}
        {%- if c.since != "" %} &middot; since {{ c.since }}{% endif -%}
      </p>
    </div>
{% endfor %}
  </div>

  <h2>Previously taught</h2>
  <div class="teaching-grid">
{% for c in past %}
    <div class="course-card" id="{{ c.id }}">
      <div class="course-head">
        <span class="course-title">{{ c.title }}</span>
        <span class="course-badge">{{ c.level }}</span>
      </div>
      <div class="course-programme">{{ c.programme }}</div>
      <div class="course-role">{{ c.role }}</div>
      <p class="course-meta">
        {%- if c.credits != "" %}{{ c.credits }} CFU, {% endif -%}
        {{ c.hours }} hours &middot; taught in {{ c.language }} &middot; {{ c.since }}
      </p>
    </div>
{% endfor %}
  </div>
</div>
