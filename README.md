# Music tribes

## Opis aplikacije

Music tribes je aplikacija/društvena mreža koja omogućuje kolaborativno
dijeljenje playlista. Aplikacija omogućuje registraciju korisnika i kreiranje
plemena (Tribe). Unutar Tribea moguće je kreirati playliste koje će sadržavati
pjesme. 

Unutar svake playliste moguće je dodavati pjesme, komentirati ih i lajkati.
Pjesme se dodaju kao linkovi na youtube. Pjesme je moguće sortirati po broju
likeova i po datumu dodavanja (uzlazno ili silazno).

Aplikacija ima dvije vrste korisnika: Admine i korisnike. Admini imaju pristup
svim sadržajima u aplikaciji i imaju read/write pristup u sve sadržaje.
Korisnici se registriraju u aplikaciju kroz sučelje za registraciju i imaju
mogućnost kreirati Tribe ili se priključiti postojećem Tribeu. Korisnik koji
kreira Tribe ima status *Poglavica* ili *Chieftain* i ima mogućnost uređivanja svih
sadržaja unutar tribea (efektivno je admin/moderator Tribea). Također, jedino
*Chieftain* ima mogućnost kreiranja playliste. Ostali korisnici
koji se priključe u Tribe mogu: dodavati pjesme, komentirati na pjesme i
lajkati. 

Na početnoj stranici aplikacije vidi se popis Tribeova. Svaki registrirani
korisnik može se priključiti bilo kojem Tribeu. Chieftain ima mogućnost
izbaciti bilo kojeg člana Tribea.

Unutar svakog Tribea vidi se popis playlista i popis članova tog Tribea.
Osim toga, na prikazu Tribea nalazi se i chatbox u kojem je moguće raspravljati o
generalnim stvarima u vezi Tribea, kao npr. zamoliti Chieftaina otvaranje nove
playliste ili izbacivanje destruktivnog člana.

Svaki korisnik može urediti svoj profil kroz sučelje za to i dodati osobne
podatke, kao i postaviti profilnu sliku. Korisnikova profilna slika se onda
prikazuje pored njegovih komentara.

## Ograničenja

- Anonimni korisnici (ne-ulogirani) imaju read-only pristup Tribeovima i
  playlistama. Ne mogu lajkati, komentirati niti pisati u chatbox Tribea, ali
  vide sve sadržaje.
- Registrirani korisnici imaju privilegije koje su opisane gore unutar Tribeova
  kojima pripadaju, ali ih se van njihovog Tribea tretira kao anonimne
  korisnike (read-only pristup).
- Admini mogu uređivati sve i vide sve. Registracija Admina se vrši unutar
  Django Admin sučelja, te je unutar admin sučelja moguće i brisanje korisnika
  i Tribeova.  Sve ostale moderacijske aktivnosti (brisanje komentara, brisanje pjesama,
  brisanje poruka iz Tribe chatboxa) potrebno je omogućiti direktno u sučelju
  aplikacije. 
- Chieftan ima mogućnost brisanja svega u svom Tribeu, ali ne može obrisati
  korisnika, može ga samo izbaciti iz Tribea. U ostalim Tribeovima u kojima je
  samo član, nema moderacijske sposobnosti.


## Persone

[Malo više o user personas](https://www.interaction-design.org/literature/article/personas-why-and-how-you-should-use-them)

Persone podrazumijevaju tipove korisnika iz perspektive dizajna sučelja. Ovisno
koji je cilj određene persone i na kojem dijelu aplikacije se nalaze, mijenjaju
se njihove ovlasti i motivi.

- Admin: Korisnički računi sa admin privilegijama. Imaju pravo pristupa u
  Django Admin dashboard i mogu mijenjati stvari na razini baze. Specijalni
  slučaj Admin persone je SuperAdmin, koji predstavlja korisnički račun kreiran
  pomoću python manage.py createsuperuser naredbe, kako bi se moglo
  pristupiti Django Admin dashboardu. SuperAdmin može sve što i Admin i sve
  funkcionalnosti koje može izvršiti Admin, može i SuperAdmin.
- Chieftain: Korisnički račun koji je kreirao određeni Tribe. Njegove ovlasti
  nadilaze ovlasti običnih korisnika samo u Tribeu koji je kreirao.
- Member: Korisnički račun koji je član određenog Tribea. Ima ovlasti unutar tog
  tribea definirane u opisu. Svaki Chieftain je ujedno i Member svog Tribea.
- User: Korisnički račun koji nije član određenog Tribea, ali je ulogiran u
  aplikaciji.
- Anon: Visitor aplikacije koji nije ulogiran.
- Anyone: Persona koja uključuje sve ostale persone. Funkcionalnost koja je
  dozvoljena Anyone personi, dozvoljena je svim ostalim personama.

NAPOMENA: Svi korisnički računi koriste User model. Admini imaju postavljene
privilegije unutar Django Admin sučelja. Privilegije ostalih rola ovise o tome
koji dio aplikacije pregledavaju. Navedene persone nisu odvojeni modeli niti
odvojeni zapisi u bazi, već se isključivo promatraju kao semantički objekti iz
perspektive posjetitelja aplikacija. Jedan korisnički račun može imati više
Persona ovisno o tome na kojem dijelu aplikacije se korisnik nalazi. 

Primjer: Kada govorimo o roli Chieftain ona podrazumjeva korisnički račun koji
pregledava svoj Tribe koji je kreirao. Kada Chieftain jednog Tribea
pregledava neki drugi Tribe koji nije on kreirao, tada njegova rola nije
Chieftan nego Member (ako je član Tribea) ili User (ako nije član Tribea).
Isto tako, svaki Chieftain svog Tribea je ujedno i Member svog Tribea.

## Stranice

Osnovne stranice koje se koriste kroz projekt. Određene stranice će biti
potrebne za implementaciju određenih funkcionalnosti, ali nisu ovdje
eksplicitno navedene jer se podrazumijevaju. Primjer: iako stranica za upisivanje
emaila i passworda za registraciju novog korisnika nije navedena, podrazumjeva
se njeno postojanje kako bi se moglo omogućiti registriranje novog korisnika.
Isto vrijedi i za login stranicu i ostale slične stranice. 

Naravno, ukoliko je kroz dizajn predviđena implementacija određene funkcionalnosti
bez zasebne stranice, nije ju potrebno implementirati. Primjer: ukoliko je u dizajnu
zamišljeno logiranje/prijavljivanje korisnika direktno sa HOME stranice, nije
potrebno implementirati dodatnu LOGIN stranicu.

- HOMEPAGE stranica - početna stranica projekta. Sadrži popis Tribeova, sučelje
  za otvaranje novog Tribea i slično.
- TRIBE stranica - Stranica određenog Tribea. Sadrži popis playlista, popis
  Tribe membera i chatbox.
- PLAYLIST stranica - Stranica određenog Playlista. Sadrži popis pjesama i
  kontrole za like, komentiranje i sortiranje.
- EDIT_USER stranica - Stranica u kojoj pojedini korisnik uređuje svoje
  korisničke podatke.
- ADMIN_DASH stranica - Stranica Django Admin dashboarda. Sadrži sve što je
  potrebno kako bi Admin mogao kreirati/brisati/uređivati korisničke račune te
  brisati/uređivati Tribeove.

Svaka stranica koja je navedena smije sadržavati i više funkcionalnosti od
navedenih, ako je dizajn aplikacije zamišljen tako da se određene
funkcionalnosti obavljaju sa te stranice. Naravno, ukoliko ostatak
specifikacije ne određuje drugačije.

# User stories

[Više o Epic user stories](https://www.agilealliance.org/glossary/epic)

Svaki Epic user story podjeljen je u više user storyja, kojima su definirane
funkcionalnosti aplikacije iz perspektive pojedine persone. Svaki User story
ima definiran acceptance criteria koji potvrđuje ispunjavanje tog User storija.
Epic user story je ispunjen kada su ispunjeni svi acceptance kriteriji svih
storija unutra tog Epica.

NAPOMENA: Neki user storiji imaju i polje Need. U tom polju su eksplicitno navedeni
zahtjevi za funkcionalnost koji se ne mogu zaključiti iz teksta storyja. Tamo
gdje nema polja Need, potrebni resursi za ispunjenje storyja mogu se
zdravo-razumski zaključiti. Primjer: ako story kaže da User mora moći otvoriti
stranicu TRIBE, podrazumjeva se kako u bazi postoji barem jedan Tribe čiju
stranicu User može posjetiti. Time nije potrebno eksplicitno naglašavati
potrebu za postojanje Tribea kao preduvjet ispunjenja storyja.

## Epic 1: Admini mogu uređivati aplikaciju direktno iz ADMIN_DASH sučelja

- S1-1 
  Kao SuperAdmin, kada pristupim ADMIN_DASH stranici, trebam moći
  uređivati korisnike i postaviti im Admin privilegije

  Acceptance criteria: 
  - SuperAdmin se može ulogirati u ADMIN_DASH sa danim korisničkim podacima
  - SuperAdmin može kreirati novog Admina i postaviti mu Admin ovlasti
  - SuperAdmin može obrisati svakog korisnika
  - SuperAdmin može uređivati podatke svakog korisnika, uključujući i druge
    Admine
  - SuperAdmin može dodati ili ukloniti korisniku Admin privilegije bez
    brisanja korisnika.

- S1-2
  Kao Admin, kada pristupim ADMIN_DASH stranici, trebam moći
  uređivati korisnike i postaviti im Admin privilegije

  Acceptance criteria: 
  - Admin se može ulogirati u ADMIN_DASH sa danim korisničkim podacima
  - Admin može kreirati novog Admina i postaviti mu Admin ovlasti
  - Admin ne može obrisati ili uređivati SuperAdmina
  - Admin može obrisati svakog drugog korisnika
  - Admin može uređivati podatke svakog drugog korisnika, uključujući i druge
    Admine
  - Admin može dodati ili ukloniti korisniku Admin privilegije bez
    brisanja korisnika.

- S1-3
  Kao Admin, kada pristupim ADMIN_DASH stranici, trebam moći uređivati podatke
  o svim Tribeovima

  Acceptance criteria:
  - Admin vidi sve Tribeove
  - Admin može uređivati sva polja unutar pojedinog Tribea
  - Admin može obrisati Tribe
  - Admin može kreirati novi Tribe i povezati ga na bilo kojeg korisnika
    uključujući i sebe
  - Admin može promijeniti vlasništvo Tribea (promijeniti korisnika koji je
    Chieftain pojedinog Tribea)

## Epic 2: Anon se može registrirati i prijaviti i urediti svoje podatke

- S2-1
  Kao Anon, kada pristupim HOMEPAGE stranici, mogu registrirati novi korisnički
  račun, nakon čega me sustav redirecta nazad na HOMEPAGE

  Need: username, email, password

  Acceptance criteria:
  - Anon vidi link na funkcionalnost registracije 
  - Anon može kreirati novi korisnički račun 
  - Anon je redirectan nazad na HOMEPAGE nakon kreiranja računa

- S2-2 
  Kao Anon, kada pristupim HOMEPAGE stranici, mogu se prijaviti u aplikaciju,
  nakon čega me sustav redirect nazad na HOMEPAGE

  Need: ispravan username ili email, password

  Acceptance criteria:
  - Anon vidi link na funkcionalnost za prijavu
  - Anon se može prijaviti u aplikaciju
  - Anon je redirectan nazad na HOMEPAGE nakon prijave

- S2-3
  Kao User, iz bilo kojeg dijela aplikacije, mogu pristupiti EDIT_USER stranici
  i urediti svoje korisničke podatke

  Acceptance criteria:
  - Link na EDIT_USER stranicu vidljiv je u bilo kojem dijelu aplikacije
    (navbar)
  - Klik na link otvara EDIT_USER stranicu
  - User može promijeniti svoje podatke upisane pri registraciji
  - User ne može pristupiti podacima drugog Usera
  - User ne može promijeniti podatke drugog Usera

- S2-4
  Kao User, kada pristupim EDIT_USER stranici, mogu postaviti svoj logo
  (avatar)

  Need: URL do slike logoa

  Acceptance criteria:
  - User može upisati URL za svoju profilnu sliku tj. logo
  - Nakon spremanja, profilna je vidljiva na EDIT_PAGE stranici

## Epic 3: User vidi Tribeove i može kreirati novi Tribe

- S3.1
  Kao User, kada pristupim HOMEPAGE stranici, mogu kreirati novi Tribe

  Need: Tribe name, Tribe logo, genre

  Acceptance criteria:
  - User može kreirati novi Tribe, zadati mu ime i logo

  Logo može biti i direktan URL na sliku dostupnu online. Bonus bodovi za
  implementaciju uploada logoa Tribea.

- S3-2
  Kao User, kada pristupim HOMEPAGE stranici, mogu vidjeti postojeće Tribeove

  Acceptance criteria: 
  - User vidi sve postojeće Tribeove
  - Prikazan je i logo i ime Tribea

- S3-3 
  Kao User, kada pristupim HOMEPAGE stranici, na popisu Tribeova vidim Tribeove
  razdvojene po tome jesam li Chieftain Tribea, jesam li Member, te ukoliko ne
  pripadam tom Tribeu

  Need: Kreiran minimalno po jedan Tribe čiji je User Chieftain, čiji je Member,
  te kojem ne pripada

  Acceptance criteria:
  - Tribeovi koje User vidi su odvojeni u tri segmenta: prvo oni čiji je
    Chieftain, pa Member, pa kojima ne pripada

- S3-4
  Kao User, kada pristupim HOMEPAGE stranici, mogu se priključiti Tribeu čiji
  nisam Member

  Acceptance criteria:
  - User može kliknuti na button za priključenje Tribeu
  - User ne vidi button za priključenje Tribeu ako je već Member tog Tribea
  - Nakon priključenja Tribeu, User vidi Tribe u popisu Tribeovima čiji je
    Member

- S3-5
  Kao User, kada pristupim HOMEPAGE stranici, mogu pristupiti TRIBE stranici za
  bilo koji Tribe

  Acceptance criteria: 
  - Klik na link za Tribe vodi usera na TRIBE stranicu za taj Tribe 



## Epic 4: Chieftain može uređivati svoj Tribe, ali ne može druge

- S4-1
  Kao Chieftain, kada pristupim TRIBE stranici svog Tribea, mogu kreirati i
  brisati playliste

  Need: playlist name, playlist description

  Acceptance criteria:
  - Chieftain unutar svog Tribea ima sučelje za kreiranje nove playliste
  - Nakon kreiranja playliste, playlista je vidljiva na TRIBE stranici
  - Chieftain može obrisati playlistu unutar svog Tribea klikom na tipku za
    brisanje
  - 80% posjetitelja stranice mora bez prethodne obuke moći prepoznati koja
    tipka služi za brisanje koje playliste (tipka mora biti intuitivno
    smještena) 
  
- S4-2
  Kao Chieftain, kada pristupim TRIBE stranici, mogu uređivati
  naziv i opis svake playliste

  Acceptance criteria:
  - Postoji sučelje za izmjenu naziva i opisa playliste
  - Nakon izmjene, playlista je prikazana s izmjenjenim parametrima na TRIBE
    stranici

- S4-3

  Kao Chieftain, kada pristupim TRIBE stranici, vidim popis Membera
  mog Tribea (uključujući i mene)

  Acceptance criteria:
  - Vidljiv je popis svih Membera određenog Tribea

- S4-4 
  Kao Chieftain, kada pristupim TRIBE stranici, mogu izbaciti
  Membera iz Tribea

  Acceptance criteria:
  - Chieftain unutar svog Tribea ima tipku za izbacivanje Membera iz Tribea
  - Chieftain ne može sebe izbaciti iz Tribea



## Epic 5: Member na TRIBE stranici

- S5-1 
  Kao member, kada pristupim TRIBE stranici, vidim sadržaje unutar TRIBE
  stranice

  Acceptance criteria:
  - Member vidi popis playlista
  - Member vidi popis članova
  - Member vidi sebe u popisu članova


- S5-2 
  Kao member, kada pristupim TRIBE stranici, vidim da sam Member tog Tribea

  Acceptance criteria:
  - Member vidi tekst Joined i ikonicu kvačice na TRIBE stranici

- S5-3
  Kao Member, kada pristupim TRIBE stranici, mogu napustiti Tribe

  Acceptance criteria:
  - Member vidi tipku za napuštanje Tribea
  - Klikom na tipku Membera se briše iz Tribea
  - Member je sada User u tom Tribeu
  - User više nije na popisu članova Tribea

- S5-4
  Kao User, kada pristupim TRIBE stranici Tribea čiji nisam član ili koji sam
  napustio, mogu se ponovno učlaniti u taj Tribe

  Acceptance criteria: 
  - User vidi tipku za učlanjivanje u Tribe i klikće na nju
  - User je sada Member
  - Nakon klika, Memberu se prikazuje TRIBE stranica i njegov username se
    nalazi u popisu članova



## Epic 6: Tribe Chatbox

- S6-1 
  Kao Member, kada pristupim TRIBE stranici, vidim popis poruka u Chatboxu
  Tribea koje su pisali Memberi Tribea

  Acceptance criteria:
  - Member vidi Chatbox na TRIBE stranici
  - Svaka poruka sadrži mali logo Membera koji ju je ostavio, username, tekst
    poruke i timestamp kada je kreirana

- S6-2
  Kao Member, kada pristupim TRIBE stranici, mogu ostaviti poruku u Chatboxu

  Acceptance criteria:
  - Member upisuje poruku u sučelje chatboxa
  - TRIBE stranica se refresha
  - Chatbox sadrži napisanu poruku

- S6-3
  Kao Anyone, kada pristupim TRIBE stranici, poruke napisane u Chatboxu na toj
  TRIBE stranici vidim samo unutar te TRIBE stranice

  Acceptance criteria:
  - Anyone napiše poruku u Chatbox jednog Tribea
  - Ta poruka se ne vidi u niti jednom drugom Chatboxu na niti jednoj drugoj
    TRIBE stranici

- S6-4
  Kao Chieftain, kada pristupim TRIBE stranici, mogu brisati poruke
  svih Membera iz Chatboxa mog Tribea

  Acceptance criteria:
  - Chieftain za svaku poruku u chatboxu vidi tipku za brisanje poruke
  - Klik na tipku briše poruku iz baze
  - Poruka se više ne vidi u Chatboxu


- S6-5
  Kao Member, User ili Anon, kada pristupim TRIBE stranici, ne vidim opcije za brisanje poruka
  u Chatboxu i ne mogu ih moderirati

  Acceptance criteria:
  - Kontrole za brisanje poruka iz Chatboxa nisu vidljive
  - Direktan request na delete URL za poruku neće obrisati poruku iz baze

- S6-6
  Kao Member ili User, kada pristupim TRIBE stranici, ne mogu brisati poruke u
  Chatboxu čak niti ako sam Chieftain nekog drugog Tribea

  Need: Persona je Member ili User na otvorenoj TRIBE stranici, ali nije
  Chieftain promatranog Tribea. Persona je Cheiftain nekog drugog Tribea.

  Acceptance criteria:
  - Persona otvori TRIBE stranicu gdje nije Chieftain
  - Kontrole za brisanje poruka iz Chatboxa nisu vidljive
  - Direktan request na delete URL za poruku neće obrisati poruku iz baze

- S6-7
  Kao Chieftain, kada pristupim TRIBE stranici, 
  za sve moje poruke u Chatboxu vidljivo je da ih je napisao Chieftain Tribea. 

  Acceptance criteria:
  - Poruke koje je u Chatbox Tribea napisao Chieftain Tribea vizualno su
    istaknute i drugačijeg su izgleda od poruka koje su napisali Memberi Tribea
  - Poruke ili imaju dodatnu ikonicu, napisane su drugom bojom, ili oboje
  - Odabir vizualnog isticanja ostavljen je dizajneru u skladu s ostalim
    dizajnerskim odlukama
  - Poruke ostalih Membera nisu vizualno istaknute




## Epic 7: PLAYLIST stranica

- S7-1
  Kao Member, kada pristupim TRIBE stranici, vidim sve playliste unutar Tribea
  i mogu im pristupiti

  Acceptance criteria:
  - Moguće je kliknuti na link za svaku playlistu
  - Klik vodi Membera na PLAYLIST stranicu

- S7-2
  Kao Member, kada pristupim PLAYLIST stranici, vidim podatke o playlisti

  Acceptance criteria:
  - Vidi se naziv i opis playliste, tko ju je kreirao i kada
  - Vidi se popis pjesama u playlisti
  - Ukoliko nema pjesama, piše poruka kako je playlista prazna

- S7-3
  Kao Member, kada pristupim PLAYLIST stranici, mogu dodati novu pjesmu u
  playlistu

  Need: Track artist, Track title, youtube url, duration
  
  Acceptance criteria:
  - Vidljiva je tipka za dodavanje nove pjesme
  - Klik na tipku otvara sučelje za dodavanje
  - Nakon dodavanja pjesma se sprema u bazu i vidljiva je u popisu pjesama
    unutar playliste

- S7-4
  Kao Anyone, kada pristupim PLAYLIST stranici, vidim podatke o pjesmama u
  playlisti i mogu poslušati bilo koju pjesmu u popisu pjesama

  Acceptance criteria: 
  - Anyone vidi podatke u formatu: "track_artist - track_title (duration)" za
    svaku pjesmu u popisu pjesama
  - url nije vidljiv u popisu pjesama
  - za svaku pjesmu vidljiva je tipka play, klikom na nju otvara se youtube
    link u novom tabu

- S7-5
  Kao Member, kada pristupim PLAYLIST stranici, mogu lajkati i unlikeati bilo koju
  pjesmu iz popisa i vidim za svaku pjesmu broj likeova

  Acceptance criteria:
  - Member vidi LIKE tipku
  - Klikom na tipku zapisuje se like u bazu i ponovno prikazuje PLAYLIST
    stranica
  - Member sada vidi UNLIKE tipku.
  - Klikom na tipku briše se zapis iz baze i ponovno prikazuje PLAYLIST
    stranica
  - Member sada ponovno vidi LIKE tipku
  - Member ni na koji način ne može imati više od jednog likea na određenu
    pjesmu, čak niti preko direktnog poziva na like URL za pjesmu
  - Tekst LIKE/UNLIKE tipki sadrži i broj lajkova na tu pjesmu

- S7-6 
  Kao Member, kada pristupim PLAYLIST stranici, mogu vidjeti koliko pojedina
  pjesma ima komentara te mogu čitati te komentare

  Acceptance criteria:
  - Member vidi indikator koji govori da postoje komentari na pjesmu
  - Indikator pokazuje tekst "Komentiraj" ukoliko nema komentara, ili tekst
    "Komentari (BROJ_KOMENTARA)" ukoliko ima komentara
  - Klik na indikator prikazuje popis komentara za tu pjesmu
  - Svaki komentar sadrži logo Membera koji ga je napisao, tekst komentara i
    timestamp
  - Member vidi kontrolu za skrivanje popisa komentara za tu pjesmu. 
  - Klik na kontrolu za skrivanje će sakriti popis komentara za pjesmu
  - Popis komentara se prikazuje/skriva i kada nema komentara, ali sadrži tekst
    "Još nitko nije komentirao. Budi prvi!"

  Engineering notes:
  - Popis komentara se prikazuje i skriva bez refresha PLAYLIST stranice
  - Preporuka je koristiti JS i CSS za prikazivanje/skrivanje div elementa koji
    sadrži komentare. 
  - Moguće je implementirati i modalni prozor (pop-up) koji sadrži popis
    komentara

  

- S7-7
  Kao Member, kada pristupim PLAYLIST stranici, mogu komentirati svaku pjesmu u 
  popisu pjesama

  Need: tekst komentara

  Acceptance criteria:
  - Klik na indikator za popis komentara iz S7-6 prikazuje popis komentara 
  - Popis komentara sadrži i formu za unos novog komentara i tipku "Ostavi
    komentar"
  - Klikom na tipku sprema se komentar u bazu i refresha se PLAYLIST stranica
  - Komentar je vidljiv nakon prikaza popisa komentara za tu pjesmu
  - Tekst indikatora komentara prikazuje broj komentara uvećan za objavljeni
    komentar


- S7-8 
  Kao User ili Anon, kada pristupim PLAYLIST stranici, mogu vidjeti komentare
  na pjesme ali ne mogu komentirati

  Acceptance criteria:
  - User i Anon vide popis komentara kao i Member u S7-6, ali ne vide formu za
    komentiranje iz S7-7
  - User i Anon ne mogu ostaviti komentar čak ni pozivom direktnog URL-a za
    komentiranje

- S7-9 
  Kao User ili Anon, kada pristupim PLAYLIST stranici, mogu vidjeti broj
  lajkova za pjesmu, ali ne mogu lajkati

  Acceptance criteria:
  - Persone vide broj likeova za svaku pjesmu
  - Ne vide LIKE tipku
  - Ne mogu staviti like niti pozivom direktnog URL-a za lajkanje



## Epic 8: Moderiranje PLAYLIST stranice

- S8-1
  Kao Admin ili Chieftain, kada pristupim PLAYLIST stranici, mogu obrisati
  svaku pjesmu u popisu

  Acceptance criteria:
  - Persona vidi tipku za brisanje pjesme pored svake pjesme u popisu
  - Klik na tipku briše pjesmu u bazi
  - Pjesma se više ne pojavljuje u popisu pjesama
  
- S8-2
  Kao Member, kada pristupim PLAYLIST stranici, mogu obrisati iz playliste
  pjesmu koju sam ja dodao, ali ne mogu obrisati pjesme koje su dodali drugi 
  Memberi

  Acceptance criteria:
  - Pored pjesme koju je dodao, Member vidi tipku obriši
  - Ne vidi tipku pored pjesama koje nije on dodao
  - Klik na tipku briše pjesmu iz baze i ne pojavljuje se u playlisti
  - Ne može obrisati pjesme koje nije on dodao, čak niti preko direktnog URL-a
    za brisanje
  
- S8-3
  Kao Admin ili Chieftain, kada pristupim PLAYLIST stranici, mogu obrisati
  svaki komentar

  Acceptance criteria:
  - Persona vidi tipku za brisanje komentara pored svakog komentara
  - Klik na tipku briše komentar iz baze i uklanja ga iz popisa komentara

- S8-4
  Kao Chieftain, kada pristupim PLAYLIST stranici, mogu brisati pjesme i
  komentare samo iz playliste koja je u mom Tribeu

  Acceptance criteria:
  - Korisnik otvara playlistu koja nije u njegovom Tribeu
  - ne vidi kontrole za brisanje pjesama i komentara
  - ne može obrisati ni pjesmu ni komentar
