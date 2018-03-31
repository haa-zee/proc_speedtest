#!/bin/bash

# Fordítások

CFILE=proc_speed_test_C
gcc -O2 -Wall $CFILE.c -o $CFILE

CFILE=proc_speed_test_C2
gcc -O2 -Wall $CFILE.c -o $CFILE

javac Proc_Speed_Test.java

rustc -O proc_speed_test_Rust.rs

# Fordítások vége
# Futtatások

# a time format azért ilyen, hogy az '=' kezdetű sorokat közvetlenül .csv-be tudjam menteni,
# amit aztán egy LibreOffice fel tud dolgozni
alias tm='/usr/bin/time -f "= \"%C\";%e;%S;%U;%I;%O;%c"'
shopt -s expand_aliases

echo -e "\npython 2.7(?)"
tm python ./proc_speed_test.py

echo -e "\npython 3"
tm python3 ./proc_speed_test.py

echo -e "\nruby"
tm ruby ./proc_speed_test.rb

echo -e "\npypy"
tm pypy ./proc_speed_test.py

echo -e "\njava"
tm java Proc_Speed_Test

echo -e "\nperl"
tm perl ./proc_speed_test.pl

echo -e "\nC"
tm ./proc_speed_test_C

echo -e "\nC"
tm ./proc_speed_test_C2

echo -e "\nC"
tm ./proc_speed_test_Rust

echo -e "\nLUA"
tm luajit ./proc_speed_test.lua

