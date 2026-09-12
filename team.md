---
layout: page
title: Team
permalink: /team/
---

<style>
.lab-director {
  display: flex;
  gap: 2em;
  align-items: center;
  margin: 2em 0 2.5em;
}

.director-photo {
  flex: 0 0 210px;
  border-radius: 8px;
  overflow: hidden;
  border: 3px solid #eee;
}

.director-photo img {
  width: 100%;
  display: block;
  border: none !important;
  border-radius: 0 !important;
  margin: 0 !important;
  max-width: none !important;
}

.director-name {
  display: block;
  font-weight: bold;
  font-size: 1.35em;
  color: #222;
}

.director-role {
  display: block;
  font-size: 0.85em;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  color: #6a0dad;
  margin-bottom: 0.8em;
}

.director-bio {
  text-align: justify;
  margin: 0;
}

/* Sotto i 700px la foto va sopra il testo invece che accanto */
@media (max-width: 700px) {
  .lab-director {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .director-photo { flex-basis: auto; width: 180px; }
  .director-bio { text-align: left; }
}

.people-section {
  margin: 2em 0;
}

.people-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.5em;
}

.person-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  width: 160px;
}

.img-circle {
  width: 130px;
  height: 130px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid #eee;
  margin-bottom: 0.8em;
  transition: border-color 0.3s ease;
}

.img-circle:hover {
  border-color: #6a0dad;
}

.img-circle img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 0 !important;
  border: none !important;
  margin: 0 !important;
  max-width: none !important;
  display: block;
}

.person-name {
  font-weight: bold;
  font-size: 0.95em;
  color: #222;
  margin-bottom: 0.2em;
}

/* Allinea il ruolo in fondo alla scheda, così resta alla stessa altezza
   anche quando il nome accanto occupa due righe. */
.person-role {
  font-size: 0.8em;
  color: #888;
  margin-top: auto;
}
</style>

<div class="lab-director">
  <div class="director-photo">
    <img src="/images/people/Longo-director.jpg" alt="Francesco Longo">
  </div>
  <div class="director-text">
    <span class="director-name">Francesco Longo</span>
    <span class="director-role">Lab Director &middot; Associate Professor</span>
    <p class="director-bio">Francesco Longo is Associate Professor at the Department of Engineering of the University of Messina, where he leads the STRATUS Lab. His work spans distributed systems, cloud and edge computing, and the security of industrial and automotive infrastructure, with more than 170 publications in the field. He is a founding partner of <a href="https://smartme.io/" target="_blank" rel="noopener">SmartMe.IO</a>, a Messina-based company building IoT and resilience engineering platforms.</p>
  </div>
</div>

<div class="people-section">
  <div class="people-grid">

    <div class="person-card">
      <div class="img-circle">
        <img src="/images/people/Merlino.png" alt="Giovanni Merlino">
      </div>
      <span class="person-name">Giovanni Merlino</span>
      <span class="person-role">Associate Professor</span>
    </div>

    <div class="person-card">
      <div class="img-circle">
        <img src="/images/people/Fabiano.png" alt="Manuel Fabiano">
      </div>
      <span class="person-name">Manuel Fabiano</span>
      <span class="person-role">PhD Student</span>
    </div>

    <div class="person-card">
      <div class="img-circle">
        <img src="/images/people/Bucaria.png" alt="Vincenzo Bucaria">
      </div>
      <span class="person-name">Vincenzo Bucaria</span>
      <span class="person-role">PhD Student</span>
    </div>

    <div class="person-card">
      <div class="img-circle">
        <img src="/images/people/Lombardo.png" alt="Giovanni Lombardo">
      </div>
      <span class="person-name">Giovanni Lombardo</span>
      <span class="person-role">PhD Student</span>
    </div>

    <div class="person-card">
      <div class="img-circle">
        <img src="/images/people/Pispisa.png" alt="Gaetano Pio Pispisa" style="object-position: 75% top !important;">
      </div>
      <span class="person-name">Gaetano Pio Pispisa</span>
      <span class="person-role">PhD Student</span>
    </div>

  </div>
</div>
