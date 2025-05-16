import java.util.Scanner;

public class App {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Lampada lampada = new Lampada();
        int opcao;

        do {
            System.out.println("\n--- Menu da Lâmpada ---");
            System.out.println("1 - Ligar lâmpada");
            System.out.println("2 - Desligar lâmpada");
            System.out.println("3 - Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    lampada.ligar();
                    break;

                case 2:
                    lampada.desligar();
                    break;

                case 3:
                    System.out.println("Encerrando o programa...");
                    break;
            
                default:
                    System.out.println("Opção inválida. Tente novamente...");
            
            }

        } while (opcao != 3);
    }
}
