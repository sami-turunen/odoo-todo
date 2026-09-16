from odoo import models, fields, api
from odoo.fields import Datetime


class TodoTask(models.Model):
    _name = "todo.task" # Tietokannan taulun nimi (todo_task)
    _description = "Todo Task"

    name = fields.Char(string="Tehtävän nimi", required=True) # Tehtävän nimi
    kuvaus = fields.Text(string="Kuvaus") # Tehtävän kuvaus

    """
    Seuraavat 2 kenttää ovat ajastimen aloitus ja lopetus ajat
    Käyttäjän ei itse tarvitse itse niitä asettaa, koska ajastin nappi hoitaa sen
    """
    aloitus_aika = fields.Datetime(string="Aloitusaika")
    lopetus_aika = fields.Datetime(string="Lopetusaika")

    user_id = fields.Many2one("res.users", string="Käyttäjä", default=lambda self: self.env.user)

    # Kenttä joka kertoo onko ajastin käynnissä, alussa False
    ajastin_kaynnissa = fields.Boolean(string="Ajastin käynnissä", default=False)

    # Kenttä joka kertoo tehtävän keston tunneissa
    kesto_tunneissa = fields.Float(string="Kesto (Tunneissa)", compute="_laske_kesto", store=True)

    # Tätä funktiota kutsutaan jos aloitus_aika tai lopetus_aika muuttuvat
    @api.depends("aloitus_aika", "lopetus_aika")
    def _laske_kesto(self):
        """
        Laskee tehtävän keston tunneissa, mikäli aloitus_aika ja lopetus_aika arvot ovat asetettu, eli tehtävä suoritettu.
        :return: None
        """
        for tehtava in self:
            if tehtava.aloitus_aika and tehtava.lopetus_aika:
                # Laskee keston sekunneissa ja muuntaa sen tunneiksi
                aloitus = tehtava.aloitus_aika.replace(second=0, microsecond=0)
                lopetus = tehtava.lopetus_aika.replace(second=0, microsecond=0)

                erotus = lopetus - aloitus
                tehtava.kesto_tunneissa = erotus.total_seconds() / 3600.0
            else:
                tehtava.kesto_tunneissa = 0.0 # Jos tehtävä on kesken, kesto on 0.0

    def aloita_ajastin(self):
        """
        Aloittaa ajastimen, asettaa aloitusajan tämän hetken aikaan ja asettaa lopetusajaksi False

        :return: None
        """
        self.write({
            "aloitus_aika": Datetime.now(),
            "lopetus_aika": False,
            "ajastin_kaynnissa": True
        })


    def lopeta_ajastin(self):
        """
        Lopettaa ajastimen ja asettaa lopetusajan tämän hetken aikaan

        :return: None
        """
        self.write({
            "lopetus_aika": Datetime.now(),
            "ajastin_kaynnissa": False
        })