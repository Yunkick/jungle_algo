import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner a  = new Scanner (System.in);
		int x = a.nextInt();
		int y = a.nextInt();
		int z = a.nextInt();
		int n = 0;
		
		n = x * 60 + y + z;
		
		x = n/60;
		y = n%60;
		
		
		if (x>=24)
			x = x - 24;
		
		System.out.println(x + " " + y);

		
	}
	
		
}
