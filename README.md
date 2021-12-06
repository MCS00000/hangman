HANGMAN

Spēli uzsākot lietotājam tiek dota izvēle starp 2 spēles valodām- latviešu valoda, kuru izvēloties vārdi tiek ņemti no lokālās latviešu vārdu datubāzes vai angļu valoda, kur, izmantojot API, tiek iegūts nejauši izvēlēts vārds angļu valodā. Lai veiktu šo izvēli spēlētājam attiecīgi jāievada 1 vai 2. Gadījumā, ja spēlētājs izvēlas opciju spēlēt ar latviešu vārdiem, spēlētājam tiks dota iespēja izvēlēties vienu no trim grūtības pakāpēm- viegli, vidēji vai grūti. Brīdī, kad programma izvadīs attiecīgo paziņojumu, lietotājam jāievada kā teksts izvēlētais spēles grūtums, piemēram "vidēji". Spēles grūtumu ievadot nepareizi, tas tiks pieprasīts atkārtoti. Nospiežot pogu enter, sāksies pirmais spēles raunds ar izvēlēto grūtības pakāpi. Ja spēlētājs ir izvēlējies spēlēt ar angļu vārdiem, grūtības pakāpe nav jāizvēlas un uzreiz sākas spēles pirmais raunds.

Raundam sākoties tiks norādīts minamā vārda garums un piešķirtas 6 dzīvības jeb 6 iespējas veikt nepareizus minējumus pirms spēle tiek zaudēta.
Spēles mērķis ir uzminēt vārdu ievadot minamos burtus pa vienam vai ievadot visu vārdu.

Ievadot burtus pa vienam lietotājam tiks atgriezts paziņojums par to vai šis burts vārdā ir vai tā nav vai arī burts jau ir minēts iepriekš. Nepareiza burta ievades gadījumā tiks zaudēta viena dzīvība un spēle turpināsies kā iepriekš. Minētais burts tiks pievienots minēto burtu sarakstam, kas ir redzams lietotājam. Pareiza burta ievades gadījumā tas tiks atainots progresā aizstājot domu zīmi ar uzminēto burtu vietā, kur tas atrodas vārdā. Ja šajā vārdā burtsa atkārtojas vairākas reizes, tas tiks atklāts visās tā pozīcijās. Ja burts tiek ievadīts atkārtoti, tiek izvadīts atbilstošs paziņojums un bez citām izmaiņām spēle turpinās.

Ievadot vārdus ir jāievada atbilstoša garuma vārdi, citādi spēle atgriež paziņojumu par to, ka vārds ir ievadīts nepareizi. Spēle turpinās bez citām izmaiņām. Ja tiek ievadīts pareiza garuma vārds, taču tas nav pareizs, tiek zaudēta viena dzīvība un spēle turpinās. Ja vārds tiek atminēts pareizi, spēle beidzas tāpat kā tad, ja vārds tiek atminēts pa vienam burtam.

Gadījumā, ja vārds netiek atminēts un beidzas visas dzīvības, tiek izvadīts paziņojums, ka spēle ir zaudēta un tiek atklāts neuzminētais vārds. Pēc 5 sekunžu atskaites sākas nākamā spēles partija.

Spēles laikā minējuma vietā ievadot "HELP!" tiks izvadīts minamā vārda skaidrojums, ja tāds ir pieejams un lietotājam tiks atņemta viena dzīvība.
Ievadot “STOP!” spēle tiks pārtraukta.
