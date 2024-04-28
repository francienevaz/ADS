package empresa;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		ArrayList<String> nomes = new ArrayList();
		Scanner teclado = new Scanner(System.in);
		String msg;
		System.out.println("Digite quantos nomes ira inserir:");
		int total = teclado.nextInt();
		
		System.out.println("Digite os nomes:");
		for (int i = 0; i < total; i++) {
			msg = teclado.next();
			nomes.add(msg);
		}
		
		System.out.println("Ordem normal");
		for (String nome : nomes) {
			System.out.println(nome);
		}
		System.out.println("Ordem inversa");
		for (int i = total-1; i >=0; i--) {
			System.out.println(nomes.get(i));
		}
	}
	
	
	/* Versão alternativa com o reverse
	
	public static void main(String[] args) {
		ArrayList<String> nomes = new ArrayList();
		Scanner teclado = new Scanner(System.in);
		String msg;
		System.out.println("Digite quantos nomes ira inserir:");
		int total = teclado.nextInt();
		
		System.out.println("Digite os nomes:");
		for (int i = 0; i < total; i++) {
			msg = teclado.next();
			nomes.add(msg);
		}
		
		System.out.println("Ordem normal");
		System.out.println(nomes);
		Collections.reverse(nomes);
		System.out.println(nomes);
	}
	*/
	
}
