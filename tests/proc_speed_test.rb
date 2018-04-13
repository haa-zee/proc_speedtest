#!/usr/bin/env ruby -w

ctr=0
err=0

10000.times { 
	Dir.glob("/proc/[0-9]*/stat").each { |f|
		begin
			fobj=File.new(f,"r") 
			fobj.readlines		
			fobj.close
			ctr+=1
		rescue
			err+=1
		end
	}
}

printf("Count: %u\n",ctr)
printf("Error: %u\n",err)
