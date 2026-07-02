# VCO Design und Simulation
Mirco Ick, Torben Becker, Tassilo Hertling
2026-07-02

# Einleitung

In diesesm Projekt gilt es einen VCO (Voltage Controlled Oszillator) zu
designen und in Betrieb zu nehmen. Das Design soll bestimmte
Anforderungen erfüllen, damit es in einem Laborversuch als FM-Modulator
genutzt werden kann. In der Vergangenheit wurde im Laborversuch eine VCO
Schaltung mit alten und abgekündigkten Komponenten verwendet. Diese
Schaltung soll nun mit neuen und verfügbaren Komponenten erneuert
werden.

Die VCO Schaltung soll eine FM-Modulation mit einem Trägersignal bei der
Frequenz $5,5\,\text{MHz}$ durchführen und einen Modulationsbereich
zwischen $5\,\text{MHz}$ und $6\,\text{MHz}$ verwenden. Der
Einstellungsbereich soll mit $1\,\text{V}$ pro $1\,\text{MHz}$
eingestellt werden. Somit kann das zu modulierende Signal einen
Spannungsbereich von $V_{pp} = 1\,\text{V}$ haben. Die Ein- und
Ausgangsimpedanz soll $50\,\Omega$ betragen.

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

# [Technische Spezifikationen (Kundenanforderungen)](/Kundenanforderungen)

- **Mittenfrequenz ($f_0$):** $5,5\,\text{MHz}$ (Zwischenfrequenz / ZF)
  bei einer Steuerspannung von $0\,\text{V}$.

- **Linearer Modulationsbereich:** $\pm 0,5\,\text{MHz}$ (Frequenzhub)
  bei einer Steuerspannung von $\pm 0,5\,\text{V}$.

  - *Arbeitsbereich:* $5,0\,\text{MHz}$ bis $6,0\,\text{MHz}$ linear im
    Spannungsbereich von $-0,5\,\text{V}$ bis $+0,5\,\text{V}$.

- **Frequenzstabilität:** Es darf keine Frequenzverschiebung (Drift)
  durch thermische oder externe Einflüsse auftreten.

- **Systemimpedanz:** Ein- und Ausgangswiderstand müssen exakt
  $50\,\Omega$ betragen.

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

<img src=".\report/images/circuit.png" style="width:60.0%" />

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

## Wien-Robinson-Oszillator

Um den Wien-Robinson-Oszillator besser verstehen zu können wurde sich
als erstes die Grundschaltung, die Wien-Robinson-Brücke, nochmals
angeschaut. Hierbei handelt es sich um eine frequenzabhängige
Wechselstrom-Messbrücke, die als sogenannte Nullbrücke konzipiert ist.
Das bedeutet, dass die Differenzspannung in der Brückendiagonale bei
einer spezifischen Resonanzfrequenz exakt
$\underset{\scriptscriptstyle\sim}{U} = 0\,\text{V}$ beträgt. Ein
Schaltung ist der
<a href="#fig-wienrobbruecke" class="quarto-xref">Abbildung 2</a> zu
entnehmen.

<div id="fig-wienrobbruecke">

<img src=".\report/images/wien_rob_bruecke.png" style="width:70.0%" />

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

<img src=".\report/images/wien3.png" style="width:80.0%" />

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
ursprünglichen Resonanzfrequenz $f_0=1592\,\text{Hz}$ und anschließend
mit Änderung des OPV’s (LT7171) auf die gewünschten $5,5\,\text{MHz}$,
umgesetzt wurde, konnte sich um den geforderten Frequenzhub von
$\Delta f=1\,\text{MHz}$ bei einer Steuerspannungsänderung von
$U_{str}=\pm 0,5\,\text{V}$ gemacht werden. Für den ersten Entwurf
wurden nun Varaktoren parallel zu den beiden Kondensatoren $C$
geschaltet. Ein erster Versuch ist der **?@fig-wienvarak** zu
entnehemen.

**Abbildung mit Wien-Robinson-Oszillator mit Frequenzhub**

Nach umsetzen dieser Schaltung haben sich jedoch zwei Probleme
kristallisiert. Zum einen kamen in den verschiedenen Simulationen (KiCAD
bzw. NG-Spice und LT-Spice) unterschiede Ergebnisse heraus, und zum
anderen war es nicht möglich die Kennlinie der Resonanzfrequenz $f_0$
über die Steuerspannung $U_{str}$ linear zu bekommen. Nach vielen
vergeblichen Versuchen wurde sich dann dazu entschieden den kompletten
Aufbau neu aufzusetzen und eine andere Schaltung zu verwenden.

## Wien-Robinson VCO

## Komponenten

Um den Wien-Robinson-Oszilator im gewünschten Berreich zu bekommen
musste die Grundschaltung angepasst werden und entsprechende Bauteile
rausgesucht werden.

### Operationsverstärker

Da die Schaltung um $5\,\text{MHz}$ schwingen soll muss der OPV sowohl
ultra-high-speed sein als auch eine hohe Slew-rate haben.

### Varaktoren

Damit die Mittenfrequenz verschoben werden kann wurden varaktoren
Parrallel zu den Kondensatoren der Wien-Robinson-Brücke geschaltet. Um
sich in einem Lineraren Berreich zu bewegen müssen die kennlinien der
varaktoren in dem beschalteten Berreich auch linerar sein. Zudem müssen
sie eine Möglichst hohe änderung der Kapazität in diesem Berreich haben.

### Diode

?

# Charakterisierung

# Literaturverzeichnis

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-wienrobinsonbruecke" class="csl-entry">

<span class="nocase">de-academic.com</span>. 2000-2026.
*Wien-Robinson-Brücke*. Design Reference.
<https://de-academic.com/dic.nsf/dewiki/1507065>.

</div>

<div id="ref-wienbruecke" class="csl-entry">

Mietke, Detlef. 2002-2026. *Wien-Robinson-Oszillator*. Design Reference.
<https://www.elektroniktutor.de/signalkunde/wien_osz.html>.

</div>

</div>
