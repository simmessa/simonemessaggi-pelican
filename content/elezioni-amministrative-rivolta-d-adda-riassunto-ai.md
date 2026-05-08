---
date: 2026-05-7
title: Elezioni amministrative a Rivolta d'Adda, un riassunto generato dall'IA
slug: elezioni-amministrative-rivolta-d-adda-riassunto-ia
lang: it
cover: images/elezioni-amministrative-riassunti-ia.webp
author: simmessa
status: published
category: Rants
tags: AI, Politics
---

Come ogni 5 anni, anzi, questa volta un po' prima, per le ragioni che [sappiamo](https://bergamo.corriere.it/notizie/26_aprile_18/treviglio-accuse-di-violenza-sessuale-su-due-pazienti-il-medico-giovanni-sgroi-a-giudizio-ba6fe8bb-b570-4401-8c28-1449c4375xlk.shtml), e' giunto il momento di andare alle urne per il [comune di Rivolta d'Adda.](https://www.comune.rivoltadadda.cr.it/it)

Anche a questa tornata elettorale le liste che si contendono il municipio sono tre e presentano i loro candidati, alcuni sono "nuovi volti" altri li definirei invece "volti noti". Votare un candidato "a simpatia" oppure andare "sulla fiducia" non e' mai stato il mio criterio preferenziale, e quindi mi apprestavo ad approfondire la situazione politica...

_Guardati i programmi, senti cosa promettono, mi sono detto, e fatti la tua idea._

Avevo fatto lo stesso alle scorse elezioni, per poi scoprire che i due programmi si sovrapponevano in modo inquietante e, a distanza di anni, non ho notato cambiamenti particolarmente significativi, o meglio, non mi sento di dire che i cambiamenti che ho notato fossero troppo legati a quelli del programma pubblicizato in campagna elettorale.

Ma non voglio annoiarvi con la vacuita' delle promesse elettorali, che tanta letteratura e polemica generano ogni anno, quanto piuttosto riflettere sui cambiamenti tecnologici piu' recenti e sui nuovi approcci di risolvere "problemi" che queste tecnologie ci propongono.

## Perche' leggere i programmi elettorali, o meglio, chi ha tempo di farlo?

Naturalmente, nel valutare un candidato e il suo movimento politico, voglio verificare su quali concetti, idee e proposte basa la sua candidatura.

In pratica, le campagne elettorali degli ultimi anni si sviluppano principalmente sui social, con qualche comizio qua e la', se va bene un mini sito a sostegno della campagna. La questione della valutazione del programma si fa piu' ardua nel mio caso perche':

- **Non uso i social** mi sono annoiato di star dietro alle apparenze e alle pose che la stragrande maggioranza degli individui si spara
- **Non vado ai comizi** anche se l'idea di mangiare gratis mi alletta, va a finire che mi dimentico, e so gia' che non mi sentirei a mio agio

Inoltre, non partecipo attivamente alla vita politica, anzi diciamo alla vita "sociale" del mio Comune, quindi mi e' difficile venire in contatto con le persone che sostengono il candidato X o Y, partecipo pochissimo agli eventi che organizzano.

Va a finire che mi guardo il sito, un'occhiata veloce ai post sulle pagine FB ecc e mi faccio la mia idea.

O meglio questo farei se non mi fosse venuto in mente che potrei demandare questo compito a qualcuno che ci mette meno e che con ogni probabilita' fara' un lavoro migliore di me nel raccogliere le informazioni.

## Agente, mi da il suo parere?

Quindi mi sono messo in testa di usare il metodo che va per la maggiore, trattandosi di cose che vanno fatte ma che non muoio dalla voglia di fare: Far studiare Liste, programmi e candidati all'intelligenza artificiale.

Chi mi conosce lo sa, mi occupo di tecnologia e poco altro "sin dalla nascita", e sto facendo molti esperimenti in ambito di intelligenza artificiale, in particolar modo utilizzando agenti per lo [sviluppo software.](/2026/03/en/fastview-fast-image-viewer-rust-agentic-coding/).

Ma, se ho capito qualcosa dell'IA agentica, e' che e' ben contenta di risolvere problemi di ogni genere, non solamente quelli legati al coding, e cosi' ho tentato l'ennesimo esperimento: _Far fare a lei lo sporco lavoro di analizzare tutto il materiale elettorale._

## Lo stack tecnologico

Non amo l'approcio IA as a service, quindi niente Claude Antrophic, niente Gemini, ChatGPT e soprattutto niente Grok (che pero' e' un bel nome per un orco, bravo Elon).

_Quindi cosa ho usato?_

un LLM (Large Language Model) open weight eseguito in locale su mio hardware, nello specifico parliamo di Qwen3.6 35B A3B, che e' un modello sviluppato da Alibaba Cloud (sempre interessante il collegamento poetico con i 40 ladroni) nella versione quantizzata Q5_K_M, scaricato da Huggingface [qui.](https://huggingface.co/bartowski/Qwen_Qwen3.6-35B-A3B-GGUF), se lo volete provare tenete presente che vi serviranno 30GB di VRAM, o un sistema dotato di memoria unificata.

L'inference engine usato e' [llama.cpp](https://github.com/ggml-org/llama.cpp) che per chi non lo sapesse e' il motore sottostante ad Ollama, tra gli altri.

Ma LLM e server non bastano, per avere modo di consultare Web e costruire una comparazione sensata serve un'harness, e per questa parte mi sono affidato a [Pi-agent.](https://pi.dev)

Ultimo ingrediente, per abilitare le ricerche su internet ho definito un tool basato su SearXNG che potesse ottenere informazioni sul web.

## Metodologia e risultato: il riassunto

Il metodo e' stato piuttosto spartano, ho creato un file links.txt con una serie di link ai siti o pagine facebook elettorali, per dare uno spunto iniziale all'agent, dopodiche' ho aggiunto alcuni elementi, principalmente per sopperire a dei limiti tecnici dell'agent.

Per esempio, lo scraping / parsing di pagine FB viene severamente limitato da Meta, una delle principali aziende al mondo che fa scraping del Web per il training dei propri modelli AI, quale ironica ipocrisia...

In questi casi ho scaricato materiale della campagna (immagini e pdf) da FB e le ho date in pasto all'agente, usando la mia utenza del social (sigh.), mi sono limitato a FB perche' ho notato che i post su IG erano praticamente gli stessi, non ho considerato contenuti video per non allungare a dismisura i tempi di calcolo sul mio hardware (i video consumano molti piu' token e dicono sostanzialmente poco di piu').

![Pi agent mentre fa la sua magia](/images/pi-agent-doing-its-thing.jpg)

Il tutto si e' svolto su piu' iterazioni, perche' osservando il summary agentico ho notato che c'erano delle mancanze, ad esempio le difficolta' nel predere il contenuto da Facebook, e mi sono mosso in modo da cercare di colmarle, prompt dopo prompt.

## Considerazioni varie

Non entro nel merito di quanto analizzato da AI, ma posso dire che il livello che hanno raggiunto i local LLM e' davvero notevole e, a patto di avere l'hardware necessario a disposizione, ha un potenziale tremendo!

Altra cosa molto interessante, la possibilita' di "rifare" il lavoro utilizzando un altro agente, e partendo dagli stessi presupposti.

A questo scopo ho pubblicato i file di partenza su un [repository github](https://github.com/simmessa/elezioni-amministrative-2026-Rivolta-d-Adda), quindi, se volete approfondire, e avete le necessarie competenze tecniche, vi invito a farlo! Sbizzarritevi, usate ChatGPT, Granite, Gemma o, perche' no, Bonsai quantizzato ad 1 bit!

Questo rende il lavoro riproducibile, e anche migliorabile, se volete.

## Finalmente: Il riassunto, cos'e', cosa non e'

Il riassunto e' un file in formato Markdown che trovate pubblicato anche qui:

[Buona lettura.](/2026/05/riassunto-amministrative-2026)

Ovviamente si tratta di un riassunto automatico, l'AI non prende le parti politiche di nessuno, quindi dovrebbe essere libero da bias vari, anche se non si puo' garantire che tecnicamente il modello sia imparziale, perche' il training viene svolto partendo da materiale generato da esseri umani, e che quindi raramente possiamo definire "oggettivo".

_Ma quindi che cosa diavolo ha prodotto l'IA, qual'e' il risultato del suo lavoro?_

Sicuramente e' uno spunto, che io ho trovato utile per analizzare le proposte elettorali. Serve infatti ad avere un'idea di chi si e' preparato di piu', su quali temi, e quali sono le principali "intenzioni" di lavoro dei candidati, aggiungo anche che da' anche una discreta idea di chi sia il "target" di ciascuna lista.

Piu' facile, io credo, dire cosa **non e'** questo riassunto:

- Non e' un'indicazione di voto
- Non e' l'endorsement di una lista o candidato
- Non e' un documento scientifico e nonostante gli sforzi, non e' detto che sia oggettivo

Ve lo lascio, per dare un senso alle ore di lavoro che ci sono andate dentro (non molte, per la verita'), e perche' come ho sentito dire da Harlan Ellison:

_Tutti abbiamo diritto ad avere un'opinione, ma tutti abbiamo il dovere di averla informata._

S.