public class Main {

	public static void main(String[] args) {

		int x = 50, y = 100, z = x, zz = y;
		y = z; x = zz;

		System.out.println(x);
		System.out.println(y);

	}

}
