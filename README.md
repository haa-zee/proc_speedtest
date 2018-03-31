# proc_speedtest
Egy kis sebességteszt a /proc alatti fájlok olvasásához

Kíváncsi voltam, egy pythonban megírt monitoring program mennyire vállalható, aztán meg jött, hogy akkor ki is kéne próbálni, hogy mennyivel gyorsabb ugyanaz C-ben.  Meglepő, hogy a jelek szerint a python3 kb. dupla ideig fut, mint akár a python2, akár a ruby...  Ahogy az is, hogy a pypy-vel futtatott kód alig gyorsabb, mint az interpreteres verzió.
De számomra a legmeglepőbb az volt, hogy a java változat, amit nem tudtam eléggé primitívre alakítani, egyedül a python3-as verziónál fut gyorsabban. Update: a java kód optimalizálása drasztikus javulást eredményezett.


####Kernel: 4.13.0-37-generic #42~16.04.1-Ubuntu SMP 
####CPU: 
processor	: 3
vendor_id	: GenuineIntel
cpu family	: 6
model		: 78
model name	: Intel(R) Core(TM) i5-6300U CPU @ 2.40GHz
stepping	: 3
microcode	: 0xc2


####Futásidők (öt futtatás átlagai, kerekítve):

- C:		18s
- Java:		29s
- LUA:		18s
- Perl:		24s
- Pypy:		25s
- Python:	30s
- Python3:	65s
- Ruby:		27s



Készült: 2018.03.31





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

