import java.util.*;

class can_win {

	static boolean solve(int arr[], int leap) {
		int i = 0;
		
		while(true) {

			boolean condition1 = false;
			boolean condition2 = false;

			if(i + leap >= arr.length) {
				return true;
			}

			if(arr[i + leap] == 0) {
				i += leap;
				condition1 = true;
			}

			else if(arr[i + 1] == 0) {
				i += 1;
				condition2 = true;
			}

			if (condition1 == false && condition2 == false) {
				return false;
			}
		}	
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		String line1 = new String();
		String line2 = new String();

		line1 = scan.nextLine();

		String[] string_input1 = line1.split(" ", 3);
		int size, leap;

		size = Integer.parseInt(string_input1[0]);
		leap = Integer.parseInt(string_input1[1]);

		line2 = scan.nextLine();
		String[] string_input2 = line2.split(" ", size);

		int array[] = new int[size];

		for(int i = 0; i < size; i++) {
			array[i] = Integer.parseInt(string_input2[i]);
		}

		String result = solve(array, leap) == true ? "YES":"NO";
		System.out.print(result);
	}
}