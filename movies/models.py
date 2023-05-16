# Import knihovny models (součást balíčku django.db), která obsahuje programové prostředky
# pro vytváření modelů
from django.db import models

# ---------------------------------------------------------------------------------------------------------------------
# Modely-třídy, které tvoří datovou strukturu aplikace
# ---------------------------------------------------------------------------------------------------------------------
class Genre(models.Model):
    '''
    Třída Genre je modelem pro databázový objekt (tabulku), v němž budou ukládány názvy žánrů filmů
    V závorce za názvem třídy je uvedena třída-předek Model pocházející z knihovny (balíku, modulu) models (models.Model)
    Je zde využit princip dědičnosti - všechny naše vlastní modely pocházejí ze společného předka třídy Model
    a dědí její vlastnosti
    '''

    '''
    Fields (pole) - definice jednotlivých polí/sloupců modelu/tabulky jako atributů objektu
    Každé pole modelu (budoucí tabulky v databázi) je uloženo do vhodně pojmenované proměnné/atributu - zde "name"
    Vzniká jako instance určité třídy (zde models.CharField), která rozhoduje o datovém typu pole a o jeho vlastnostech
    V tomto případě bude pole "name" dlouhé maximálně 50 znaků (parametr max_length),
    bude obsahovat unikátní hodnoty (parametr unique),
    ve formuláři se bude zobrazovat pod označením "Genre name" (parametr verbose_name),
    a uživateli se jako nápověda nabídne text uvedený v parametru help_text
    '''
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Název žánru',
                            help_text='Zadejte označení filmového žánru (např. sci-fi, komedie)')

    '''
    Metadata - slouží ke specifikaci některých dalších vlastností modelu, 
    jež ale už mohou být v řadě případů závislé i na konkrétním typu použité databáze 
    '''
    class Meta:
        # Popisek používaný při pojmenování jednoho záznamu
        verbose_name = 'Žánr'
        # Popisek používaný při pojmenování sady záznamů
        verbose_name_plural = 'Žánry'
        # Preferovaný způsob řazení záznamů - zde vzestupně podle sloupce name
        # Pro sestupné řazení se před název sloupce připíše mínus: ordering = ['-name']
        ordering = ['name']

    '''
    Methods (metody) určují chování objektu v určité situaci  
    '''
    def __str__(self):
        '''
        Magická metoda __str__() vrací řetězec, který se používá jako textová reprezentace objektu
        (například v administraci aplikace).
        V našem případě bude objekt (žánr) reprezentován výpisem obsahu pole name.
        Atribut self ukazuje na "sám" objekt (obdoba this v jiných jazycích).
        '''
        return self.name
