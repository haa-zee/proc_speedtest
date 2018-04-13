#!/usr/bin/env perl

my $file;
my $line;
my $count;
my $err;

open( $file, "</proc/self/stat" ) or die "Hiba";
$line = readline($file);
close($file);



for( my $i=0; $i < 10000; $i++ ){
	foreach $filename (glob("/proc/[0-9]*/stat")) {
		if( open($file, "<", $filename) ){
			$line=readline($file);
			close($file);
			$count++;
		} else {
			$err++;
		}
	}
}

printf("Count: %u\n", $count);
printf("Error: %u\n", $err);

