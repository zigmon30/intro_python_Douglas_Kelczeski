public class d4 {

	public static void main(String[] args) {
// ex1 ##########################################################
		int x = 50, y = 100, z = x, zz = y;
		y = z; x = zz;

		System.out.println(x);
		System.out.println(y);
//###############################################################

// ex2 ##########################################################
		int w = 50, h = 70;  
		w = w + h;
		h = w - h;
		w = w - h;
		System.out.println(w);
		System.out.println(h);
//###############################################################		
	}

}
