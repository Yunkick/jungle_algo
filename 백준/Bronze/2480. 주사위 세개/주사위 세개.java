import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner a  = new Scanner (System.in);
		int x = a.nextInt();
		int y = a.nextInt();
		int z = a.nextInt();
		int n = 0;
		
		if (x==y  && y==z) {
			n = 10000 + x * 1000;
			
			System.out.println(n);
			
		}
		else if(x==y || x==z) {
			n = 1000 + x * 100;
			System.out.println(n);
		
		}
			else if (y==z) {
			n = 1000 + y * 100;
			System.out.println(n);
			}
		
		else
			System.out.println(Math.max(Math.max(x, y),z)*100);
	}
	
		
}