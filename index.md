---
layout: home
title: STRATUS Lab
image:
  path: /images/hero.jpg
---

<style>
.masthead {
  margin-bottom: 0 !important;
}

.main-content {
  padding-top: 0 !important;
}

.page-image {
  margin-top: 0 !important;
  padding-top: 0 !important;
  margin-bottom: 6px !important;
}

/* Altezza legata al viewport: su schermi bassi la testata si ritira
   invece di spingere il testo sotto la piega. */
.entry-feature-image {
  height: 22vh;
  min-height: 160px;
  max-height: 350px;
  width: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

.page-header h1 {
  font-size: 2.5rem;
}

.page-content p {
  margin-bottom: 0.9em;
}

/* L'acronimo sciolto, subito sotto il nome del laboratorio.
   Le lettere che lo compongono sono in colore: senza, la riga sembra un
   sottotitolo qualunque e nessuno si accorge che STRATUS vuol dire questo.
   Il selettore nomina .page-content perche' li' dentro i paragrafi sono
   giustificati, e questo va centrato. */
.page-content p.acronimo {
  text-align: center;
  margin: -0.4em 0 1.6em;
  font-size: 1.02em;
  line-height: 1.4;
  color: var(--muted);
  letter-spacing: 0.3px;
}

.page-content p.acronimo b {
  color: var(--accent);
  font-weight: 700;
}

.site-footer {
  margin-top: 10px !important;
  margin-bottom: 10px !important;
  padding-top: 14px !important;
  padding-bottom: 14px !important;
}

/* I loghi hanno proporzioni molto diverse fra loro e non stanno in una riga
   larga quanto la colonna di testo: questa fascia sfonda il contenitore. */
.partners-section {
  margin: 1.1em 0;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
  width: 94vw;
  max-width: 1040px;
}

.partners-section h3 {
  text-align: center;
  margin-bottom: 0.9em;
}

.partners-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 1.5em;
}

.partners-grid a {
  display: inline-flex;
  align-items: center;
  border-bottom: none;
}

.partners-grid img {
  height: 60px;
  width: auto;
  max-width: 120px;
  object-fit: contain;
  filter: grayscale(100%);
  opacity: 0.7;
  transition: all 0.3s ease;
}

.partners-grid a:hover img {
  filter: grayscale(0%);
  opacity: 1;
}
</style>

<p class="acronimo"><b>S</b>ecure, <b>TR</b>ustless, <b>A</b>utonomous <b>T</b>echnologies for <b>U</b>biquitous <b>S</b>ystems Laboratory</p>

STRATUS Lab is a research group at the Department of Engineering of the University of Messina, led by Prof. Francesco Longo.

Our research brings together cybersecurity, artificial intelligence, and distributed computing to advance secure, verifiable, and autonomous cyber-physical systems. Spanning embedded devices, robotics, autonomous vehicles, and cloud infrastructures, our work is guided by four pillars: Secure, Trustless, Autonomous, and Ubiquitous.

We pursue these challenges through national and international research projects and collaborations with academic and industrial partners.

The lab also supports two student teams: [Zancle E-Drive](https://www.zancle-edrive.it/), which develops electric Formula Student vehicles and competes in RoboRacer, and MetaGriPwn HackLab, which supports CyberChallenge.IT training and participates in cybersecurity competitions.

---

<div class="partners-section" id="partners">
  <h3>Our Partners</h3>
  <div class="partners-grid">
    <a href="https://www.st.com/" target="_blank" rel="noopener" title="STMicroelectronics"><img src="/images/ST.png" alt="STMicroelectronics"></a>
    <a href="https://www.cnr.it/" target="_blank" rel="noopener" title="CNR"><img src="/images/CNR.png" alt="CNR"></a>
    <a href="https://serics.eu/" target="_blank" rel="noopener" title="SERICS"><img src="/images/Serics.png" alt="SERICS"></a>
    <a href="https://www.consorzio-cini.it/" target="_blank" rel="noopener" title="CINI"><img src="/images/CINI.png" alt="CINI"></a>
    <a href="https://www.northeastern.edu/" target="_blank" rel="noopener" title="Northeastern University"><img src="/images/NE.png" alt="Northeastern University"></a>
    <a href="https://ethz.ch/" target="_blank" rel="noopener" title="ETH Zurich"><img src="/images/ETH.png" alt="ETH Zurich"></a>
    <a href="https://www.nvidia.com/" target="_blank" rel="noopener" title="NVIDIA"><img src="/images/NVIDIA.png" alt="NVIDIA"></a>
    <a href="https://smartme.io/" target="_blank" rel="noopener" title="SmartMe.IO"><img src="/images/SmartMe.png" alt="SmartMe.IO"></a>
  </div>
</div>
