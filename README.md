
17.07.2026

<div align="center">

# VCO Design und Simulation

**Entwicklung und Inbetriebnahme eines Wien-Robinson-Oszillators als
Voltage-Controlled-Ozillator ($f_0=5,5~\text{MHz}$)**

[![Simulation](https://img.shields.io/badge/Simulation-LTspice%20%7C%20NGspice-red?style=for-the-badge.png)](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html)
[![Simulation](https://img.shields.io/badge/Design-KiCad-blue?style=for-the-badge.png)](https://www.kicad.org/)
[![Hardware](https://img.shields.io/badge/Hardware-THT%20%7C%20SMD-orange?style=for-the-badge.png)](datasheets/)
[![Python](https://img.shields.io/badge/Analyse-Python-green?style=for-the-badge.png)](https://www.python.org/)

<table style="border: none; border-collapse: collapse; margin: 0 auto;" border="0">

<tr style="border: none;">

<td style="border: none; padding: 0 25px; text-align: center;">

Tassilo Hertling
<a href="https://github.com/TassiloHertling"><img src="https://img.shields.io/badge/-%20-181717?style=flat&logo=github" valign="middle" alt="GitHub"></a>
<a href="mailto:thertling@stud.hs-bremen.de"><img src="https://img.shields.io/badge/-✉-blue?style=flat" valign="middle" alt="Email"></a>
</td>

<td style="border: none; padding: 0 25px; text-align: center;">

Torben Becker
<a href="https://github.com/beckertorben"><img src="https://img.shields.io/badge/-%20-181717?style=flat&logo=github" valign="middle" alt="GitHub"></a>
<a href="mailto:tbecker@stud.hs-bremen.de"><img src="https://img.shields.io/badge/-✉-blue?style=flat" valign="middle" alt="Email"></a>
</td>

<td style="border: none; padding: 0 25px; text-align: center;">

Mirco Ick
<a href="https://github.com/mircoick"><img src="https://img.shields.io/badge/-%20-181717?style=flat&logo=github" valign="middle" alt="GitHub"></a>
<a href="mailto:mick001@stud.hs-bremen.de"><img src="https://img.shields.io/badge/-✉-blue?style=flat" valign="middle" alt="Email"></a>
</td>

</tr>

</table>

</br> </br>

**Dateiübersicht**

[KiCad-Dateien](kicad/) · [Simulationsdaten](sim/) · [Python
Code](code/) · [Datenblätter](datasheets/)

</div>

------------------------------------------------------------------------

# Einleitung

In diesem Projekt gilt es einen VCO (Voltage Controlled Oszillator) zu
designen und in Betrieb zu nehmen. Das Design soll bestimmte
Anforderungen erfüllen, damit es in einem Laborversuch als FM-Modulator
genutzt werden kann. In der Vergangenheit wurde im Laborversuch eine VCO
Schaltung mit alten und abgekündigkten Komponenten verwendet. Diese
Schaltung soll nun mit neuen und verfügbaren Komponenten erneuert
werden.

Die VCO Schaltung soll eine FM-Modulation mit einem Trägersignal bei der
Frequenz $5,5~\text{MHz}$ durchführen und einen Modulationsbereich
zwischen $5~\text{MHz}$ und $6~\text{MHz}$ verwenden. Der
Einstellungsbereich soll mit $1~\text{V}$ pro $1~\text{MHz}$ eingestellt
werden. Somit kann das zu modulierende Signal einen Spannungsbereich von
$V_{pp} = 1~\text{V}$ haben. Die Ein- und Ausgangsimpedanz soll
$50~\Omega$ betragen.

Zudem soll die Schaltung aus Komponenten bestehen, die Studierenden im
4.Semester bereits kennen, damit die Schaltung im Rahmen des
Laborversuchs im Grunde verstanden werden kann. Aus dieser
Rahmenbedingung folgt die Auswahl der spezifischen VCO-Schaltung.

Die Platine soll zudem relativ groß ausgelegt werden und es sollen
möglichst bedrahtete Bauteile verwendet werden. In dem Laborversuch soll
ebenfalls die Kennlinie des FM-Modulators aufgenommen werden. Hierfür
ist ein integrierter einstellbarer Spannungsteiler vorgesehen, der über
einen Drehregler auf der Platine eingestellt werden soll.

Die Schaltung soll ebenfalls Stabil gegenüber Schwankungen in der
Versorgungsspannung und somit in der Ausgangsfrequenz ausgelegt sein.
Anschlüsse für die im Laborversuch verwendeten Geräte wie das
Oszilloskop und dem Spektrumanalysator sollen über SMA- oder
BNC-Anschlüsse geschehen.

# Technische Spezifikationen (Kundenanforderungen)

- **Mittenfrequenz ($f_0$):** $5,5~\text{MHz}$ (Zwischenfrequenz / ZF)
  bei einer Steuerspannung von $0~\text{V}$.

- **Linearer Modulationsbereich:** $\pm 0,5~\text{MHz}$ (Frequenzhub)
  bei einer Steuerspannung von $\pm 0,5~\text{V}$.

  - *Arbeitsbereich:* $5,0~\text{MHz}$ bis $6,0~\text{MHz}$ linear im
    Spannungsbereich von $-0,5~\text{V}$ bis $+0,5~\text{V}$.

- **Frequenzstabilität:** Es darf keine Frequenzverschiebung (Drift)
  durch thermische oder externe Einflüsse auftreten.

- **Systemimpedanz:** Ein- und Ausgangswiderstand müssen exakt
  $50~\Omega$ betragen.

- **Steckverbinder:** Ein- und Ausgänge sind als **SMA-** oder
  **BNC-Buchsen** auszuführen.

- **Schaltungsarchitektur:** Einfacher, leicht zu verstehender und
  nachvollziehbarer Aufbau (diskreter Bauelemente).

- **Spannungsversorgung:** Integrierte Stabilisierung und Filterung der
  Versorgungsspannung zur Rauschunterdrückung.

- **Manuelle Steuerung:** Integrierter Spannungsteiler mit einem
  analogen Drehknopf (Potentiometer) zur Frequenzeinstellung.

- **Platinedesign:** Relativ große, robuste und mechanisch
  unempfindliche Leiterplatte.

- **Bestückungstechnologie:** Ausschließlich **stehende, bedrahtete
  Bauteile** für optimale Zugänglichkeit (keine SMD-Bauteile).

# Designverlauf

## Grundlegender VCO

Zuerst wurde im Design angefangen ein passendes VCO-Modell nach den
Anforderungen auszusuchen. Als Modell haben wurde sich für den LC-VCO
entschieden. Dieser besteht im Grunde aus einer RLC-Schaltung und einer
kreuzgekoppelten Mosfet-Schaltung. Das Design ist somit gut für
Studierende aus dem 4. Semester zu verstehen und kann auch gut mit
bedrahteten Bauteilen aufgebaut werden. Die Grundschaltung ist in
<a href="#fig-circuit" class="quarto-xref">Abbildung 1</a> zu sehen:

<div id="fig-circuit">

<img src=".\images/circuit.png" style="width:40.0%" />

Abbildung 1: VCO-Grundschaltung

</div>

In der Grundschaltung sind im oberen Bereich die beiden Induktivitäten
$L1$ und $L2$ in doppelter Ausführung zu sehen, da die
Versorgungsspannung mittig angeschlossen werden muss, um die Symmetrie
der Schaltung gewärleisten zu können. Weiter unten ist der einstellbare
Kondensator $C1$ zu sehen, dessen Wert die Schwingung der Schaltung
maßgeblich beeinflusst. Durch die Änderung des Kondensator ändert sich
auch die Frequenz $f_0$ der Schaltung. Somit kann duch eine gesteuerte
Änderung der Kapazität die Frequenz der Schwingung eingestellt werden.
Das ist das Grundprinzip des VCO´s und die Funktionsweise der
FM-Modulation. Der Widerstand $R1$ vervollständigt den RLC-Schwingkreis.
Die beiden kreugekoppelten Mosfets sind für die ständige Anregung der
Schwingung zuständig. Durch die ständige Änderung der gesamt Impedanz
des Schwingkreises ändert sich jeweils der Strom, der durch die Mosfets
am Gate Eingang anliegt. Diese Änderung bewirkt eine Rückgekoppelte
Schleife, durch welche schwingt das System dauerhaft. Nach
Implementierung dieser Schaltung in KiCad, NG- sowie LT-Spice konnte die
Funktionsweise sowie das Einstellen der Frequenz $f_0$ klarer gemacht
werden.

Im Verlauf der Entwicklung wurde sich entschieden verschiede VCO Ansätze
zu entwerfen und am Ende dem Kunden zu präsentieren. Unter den drei
Gruppen konnte sich neben dem Grund-VCO, welcher oben bereits erklärt
wurde, der Colpitts Oszillator oder der Wien-Robinson-Oszillator
ausgesucht werden. Da sich bereits im zweiten Semester ausgiebig mit der
Wien-Robinson Brücke auseinander gesetzt wurde haben wir uns für diesen
VCO entschieden, auf welchen in den nachfolgenden Kapiteln näher
eingegangen wird.

Eine Simulationsdatei ist dem Ordner
[VCO-Schwingkreis](kicad/Archiv/VCO-Schwingkreis/) zu entnehmen.

## Wien-Robinson-Oszillator

Um den Wien-Robinson-Oszillator besser verstehen zu können wurde sich
als erstes die Grundschaltung, die Wien-Robinson-Brücke, nochmals
angeschaut. Hierbei handelt es sich um eine frequenzabhängige
Wechselstrom-Messbrücke, die als sogenannte Nullbrücke konzipiert ist.
Das bedeutet, dass die Differenzspannung in der Brückendiagonale bei
einer spezifischen Resonanzfrequenz exakt
$\underset{\scriptscriptstyle\sim}{U} = 0~\text{V}$ beträgt. Ein
Schaltung ist der
<a href="#fig-wienrobbruecke" class="quarto-xref">Abbildung 2</a> zu
entnehmen.

<div id="fig-wienrobbruecke">

<img src=".\images/wien_rob_bruecke.png" style="width:70.0%" />

Abbildung 2: Wien-Robinson-Brücke
(<span class="nocase">de-academic.com</span> 2000-2026)

</div>

Wenn man nun an diese Brückendiagonale einen Operationsverstärker (OPV)
einbaut, erhält man einen aktiven Oszillator, der die
Frequenzselektivität der Brücke nutzt. Da der OPV die verschwindend
geringe Differenzspannung im Bereich der Resonanzfrequenz extrem hoch
verstärkt, reicht bereits das thermische Rauschen der Bauteile aus, um
das System resonant anzuregen. Somit erhält man einen sich selber
anwingenden Oszillator. Diese Wien-Robinson-Oszillator Schaltung ist
eine der meistgenutzen Schaltungen einer Wien-Robinson-Brücke und bietet
somit eine gute Grundlage des VCO’s. Für die ersten Tests mit dem
Wien-Robinson-Oszillator wurde die Seite des Elektroniktutors
herangezogen und versucht, die entsprechende Schaltung nachzustellen
(Mietke 2002-2026).

<div id="fig-wien">

<img src=".\images/wien3.png" style="width:80.0%" />

Abbildung 3: Wien-Robinson-Oszillator Schaltung (Mietke 2002-2026)

</div>

Die in <a href="#fig-wien" class="quarto-xref">Abbildung 3</a> zu
sehende Schaltung zeigt wie bereits erörtert den in der
Brückendiagonalen eingebaute Operationsverstärker und eine zusätzliche
Amplitudenregulierung. Durch die starke Anregung der Schwingung des
OPV’s wurde hier noch eine Amplitudenregelung eingebaut, welche aus
einem Potentiometer und zwei entgegengeschalteten Varktordioden besteht.
Ohne diese Amplitudenregelung würde die Schwingung aufgrund der
unendlichen Verstärkung des OPV schnell bis an die Grenzen der
Versorgungsspannung anwachsen und begrenzen, was zu starken Verzerrungen
des Sinussignals führen würde. Die Regelung sorgt dafür, dass sich ein
stabiler, verzerrungsfreier Dauerschwingzustand einstellt.

Nachdem nun diese Schaltung erfolgreich in KiCAD, erst auf der
ursprünglichen Resonanzfrequenz $f_0=1592~\text{Hz}$ und anschließend
mit Änderung des OPV’s (LT7171) auf die gewünschten $5,5~\text{MHz}$,
umgesetzt wurde, konnte sich um den geforderten Frequenzhub von
$\Delta f=1~\text{MHz}$ bei einer Steuerspannungsänderung von
$U_{str}=\pm 0,5~\text{V}$ gemacht werden. Für den ersten Entwurf wurden
nun Varaktoren parallel zu den beiden Kondensatoren $C$ geschaltet.

Nach umsetzen dieser Schaltung haben sich jedoch zwei Probleme
kristallisiert. Zum einen kamen in den verschiedenen Simulationen (KiCAD
bzw. NG-Spice und LT-Spice) unterschiede Ergebnisse heraus, und zum
anderen war es nicht möglich die Kennlinie der Resonanzfrequenz $f_0$
über die Steuerspannung $U_{str}$ linear zu bekommen. Nach vielen
vergeblichen Versuchen wurde sich dann dazu entschieden den kompletten
Aufbau neu aufzusetzen und eine andere Schaltung zu verwenden.

## Wien-Robinson VCO

Die nachfolgende Schaltung in
<a href="#fig-wien-vco" class="quarto-xref">Abbildung 4</a> ist die
verwendete Schaltung für den Wie-Brücken-VCO. Am Anfang auf der linken
Seite ist die Verstärkerschaltung für die Steuerspannung der
Varaktordioden zu sehen. Diese soll die Einstellmöglichkeit für einen
Spannungsbereich zwischen $0~\text{V}$ und $1~\text{V}$ ermöglichen.
Diese Spannung geht über einen Widerstand auf die jeweiligen Kathoden
der Varaktordioden. Diese ändern ihre Kapazität in Abhängigkeit der
Steuerspannung. Der paralelle Kondensator ist hierbei für einen Offset
der Frequenz eingebaut worden und ist Teil der Wien-Brücke. Die Wien
Brücke ist in der Mitte der Schaltung zu sehen, bestehend aus insg. vier
Varaktordioden (D2-D5), zwei Kondensatoren (C1,C2) und zwei Widerständen
(R1,R2). Die Nachfolgende Verstärkerschaltung, bestehend aus U1, R3 und
R4 ist für die Verstärkung der Schwingung und aufrechterhaltung
zuständig. Die Verstärkung ist hier mit R3 und R4 auf Faktor 3
eingestellt. Die Amplitudenregelung zum Einschwingen der Schaltung ist
auf der unteren rechten Seite zu sehen. Diese besteht aus D1, C3, R5,
R7, R8 und J1. Diese Kombination regelt die Verstärkung am Anfang des
Einschwingverhalten höher als 3, damit die Schaltung in einen sicheren
Eingeschwungenen Zustand gerät. Sobald die Amplitude den eingestellten
Wert erreicht, regelt sich die Verstärkung automatisch über J1 wieder
auf 3 runter. Die Schaltung schwingt nun stabil.

<div id="fig-wien-vco">

<img src=".\images/WienVCO.png" style="width:100.0%" />

Abbildung 4: Wien-Robinson-Oszillator VCO Schaltung (Geißler u. a. 1993)

</div>

Wir haben uns speziell für diese Schaltungsart entscheiden, da die
steuerbare Amplitudenregelung anfangs bessere Ergebnisse in der
Simulation mit NGSpice und LTSpice bezüglich der linearität der
Ausgangsfrequenz bessere Ergebnisse lieferte.

## Komponenten

Um den Wien-Robinson-Oszilator im gewünschten Frequenzbereich schwingen
zu lassen, musste die Grundschaltung angepasst werden und um
entsprechende Bauteile ersetzt werden.

### Operationsverstärker

Da die Schaltung maximal bei $6~\text{MHz}$ schwingen soll muss der OPV
sowohl ultra-high-speed sein als auch eine hohe Slew-rate haben.

### Varaktordioden

Damit die Mittenfrequenz verschoben werden kann, wurden varaktoren
Parrallel zu den Kondensatoren der Wien-Robinson-Brücke geschaltet. Um
sich in einem Lineraren Berreich zu bewegen müssen die Kennlinien der
Varaktoren in dem beschalteten Berreich auch linerar sein. Zudem müssen
diese eine möglichst hohe Änderung der Kapazität in diesem Berreich
vorweisen.

### Diode

Die Diode in der rückführenden Verstärkerschaltung des VCO´s muss
ebenfalls eine sehr schnelle Schottkydiode sein, da sie ebenfalls die
Signale von maximal $6~\text{MHz}$ sperren und durchlassen soll.

### Transistor

Der Transistor muss in diesem Fall ein J-FET, also ein Transistor,
welcher ohne Spannung maxiaml Leitend ist, eingebaut werden. Dieser wird
mit einer negativen Gleichspannung versorgt und muss somit nicht
High-Speed sein.

# Charakterisierung

Nachdem nun der Aufbau und die meisten Bauteile feststanden konnte sich
mit Hilfe von LTSpice eine Simulation des Aufbaus zusammengestellt
werden. Die Simulationsdateien können dem Ordner [sim](sim/) entnommen
werden.

## Bauteilauswahl der Varaktor-Diode

Die bereitgestellte [Varaktor-Dioden-Bibliothek](kicad\spicelibs)
umfasst 30 Einzelmodelle. Um eine Diode zu identifizieren, die eine
nahezu lineare Kapazitätsänderung von $\Delta C \approx 14~\text{pF}$
über einen Steuerspannungsbereich von $V_{str} = 3~\text{V}$ aufweist,
wurde ein Capometer eingesetzt. Dieses Capometer ermöglichte die
automatisierte Auswertung der Kennlinien, um die optimale Komponente für
die geplante Schaltung festzulegen. Es wird hier bei einer linear
ansteigenden Spannung die Kapazität der Diode in einer $C(V)$-Kennline
aufgetragen, wodurch der benötigte Kapaziätsunterschied direkt abgelesen
werden kann. Die LTSpice Schematic ist [hier](sim/capometer.asc)
zufinden.

Die Analyse der Modelle ergab, dass die
[BB535/SIE](datasheets/BB535.pdf) Varaktor Diode am besten zu den
Anforderungen passt. Somit wurden alle benötigten Bauteile gefunden und
die Silumation konnte durchgeführt werden.

## Simulation den Wien-Brücken-VCO’s

Um nun die Schaltung Simulieren zu können wurde LTSpice sowie auch
NGSpice über KiCAD zur Hilfe genommen. In beiden Fällen konnte der in
<a href="#fig-wien-vco" class="quarto-xref">Abbildung 4</a> zu sehende
Schaltungsaufbau genommen werden und mit den passenden Werten sowie
Bauteilen verknüpft werden. Das Simulationsergebnis der Schaltung
([KiCAD](kicad/Wien-VCO/)) Ausgewertet mit dem
[sim_plot.py](code/sim_plot.py) Skript ist der
<a href="#fig-sim-wien-vco" class="quarto-xref">Abbildung 5</a> zu
entnehmen. Für die LTSpice sowie NGSpice Bauteile wurden folgende Werte
festgelegt:

<div class="columns" style="display: flex; align-items: center;">

<div class="column" width="45%">

| Symbol | Bauteil | Typ / Wert | Model |
|:--------|:--------|:--------|:--------|
| **U1**      | Operationsverstärker | MAX4104 |[MAX4104.lib](kicad/spicelibs/MAX4104.lib) |
| **U2**      | Operationsverstärker | TL082 |  [elk.lib](kicad/spicelibs/elk.lib) |
| **J1**      | JFET | J113 |                   [J113.lib](kicad/spicelibs/J113.lib) |
| **D1**      | Diode | 1N6263 (Schottky) |   [.model 1N6263](kicad/spicelibs/models.txt)   |
| **D2-D5**   | Kapazitätsdiode |  BB535/SIE  |  [.model BB535](kicad/spicelibs/models.txt)  |
| **C1-C2**   | WRB Kondensator | $2{,}7~\text{pF}$   | |
| **C3**      | Regelungs Kondensator | $2{,}0~\text{nF}$   | |
| **C4-C5**   | V_{str} Kondensator | $100~\text{nF}$     | |
| **R1-R2**   | WRB Widerstand | $3{,}275~\text{k}\Omega$ | |
| **R3**      | Verstärker Widerstand | $2{,}32~\text{k}\Omega$  | |
| **R4**      | Verstärker Widerstand | $1{,}2~\text{k}\Omega$   | |
| **R5**      | Regelungs Widerstand | $20~\text{k}\Omega$      | |
| **R6, R9**  | V_{str} Widerstand | $100~\text{k}\Omega$     | |
| **R7**      | Regelungs Widerstand | $1{,}0~\text{k}\Omega$   | |
| **R8**      | Regelungs Widerstand | $8{,}0~\text{k}\Omega$   | |
| **R10**     | V_{str} Widerstand | $10~\text{k}\Omega$      | |
| **R11**     | V_{str} Widerstand | $75~\text{k}\Omega$      | |
| **R12**     | V_{str} Widerstand | $50~\text{k}\Omega$      | |

</div>

</div>

<div id="fig-sim-wien-vco">

<img src=".\images/sim_wien_vco.png" style="width:100.0%" />

Abbildung 5: Simulationsergebnis mit Python Auswertung

</div>

Die in <a href="#fig-sim-wien-vco" class="quarto-xref">Abbildung 5</a>
dargestellte Simulation zeigt die vollständige Schaltung im
einstellbaren Steuerspannungsbereich von $V_{str} = 0 \dots 1~\text{V}$.
Die Auswertung umfasst drei Darstellungen:

Der obere Plot zeigt die Zeitsignale der 11 simulierten Zustände.
Hierbei lässt sich die Amplitudenstabilität der Schaltung überprüfen. Zu
sehen ist, dass die Amplitude über den gesamten Steuerspannungsbereich
sowohl im positiven als auch im negativen Bereich bei ca.
$\pm 9~\text{V}$ stabil bleibt. Die unterschiedlichen Frequenzen der
Signale sind bereits im Zeitbereich visuell erkennbar.

Um nun die Frequenzanteile genauer zu betrachten dient der untere linke
Plot, welcher die Fast Fourier Transformation (FFT) der Signale
visualisiert. Die Darstellung ermöglicht den Abgleich mit den
Kundenvorgaben für die Mittenfrequenz ($f_0 = 5,5~\text{MHz}$) sowie den
Grenzfrequenzen ($f_u = 5~\text{MHz}$ bis $f_o = 6~\text{MHz}$). Die
Analyse zeigt, dass bei einer Steuerspannung von $V_{str} = 0~\text{V}$
nahezu exakt $5~\text{MHz}$ erreicht werden. Die obere Grenzfrequenz
wird mit ca. $6,025~\text{MHz}$ nur minimal überschritten, was für eine
sehr gute Abstimmung der Schaltung spricht.

Der dritte Plot implimentiert die berechneten Peak-Frequenzen der FFT
mit der Steuerspannung. Im Idealfall entspräche die Kennlinie einer
Geraden, die exakt bei $(0~\text{V}, 5~\text{MHz})$ beginnt und bei
$(1~\text{V}, 6~\text{MHz})$ endet. Die Simulationsergebnisse bilden
diesen Verlauf sehr präzise ab. Die geringfügigen Abweichungen sind
primär auf die in LTspice bzw. NGspice hinterlegten Bauteiltoleranzen
sowie auf physikalisch notwendige Kompromisse bei der Bauteilwahl
zurückzuführen.

Zusammenfassend liegen die Simulationsergebnisse über den Erwartungen
und zeigen die Funktionalität sowie die gute Machbarkeit der zu
entwerfenden Wien-Brücken-VCO Platine.

## Fertige Platine

Im folgenden ist der Messaufbau zur Messwertaufnahme und
Charakterisierung der Schaltung zu sehen. Für die Spannungsversorgung
beider Operationsverstärker wurde enine Spannungsquelle verwendet,
welche auf $5~\text{V}$ eingestellt wurde. Die Spannung und somit die
Frequenz wurde mit einem PicoScope Oszilloskop aufgenommen.

<div id="fig-plat1">

<img src=".\images/IMG_1872%20(1).JPEG" style="width:100.0%" />

Abbildung 6: Platine 1

</div>

Die beiden weiteren Bilder zeigen die bestückte Platine. Diese umfasst
die Wie-Robinson-Brücke mit den Varaktoren und der Verstärkerschaltung
des Oszillatorteils mit Ampltitudenregelung. Die Verstärkerschaltung der
Steuerspannung wurde auf dem Breadboard aufgebaut.

Die Platine wurde mit der, sich im kicad Ordner befindlichen
PDF-Dateien, belichtet und anschließend geätzt. Im Anschluss wurden alle
Löcher gebohrt und die Platine bestückt.

<img src=".\images/IMG_1873%20(1).JPEG" id="fig-plat2"
style="width:100.0%" alt="Platine 2" />
<img src=".\images/IMG_1874%20(1).JPEG" id="fig-plat3"
style="width:100.0%" alt="Platine 3" />

### Messergenisse

Im folgenden sind die Messergebnisse des zuvor gezeigten Messaufbaus zu
sehen.

<div id="fig-test">

<img src=".\images/meas_wien_vco.png" style="width:100.0%" />

Abbildung 7: Darstellung der Messergebnisse mit Python

</div>

Das obere Diagramm zeigt die Spannung am Ausgang des VCOs. Diese bleibt
ebenfalls über den gesamten Steuerbereich konstant bei einer Amplitude
von etwa $\pm 35~\text{mV}$. Zudem ist eine leichte Verzerrung der
Schwingung zu erkennen, dies ist auf den Operationsverstärker und deren
Amplitudensteuerung zurückzuführen. Anhand des Spektrums sind ebenfalls
die Peaks im Bereich des benötigten Frequenzbereichs zu sehen. Diese
ordnen sich präzise zwischen den markierten Grenzfrequenzen von
$5,0~\text{MHz}$ und $6,0~\text{MHz}$ ein, wobei sich das Nutzsignal
bei etwa $-30~\text{dBV}$ mit einem hohen Störabstand deutlich vom
Grundrauschen abhebt. Die Kennlinie der Steuerspannung zu der
Ausgangsfrequenz zeigt ebenfalls ein deutliches lineares Verhalten, wie
bereits in der Simulation zu sehen. Der abgebildete Steuerbereich von
$0~\text{V}$ bis $1~\text{V}$ deckt den geforderten Frequenzhub
präzise ab, wobei die Kurve bei $0~\text{V}$ exakt bei
$5,0~\text{MHz}$ startet und bei $1~\text{V}$ den oberen Grenzwert von
$6,0~\text{MHz}$ erreicht

# Ordnerstruktur

``` {text}
.
├── code/
├── data/
├── datasheets/
├── images/
├── kicad/
│   ├── Archiv/
|       ├── VCO-Schwingkreis/
│   ├── footprints/
│   ├── spicelibs/
│   └── Wien-VCO/
├── report/
├── sim/
├── .gitignore
└── README.md
```

# Literaturverzeichnis

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-wienrobinsonbruecke" class="csl-entry">

<span class="nocase">de-academic.com</span>. 2000-2026.
*Wien-Robinson-Brücke*. Design Reference.
<https://de-academic.com/dic.nsf/dewiki/1507065>.

</div>

<div id="ref-geissler1993" class="csl-entry">

Geißler, Rainer, Werner Kammerloher, und Hans Werner Schneider. 1993.
*Berechnungs- und Entwurfsverfahren der Hochfrequenztechnik 1*.
Vieweg+Teubner Verlag Wiesbaden.
<https://doi.org/10.1007/978-3-322-84915-1>.

</div>

<div id="ref-wienbruecke" class="csl-entry">

Mietke, Detlef. 2002-2026. *Wien-Robinson-Oszillator*. Design Reference.
<https://www.elektroniktutor.de/signalkunde/wien_osz.html>.

</div>

</div>
