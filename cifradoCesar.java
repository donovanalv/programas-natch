import java.io.IOException;
import java.util.Scanner;

public class cifradoCesar{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);

        String texto;
        int posiciones;


        System.out.println("Frase a cifrar: ");
        texto = sc.nextLine();

        System.out.print("Número de posiciones a cifrar: ");
        posiciones = sc.nextInt();

        System.out.println("Texto cifrado: "+ cifradoCesar(texto, posiciones));

    }

    public static String cifradoCesar(String texto, int codigo) {
        StringBuilder cifrado = new StringBuilder();
        codigo = codigo % 26;
        for (int i = 0; i < texto.length(); i++) {
            if (texto.charAt(i) >= 'a' && texto.charAt(i) <= 'z') {
                if ((texto.charAt(i) + codigo) > 'z') {
                    cifrado.append((char) (texto.charAt(i) + codigo - 26));
                } else {
                    cifrado.append((char) (texto.charAt(i) + codigo));
                }
            } else if (texto.charAt(i) >= 'A' && texto.charAt(i) <= 'Z') {
                if ((texto.charAt(i) + codigo) > 'Z') {
                    cifrado.append((char) (texto.charAt(i) + codigo - 26));
                } else {
                    cifrado.append((char) (texto.charAt(i) + codigo));
                }
            }
        }
        return cifrado.toString();
    }
}