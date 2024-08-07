public class App {
    public static void main(String[] args) throws Exception {
        Pilha p1 = new Pilha(10);
        p1.push("olá1");
        p1.push("olá2");
        p1.push("olá3");
        System.out.println(p1.pop());
    }
}
