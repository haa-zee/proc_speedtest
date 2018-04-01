#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import shlex
import shutil


def run_tests():
    # tests = a futtatandó tesztek listája
    # Az egyes elemek:
    #   1. Futtatandó bináris, ami lehet maga a teszt (C, Rust) vagy
    #      az interpreter (Python, Ruby, Lua, Java stb.)
    #   2. Paraméter(ek) a futtatandó program számára. Üres, ha a teszt bináris,
    #      a szkript, bájtkód fájl neve egyébként.
    #   3. A teszt neve, csak komment funkcióval.
    tests = (
        ("java", "Proc_Speed_Test", "Java"),
        ("luajit", "proc_speed_test.lua", "LUA"),
        ("perl", "proc_speed_test.pl", "Perl"),
        ("python", "proc_speed_test.py", "Python2"),
        ("python3", "proc_speed_test.py", "Python3"),
        ("pypy", "proc_speed_test.py", "Pypy"),
        ("ruby", "proc_speed_test.rb", "Ruby"),
        ("./proc_speed_test_C", "", "C"),
        ("./proc_speed_test_C2", "", "C2"),
        ("./proc_speed_test_Rust", "", "Rust")
    )

    tests = (("./proc_speed_test_Rust", "", "Rust"),)

    for (program, parameter, comment) in tests:
        print("{}:  {} {}".format(comment, program, parameter))

        # Ellenőrzöm, hogy a bináris megvan és végrehajtható-e, de ha szkript vagy bájtkód a futtatandó,
        # akkor a Java miatt nem tudom korrektül megoldani az input létének ellenőrzését, mert a java nem fájlnevet
        # vár, hanem az osztály nevét, amiben a main metódus szerepel (jar fájlokkal nem akarom bonyolítani az életet)
        # Ha megvan és futtatható (shutil.which nem null stringet ad vissza), akkor futtatom.
        if shutil.which(program):
            cmd = shlex.split(program + " " + parameter)
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # os.wait4 fontos, hogy előbb legyen, mint a proc.communicate, mert az utóbbi egyben wait is!!
            (pid, exit_code, used_resources) = os.wait4(proc.pid, 0)
            print("{}: {} {} {} {} {}".format(comment, exit_code,
                                              used_resources.ru_utime, used_resources.ru_stime,
                                              used_resources.ru_nvcsw, used_resources.ru_nivcsw))

            # TODO: a used_resources tartalmát gyűjteni több cikluson át és a futtatások végén kiírni az átlagokat
            # Lehet, hogy nem procedurális megközelítéssel kellene, hanem OOP alapon ezt a részét?

            (proc_out, proc_err) = proc.communicate()
            print(proc_out.decode('utf-8').splitlines())
        else:
            print("   Not executable")


if __name__ == "__main__":
    run_tests()
