import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner a  = new Scanner (System.in);
		int x = a.nextInt();
		int y = a.nextInt();
		
		
		
		if (y<45) {
			x--;
			y = y - 45 + 60;
			if (x<0)
				x = 23;
			
			
			System.out.println(x + " " + y);
		}
		else System.out.println(x + " " + (y - 45));
	}
		
}
