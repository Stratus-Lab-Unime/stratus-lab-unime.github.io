---
layout: page
title: Why STRATUS?
permalink: /why-stratus/
---

<style>
/* Colori e riquadri arrivano da /assets/css/stratus.css */
.lupa-photo {
  margin: 2em 0;
}

.lupa-photo img {
  width: 100%;
  border-radius: var(--radius);
  display: block;
}

.lupa-photo figcaption {
  font-size: 0.8em;
  color: var(--muted);
  margin-top: 0.6em;
  text-align: center;
}

/* La mappa satellitare. L'immagine è un file servito dal repository, non un
   riquadro incorporato: nessuno dei visitatori finisce a chiamare un servizio
   di mappe, come già per jQuery. Il segnaposto sta sopra in HTML e non dentro
   il JPEG, così il testo resta nitido a qualunque ingrandimento e traducibile.
   Le due percentuali vengono dalla proiezione: le calcola
   .github/scripts/stretto_satellite.py, da cui esce anche l'immagine. */
.mappa {
  position: relative;
  max-width: 520px;
  margin-inline: auto;
}

.mappa-punto {
  position: absolute;
  left: 54.3%;
  top: 12.9%;
  width: 14px;
  height: 14px;
  margin: -7px 0 0 -7px;
  border-radius: 50%;
  background: var(--accent-bright);
  border: 2px solid #fff;
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.35);
}

.mappa-etichetta {
  position: absolute;
  left: 54.3%;
  top: 12.9%;
  transform: translate(16px, -0.75em);
  font-size: 0.78em;
  line-height: 1.3;
  color: #fff;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.9);
  white-space: nowrap;
}

.acronym {
  color: var(--accent);
  font-weight: bold;
}
</style>

No. We are not proposing stratus computing.

Computing has borrowed enough from meteorology already. There was cloud, then fog, then edge — and, for anyone keeping score, mist computing and dew computing are both real, both published, and both still waiting for someone to need them. The atmosphere has no more layers to spare.

The acronym came first. We needed a name for a group working on <span class="acronym">S</span>ecure, <span class="acronym">TR</span>ustless, <span class="acronym">A</span>utonomous <span class="acronym">T</span>echnologies for <span class="acronym">U</span>biquitous <span class="acronym">S</span>ystems, and the letters fell out as STRATUS. Only afterwards did someone point out what a stratus actually is.

<figure class="lupa-photo">
  <img src="/images/lupa/lupa-porto.jpg" alt="A low bank of fog crossing the Strait of Messina behind a marina, under a clear sky">
  <figcaption>The fog crosses the Strait as a single flat layer, with clear air above it. Photo: <a href="https://www.normanno.com/">Normanno.com</a></figcaption>
</figure>

A stratus is the low, flat, featureless cloud that spreads in sheets instead of piling up. When it comes down far enough to touch the surface, it stops being called a cloud and starts being called fog. That is the whole difference: altitude.

And the Strait of Messina produces one of the finest examples in the Mediterranean. Here it is called **la Lupa** — the she-wolf.

It is advection fog. In spring the water of the Strait stays below 17 °C, kept cold by the deep currents that constantly exchange water between the Tyrrhenian and the Ionian. When the first warm, humid air of North African origin drifts across that cold surface, it cools abruptly, condenses, and settles into a layer one to two hundred metres thick that crosses the Strait and swallows both shores in minutes.

A stratus, lying on the sea, where we happen to work.

<figure class="lupa-photo mappa">
  <img src="/images/lupa/stretto-satellite.jpg" alt="Satellite view of the Strait of Messina, with Sicily on the left and Calabria on the right, the sickle of Messina harbour at the centre and Capo Peloro at the top">
  <span class="mappa-punto" aria-hidden="true"></span>
  <span class="mappa-etichetta">Department of Engineering</span>
  <figcaption>The Strait, from Capo Peloro down the whole length of the city. <a href="https://s2maps.eu">Sentinel-2 cloudless 2024</a> by EOX IT Services, <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> &mdash; contains modified Copernicus Sentinel data 2024. The mosaic is built from the days without clouds, so this is the one picture of the Strait with no Lupa in it.</figcaption>
</figure>

As for the name, the most credible account is that the fog made the boats howl. Unable to see one another, crews would sound a conch shell to signal their position, and the noise carried over the water like wolves calling in the dark. Other explanations compete: the wolf as the devil, blamed for ruining the crops; the hunger of sailors who could not go out to fish; or simply a curse muttered at the weather.

<figure class="lupa-photo">
  <img src="/images/lupa/lupa-madonnina.jpg" alt="The Madonna della Lettera statue at the entrance of Messina harbour, standing against the fog">
  <figcaption>La Lupa at the harbour mouth. Photo: <a href="https://www.normanno.com/">Normanno.com</a></figcaption>
</figure>

Serendipity has given science penicillin and X-rays. It gave us a name that belongs to this stretch of sea.
