import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		int max = -1000000;
		int min = 1000000;
		Scanner sc = new Scanner (System.in);
		int n = sc.nextInt();
		int arr[] = new int[n];
		
		for (int i =0; i <n; i++) {
			arr[i] = sc.nextInt();
			
			if(arr[i] > max) {
				max = arr[i];
			}
			if(arr[i] < min) { 
				min = arr[i];
			}
		}
					
		System.out.println(min + " " + max);
					
			}		
		}	
