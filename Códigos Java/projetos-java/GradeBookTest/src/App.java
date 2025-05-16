import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        
        // cria Scanner para obter entrada a partir da janela de comando
        Scanner input = new Scanner(System.in);

        // cria um objeto GradeBook e o atribui a myGradeBook
        GradeBook myGradeBook = new GradeBook();

        // exibe valor inicial de courseName
        System.out.printf("O valor inicial de courseName é: %s\n\n", myGradeBook.getCourseName());

        // solicita e lê o nome do curso
        System.out.println("Por favor, entre com o nome do curso:");
        String theName = input.nextLine(); // lê uma linha de terxto
        myGradeBook.setCourseName(theName); // configura o nome do curso
        System.out.println(); // gera saída de uma linha em branco

        //exibe mensagem de boas-vindas depois de especificar o nome do curso
        myGradeBook.displayMessage();
    }
}
