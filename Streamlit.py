#!/usr/bin/env python
# coding: utf-8

# In[98]:


import streamlit as st
import pandas as pd
import streamlit as st

# Voorafgaande instelling voor viewport
st.markdown(
    """
    <style>
    @media (min-width: 1024px) {
        .streamlit-expanderHeader {
            font-size: 20px; /* Pas dit aan naar de gewenste grootte */
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 40px;
        color: #0A1172;  /* Donkerblauwe kleur */
        font-family: 'Arial', sans-serif;  /* Je kunt het lettertype hier veranderen */
    }
    </style>
    <h1 class="title">Analyse van Bestelauto's en KWh-Behoefte op Sloterdijk Noord Poort</h1>
    """, unsafe_allow_html=True)

st.write("""
    Welkom bij onze interactieve analyse van het aantal gestationeerde bestelauto's op het bedrijventerrein Sloterdijk Noord Poort. In deze app onderzoeken we het totale aantal geregistreerde bestelbussen per postcode, de verdeling per sector en de impact van bedrijfsgrootte op het gebruik van bestelauto's. Daarnaast berekenen we de dagelijkse KWh-behoefte voor bedrijven met elektrische bestelbussen, gebaseerd op hun gemiddelde kilometrage. Deze inzichten helpen ons om beter te begrijpen hoe we de mobiliteit en energiebehoeften op dit bedrijventerrein kunnen optimaliseren.
    """)

st.markdown("<hr style='border: 3px solid darkblue;'>", unsafe_allow_html=True)


# Markdown met uitleg
st.markdown(
    '<p style="color:red; font-size: 22px; font-weight: bold;">Bepalen aantal gestationeerde bestelbussen op Sloterdijk Noord Poort</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="color:black; font-size: 22px; font-weight: bold;">1. Totale aantal bestelbussen op Postcode van Sloterdijk Noord Poort</p>',
    unsafe_allow_html=True
)
st.write("""
Om het aantal bedrijfsauto's op bedrijventerrein Sloterdijk Noord Poort te bepalen, hebben we in eerste instantie gekeken naar het aantal geregistreerde voertuigen (bestelbussen) op de bijbehorende postcode namelijk 1046.
""")

# Afbeelding toevoegen
st.image('Scherm­afbeelding 2024-10-15 om 12.32.25.png', caption='Aantal bedrijfsauto\'s op het postcodegebied van Sloterdijk Noord Poort')
st.markdown('<p style="color:green;"><strong>Hieruit schatten we het aantal gestationeerde bestelbussen op Sloterdijk Noord Poort op ongeveer 1083.</strong></p>', unsafe_allow_html=True)
st.markdown('<hr style="border:1px solid black;">', unsafe_allow_html=True)

# Subheader met uitleg
st.markdown(
    '<p style="color:black; font-size: 22px; font-weight: bold;">2. Aantal bestelbussen op Sloterdijk Noord Poort per sector</p>',
    unsafe_allow_html=True
)

st.write("""
De onderstaande cirkeldiagram toont het percentage bestelauto's per sector volgens CBS.
""")

# Cirkelgrafiek als afbeelding
st.image('Scherm­afbeelding 2024-10-15 om 12.37.12.png', caption='Percentage bestelauto\'s per sector')
st.write(""" Op basis van de bovenstaande percentages hebben we het aantal bestelbussen per sector op Sloterdijk geschat.
""")

# Data voor overzicht bestelauto's per sector
data = {
    'Sector': ['Handel', 'Vervoer en Opslag', 'Industrie', 'Overige dienstverlening'],
    'Percentage bestelauto\'s': ['20.4%', '25%', '8.3%', '24.1%'],
    'Aantal Gestationeerd op Sloterdijk': [221, 271, 90, 261]
}

df = pd.DataFrame(data)

# Dataframe tonen
st.markdown('<p style="color:green;"><strong>Schatting van het aantal bestelbussen per sector op Sloterdijk:</strong></p>', unsafe_allow_html=True)
st.dataframe(df)
st.markdown('<hr style="border:1px solid black;">', unsafe_allow_html=True)

# Uitleg bedrijfsgrootte
# Subheader met uitleg
st.markdown(
    '<p style="color:black; font-size: 22px; font-weight: bold;">3. Aantal bestelbussen op Sloterdijk Noord Poort per Bedrijfsgrootte binnen elke sector</p>',
    unsafe_allow_html=True
)

st.write("""
Deze dataset geeft een overzicht van het aantal bedrijfsbestelauto's en hun gemiddelde jaarlijkse kilometrage, uitgesplitst naar verschillende sectoren zoals industrie, handel, vervoer, en overige dienstverlening. Daarnaast is de bedrijfsomvang onderverdeeld in categorieën, variërend van kleine bedrijven (0 tot 10 werknemers) tot grote bedrijven (meer dan 100 werknemers). Dit helpt ons te zien hoe het gebruik van bedrijfsbestelauto's varieert per sector en omvang van de organisatie.
""")
st.image('Scherm­afbeelding 2024-10-15 om 20.12.44.png', caption='Aantal Bedrijfsbestelbussen en Gemiddelde Jaarkilometrage en Bedrijfsgrootte in Nederland (SBI 2008)')

st.write("""
In deze dataset hebben we de data uit de eerste set omgerekend naar percentages om de verdeling van bedrijfsbestelauto's per bedrijfsomvang binnen verschillende sectoren duidelijker te maken. Dit maakt het eenvoudiger om de gegevens toe te passen op de bedrijven op het bedrijventerrein Sloterdijk Noord Poort, waar we mee bezig zijn.
""")

# Data voor verdeling per bedrijfsgrootte en sector
data_bedrijfsgrootte = {
    'Sector': ['Industrie', 'Industrie', 'Industrie', 'Vervoer', 'Vervoer', 'Vervoer', 
               'Handel', 'Handel', 'Handel', 'Overige', 'Overige', 'Overige'],
    'Bedrijfsgrootte': ['1 tot 10 werknemers', '10 tot 100 werknemers', 'meer dan 100 werknemers', 
                        '1 tot 10 werknemers', '10 tot 100 werknemers', 'meer dan 100 werknemers', 
                        '1 tot 10 werknemers', '10 tot 100 werknemers', 'meer dan 100 werknemers', 
                        '1 tot 10 werknemers', '10 tot 100 werknemers', 'meer dan 100 werknemers'],
    'Percentage': ['50%', '30%', '20%', '54%', '27%', '19%', '40%', '20%', '8%', '50%', '30%', '10%']
}

st.markdown('<p style="color:green;"><strong>Procentuele Verdeling van Bedrijfsbestelbussen per Sector en Bedrijfsgrootte in Sloterdijk Noord Poort:</strong></p>', unsafe_allow_html=True)
df_bedrijfsgrootte = pd.DataFrame(data_bedrijfsgrootte)
st.dataframe(df_bedrijfsgrootte)

st.markdown('<hr style="border:1px solid black;">', unsafe_allow_html=True)




# In[125]:


pip install openpyxl


# In[126]:


st.markdown(
    '<p style="color:red; font-size: 22px; font-weight: bold;">Berekenen hoeveelheid benodigde KWh per dag per bedrijf</p>',
    unsafe_allow_html=True
)
st.write("""
Na het bepalen van aantal gestationeerde bestelauto's per bedrijf op het bedrijventerrein hebben we de KWh-behoeften per dag voor deze bedrijven geschat. 
Deze schatting is gebaseerd op het aantal bestelbussen per bedrijf, de gemiddelde kilometers per dag per sector voor een gemiddelde bestelbus, 
en het gemiddelde energieverbruik (KWh) per kilometer van een gemiddelde bestelbus.
""")

# Afbeelding toevoegen
st.image('Scherm­afbeelding 2024-10-15 om 13.55.30.png', caption='Gemiddelde afgelegde kilometers van een bestelbus per dag en per jaar per sector in Nederland')

import streamlit as st

st.markdown(
    '<p style="color:black; font-size: 22px; font-weight: bold;">Voorbeeldschatting voor Bedrijf A</p>',
    unsafe_allow_html=True
)

# Introductie van de situatie
st.write("""
In dit voorbeeld berekenen we de dagelijkse KWh-behoefte voor Bedrijf A. 
We gaan uit van een scenario waarbij het bedrijf 25 elektrische bestelbussen in gebruik heeft. 
Het energieverbruik varieert afhankelijk van de seizoenen, dus we berekenen het zowel voor een gemiddelde winterdag als een zomerdag.
""")

# Stap 1: Bepalen van KWh per kilometer voor Bedrijf A
st.markdown('<p style="color:green;"><strong>Stap 1: KWh per kilometer per seizoen</strong></p>', unsafe_allow_html=True)
st.write("""
De eerste stap is het bepalen van het energieverbruik (KWh) per kilometer. 
Dit is afhankelijk van de seizoensgebonden verschillen in verbruik:
- **Winterdag**: 0,2925 KWh per kilometer
- **Zomerdag**: 0,2152 KWh per kilometer
""")

# Stap 2: Het aantal bestelbussen en de afgelegde afstand voor Bedrijf A
st.markdown('<p style="color:green;"><strong>Stap 2: Aantal bestelbussen en afgelegde afstand</strong></p>', unsafe_allow_html=True)
st.write("""
Bedrijf A heeft **25 elektrische bestelbussen**. 
Elke bestelbus rijdt gemiddeld **35 kilometer per dag**.
""")

# Stap 3: Berekenen van de totale KWh-behoefte per dag voor Bedrijf A 
st.markdown('<p style="color:green;"><strong>Stap 3: Berekening van de totale KWh-behoefte per dag</strong></p>', unsafe_allow_html=True)
st.write("""
Nu vermenigvuldigen we het aantal bestelbussen, de afgelegde kilometers per bus, en het KWh-verbruik per kilometer 
om de totale KWh-behoefte per dag te berekenen.
""")

# Berekening voor winterdag
winter_kwh_per_km = 0.2925
zomer_kwh_per_km = 0.2152
aantal_bussen = 25
gem_km_per_dag = 35

# Totale KWh-behoefte per dag (winter en zomer)
winter_kwh_per_dag = aantal_bussen * gem_km_per_dag * winter_kwh_per_km
zomer_kwh_per_dag = aantal_bussen * gem_km_per_dag * zomer_kwh_per_km

# Resultaten tonen
st.write(f"**Winterdag**: {winter_kwh_per_dag:.2f} KWh per dag")
st.write(f"**Zomerdag**: {zomer_kwh_per_dag:.2f} KWh per dag")

# Conclusie
st.markdown('<p style="color:green;"><strong>Stap 4: Conclusie</strong></p>', unsafe_allow_html=True)
st.write("""
Op basis van de schattingen verbruikt Bedrijf A ongeveer:
- **255.56 KWh per dag** in de winter (op een gemiddelde dag).
- **188.30 KWh per dag** in de zomer (op een gemiddelde dag).

Dit geeft inzicht in hoeveel elektriciteit nodig is om de bestelbussen van het bedrijf volledig op te laden per dag, afhankelijk van de tijd van het jaar.
""")

st.markdown('<hr style="border:1px solid black;">', unsafe_allow_html=True)



# In[127]:


st.markdown(
    '<p style="color:red; font-size: 22px; font-weight: bold;">Inschatten laadtijden van bedrijven in verschillende sectoren</p>',
    unsafe_allow_html=True
)
st.write("""
In deze analyse hebben we de laadtijden van de bedrijven op Sloterdijk Noord Poort binnen diverse sectoren geschat. De laadtijden zijn gebaseerd op sector, grootte van het bedrijf en specifieke laadtijden van de gebruikte bestelbussen. Deze schattingen zijn gedaan met inachtneming van beschikbare data over bestelauto-activiteiten en verkeerspatronen.
""")

st.image('Scherm­afbeelding 2024-10-16 om 11.24.13.png', caption='Relatieve verkeersintensiteit bestelauto’s op Nederlandse wegen (gemiddeld)-bron kentekenscans TNO')




# In[128]:


import streamlit as st

st.markdown('<p style="color:green;"><strong>Inschatting laadmomenten per sector</strong></p>', unsafe_allow_html=True)

with st.expander("Vervoer en Opslag (Klik hier voor details)"):
    st.write("""
    **Bedrijfsomvang en Tijdsvensters**:
    - **Bedrijven met 10 tot 100 werknemers**: Laadtijden langer dan 5 uur, tijdsvenster: 17:00 - 00:00.
    - **Grotere bedrijven** (meer dan 100 werknemers): Tijdsvenster: 00:00 - 06:00.
    
    **Reden voor deze planning**:
    In de sector Vervoer en Opslag wordt veel logistiek werk in de avond en nacht uitgevoerd, deels om infrastructuurbeperkingen te omzeilen. Het wegennetwerk is vaak minder druk in deze tijdsvensters, wat efficiënte vervoersbewegingen mogelijk maakt. Daarnaast hebben bedrijven met minder werknemers vaak langere laadtijden door beperkte middelen, waardoor zij meer tijd nodig hebben om logistieke operaties af te ronden.
    
    **Impact op bedrijfsvoering**:
    Door het kiezen van deze tijdsvensters kunnen bedrijven de piekuren in het verkeer vermijden, wat resulteert in lagere transportkosten en efficiëntere doorlooptijden.
    """)

# Sector: Industrie
with st.expander("Industrie (Klik hier voor details)"):
    st.write("""
    **Bedrijfsomvang en Tijdsvensters**:
    - **Bedrijven met meer dan 100 werknemers (laadtijd = 5 uur)**: Tijdsvensters: 12:00 - 15:00, 17:00 - 20:00.
    - **Bedrijven met meer dan 100 werknemers (laadtijd > 5 uur)**: Tijdsvenster: 17:00 - 00:00.
    
    **Reden voor deze planning**:
    Grote industriële bedrijven hebben vaak een strakke planning om te zorgen dat de logistieke operaties de kernproductieprocessen niet verstoren. Daarom worden de laadtijden vaak buiten de piekuren van de productie gepland. Bedrijven met langere laadtijden krijgen een uitgebreider tijdsvenster om alle benodigde goederen te verwerken.
    
    **Impact op bedrijfsvoering**:
    Deze aanpak minimaliseert stilstand van productie en zorgt ervoor dat logistieke processen soepel verlopen, waardoor productiviteitsverlies wordt vermeden.
    """)

# Sector: Handel
with st.expander("Handel (Klik hier voor details)"):
    st.write("""
    **Bedrijfsomvang en Tijdsvensters**:
    - **Bedrijven met 10 tot 100 werknemers**: Tijdsvenster: 18:00 - 01:00.
    - **Grotere bedrijven**: Tijdsvenster: 01:00 - 07:00.
    
    **Reden voor deze planning**:
    In de handelssector zijn laadtijden vaak gepland buiten de openingsuren van de winkels of distributiecentra. Dit zorgt ervoor dat klanten en personeel niet worden gestoord tijdens de operationele uren van de dag. Kleinere bedrijven kunnen laadtijden toestaan in de vroege avond, terwijl grotere bedrijven ervoor kiezen dit tijdens de nachtelijke uren te doen, wanneer het verkeer en de bedrijfsactiviteiten minimaal zijn.
    
    **Impact op bedrijfsvoering**:
    Het vermijden van laadtijden tijdens openingsuren verhoogt de klanttevredenheid en voorkomt verstoringen in de dagelijkse operaties.
    """)

# Sector: Overige Dienstverlening
with st.expander("Overige Dienstverlening (Klik hier voor details)"):
    st.write("""
    **Bedrijfsomvang en Tijdsvensters**:
    - **Bedrijven met 10 tot 100 werknemers**: Tijdsvenster: 17:00 - 00:00.
    - **Grotere bedrijven**: Tijdsvenster: 00:00 - 06:00.
    
    **Reden voor deze planning**:
    Bedrijven in de dienstverlenende sector voeren hun operaties vaak buiten kantoortijden uit om zo min mogelijk verstoring te veroorzaken bij klanten. Dit geldt vooral voor bedrijven met een grotere workforce die ’s nachts werken om logistieke operaties uit te voeren zonder de dagtaken te onderbreken.
    
    **Impact op bedrijfsvoering**:
    Door het plannen van laadtijden buiten kantoortijden worden zakelijke processen en klantinteracties niet beïnvloed, wat de efficiëntie en klanttevredenheid verhoogt.
    """)

st.write("Klik op een sector voor meer informatie over de logistieke planning en het waarom achter bepaalde tijdsvensters.")
st.markdown('<hr style="border:1px solid black;">', unsafe_allow_html=True)



# In[129]:


st.markdown(
    '<p style="color:red; font-size: 22px; font-weight: bold;">Weergave gemaakte inschattingen per Bedrijf</p>',
    unsafe_allow_html=True
)
st.write("""
Hieronder staat een dataset die alle schattingen per bedrijf verzamelt, met betrekking tot het aantal gebruikte bestelwagens, de benodigde kWh, de gemiddelde laadtijd en de laadmomenten per dag.
""")
df = pd.read_excel('new.xlsx')
st.dataframe(df)

st.markdown('<hr style="border:1px solid black;">', unsafe_allow_html=True)


# In[130]:


st.markdown(
    '<p style="color:red; font-size: 22px; font-weight: bold;">Weergave datset met KWh per bedrijf gedurend het jaar 3034 </p>',
    unsafe_allow_html=True
)
st.write("""
De bovenstaande dataset met schattingen per bedrijf is in Python gebruikt om met behulp van code voor elk uur van het jaar te berekenen hoeveel energie elk bedrijf nodig heeft om hun bestelauto's op te laden, rekening houdend met de laadtijden en het seizoen.
""")
last = pd.read_excel('hoop.xlsx')
st.dataframe(last)


# In[ ]:





# In[ ]:





# In[ ]:




