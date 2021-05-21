import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		String s1;


		System.out.println("Digite uma frase");
		s1 = sc.nextLine();
		System.out.println("Voce digitou: ");
		System.out.println(s1);
		String s1_invertida = new StringBuilder(s1).reverse().toString();
    System.out.println("palavra invertida: ");
		System.out.println(s1_invertida);

		sc.close();
	}

}
