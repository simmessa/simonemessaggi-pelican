---
date: 2008-03-12
title: Email usa e getta sul tuo server di posta
slug: throwaway-emails-for-dummies
lang: it
cover: images/self-hosted-throwaway-email.jpeg
author: simmessa
status: published
category: Tech
tags: Tutorial, Email, Hack
---

Hai un server email privato? Bene! Vuoi avere un'email che puoi dare via per le registrazioni senza preoccuparti della quantità infinita di spam che finirai per ricevere?

Allora continua a leggere, forse questo articolo e' per te...

Uno dei modi semplici in cui molti, se non tutti, dei punti sopra possono essere realizzati è un hack molto semplice della vostra configurazione *nix.

# Divertiamoci con /etc/aliases

Cos'è un file /etc/aliases sui sistemi *nix? è un repository centrale per i nomi utente locali sul server utilizzato quando si tratta di consegna e-mail.

Non ho molto da dire sugli alias che non si poteva trovare su migliori risorse online, quindi non vi so dare grandi spiegazioni qui.

Uso postfix sul mio server, e lo adoro, rende l'impostazione e-mail molto facile mentre sotto il cofano è parecchio potente.

Cosa c'è in un file di alias? Scopriamolo.

Ecco un esempio rapido di /etc/aliases:

```
    # See man 5 aliases for format

    some_alias: some_unix_username
    some_other_alias: some_other_username
```
E' piuttosto semplice, giusto?

Ora, la grande domanda e': cosa possiamo fare attraverso una manipolazione degli alias?

Molto, è un file di testo dopotutto ;)

Ecco cosa troverai alla fine del mio alias attuale:

```
    cut...
    #weekmail_start
    this_alias_changes_every_day: my_linux_username
    #weekmail_end
```

Il concetto qui è piuttosto semplice, stiamo per creare una nuova e-mail diversa ogni giorno, utilizzando alcuni parametri che cambiano ogni giorno, in modo che non sarà disponibile per spamming in tempi successivi. Il punto è quello di inventare una regola con cui siamo in grado di calcolare l'indirizzo e-mail esatto ogni giorno.

Ecco come usiamo alcuni comandi disponibili su bash in linux:

```bash
    #!/bin/bash

    #need day of the week

    dotw=`date +%A`
    number=`date +%d`
    month=`date +%m`

    alias="$dotw$number$month"

    alias=`echo $alias|tr "[:upper:]" "[:lower:]"`

    if [ -z $1 ]; then
    echo "Needs filename as argument."
    exit 1
    elif [ -f "$1" ]; then
    fname="$1"
    fi

    cat $fname|sed '/weekmail_start/,/weekmail_end/d' >$fname.weekmail

    cat /sbin/weekmail|sed 's/replaceme/'$alias'/' >/sbin/weekmail_changed

    cat $fname.weekmail /sbin/weekmail_changed >$fname

    newaliases
```

## Logica degli alias usa e getta

Ok, i passi qui sono abbastanza lineari, ma controlliamoli assieme:

1) riempire alcune varsiabili con cose che cambiano ogni giorno, prese tramite il comando "date" per creare degli alias usa e getta.
2) tagliare la parte "weekmail" dal file /etc/aliases (questo passaggio coinvolge l'editor sed) e salvare il risultato in un file temporaneo.
3) prendere una nuova porzione di weekmail da un altro file statico (/sbin/weekmail in questo esempio) e sostituire una stringa conosciuta con l'alias appena calcolato, quindi memorizzarlo da qualche parte.
4) creare un nuovo /etc/aliases unendo i due file precedentemente creati
5) invocare `newaliases` per assicurarsi che il vostro nuovo alias sia attivato

Ora basta metterlo nel crontab con "crontab -e":

```
    10 0 * * * /path_to/your_weekmail_script /etc/aliases
```

Et Voila'! Questo è un bel indirizzo email spazzatura che hai appena creato, fresco ogni giorno!

Sono abbastanza sicuro che i vantaggi di questo approccio dopo aver impostato delle wildcard pigliatutto (*@yourdomain.com) sono evidenti...

Assicurati di inviarmi il tuo feedback se usi anche tu questo hack... il mio script è stato buttato giu' velocemente (circa 10 minuti) e quindi dovrebbe essere il minimo sindacale...migliorabile.

Spero che vi sia utile, ragazzi. Vi faccio i migliori auguri!

_p.s.: Riporto qui un articolo davvero vecchio (2008) comparso sul mio primo blog, ma che suona stranamente attuale, dato che il problema dello SPAM e' esploso in questi quasi 20 anni_