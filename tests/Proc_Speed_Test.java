import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.*;

import java.lang.reflect.Method;

public class Proc_Speed_Test {

	
	public void run_test(){
			int ctr=0, err=0;
			Path dir;
			try {
				dir = Paths.get("/proc");

					for(int i=0; i<10000; i++){
						try {
							DirectoryStream<Path> stream = Files.newDirectoryStream( dir, "[0-9]*" );

							for(Path path : stream){
								Path path2file = path.resolve("stat");
								try ( BufferedReader br = Files.newBufferedReader( path2file ) )
								{
										String line;
										line = br.readLine();
										ctr++;
								} catch(IOException e){
									err++;
								}
							}
						} catch(Exception e) {
							System.out.println("--Error--");
							System.out.println(e);
						}
					}
					System.out.format("Count: %d%n",ctr);
					System.out.format("Error: %d%n",err);
			} catch(Exception e) { }
	}


	public static void main(String args[]){
		Proc_Speed_Test pst;
		pst=new Proc_Speed_Test();
		pst.run_test();
		
	}
}
