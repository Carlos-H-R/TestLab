package main;
import data.Objeto;

public class TestArray{
    public static void main(String[] args) {
        Objeto[] a = new Objeto[10];
        a[4] = new Objeto(
            "Teste"
        );
        for (int i=0; i<a.length;i++){
            System.out.println(a[i]);
        }
    }
}