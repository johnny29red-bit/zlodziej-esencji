import time
import streamlit as st

st.markdown(
    """
    <style>
    div.stButton > button {
        transition: all 0.2s;
    }
    div.stButton > button:hover {
        background-color: crimson;
        color: white;
        border-color: crimson;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)
ma_esencja = False
Wygrana = False


def pisz(tekst):
    placeholder = st.empty()
    if tekst in st.session_state.pokazane:
        placeholder.text(tekst)
        return
    wyswietlany_tekst = ""
    for litera in tekst:
        wyswietlany_tekst += litera
        placeholder.text(wyswietlany_tekst)
        time.sleep(0.04)
    st.session_state.pokazane.append(tekst)


if "etap" not in st.session_state:
    st.session_state.etap = "start"
if "pokazano_intro" not in st.session_state:
    st.session_state.pokazano_intro = False
if "ostatnia_wiadomosc" not in st.session_state:
    st.session_state.ostatnia_wiadomosc = ""
if "pokazane" not in st.session_state:
    st.session_state.pokazane = []
if "ostatni_etap" not in st.session_state:
    st.session_state.ostatni_etap = "start"


def gra():
    global Wygrana, ma_esencja

    if st.session_state.etap != st.session_state.ostatni_etap:
        st.session_state.pokazane = []
        st.session_state.ostatni_etap = st.session_state.etap

    if st.session_state.etap == "start":

        if not st.session_state.pokazano_intro:
            st.write(
                "-----------------------------------------------------------------"
            )
            pisz("Witaj w grze Złodziej Esencji.")
            pisz("Jesteś przed posesją Rosyjskiego Mafiozy.")
            pisz("Perfum znajduje się w jego biurze na górze wieży.")
            pisz(
                "Aby wygrać w tej grze, musisz ukraść najlepsze perfumy na"
                " świecie."
            )
            pisz("Powodzenia!")
            st.write(
                "-----------------------------------------------------------------"
            )
            st.session_state.pokazano_intro = True

        if st.session_state.ostatnia_wiadomosc:
            pisz(st.session_state.ostatnia_wiadomosc)

            if st.button("Powrót na początek"):
                st.session_state.etap = "start"
                st.session_state.pokazano_intro = False
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()
        else:
            st.write("Jak wejdziesz?")

            if st.button("Furtka"):
                st.session_state.etap = "Furtka"
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()

            if st.button("Mur"):
                st.session_state.ostatnia_wiadomosc = (
                    "Nie masz liny, nie przejdziesz przez ten mur bez niej."
                )
                st.rerun()

            if st.button("Samolot"):
                st.session_state.ostatnia_wiadomosc = (
                    "Skaczesz bez spadochronu? Zgon."
                )
                st.rerun()

            if st.button("Kanały"):
                st.session_state.ostatnia_wiadomosc = (
                    "Idziesz 10 min kanałami, ale wyjście jest zablokowane. Dusisz"
                    " się w smrodzie.\nZgon."
                )
                st.rerun()

            if st.button("Ochroniarz"):
                st.session_state.ostatnia_wiadomosc = ""
                st.session_state.etap = "Ochronairz"
                st.rerun()

    elif st.session_state.etap == "Furtka":

        if not st.session_state.ostatnia_wiadomosc:
            pisz("Ładne kulturalne wejście.")
            pisz("Gdzie idziesz dalej?")

            if st.button("Schody"):
                st.session_state.etap = "Schody"
                st.rerun()

            if st.button("Ochroniarz"):
                st.session_state.ostatnia_wiadomosc = (
                    "Ochronairz cię nokałtuje\nZgon"
                )
                st.rerun()

            if st.button("Wspinaczka"):
                st.session_state.ostatnia_wiadomosc = (
                    "Myślisz, że jesteś Jamsem Bondem?\nRośliny pękają i"
                    " spadasz.\nUmierasz!"
                )
                st.rerun()

            if st.button("Winda"):
                st.session_state.ostatnia_wiadomosc = (
                    "Wchodzisz do windy\nWinda jedzie\nOchroniarze słyszą"
                    " ruszającą windę\nDrzwi się otwierają, stoisz twarzą w"
                    " twarz z 4 ochroniarzami\nUmierasz"
                )
                st.rerun()
        else:
            pisz(st.session_state.ostatnia_wiadomosc)

            if st.button("Powrót na początek"):
                st.session_state.etap = "start"
                st.session_state.pokazano_intro = False
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()

    elif st.session_state.etap == "Ochronairz":

        if not st.session_state.ostatnia_wiadomosc:
            pisz("Przebierasz się za ochroniarza i wchodzisz na posesję.")
            pisz("Spotykasz ochroniarza. On: -Jak się nazywasz?")

            if st.button("Co cię to obchodzi?"):
                st.session_state.etap = "Cela"
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()

            if st.button("Tomek"):
                st.session_state.ostatnia_wiadomosc = (
                    "Ty - Tomek.\nOchroniarz się śmieje i puszcza cię wolno\n"
                    "Niestety gubisz się i łapią cię kamery"
                )
                st.rerun()

            if st.button("Mrożon"):
                st.session_state.ostatnia_wiadomosc = (
                    "Niestety nie potrafisz używać swoich mocy i trafiasz w siebie"
                    "Zamrażasz się\nZgon"
                )
                st.rerun()
        else:
            pisz(st.session_state.ostatnia_wiadomosc)

            if st.button("Powrót na początek"):
                st.session_state.etap = "start"
                st.session_state.pokazano_intro = False
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()

    elif st.session_state.etap == "Cela":

        if not st.session_state.ostatnia_wiadomosc:
            pisz("Ochroniarz zgarnia cię do celi.")
            pisz("Generał pyta: - Co ty tutaj robisz?")

            if st.button("Mówisz prawdę"):
                st.session_state.ostatnia_wiadomosc = (
                    "Nie polecam mówić prawdy. Trafiasz do lochu na zawsze.\nZgon."
                )
                st.rerun()

            if st.button("Milczysz"):
                st.session_state.etap = "Biuro"
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()

            if st.button("Nie ważne"):
                st.session_state.ostatnia_wiadomosc = (
                    "Ochroniarz bije cię do śmierci\nZgon"
                )
                st.rerun()
        else:
            pisz(st.session_state.ostatnia_wiadomosc)

            if st.button("Powrót na początek"):
                st.session_state.etap = "start"
                st.session_state.pokazano_intro = False
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()

    elif st.session_state.etap == "Schody":

        if not st.session_state.ostatnia_wiadomosc:
            pisz("Słuszny wybór, ruch to zdrowie")
            pisz("Jesteś przy biurze")

            if st.button("Drzwi"):
                st.session_state.ostatnia_wiadomosc = (
                    "Szarpiesz za klamkę i robisz hałas."
                    "Ochroniarze przychodzą i cię  zabijają\nZgon"
                )
                st.rerun()

            if st.button("Okno"):
                st.session_state.etap = "Biuro"
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()
        else:
            pisz(st.session_state.ostatnia_wiadomosc)

            if st.button("Powrót na początek"):
                st.session_state.etap = "start"
                st.session_state.pokazano_intro = False
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()

    elif st.session_state.etap == "Biuro":

        if not st.session_state.ostatnia_wiadomosc:
            pisz("Udaje ci się wejść do biura")
            pisz("Ochroniarze nic nie wiedzą")
            pisz("Gdzie szukasz fiolki?")

            if st.button("Zobacz pod łóżkiem"):
                st.session_state.ostatnia_wiadomosc = (
                    "Kładziesz się na podłoge i spada na ciebie pudełko amunicji\nZgon"
                )
                st.rerun()

            if st.button("W biurku"):
                st.session_state.etap = "Ucieczka"
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()

            if st.button("Zobacz za obrazem"):
                st.session_state.ostatnia_wiadomosc = (
                    "Odsuwasz obraz\nOn spada na podłoge i robi wielki hałas"
                    "Ochroniarze przychodzą i cie zabijają\nZgon"
                )
                st.rerun()

            if st.button("Zobacz w sejfie"):
                st.session_state.ostatnia_wiadomosc = (
                    "Próbujesz zgadnąć kod, ale ochroniarze dostaja wiadomość"
                    "Przychodzą i cie zabijają"
                    "Zgon"
                )
                st.rerun()

        else:
            pisz(st.session_state.ostatnia_wiadomosc)

            if st.button("Powrót na początek"):
                st.session_state.etap = "start"
                st.session_state.pokazano_intro = False
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()
    
    elif st.session_state.etap == "Ucieczka":
        
        if not st.session_state.ostatnia_wiadomosc:
            pisz("Udało ci się znaleźć fiolkę"
            "Przydałoby się teraz uciec"
            )
        if st.button("Ucieczka"):
            st.session_state.etap = "Ucieczken"
            st.session_state.ostatnia_wiadomosc = ""
            st.rerun()

        else:
            pisz(st.session_state.ostatnia_wiadomosc)

            if st.button("Powrót na początek"):
                st.session_state.etap = "start"
                st.session_state.pokazano_intro = False
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()
    
    elif st.session_state.etap == "Ucieczken":

        if not st.session_state.ostatnia_wiadomosc:
            pisz("Dobry wybór"
            "Jak uciekasz?")
        
        if st.button("Główna brama"):
            st.session_state.etap = "dwor"
            st.session_state.ostatnia_wiadomosc = ""
            st.rerun()
        
        if st.button("Mur"):
            st.session_state.ostatnia_wiadomosc =(
            "Nie masz liny, nie przejdziesz przez ten mur"
            )
        
        if st.button("NIGGER"):
            pisz("NIGEGR")

        else:
            pisz(st.session_state.ostatnia_wiadomosc)

            if st.button("Powrót na początek"):
                st.session_state.etap = "start"
                st.session_state.pokazano_intro = False
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()
    
    elif st.session_state.etap == "dwor":
        if not st.session_state.ostatnia_wiadomosc:
            pisz("Jesteś poza posesją\nGdzie idziesz?")
        
        if st.button("Prawo"):
            st.session_state.etap = "skok"
            st.session_state.ostatnia_wiadomosc = ""
            st.rerun()
        
        if st.button("Prawo"):
            st.session_state.ostatnia_wiadomosc = (
                "Spotykasz ochronairzy\nZabijają cię\nZgon"
            )
            st.rerun()

        else:
            pisz(st.session_state.ostatnia_wiadomosc)

            if st.button("Powrót na początek"):
                st.session_state.etap = "start"
                st.session_state.pokazano_intro = False
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()
    
    elif st.session_state.etap == "skok":
        if not st.session_state.ostatnia_wiadomosc:
            pisz("Dobry wybór\nSkaczesz do wodyczy idziesz brzegiem")
        
        if st.button("Skaczesz"):
            st.session_state.ostatnia_wiadomosc =(
                "Udaje ci się uciec\nBrawo\nWYGRANA"
            )
            st.rerun()
        
        if st.button("Brzeg"):
            st.session_state.ostatnia_wiadomosc = (
                "Ochroniarze cię łapią\nZgon"
            )
            st.rerun()
            
        else:
            pisz(st.session_state.ostatnia_wiadomosc)

            if st.button("Powrót na początek"):
                st.session_state.etap = "start"
                st.session_state.pokazano_intro = False
                st.session_state.ostatnia_wiadomosc = ""
                st.rerun()
gra()
