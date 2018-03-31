#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <dirent.h>

int main () {
    unsigned int errctr=0 ,ctr=0;
    char buff[10000];

    DIR *dp;
    struct dirent *ep;

    for(int j=0; j<10000; j++) {
	if ((dp = opendir ("/proc"))) {
	    while ((ep = readdir (dp))) {
		FILE *f;
		if (ep->d_name[0] > '9' || ep->d_name[0] < '0') continue; // nem számozott mappa
		char fname[1000] = "/proc/";
		strcat(fname, ep->d_name);
		strcat(fname, "/stat");
		if ((f=fopen(fname, "r"))) {
		    if (!fgets(buff, sizeof(buff), f)) {
			fprintf(stderr, "Coundn't read from file: %s\n", fname);
		    }
		    fclose(f);
		    ctr++;
		} else {
		    fprintf(stderr, "Couldn't open file: %s\n", fname);
		    errctr++;
		}
	    }
	    (void) closedir (dp);
	} else perror ("Couldn't open the directory");
    }
    printf("Count: %u\n",ctr);
    printf("Error Count: %u\n",errctr);
    return 0;
}
