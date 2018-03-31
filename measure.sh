#!/bin/bash

alias tm='/usr/bin/time -f "= \"%C\" %e %S %U %I %O %c"'
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

echo -e "\nLUA"
tm luajit ./proc_speed_test.lua

