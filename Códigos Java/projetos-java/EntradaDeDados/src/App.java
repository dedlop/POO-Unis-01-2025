import java.util.Scanner; // Programa utiliza a classe Scanner

public class App {
    public static void main(String[] args) throws Exception {
        
        // cria uma Scanner para obter entrada da janela de comando
        Scanner input = new Scanner(System.in);

        int number1;  // primeiro número a adicionar
        int number2;  // segundo número a adicionar
        int sum;  // soma de number1 e number2

        System.out.print("Digite o primeiro número: "); // prompt
        number1 = input.nextInt(); // lê o primeiro número fornecido pelo usuário

        System.out.print("Digite o segundo número: "); // prompt
        number2 = input.nextInt();  // lê o segundo número fornecido pelo usuário

        sum = number1 + number2; // soma os números, depois armazena o total em sum

        System.out.printf("A soma é %d", sum); // exibe a soma

    }
}
