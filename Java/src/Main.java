public class Main {

    public static void SelectionSort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            int menor = i;
            for (int j = i + 1; j < array.length; j++) {
                if (array[j] < array[menor]) {
                    menor = j;
                }
            }
            if (array[menor] != array[i]) {
                int aux = array[menor];
                array[menor] = array[i];
                array[i] = aux;
            }
        }
    }

    public static void InsertionSort(int[] array) {
        for(int i = 1; i< array.length;i++) {
            int chave = array[i];
            int j = i - 1;
            while (j >= 0 && array[j] >chave) {
                array[j + 1] = array[j];
                j -= 1;
                array[j + 1] = chave;
            }
        }
    }

    private static void quickSort(int[]array, int inicio, int fim) {
        if (inicio < fim) {
            int posicaoPivo = separar(array, inicio, fim);
            quickSort(array, inicio, posicaoPivo - 1);
            quickSort(array, posicaoPivo + 1, fim);
        }
    }

    private static int separar(int[] array, int inicio, int fim) {
        int pivo = array[inicio];
        int i = inicio + 1, f = fim;
        while (i <= f) {
            if (array[i] <= pivo)
                i++;
            else if (pivo < array[f])
                f--;
            else {
                int troca = array[i];
                array[i] = array[f];
                array[f] = troca;
                i++;
                f--;
            }
        }
        array[inicio] = array[f];
        array[f] = pivo;
        return f;
    }

    public static void BubbleSort(int[] array) {
        boolean troca = true;
        int aux;
        while (troca) {
            troca = false;
            for (int i = 0; i < array.length - 1; i++) {
                if (array[i] > array[i + 1]) {
                    aux = array[i];
                    array[i] = array[i + 1];
                    array[i + 1] = aux;
                    troca = true;
                }
            }
        }
    }
    public static void main(String[] args) {
        int[] array = {10, 8, 7, 4, 3, 11, 13, 15, 10, 11, 1, 4, 7};
        BubbleSort(array);
        for(int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
    }


}