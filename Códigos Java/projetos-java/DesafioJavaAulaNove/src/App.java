import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner input = new Scanner(System.in);

        System.out.print("Informe o raio do círculo: ");
        double raio = input.nextDouble();

        double pi = 3.14159;
        double area = pi * (raio * raio);

        System.out.printf("A área do círculo é: %.2f\n", area);

    }
}
