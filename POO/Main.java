import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Aluno a1 = new Aluno("Julia", 0101, 0.1, new Curso("Engenharia", 1200));

        a1.info();

        System.out.println("Pagamento: ", + a1.pagamento());       
        
    }
}