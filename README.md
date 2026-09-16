# Odoo 19 TODO -sovellus
Tehtävien- ja ajanhallintasovellus Odoo 19 -järjestelmälle.

## Esivaatimukset

* **Käyttöjärjestelmä:** Windows 11
* **Odoo Versio:** Odoo 19.0 (Englanninkielinen käyttöliittymä tässä)
* **[Latausosoite](https://www.odoo.com/page/download)**

## Asennusohje

### 1. Kloonaa repositorio
Avaa PowerShell / Komentorivi järjestelmänvalvojana ja aja seuraavat komennot

```powershell
cd "C:\Program Files\Odoo 19.0.20260914\server\odoo\addons"
git clone https://github.com/sami-turunen/odoo-todo.git todo_app
```
(Vaihtoehtoisesti voit ladata koodin ZIP-tiedostona osoitteesta [github.com/sami-turunen/odoo-todo](https://github.com/sami-turunen/odoo-todo) ja purkaa sen kansioon C:\Program Files\Odoo 19.0.20260914\server\odoo\addons\todo_app).

### 2. Aktivoi kehittäjätila (Developer Mode)
- Avaa selaimessa osoite http://localhost:8069/odoo/apps.

- Klikkaa vasemman yläkulman valikkonappia ja valitse Settings.

- Skrollaa sivua alas kohtaan Developer Tools.

- Klikkaa linkkiä Activate the developer mode.



### 3. Asenna moduuli
- Klikkaa valikkonappia ja valitse Apps.
- Päivitä sovelluslista Update Apps List -toiminnolla sivun yläosasta
- Valitse vasemman reunan kategoriaksi Productivity
- Etsi moduuli TODO sovellus
(Jos moduulia ei näy, voit myös kokeilla uudelleenkäynnistää itse odoon PowerShellillä: `Restart-Service odoo-server-19.0`)
- Klikkaa Activate.

### 4. Käyttö
Kun asennus on valmis, avaa sovellus klikkaamalla valikkonappia ja valitsemalla TODO Sovellus.


### Haasteet kehitysvaiheessa:
Odoo järjestelmä oli itselle entuudestaan jo hieman tuttu, joten kaikki ei ollut aivan uutta asiaa, mutta tässä pari ongelmaa jotka tulivat vastaan:

- Odoo 19:ssä käyttöliittymän listanäkymässä käytetään uutta `<list>`-tägiä vanhan `<tree>`-tägin sijaan, mikä aiheutti alussa yhteensopivuusvirheen. Ratkaisuna käytin `list`-tägiä `tree`-tägin sijaan.
- Syötekenttien heikko visuaalinen kontrasti: Oletuksena syötekentiltä puuttuivat selkeät reunat ja ne näkyivät pelkkänä tekstinä ennen "muokkaustilaan" siirtymistä, käyttökokemuksen parantamiseksi lisäsin CSS-tyylejä.
- Ajan pyöristysvirhe keston laskennassa: `widget="float_time"` laskee keston sekuntitarkkuudella, jolloin esimerkiksi 51 minuutin ja 20 sekunnin pituinen tehtävä pyöristyi käyttöliittymässä muotoon 00:52 (52 minuuttia). Tämän ratkaisin nollaamalla sekunnit Python-koodissa (`.replace(second=0, microsecond=0)`)


Käytetty aika: Noin 7-8 tuntia 3 päivän ajalla (Sisältää ohjelman, dokumentaation ja ohjeen kirjoituksen).
