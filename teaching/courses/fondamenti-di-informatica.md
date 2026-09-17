---
layout: page
title: Fondamenti di Informatica
permalink: /teaching/courses/fondamenti-di-informatica/
course_id: fondamenti-di-informatica
---

{% assign c = site.data.teaching | where: "id", page.course_id | first %}
{% include course-header.html %}

<div class="faq-item" id="topics">
  <h2>Di cosa parla il corso?</h2>
  <p>Di come si rappresenta ed elabora l'informazione in un calcolatore e di come si programma in C. Il modulo A parte dal sistema binario, dall'architettura di Von Neumann e dagli algoritmi per arrivare ai costrutti del linguaggio C, agli array e ai puntatori; il modulo B affronta ricorsione, complessità computazionale, algoritmi di ricerca e ordinamento e le strutture dati elementari: liste, pile e code.</p>
  <p>Il programma ufficiale sta sulla <a href="{{ c.links.catalogue }}">pagina del corso nel catalogo di Ateneo</a>, con una scheda per ciascuno dei due moduli.</p>
</div>

<div class="faq-item" id="material">
  <h2>Dove trovo il materiale didattico?</h2>
  <p>Il materiale più aggiornato sta sul sistema di e-learning di Ateneo. Fate sempre riferimento all'ultimo anno accademico, che in questo momento è il <a href="{{ c.links.elearning }}">2026/2027</a>. Per accedere ai file dovete iscrivervi al corso.</p>
  <p>Il collegamento porta a una pagina di Ingegneria Biomedica: è quella corretta, non avete sbagliato. L'insegnamento è incardinato su quel corso di laurea.</p>
</div>

<div class="faq-item" id="contact">
  <h2>Come contatto il professore e dove trovo gli avvisi?</h2>
  <p>Potete scrivermi a <a href="mailto:flongo@unime.it">flongo@unime.it</a>, su WhatsApp o su Teams quando volete: non disturbate mai. Se sono impegnato, concordiamo un appuntamento.</p>
  <p>Il ricevimento in presenza è il martedì dalle 15.00 alle 16.00, al Dipartimento di Ingegneria, blocco B, settimo piano, stanza 743. Mandatemi prima una mail o un messaggio, per avere conferma che ci sono.</p>
  <p>Gli avvisi dell'ultimo minuto passano dalla chat WhatsApp di classe, che uso anche per le notizie dal Dipartimento e dall'Ateneo. Ne creo una nuova a ogni anno accademico: il link si trova nel blocco di slide #0 del modulo A, sull'e-learning.</p>
</div>

<div class="faq-item" id="exam">
  <h2>Come è strutturato l'esame?</h2>
  <p>Tre prove scritte e un orale. I numeri dei deck sono quelli delle slide dei due moduli.</p>
  <ul>
    <li><b>Prima prova scritta</b>, test a risposta multipla più un esercizio su carta: conoscere i principi di base dell'informatica, l'architettura dell'elaboratore, la rappresentazione digitale dell'informazione e i concetti di base dei linguaggi, ovvero tutto il programma fino al linguaggio C escluso (modulo A, deck da 01 a 05).</li>
    <li><b>Seconda prova scritta</b>, prova di programmazione: conoscere i concetti di base del linguaggio C, variabili e I/O di base, espressioni e operatori, strutture di controllo, array e stringhe, puntatori, tipi strutturati, funzioni e file, ovvero tutta la parte sul C fino alla fine del primo semestre (modulo A, deck da 06 a 13).</li>
    <li><b>Terza prova scritta</b>, un software da realizzare in C: saper implementare, date le specifiche, un software che svolge un compito ben preciso usando algoritmi e strutture dati semplici, ovvero la parte sul C fino a liste, pile e code incluse (modulo B, deck da 01 a 02).</li>
    <li><b>Prova progettuale</b>, facoltativa e permessa solo ai più meritevoli: l'implementazione di un software complesso date le sue specifiche, con algoritmi e strutture dati avanzate, ovvero la parte sul C fino a liste di liste e strutture dati più complesse (modulo B, deck 03).</li>
    <li><b>Prova orale</b>: conoscere le strutture dati e gli algoritmi trattati a lezione e saperli implementare in C, ovvero l'ultima parte del programma, dalla ricorsione fino agli alberi (modulo B, deck da 04 a 09). Si sostiene solo dopo aver superato tutte le prove scritte.</li>
  </ul>
  <p>Durante il primo semestre si svolgono due prove in itinere, corrispondenti alla prima e alla seconda prova scritta. Valgono esattamente un anno, fino alla corrispondente prova in itinere dell'anno successivo: per gli studenti in corso, fino all'appello di novembre incluso.</p>
  <p>Se non sostenete o non superate le prove in itinere, a ogni appello potete ripetere la prima e la seconda prova scritta, sostenere la terza prova scritta e sostenere la prova orale, quest'ultima solo dopo aver superato tutte le prove scritte.</p>
  <p>I testi degli appelli precedenti sono raccolti per prova: <a href="https://drive.google.com/drive/folders/19wuUuArBTbhi1hpOWUDAXQ4I7mww5mTy">prima</a>, <a href="https://drive.google.com/drive/folders/1wdfgNtqygGgs8Fym3zvkRnAkh5R5IIe-">seconda</a> e <a href="https://drive.google.com/drive/folders/1BBWfuju_t2m774QvXoGM7asBNmHu_0L0">terza</a>.</p>
</div>
