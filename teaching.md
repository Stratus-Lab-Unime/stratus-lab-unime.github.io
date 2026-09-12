---
layout: page
title: Teaching
permalink: /teaching/
---

<style>
.teaching-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5em;
  margin: 2em 0;
}

/* Riquadri, pillole e colori stanno in /assets/css/stratus.css */
.course-card {
  transition: box-shadow 0.3s ease, transform 0.3s ease;
  text-decoration: none;
  display: block;
}

.course-card:hover {
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  transform: translateY(-3px);
  text-decoration: none;
}

.course-title {
  font-size: 1.1em;
  margin-bottom: 0.5em;
}

.course-degree {
  font-size: 0.85em;
  margin-bottom: 0.8em;
  line-height: 1.5;
}

.course-degree span {
  font-style: italic;
}

.course-badge {
  margin-bottom: 0.8em;
}

.course-professor {
  font-size: 0.85em;
  display: flex;
  align-items: center;
  gap: 0.4em;
}

.course-professor i {
  color: var(--accent-bright);
}

@media (max-width: 600px) {
  .teaching-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="teaching-grid">

  <a class="course-card" href="/teaching/fondamenti-di-informatica/">
    <div class="course-title">Fondamenti di Informatica</div>
    <span class="course-badge">Bachelor's Degree</span>
    <div class="course-degree">Bachelor's Degree Programme in <span>"Ingegneria Elettronica ed Informatica"</span></div>
    <div class="course-professor"><i class="fas fa-user"></i> Prof. Francesco Longo</div>
  </a>

  <a class="course-card" href="/teaching/cybersecurity/">
    <div class="course-title">CyberSecurity</div>
    <span class="course-badge">Master's Degree</span>
    <div class="course-degree">Master's Degree Programme in <span>"Engineering in Computer Science"</span></div>
    <div class="course-professor"><i class="fas fa-user"></i> Prof. Francesco Longo</div>
  </a>

  <a class="course-card" href="/teaching/embedded-systems/">
    <div class="course-title">Embedded Systems</div>
    <span class="course-badge">Master's Degree</span>
    <div class="course-degree">Master's Degree Programme in <span>"Engineering in Computer Science"</span></div>
    <div class="course-professor"><i class="fas fa-user"></i> Prof. Francesco Longo</div>
  </a>



</div>
