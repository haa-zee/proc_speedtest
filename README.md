# proc_speedtest
Egy kis sebességteszt a /proc alatti fájlok olvasásához

Kíváncsi voltam, egy pythonban megírt monitoring program mennyire vállalható, aztán meg jött, hogy akkor ki is kéne próbálni,
hogy mennyivel gyorsabb ugyanaz C-ben.  Meglepő, hogy a jelek szerint a python3 kb. dupla ideig fut, mint akár a python2, akár
a ruby...  Ahogy az is, hogy a pypy-vel futtatott kód alig gyorsabb, mint az interpreteres verzió.
<s>De számomra a legmeglepőbb az volt, hogy a java változat, amit nem tudtam eléggé primitívre alakítani, egyedül a python3-as verziónál fut gyorsabban.</s><br>
Update: a java kód optimalizálása drasztikus javulást eredményezett.
Különösen izgalmas volt a LUA által produkált eredmény, ami a notebookomon megközelítette a C-ben írt kódok sebességét, igaz, a "szerveremen", ami egy N3150-es Celeron procival működik, már nem volt ennyire vidám a helyzet. :)
<br>

## Módosítások a környezetben
Eredetileg egy shell szkript volt az egész, amit manuálisan kellett futtatni többször, különböző logokba irányítva az outputot, majd az így készült fájlokból kibányászni a futásidőket és pl. LibreOffice-ban táblázatosítani az egészet. Ugyan a "projekt" továbbra is totálisan értelmetlen, de szórakozásból átalakítottam. Kapott egy új shell szkriptet, ami csak arra kell, hogy a python program unbuffered módban használja a stdout-ot. A python program (measure.py) intézi mostantól a futtatásokat, ha valaki, valaha még futtatni akarná :)  Van neki egy JSON formátumú konfig fájlja (proc_speed_test.json), ami két paramétert tartalmaz:
<br><br>
repeat: &lt;n&gt; - ez adja meg, hogy hányszor kell futtatni a teszteket
<br>tests: &lt;lista&gt; - ez pedig egy lista a futtatandó tesztekről.
<br>A lista formája: [ [ "futtatandó program", "paraméter", "elnevezés" ], ... ]

- "futtatandó program" - C, Rust stb. gépi kódra forduló programok esetén maga a teszt, egyéb esetben az interpreter neve, ha nincs a PATH-ban, akkor a teljes elérési úttal.
- "paraméter" - interpreteres nyelvek esetében a szkript neve, java esetében az osztályé, egyéb esetben lényegtelen
- "elnevezés" - egy komment, ami megjelenik a logokban, ezzel azonosítható, hogy mely teszt eredményeit látod.
Példa: lásd a mellékelt proc_speed_test.json fájlt! (valamivel érthetőbb, mint ez a fenti pár sor :) )
<br>

A futtató környezet kb. annyit csinál, hogy lefuttatja a repeat paraméter értékének megfelelően a teszteket. Amelyik teszt binárisa nem elérhető, azzal nem próbálkozik. Amelyik teszt hibára fut, azt törli a további futtatásokból. A logba bekerül a tesztek stdout/stderr kimenete, valamint a futások végén a tesztek futásideje, azok átlagai.
Mivel ez az egész csak magamnak készült, én meg lusta vagyok és motiválatlan, a paraméterek ellenőrzésének nagy része kimaradt, így pl. a repeat-nek meg lehet próbálni nem numerikus értéket adni. :D
<br>


## Hardver/szoftver környezet főbb jellemzői:
### Kernel: 
4.13.0-38-generic #43~16.04.1-Ubuntu SMP 
### CPU: 
<pre>
processor	: 3
vendor_id	: GenuineIntel
cpu family	: 6
model		: 78
model name	: Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz
stepping	: 3
microcode	: 0xc2
</pre>

#### Futásidők (öt futtatás átlagai, kerekítve):
- C2:      16s
- C:       18s
- LUA:     18s
- Ruby:    27s
- Perl:    24s
- Rust:    21s
- Pypy:    25s
- Python2: 31s
- Python3: 66s
- Java:    31s


<s>- C:		18s
- Java:		29s
- LUA:		18s
- Perl:		24s
- Pypy:		25s
- Python:	30s
- Python3:	65s
- Ruby:		27s
</s>


<s>Készült: 2018.03.31</s>


Köszönet tbs (LUA) és hg2ecz (C2 & Rust) huptársaknak :)



--------------------------------------------------------------------------------------------------------------------------------
### Elavult infók.<br>
Futásidők nagyjából (öt futtatás átlagai), 4.13.0-32 kernellel:
-  C: 		27s
-  Python 2.7:	41s
-  Python 3:	85s
-  Pypy:	38s
-  Ruby:	33s
-  Java:	65s 

Újabb kernellel(4.13.0-36 - rendesen felgyorsult), immár a perl is tesztelve:
-  C:		18s
-  Python 2.7:	33s
-  Python 3:	70s
-  Pypy:	25s
-  Ruby:	28s
-  Java:	55s
-  Perl:	25s

