public class Curso {
    String nome;
    double mensalidade;

    Curso(String nome, double mensalidade) {
        super();
        this.nome = nome;
        this.mensalidade = mensalidade;    
    }

    void info() {
        System.out.println("Nome do Curso: ", + nome);
        System.out.println("Valor da Mensalidade: ", + mensalidade);
    }
}