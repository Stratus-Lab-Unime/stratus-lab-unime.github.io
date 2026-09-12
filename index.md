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
  text-align: justify;
  margin-bottom: 0.9em;
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

The **STRATUS Lab** — *Secure, TRustless, Autonomous Technologies for Ubiquitous Systems Laboratory* — is a research group at the Department of Engineering of the University of Messina, led by Prof. Francesco Longo.

The group works where computing has left the data center: security and formal verification for industrial and automotive systems, trustless architectures built on self-sovereign identity and federated learning, autonomy for robots and vehicles under real-world constraints, and the virtualization and orchestration that hold the cloud-to-things continuum together. This work is carried out through national and international research projects, and through long-standing collaborations with leading industrial and academic partners in Italy, Europe and the United States.

The lab supports two student teams: [Zancle E-Drive](https://www.zancle-edrive.it/), which builds a fully electric single-seater for Formula Student and races in [RoboRacer](https://roboracer.ai/), and the MetaGriPwn HackLab, which competes in CyberChallenge.IT and other cybersecurity competitions.

---

<div class="partners-section">
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
