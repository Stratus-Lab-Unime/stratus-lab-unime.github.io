---
layout: page
title: Teaching
permalink: /teaching/
---

<style>
/* Riquadri e colori stanno in /assets/css/stratus.css */
.audience {
  background: var(--surface);
  border: 1px solid var(--line);
  border-left: 4px solid var(--accent-bright);
  border-radius: var(--radius);
  padding: 1.3em 1.5em;
  margin-bottom: 1.2em;
}

.audience h2 {
  font-size: 1.05em;
  color: var(--accent);
  margin: 0 0 0.6em;
}

.audience p {
  font-size: 0.9em;
  line-height: 1.6;
  margin: 0;
}

.audience p + p {
  margin-top: 0.7em;
}

.audience .wip {
  color: var(--muted);
  font-style: italic;
}

/* Un blocco che porta altrove si clicca tutto, non solo sulla parola: il link
   sta nel titolo e il suo ::after copre l'intero riquadro. Non si può usare un
   <a> intorno al blocco perché kramdown lo tratta come elemento inline e
   chiuderebbe il tag prima dell'<h2>. */
.audience--link {
  position: relative;
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}

.audience--link h2 a {
  color: inherit;
  text-decoration: none;
  border-bottom: none;
}

.audience--link h2 a::after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}

.audience--link:hover {
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transform: translateY(-3px);
}
</style>

Teaching, thesis supervision and internships with Francesco Longo, at the Department of Engineering of the University of Messina.

<div class="audience audience--link">
  <h2><a href="{{ '/teaching/courses/' | relative_url }}">If you are taking one of my courses</a></h2>
  <p>The list of courses, current and past, with credits, hours and the degree programme each one belongs to.</p>
</div>

<div class="audience">
  <h2>If you would like to do your thesis or internship with me</h2>
  <p class="wip">Under construction.</p>
</div>

<div class="audience">
  <h2>If you are already working on your thesis with me</h2>
  <p class="wip">Under construction.</p>
</div>
