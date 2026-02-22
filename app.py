import streamlit as st
# Frage: Warum war die Eroberung der Etrusker so bedeutsam?
# Frage zur Staatsform


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
    st.write("[1]")
    
    if st.button("Start", key = "start_1"):
        st.session_state["index"] += 1 #1

elif st.session_state["index"] == 1:
    st.title("Wann wurde Rom zur Republik?");

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_2"):
            st.session_state["index"] += 0.5 #1,5

    with col2:
        st.write("A) Sie wurde 509 v. Chr gegründet.")

    with col1:
        if st.button("B", key = "b_2"):
            st.session_state["index"] += 0.7 #1,7
            st.session_state["punktestand"] += 1 #1

    with col2:
        st.write("B) Sie hat um etwa 503/4 angefangen sich zu entwickenln.")

    with col1:
        if st.button("C", key = "c_2"):
            st.session_state["index"] += 0.5 #1,5

    with col2:
        st.write("C) Sie entstand zu Anfang der römischen Geschichte um 735 v. Chr. .")


elif st.session_state["index"] == 1.5:
    st.title("Das war falsch.")
    st.write("Die römische Republik begann sich um 504/3 v. Chr. zu entwickeln.")

    if st.button("OK", key = "ok_2"):
        st.session_state["index"] += 0.2 #2

elif st.session_state["index"] == 1.7:
    st.title("Buchstabe")
    st.write("Dein erster Buchstabe ist: D ")

    if st.button("Weiter", key = "weiter_2"):
        st.session_state["index"] += 0.3 #2

elif st.session_state["index"] == 2:
    st.title("Was bedeutet res publicas, woraus das Wort Republik stammt?")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_3"):
            st.session_state["index"] += 0.5 #2,5

    with col2:
        st.write("A) Zusammenschluss")

    with col1:
        if st.button("B", key = "b_3"):
            st.session_state["index"] += 0.5 #2,5

    with col2:
        st.write("B) Volksherrschaft")

    with col1:
        if st.button("C", key = "c_3"):
            st.session_state["index"] += 0.7 #2,7
            st.session_state["punktestand"] += 1 #2

    with col2:
        st.write("C) Die gemeinsame Sache")

elif st.session_state["index"] == 2.5:
    st.title("Das war falsch.")
    st.write("Tatsächlich bedeutet res publicas in etwa übersetzt 'die gemeinsame Sache'. ")

    if st.button("OK", key = "ok_3"):
        st.session_state["index"] += 0.2 #2,7

elif st.session_state["index"] == 2.7:
    st.title("Buchstabe")
    st.write("Dein zweiter Buchstabe ist: e")

    if st.button("Weiter", key = "weiter_3"):
        st.session_state["index"] += 0.3 #3

elif st.session_state["index"] == 3:
    st.title("Wie hieß die erste Verschriftlichung der Gesetze der römischen Republik?")
    
    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_4"):
            st.session_state["index"] += 0.7 #3,7
            st.session_state["punktestand"] += 1 #3

    with col2:
        st.write("A) Es war das Zwölftafelgesetz von 450 v. Chr. .")

    with col1:
        if st.button("B", key = "b_4"):
            st.session_state["index"] += 0.5 #3,5

    with col2:
        st.write("B) Es war die Lex Canuleia aus dem Jahr 497 v. Chr. .")

    with col1:
        if st.button("C", key = "c_4"):
            st.session_state["index"] += 0.5 #3,5

    with col2:
        st.write("C) Es war das Palantingesetz von 450 v. Chr. .")

elif st.session_state["index"] == 3.5:
    st.title("Das ist falsch.")
    st.write("Es war tatsächlich das Zwölftafelgesetz von 450 v. Chr., welches primär durch den ersten großen Generalstreik der Plebejer ausgelöst wurde.")

    if st.button("OK", key = "ok_4"):
        st.session_state["index"] += 0.2 #3,7

elif st.session_state["index"] == 3.7:
    st.title("Buchstabe")
    st.write("Dein dritter Buchstabe ist: r")

    if st.button("Weiter", key = "weiter_4"):
        st.session_state["index"] += 0.3 #4

elif st.session_state["index"] == 5:
    st.title("Was ist die Aufgabe des Senats?")
    
    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_5"):
            st.session_state["index"] += 0.5 #5,5

    with col2:
        st.write("A) Der Senat stimmt mit den Magistrate und den Volkstribunen über Gesetze ab.")

    with col1:
        if st.button("B", key = "b_5"):
            st.session_state["index"] += 0.7 #5,7
            st.session_state["punktestand"] += 1 #4

    with col2:
        st.write("B) Er berät primär die Magistrate zu politischen Entscheidungen.")

    with col1:
        if st.button("C", key = "c_5"):
            st.session_state["index"] += 0.5 #5,5

    with col2:
        st.write("C) Er entscheidet darüber, wer die Magistrate erhält.")

elif st.session_state["index"] == 5.5:

    st.title("Das ist falsch.")
    st.write("Der Senat gibt primär den Magitraten Empfehlungen.")

    if st.button("OK", key = "ok_5"):
        st.session_state["index"] += 0.2 #5,7

elif st.session_state["index"] == 5.7:
    st.title("Buchstabe")
    st.write("Dein fünfte Buchstabe ist: p")

    if st.button("Weiter", key = "weiter_6"):
        st.session_state["index"] += 0.3 #6

elif st.session_state["index"] == 4:

    st.title("Was sind die Magistrate?")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_6"):
            st.session_state["index"] += 0.7 #4,7
            st.session_state["punktestand"] += 1 #5

    with col2:
        st.write("A) Es waren die römischen Ämter, der Regierung.")

    with col1:
        if st.button("B", key = "b_6"):
            st.session_state["index"] += 0.5 #4,5

    with col2:
        st.write("B) Es waren die Bezeichnung für die Mitglieder mit Senat.")

    with col1:
        if st.button("C", key = "c_6"):
            st.session_state["index"] += 0.5 #4,5

    with col2:
        st.write("C) Der Name, der Ämter zur Vertretung der Plebejer.")

elif st.session_state["index"] == 4.5:
    st.title("Das ist falsch.")
    st.write("Die Mandate sind die Ämter der römischen Regierung.")

    if st.button("OK", key = "ok_6"):
        st.session_state["index"] += 0.2 #4,7

elif st.session_state["index"] == 4.7:
    st.title("Buchstabe")
    st.write("Dein vierter Buchstabe ist: e")

    if st.button("Weiter", key = "weiter_5"):
        st.session_state["index"] += 0.3 #5

elif st.session_state["index"] == 6:
    st.title("Welches Element der Verfassung könnte man als aristokratisch bezeichnen?")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_7"):
            st.session_state["index"] += 0.5 #6,5

    with col2:
        st.write("A) Die römschen Ämter, da sie zumeist mit Personen aus der Oberschicht besetzt wurden.")

    with col1:
        if st.button("B", key = "b_7"):
            st.session_state["index"] += 0.5 #6,5

    with col2:
        st.write("B) Den Konsul spezifisch, da dieses Amt davon ausgeht, dass jemand die Macht über das Militär und oberstes Amt der Regierung erhalten soll.")

    with col1:
        if st.button("C", key = "c_7"):
            st.session_state["index"] += 0.7 #6,7
            st.session_state["punktestand"] += 1 #6

    with col2:
        st.write("C) Der Senat, da seine Mitglieder nur beitreten können, wenn sie bereits Regierungsämter belegt haben und somit zu den Machtigen und Erfahrenen zählen.")

elif st.session_state["index"] == 6.5:
    st.title("Das ist falsch.")
    st.write("Da der Senat das aristokratische Element darstellt. Jenes bedeutet übersetzt die Herrschaft der Besten und der Senat war zusammengesetzt aus mächtigen Menschen, welche zuvor ein Amt besaßen und somit zu jener Elite zählten.")

    if st.button("OK", key = "ok_7"):
        st.session_state["index"] += 0.2 #6,7

elif st.session_state["index"] == 6.7:
    st.title("Buchstabe")
    st.write("Dein sechster Buchstabe ist: u")

    if st.button("Weiter", key = "weiter_7"):
        st.session_state["index"] += 0.3 #7

elif st.session_state["index"] == 7:
    st.title("Wie wird die Vertretung der Plebejer in der Regierung genannt?")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_8"):
            st.session_state["index"] += 0.5 #7,5

    with col2:
        st.write("A) Volksämter")

    with col1:
        if st.button("B", key = "b_8"):
            st.session_state["index"] += 0.7 #7,7
            st.session_state["punktestand"] += 1 #7

    with col2:
        st.write("B) Volkstribunen")

    with col1:
        if st.button("C", key = "c_8"):
            st.session_state["index"] += 0.5 #7,5

    with col2:
        st.write("C) Plebiszite")

elif st.session_state["index"] == 7.5:

    st.title("Das ist falsch.")
    st.write("Die Vertretung der Plebejer in der Regierung nennt sich Volkstribunen.")

    if st.button("OK", key = "ok_8"):
        st.session_state["index"] += 0.2 #7,7

elif st.session_state["index"] == 7.7:
    st.title("Buchstabe")
    st.write("Dein siebter Buchstabe ist: b")

    if st.button("Weiter", key = "weiter_7"):
        st.session_state["index"] += 0.3 #8

elif st.session_state["index"] == 8:

    st.title("Warum war die Eroberung der Etrusker so bedeutsam?")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_9"):
            st.session_state["index"] += 0.5 #8,5

    with col2:
        st.write("A) Da die Etrusker zuvor um 387 v.Chr. Rom Monate lang belagerten und plünderten.")

    with col1:
        if st.button("B", key = "b_9"):
            st.session_state["index"] += 0.7 #8,7
            st.session_state["punktestand"] += 1 #8

    with col2:
        st.write("B) Rom wurde von Etruskern gegründet und war nun stärker als diese mächtige Hochkultur.")

    with col1:
        if st.button("C", key = "c_9"):
            st.session_state["index"] += 0.5 #8,5

    with col2:
        st.write("C) Die Etrusker hatte es zuvor fast geschaft die römische Republik um 400 v. Chr. zu erobern.")

elif st.session_state["index"] == 8.5:

    st.title("Das ist falsch.")
    st.write("Die Etrusker war der Ursprung von Rom und hat sich erst als Republik unabhängig von den Etruskern gemacht. Letztlich unterwirft Rom die Etrusker, was als Zeichen des Wachstum und der Stärker der Römer gewertet werden kann.")

    if st.button("OK", key = "ok_9"):
        st.session_state["index"] += 0.2 #8,7

elif st.session_state["index"] == 8.7:
    st.title("Buchstabe")
    st.write("Dein achter Buchstabe ist: l")

    if st.button("Weiter", key = "weiter_9"):
        st.session_state["index"] += 0.3 #9

elif st.session_state["index"] == 9:

    st.title("Welche Staatsform war die römische Republik aus heutiger Sicht?")

    col1, col2 = st.columns([1, 3])

    with col1:
        if st.button("A", key = "a_10"):
            st.session_state["index"] += 0.5 #9,5

    with col2:
        st.write("A) Sie war eine Aristokratie, also die Herrschaft einer qualifizierten und privilegierten Minderheit.")

    with col1:
        if st.button("B", key = "b_10"):
            st.session_state["index"] += 0.5 #9,5

    with col2:
        st.write("B) Sie war eine repräsentative Demokratie, da die Magistrate und Volkstribunen von dem Volk direkt gewählt werden.")

    with col1:
        if st.button("C", key = "c_10"):
            st.session_state["index"] += 0.7 #9,7
            st.session_state["punktestand"] += 1 #9

    with col2:
        st.write("C) Sie war eine Oligarchie, also die Herrschaft der Wenigen. Da die Herrscherelite eine gesellschaftliche Minderheit darstellte und primär Eigeninteressen verfolgte.")

elif st.session_state["index"] == 9.5:

    st.title("Das ist falsch.")
    st.write("Die römische Republik war durch die enormen Privilegien der Patrizier Oligarchie. Da eine Aristokratie dann zur Oligarchie wird, wenn die Herrschenden nur dem Eigennutz einer gesellschaftlichen Minderheit dienen.")

    if st.button("OK", key = "ok_10"):
        st.session_state["index"] += 0.2 #9,7

elif st.session_state["index"] == 9.7:
    st.title("Buchstabe")
    st.write("Dein neunter Buchstabe ist: i")

    if st.button("Weiter", key = "weiter_10"):
        st.session_state["index"] += 0.3 #10

elif st.session_state["index"] == 10:

    st.title("Fertig!")
    st.write("Vielen Dank für das Mitmachen :-)")
    st.write(f"Dein Score ist {st.session_state.punktestand} von 9 Punkten.")

    st.title("Das Buchstabenrätzel:")
    st.write("Super! Deine letzten beiden Buchstaben sind 'ca', um das Buchstabenrätzel zu lösen.")
    st.write("Und natürlich ist es in Latein (-:")

    if st.button("Lösungen", key = "lösungen_12"):
        st.session_state["index"] += 2 #12

    st.title("Bildquellen")

    if st.button("Bildquellen", key = "bildquellen_11"):
        st.session_state["index"] += 1 #11

elif st.session_state["index"] == 11:
    st.title("Bildquellen")
    st.write("[1] unbekannt: Römisches Reich. In: https://romischesreich.de, o.D. URL: https://romischesreich.de/ (zuletzt abgerufen: 15.02.2026)")
    if st.button("Zurück", key = "zurück_11"):
        st.session_state["index"] -= 1 #10

elif st.session_state["index"] == 12:
    st.title("Lösungen des Buchstabenrätzel")
    st.write("Wenn du jetzt die Buchstaben 'derepublica' hast, hast du das Rätzel vervollständigt.")
    st.write("Es ist der Name des Buches 'de re publica' von Cicero der unter anderem römischer Konsul war und um etwa bis 50 v. Chr. den römischen Staat zu der Zeit beschrieb.")
    st.write("PS.: Den Title des Buches müsstest du schon übersetzten können...")

    if st.button("Zurück", key = "zurück_12"):
        st.session_state["index"] -= 2 #10











    
    
     

