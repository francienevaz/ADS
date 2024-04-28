package empresa;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		int idade=10;
		float peso;
		String nome = "Mario";
		int tamanho = nome.length();
		nome = "Super " + nome;
		//System.out.printf("Idade: %d\n", idade);
		System.out.printf("Idade: " + idade);
		
		if(idade>18) {
			System.out.println("Acessoliberado");
		}
		
		for(int i=0; i<10;i++) {
			System.out.println("msg");
		}
		
		//int[] megasena = {11,34,43,22,45,17};
		int[] megasena = new int[6];
		
		
		Scanner teclado = new Scanner(System.in);
		idade = teclado.nextInt();
		System.out.printf("Idade: " + idade);
	}
}
