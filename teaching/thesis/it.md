---
layout: page
translation: /teaching/thesis/
translation_label: English
lang: it
title: Lavorare alla tesi
permalink: /teaching/thesis/it/
---

Per chi sta già facendo la tesi con il Prof. Francesco Longo allo STRATUS Lab: la burocrazia, il lavoro quotidiano, i modelli e la consegna. This page is also available <a href="{{ '/teaching/thesis/' | relative_url }}">in English</a>.

<details class="faq-item" id="richiesta">
  <summary><h2>Come si ufficializza la richiesta di tesi?</h2></summary>
  <p>Con il modulo del Dipartimento, diverso per la triennale e per la magistrale. Va compilato, controfirmato dal relatore e consegnato al referente per le istanze, il cui nome e i cui contatti sono scritti nel modulo stesso.</p>
  <ul>
    <li><a href="https://ingegneria.unime.it/sites/dip05/files/2025-07/richiesta%20tesi%20lauree%20triennali%20attive%20agg.%20link.pdf">Richiesta di tesi, laurea triennale</a></li>
    <li><a href="https://ingegneria.unime.it/sites/dip05/files/2025-07/richiesta%20tesi%20lauree%20magistrali%20attive%20agg.%20link.pdf">Richiesta di tesi, laurea magistrale</a></li>
  </ul>
  <p class="faq-warning">La domanda va presentata almeno <b>90 giorni</b> prima dell'inizio della prima sessione di laurea utile per la triennale, almeno <b>6 mesi</b> per la magistrale. Fa fede la data di registrazione al protocollo, non quella in cui si consegna il foglio.</p>
  <p>Il modulo è indirizzato al Direttore del Dipartimento e al Coordinatore del Corso di Laurea, ma le uniche firme da procurarsi sono quella dello studente e quella del relatore, più quella del correlatore dove c'è: il visto del Direttore arriva dopo.</p>
  <p>Il titolo e l'argomento indicati nel modulo sono provvisori. L'argomento non è strettamente vincolante e il titolo definitivo si comunica al momento della domanda di laurea. Il correlatore è previsto solo per la magistrale, e richiede un'attestazione del relatore sulla sua qualificazione scientifica o professionale.</p>
  <p>Tutti i moduli si trovano nella <a href="https://ingegneria.unime.it/it/didattica/modulistica-didattica">modulistica didattica del Dipartimento</a>.</p>
</details>

<details class="faq-item" id="tirocinio">
  <summary><h2>Come si attiva il tirocinio?</h2></summary>
  <p>Il tirocinio vale <b>225 ore, 9 CFU</b> per la triennale e <b>175 ore, 7 CFU</b> per la magistrale.</p>
  <p>Si può svolgere allo STRATUS Lab, e in quel caso si usa il modulo per il tirocinio presso strutture dell'Ateneo. In alternativa si può concordare un tirocinio in azienda: il laboratorio collabora stabilmente con imprese grandi, medie e piccole del territorio nei settori dei sistemi embedded, della cybersecurity e dell'intelligenza artificiale, e i partner più stabili sono elencati <a href="{{ '/#partners' | relative_url }}">in home page</a>.</p>
  <ul>
    <li><a href="https://ingegneria.unime.it/sites/dip05/files/2025-01/istanza%20tirocinio%20-%20ulteriori%20attivit%C3%A0%20presso%20Unime%20-%20ultima%20versione.pdf">Istanza di tirocinio presso strutture dell'Ateneo</a>, per il tirocinio in laboratorio</li>
    <li><a href="https://ingegneria.unime.it/sites/dip05/files/2026-07/istanza%20tirocinio%20presso%20imprese%20ecc%20agg.%2021.07.2026.pdf">Istanza di tirocinio presso imprese ed enti</a>, per il tirocinio in azienda</li>
  </ul>
  <p>Entrambi i moduli vanno indirizzati al Coordinatore del Corso di Laurea, indicano come docente tutor il Prof. Longo, le ore e i crediti, e richiedono di aver frequentato un corso sulla sicurezza sul lavoro.</p>
</details>

<details class="faq-item" id="lavoro">
  <summary><h2>Come si lavora durante la tesi?</h2></summary>
  <p>Il Prof. Longo apre una chat su Teams dedicata alla tesi. <b>Tutte le comunicazioni sulla tesi passano da lì.</b> Periodicamente si organizzano incontri, online o in presenza, per verificare l'andamento del lavoro.</p>
  <p>Viene creata anche una cartella su OneDrive. Ci vanno il codice prodotto e tutto il materiale necessario a riprodurre il lavoro, i capitoli della tesi man mano che vengono scritti e la presentazione finale. I link ai file caricati vanno riportati nella chat: è così che il relatore e gli altri membri del laboratorio li trovano, li leggono e suggeriscono come migliorarli.</p>
  <p>Il codice va inoltre in un repository GitHub creato dallo studente, il cui link va riportato nella chat. Il laboratorio ne fa un fork nella propria organizzazione, a garanzia della paternità del codice.</p>
</details>

<details class="faq-item" id="scrittura">
  <summary><h2>Come si scrive la tesi?</h2></summary>
  <p>Ci sono dei modelli pronti, con il frontespizio, la struttura dei capitoli e una guida in corsivo grigio che si cancella mano a mano che si scrive. Quello che resta è una tesi impaginata come il Dipartimento la vuole.</p>
  <p><b>Tesi triennale, in italiano</b></p>
  <ul>
    <li><a href="{{ '/teaching/thesis/tesi-triennale-modello.docx' | relative_url }}">Modello completo, Word</a></li>
    <li><a href="{{ '/teaching/thesis/tesi-triennale-modello-latex.zip' | relative_url }}">Modello completo, LaTeX</a></li>
    <li><a href="{{ '/teaching/thesis/tesi-triennale-frontespizio.docx' | relative_url }}">Solo il frontespizio, Word</a></li>
  </ul>
  <p><b>Tesi magistrale, in inglese</b></p>
  <ul>
    <li><a href="{{ '/teaching/thesis/masters-thesis-template.docx' | relative_url }}">Modello completo, Word</a></li>
    <li><a href="{{ '/teaching/thesis/masters-thesis-template-latex.zip' | relative_url }}">Modello completo, LaTeX</a></li>
    <li><a href="{{ '/teaching/thesis/masters-thesis-title-page.docx' | relative_url }}">Solo il frontespizio, Word</a></li>
  </ul>
  <p>I due formati producono lo stesso documento, quindi la scelta è solo questione di abitudine. Per LaTeX si consiglia <a href="https://www.overleaf.com/">Overleaf</a>: l'archivio si carica con New Project &rarr; Upload Project e si compila con pdfLaTeX, senza installare niente.</p>
  <p>Gli strumenti di intelligenza artificiale si possono usare per migliorare la forma, la chiarezza e la correttezza della lingua, non per generare contenuti, risultati o argomentazioni che lo studente non sappia spiegare e difendere.</p>
</details>

<details class="faq-item" id="consegna">
  <summary><h2>Come si consegna la tesi e ci si laurea?</h2></summary>
  <p>La domanda di conseguimento del titolo si presenta su Esse3, dove la procedura si apre <b>40 giorni</b> prima della data di laurea. Vanno caricati quattro documenti:</p>
  <ul>
    <li>il documento d'identità in corso di validità;</li>
    <li>il frontespizio firmato;</li>
    <li>il contenuto definitivo della tesi;</li>
    <li>tutti i file restituiti dal sistema antiplagio.</li>
  </ul>
  <p>Il frontespizio <b>non va stampato</b>: si compila, si manda nella chat della tesi, il relatore lo firma e lo rimanda lì.</p>
  <p>L'antiplagio produce una ricevuta e un report: formalmente serve il report, ma conviene caricare tutto quello che il sistema restituisce, così non si sbaglia.</p>
  <p class="faq-warning">Entro la stessa finestra il relatore deve approvare l'elaborato: quella approvazione è l'atto finale del deposito della tesi, che va completato almeno <b>7 giorni lavorativi</b> prima della prova finale. Questa è anche la distanza minima prevista fra l'ultimo esame di profitto e l'esame di laurea.</p>
</details>

{% include faq-toggle.html %}
