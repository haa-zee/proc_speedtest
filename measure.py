#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import shlex
import shutil
import json


def run_tests():

    # Paraméter fájl: proc_speed_test.json
    # Formátum:
    # { "counter": <n>, "tests": [["program", "paraméter", "elnevezés"], ...] }
    # counter: hányszor kell futtatni a teszteket
    # tests: az egyes tesztek leírása lista formátumban, ahol a program a bináris vagy az interpreter, paraméter az
    #        interpreternek átadandó szkript név, illetve java jellegű program esetében az osztály neve, az elnevezés
    #        egy komment, ami alapján később azonosítani lehet az eredményeket
    tests = []
    try:
        with open('proc_speed_test.json', 'r') as conf_file:
            config_data = json.load(conf_file)
        print("Counter: {}\n".format(config_data['counter']))
        for (prog, param, name) in config_data["tests"]:
            tests.append((prog, param, name))
        for i in tests:
            print(i)

    except Exception as e:
        print(type(e), file=sys.stderr)
        print(e.__str__(), file=sys.stderr)
        sys.exit(-1)


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
