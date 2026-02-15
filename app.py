import streamlit as st

page_bg = """
    <style>
    .stApp {
    background-color: #333333;
    font-family: "Courier New", monospace;
    }
    h1 {
    color: #ff2800;
    text-decoration: underline;
    font-family : "Courier New" , monospace;
    font-style: bold;
    }
    span, label {
    color: white,
    font-family: "Courier New", monospace;
    }
    blockquote, p.quote {
    font-family: "Courier New", monospace;
    font-style: italic;
    color: #ffcc00;
    }
    div.stButton > button {
    background-color:#333333;
    color: white;
    border-radius: 10px;
    border: 1px solid #ff2800;
    }
    div[data-baseweb="slider"] > div > div {
    background: #ff2800 !important;
    }
    div[data-baseweb="slider"] > div > div > div {
    background: #ff2800 !important;
    }
    div[data-testid="stProgressBar"] > div > div {
    background-color: #ff2800 !important;
    }
    </style>
    """

st.markdown(page_bg, unsafe_allow_html=True)

if "index" not in st.session_state:
    st.session_state["index"] = 0;

if "punktestand" not in st.session_state:
    st.session_state["punktestand"] = 0;

if st.session_state["index"] == 0:
    st.title("Was weißst du über die römische Republik?")
    st.write("In diesem Quiz findest du es heraus.")
    st.image("./römisches-reich.jpg")
    
    if st.button("Start", key = "start_1"):
        st.session_state["index"] += 1 #1

elif st.session_state["index"] == 1:
    st.title("Wann wurde Rom zur Republik?");

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_2"):
            st.session_state["index"] += 0.5 #1,5

    with col2:
        st.write("Sie wurde 509 v. Chr gegründet.")

    with col1:
        if st.button("B", key = "b_2"):
            st.session_state["index"] += 1 #2
            st.session_state["punktestand"] += 1 #1

    with col2:
        st.write("Sie hat um etwa 503/4 angefangen sich zu entwickenln.")

    with col1:
        if st.button("C", key = "c_2"):
            st.session_state["index"] += 0.5 #1,5

    with col2:
        st.write("Sie entstand zu Anfang der römischen Geschichte um 735 v. Chr. .")


elif st.session_state["index"] == 1.5:
    st.title("Das war falsch.")
    st.write("Die römische Republik begann sich um 504/3 v. Chr. zu entwickeln.")

    if st.button("OK", key = "ok_2"):
        st.session_state["index"] += 0.5 #2

elif st.session_state["index"] == 2:
    st.title("Was waren die 3 Hauptprinzipien des Staatswesen der Republik?")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_3"):
            st.session_state["index"] += 0.5 #2,5

    with col2:
        st.write("Gemeinschaft, Gewaltenteilung und Annuität.")

    with col1:
        if st.button("B", key = "b_3"):
            st.session_state["index"] += 0.5 #2,5

    with col2:
        st.write("Kollegialität, Iterationsverbot und Mitbestimmung.")

    with col1:
        if st.button("C", key = "c_3"):
            st.session_state["index"] += 1 #3
            st.session_state["punktestand"] += 1 #2

    with col2:
        st.write("Kollegialität, Annualität und Iterationsverbot.")

elif st.session_state["index"] == 2.5:
    st.title("Das war falsch.")
    st.write("Tatsächlich waren die 3 Hauptprinzipien die Kollegialität, Annualität und das Iterationsverbot.")

    if st.button("OK", key = "ok_3"):
        st.session_state["index"] += 0.5 #3

elif st.session_state["index"] == 3:
    st.title("Wie hieß die erste Verschriftlichung der Gesetze der römischen Republik?")
    
    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_4"):
            st.session_state["index"] += 1 #4
            st.session_state["punktestand"] += 1 #3

    with col2:
        st.write("Es war das Zwölftafelgesetz von 450 v. Chr. .")

    with col1:
        if st.button("B", key = "b_4"):
            st.session_state["index"] += 0.5 #3,5

    with col2:
        st.write("Es war die Lex Canuleia aus dem Jahr 497 v. Chr. .")

    with col1:
        if st.button("C", key = "c_4"):
            st.session_state["index"] += 0.5 #3,5

    with col2:
        st.write("Es war das Palantingesetz von 450 v. Chr. .")

elif st.session_state["index"] == 3.5:
    st.title("Das ist falsch.")
    st.write("Es war tatsächlich das Zwölftafelgesetz von 450 v. Chr., welches primär durch den ersten großen Generalstreik der Plebejer ausgelöst wurde.")

    if st.button("OK", key = "ok_4"):
        st.session_state["index"] += 0.5 #4

elif st.session_state["index"] == 5:
    st.title("Was ist die Aufgabe des Senats?")
    
    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_5"):
            st.session_state["index"] += 0.5 #5,5

    with col2:
        st.write("Der Senat stimmt mit den Magistrate und den Volkstribunen über Gesetze ab.")

    with col1:
        if st.button("B", key = "b_5"):
            st.session_state["index"] += 1 #6
            st.session_state["punktestand"] += 1 #4

    with col2:
        st.write("Er berät die Magistrate und die Volkstributen Vorschlägen und Empfehlungen.")

    with col1:
        if st.button("C", key = "c_5"):
            st.session_state["index"] += 0.5 #5,5

    with col2:
        st.write("Er entscheidet darüber, wer die Magistrate erhält.")

elif st.session_state["index"] == 5.5:

    st.title("Das ist falsch.")
    st.write("Der Senat gibt den Magitraten Empfehlungen und legt den Volkstribunen Gesetzesvorschläge vor.")

    if st.button("OK", key = "ok_5"):
        st.session_state["index"] += 0.5 #6

elif st.session_state["index"] == 4:

    st.title("Was sind die Magistrate?")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_6"):
            st.session_state["index"] += 1 #5
            st.session_state["punktestand"] += 1 #5

    with col2:
        st.write("Es waren die römischen Ämter, der Regierung.")

    with col1:
        if st.button("B", key = "b_6"):
            st.session_state["index"] += 0.5 #4,5

    with col2:
        st.write("Es waren die Mandate, die man als Senatsmitglied bekam.")

    with col1:
        if st.button("C", key = "c_6"):
            st.session_state["index"] += 0.5 #4,5

    with col2:
        st.write("Der Name, der Ämter zur Vertretung der Plebejer.")

elif st.session_state["index"] == 4.5:
    st.title("Das ist falsch.")
    st.write("Die Mandate sind die Ämter der römischen Regierung.")

    if st.button("OK", key = "ok_6"):
        st.session_state["index"] += 0.5 #5

elif st.session_state["index"] == 6:
    st.title("Wie werden jährlich die Magistrate der römischen Republik gewählt?")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_7"):
            st.session_state["index"] += 0.5 #6,5

    with col2:
        st.write("Bei der Volksversammlung können alle männlichen Bürger gleichberechtigt ihre Stimme ab.")

    with col1:
        if st.button("B", key = "b_7"):
            st.session_state["index"] += 0.5 #6,5

    with col2:
        st.write("Die Volksversammlung wählt Repräsentaten, die für sie die Personen für die Magistrate ernennen. Dabei wählen die Patrizier mehr Representanten.")

    with col1:
        if st.button("C", key = "c_7"):
            st.session_state["index"] += 1 #7
            st.session_state["punktestand"] += 1 #6

    with col2:
        st.write("Die Volksversammlung wählt die Magistrate in dem Zenturiatskomitien, wo jede Gesellschaftsgruppe Zenturien zugewiesen, was nach der Vermögensklasse passiert.")

elif st.session_state["index"] == 6.5:
    st.title("Das ist falsch.")
    st.write("Die Magistrate werden von den Zenturiatskomitien gewählt, wo Zenturien von der Volksversammlungen gewählt wird. Und desto mehr Vermögen man hatte, desto mehr zählte die jeweilige Stimme.")

    if st.button("OK", key = "ok_7"):
        st.session_state["index"] += 0.5 #7

elif st.session_state["index"] == 7:
    st.title("Wie wird die Vertretung der Plebejer in der Regierung genannt?")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_8"):
            st.session_state["index"] += 0.5 #7,5

    with col2:
        st.write("Volksämter")

    with col1:
        if st.button("B", key = "b_8"):
            st.session_state["index"] += 1 #8
            st.session_state["punktestand"] += 1 #7

    with col2:
        st.write("Volkstribunen")

    with col1:
        if st.button("C", key = "c_8"):
            st.session_state["index"] += 0.5 #7,5

    with col2:
        st.write("Plezite")

elif st.session_state["index"] == 7.5:

    st.title("Das ist falsch.")
    st.write("Die Vertretung der Plebejer in der Regierung nennt sich Volkstribunen.")

    if st.button("OK", key = "ok_8"):
        st.session_state["index"] += 0.5 #8

elif st.session_state["index"] == 8:

    st.title("Warum war die Eroberung der Etrusker so bedeutsam?")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_9"):
            st.session_state["index"] += 0.5 #8,5

    with col2:
        st.write("Da sie die Römer vorher schon mal eroberten.")

    with col1:
        if st.button("B", key = "b_9"):
            st.session_state["index"] += 1 #9
            st.session_state["punktestand"] += 1 #8

    with col2:
        st.write("Rom wurde von Etruskern gegründet und war nun stärker als diese mächtige Hochkultur.")

    with col1:
        if st.button("C", key = "c_9"):
            st.session_state["index"] += 0.5 #8,5

    with col2:
        st.write("Die Etrusker hatte es zuvor fast geschaft die römische Republik um 400 v. Chr. zu erobern.")

elif st.session_state["index"] == 8.5:

    st.title("Das ist falsch.")
    st.write("Die Etrusker war der Ursprung von Rom und hat sich erst als Republik unabhängig von den Etruskern gemacht. Letztlich unterwirft Rom die Etrusker, was als Zeichen des Wachstum und der Stärker der Römer gewertet werden kann.")

    if st.button("OK", key = "ok_9"):
        st.session_state["index"] += 0.5 #9

elif st.session_state["index"] == 9:

    st.title("Welche Staatsform war die römsische Republik aus heutiger Sicht?")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_10"):
            st.session_state["index"] += 1 #10
            st.session_state["punktestand"] += 1 #9

    with col2:
        st.write("Sie war eine Aristokratie, also die Herrschaft einer qualifizierten und privilegierten Minderheit.")

    with col1:
        if st.button("B", key = "b_10"):
            st.session_state["index"] += 0.5 #9,5

    with col2:
        st.write("Sie war eine repräsentative Demokratie, da die Magistrate und Volkstribunen von dem Volk direkt gewählt werden.")

    with col1:
        if st.button("C", key = "c_10"):
            st.session_state["index"] += 0.5 #9,5

    with col2:
        st.write("Die römische Republik war eine Republik, also Übersetzt ein Gemeinwesen. Genaugesagt eine demokratische Republik, aufgrund der jährlichen Wahlen der Regierungsämter.")

elif st.session_state["index"] == 9.5:

    st.title("Das ist falsch.")
    st.write("Die römische Republik war durch die enormen Privilegien der Patrizier eine Aristokratie.")

    if st.button("OK", key = "ok_10"):
        st.session_state["index"] += 0.5 #10

elif st.session_state["index"] == 10:

    st.title("Fertig!")
    st.write("Vielen Dank für das Mitmachen :-)")
    st.write(f"Dein Score ist {st.session_state.punktestand} von 9 Punkten.")











    
    
     

