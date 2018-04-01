#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
        ("rubyxx", "proc_speed_test.rb", "Ruby"),
        ("./proc_speed_test_C", "", "C"),
        ("./proc_speed_test_C2", "", "C2"),
        ("./proc_speed_test_Rust", "", "Rust")
    )

    for (program, parameter, comment) in tests:
        print("{}:  {} {}".format(comment, program, parameter))
        if shutil.which(program):
            print("   Executable")
        else:
            print("   Not executable")


if __name__ == "__main__":
    run_tests()