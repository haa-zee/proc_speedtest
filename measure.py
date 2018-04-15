#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import shlex
import shutil
import json
from typing import List, Any

PARAMETER_FILE = 'measure.json'  # type: str


def run_tests():
    # Paraméter fájl: measure.json
    # Formátum:
    # { "repeat": <n>, "tests": [["program", "paraméter", "elnevezés"], ...] }
    # repeat: hányszor kell futtatni a teszteket
    # tests: az egyes tesztek leírása lista formátumban, ahol a program a bináris vagy az interpreter, paraméter az
    #        interpreternek átadandó szkript név, illetve java jellegű program esetében az osztály neve, az elnevezés
    #        egy komment, ami alapján később azonosítani lehet az eredményeket (erre elvben jó lenne a program mező
    #        tartalma is, csak rondának találtam a ./speed_test formát.
    tests = {}
    try:
        with open(PARAMETER_FILE, 'r') as conf_file:
            config_data = json.load(conf_file)

        for (prog, param, name) in config_data["tests"]:
            # A tests dictionary-be csak azok a tesztek kerülnek be, amelyek programja futtathatónak tűnik.
            # pl. ha nincs java telepítve, akkor a java teszt kimarad. Azt sajnos nem tudtam megoldani egyszerűen,
            # hogy ha csak a paraméterként átadott szkript hiányzik, akkor is elsőre dobja ki
            if shutil.which(prog):
                cmd = shlex.split(prog + " " + param)
                tests[name] = [cmd, []]
            else:
                print("{} is missing or not executable".format(prog), file=sys.stderr)

    except Exception as e:
        print(type(e), file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(-1)

    for i in range(config_data["repeat"]):
        print("Round: {}".format(i+1))
        faulty_tests = []  # type: List[Any]
        for test_name in tests.keys():
            cmd = tests[test_name][0]
            print("  - {} ({})".format(test_name, cmd))
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # os.wait4 fontos, hogy előbb legyen, mint a proc.communicate, mert az utóbbi egyben wait is!!
            (pid, exit_code, used_resources) = os.wait4(proc.pid, 0)

            if exit_code == 0:
                tests[test_name][1].append(used_resources)
            else:
                print("Test {} failed. Exit code: {}".format(test_name, exit_code), file=sys.stderr)
                faulty_tests.append(test_name)

            (proc_out, proc_err) = proc.communicate()

            for line in proc_err.decode('utf-8').splitlines():
                print("    Test {} stderr: {}".format(test_name, line), file=sys.stderr)
            for line in proc_out.decode('utf-8').splitlines():
                print("    Test {} stdout: {}".format(test_name, line))

        for test_name in faulty_tests:
            del tests[test_name]
            print("Faulty test {} deleted".format(test_name), file=sys.stderr)

    for test_name in tests:
        print("\n\n")
        print("Test: {}".format(test_name))
        summ_ut = 0
        summ_st = 0
        for results in tests[test_name][1]:
            print("    User: {}  System: {}".format(results.ru_utime, results.ru_stime))
            summ_ut += results.ru_utime
            summ_st += results.ru_stime

        avg_ut = summ_ut/len(tests[test_name][1])
        avg_st = summ_st/len(tests[test_name][1])
        print("    U.avg: {}   S.avg: {}    Total avg: {}".format(avg_ut, avg_st, avg_ut+avg_st))


if __name__ == "__main__":
    run_tests()
    sys.exit(0)
