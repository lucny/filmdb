# Import knihovny models (součást balíčku django.db), která obsahuje programové prostředky
# pro vytváření modelů
from django.db import models
# Import vestavěného modulu os, který obsahuje různé utility pro práci s daným OS
import os

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


class Film(models.Model):
    '''
    Třída Film je modelem pro databázový objekt (tabulku), který bude obsahovat základní údaje o filmech
    '''
    # Fields
    # Znakové pole o maximální délce 200 znaků pro vložení názvu filmu
    title = models.CharField(max_length=200,
                             verbose_name='Název filmu',
                             help_text='Zadejte název filmu')
    # Textové pole pro vložení delšího textu popisujícího děj filmu
    # Formulářový prvek nemusí je nepovinný - atribut null=True
    # a textové pole nemusí být vyplněno - atribut blank=True
    plot = models.TextField(null=True,
                            blank=True,
                            verbose_name='Děj')
    # Pole obsahuje datum uvedení filmu, které musí být zadáno v náležitém tvaru (YYYY-MM-DD); nepovinný údaj
    release_date = models.DateField(null=True,
                                    blank=True,
                                    verbose_name='Datum uvedení',
                                    help_text='Zadejte, prosím, datum ve formátu: <em>den.měsíc.rok</em>')
    # Celočíselné pole pro nepovinné zadání stopáže (délky) filmu v minutách
    runtime = models.PositiveSmallIntegerField(null=True,
                                  blank=True,
                                  verbose_name='Délka filmu',
                                  help_text='Prosím, zadejte celočíselný údaj vyjadřující délku filmu v minutách')
    # Pole pro zadání desetinného čísla pro hodnocení filmu v rozsahu 0.0 až 10.0
    # Výchozí hodnota je nastavena na 5.0
    # K validaci hodnot jsou použity metody z balíku/knihovny django.core.validators
    rating = models.FloatField(default=5.0,
                             null=True,
                             verbose_name='Hodnocení',
                             help_text='Zadejte desetinné číslo v rozsahu 0.0 až 10.0')
    # Vytvoří vztah mezi modely Film a Genre typu M:N
    genres = models.ManyToManyField(Genre,
                                    verbose_name='Žánry',
                                    help_text='K označení většího počtu žánrů můžete stisknout klávesu CTRL')

    # Metadata
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmy'
        # Záznamy budou řazeny primárně sestupně (znaménko mínus) podle data uvedení,
        # sekundárně vzestupně podle názvu
        ordering = ['-release_date', 'title']

    # Methods
    def __str__(self):
        '''
        Součástí textové reprezentace filmu bude jeho název, rok uvedení a hodnocení
        '''
        return f'{self.title} ({str(self.release_date.year)}), hodnocení: {str(self.rating)}'


class Attachment(models.Model):
    '''
    Třída Attachment je modelem pro databázový objekt (tabulku), který bude obsahovat údaje o přílohách filmů
    '''
    # Fields
    # Povinný titulek přílohy - text do délky 200 znaků
    title = models.CharField(max_length=200,
                             verbose_name='Titulek přílohy',
                             help_text='Doplňte stručný popis přílohy (do 200 znaků)')
    # Časový údaj o poslední aktualizaci přílohy - automaticky se ukládá aktuální čas
    last_update = models.DateTimeField(auto_now=True)
    # Pole pro upload souboru
    def attachment_path(self, filename):
        ''' Pomocná metoda, která zajistí uložení přílohy do složky attachments a podsložky označené podle id filmu '''
        return os.path.join('attachments', str(self.film.id), filename)

    # Parametr upload_to zajistí uložení souboru do složky specifikované v návratové hodnotě metody attachment_path
    file = models.FileField(upload_to=attachment_path,
                            null=True,
                            verbose_name='Příloha',
                            help_text='Vložte soubor s požadovanou přílohou')
    # Konstanta, v níž jsou ve formě n-tic (tuples) předdefinovány různé typy příloh
    TYPE_OF_ATTACHMENT = (
        ('audio', 'audio'),
        ('obrázek', 'obrázek'),
        ('text', 'text'),
        ('video', 'video'),
        ('jiná', 'jiná'),
    )
    # Pole s definovanými předvolbami pro uložení typu přílohy
    type = models.CharField(max_length=10,
                            choices=TYPE_OF_ATTACHMENT,
                            blank=True,
                            default='obrázek',
                            verbose_name='Typ přílohy',
                            help_text='Vyberte některý z uvedených typů příloh')
    # Cizí klíč, který zajišťuje propojení přílohy s daným filmem (vztah N:1)
    # Parametr on_delete slouží k zajištění tzv. referenční integrity - v případě odstranění filmu
    # budou odstraněny i všechny jeho přílohy (models.CASCADE)
    film = models.ForeignKey(Film,
                             on_delete=models.CASCADE,
                             verbose_name='Film',
                             help_text='Vyberte film, s nímž má být příloha spojena')
    # Metadata
    class Meta:
        verbose_name = 'Příloha'
        verbose_name_plural = 'Přílohy'
        # Primárně seřazeno podle poslední aktualizace souborů, sekundárně podle typu přílohy
        ordering = ['-last_update', 'type']

    # Methods
    def __str__(self):
        ''' Textová reprezentace objektu '''
        return f'{self.title} ({self.type})'
