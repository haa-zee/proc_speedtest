use std::fs;
use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;


fn main() {
    let mut cnt=0;
    let mut errcnt=0;
    for _i in 0..10000 {
	if let Ok(entries) = fs::read_dir("/proc") {
	    for entry in entries {
		if let Ok(entry) = entry {
		    let fname = entry.file_name().into_string().unwrap();
		    if fname.parse::<i32>().is_ok() {
			if let Ok(file) = File::open("/proc/".to_owned()+&fname+"/stat") {
			    let mut reader = BufReader::new(file);
			    let mut line = String::new();
			    let _len = reader.read_line(&mut line).unwrap();
			    //println!("-> {}, {}", len, line);
			    cnt += 1;
			} else {
			    errcnt += 1;
			}
		    }
		}
	    }
	}
    }
    println!("Count: {}", cnt);
    println!("Error count: {}", errcnt);
}
