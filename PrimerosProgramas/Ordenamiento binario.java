

public class Ordenamientobinario{

    public static void insercion(int array[]) {
        for (int i = 1; i < array.length; i++){
            int key = array[i];
            int j = Math.abs(Arrays.binarySearch(array, 0, i, key) + 1);
            System.arraycopy(array, j, array, j+1, i-j);
            array[j] = key;
        }
    }
    /* imprimimos la matriz */
   public static void imprimirArreglo(int array[]){
       for (int i=0; i < array.length; i++)
           system.out.print(array[i] + " ");
       system.out.println();
   }

   //metodo principal
   public static void main(String[] args){
       int[] array = {5, 9, 20, 54, 1, 12, 100};
       system.out.println("Matriz de ordenaciòn: ");
       imprimirArreglo(array);
       insercion(array);
       system.out.println("\n Matriz despues de ordenar: ");
       imprimirArreglo(array);
   }
}
