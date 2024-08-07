public class Pilha {
    
    private Object[] itens;
    private int topo;

    public Pilha(int quantidade) {
        itens = new Object[quantidade]; //Define o tamanho fixo
        topo = -1; // Inicializa a pilha vazia
    }

    public void push(Object valor) {
        if (isFull()) {
            throw new IllegalStateException("Pilha cheia");
        }
        topo++;
        itens[topo] = valor;
    }

    public Object pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Pilha vazia");
        }
        Object removido = itens[topo]; //Copia item do topo
        itens[topo] = null; // Libera espaço 
        topo--;
        return removido;
    }

    public Object peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Pilha vazia");
        }
        return itens[topo];
    }

    public boolean isEmpty() {
        return topo == -1;
    }

    public boolean isFull() {
        return topo == itens.length - 1;
    }
}