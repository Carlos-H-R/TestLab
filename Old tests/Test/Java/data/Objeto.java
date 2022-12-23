package data;

public class Objeto{
    private String tipo;

    public Objeto(String tipo){
        this.tipo = tipo;
    }

    public String toString(){
        return tipo;
    }

    public void setTipo(String tipo){
        this.tipo = tipo;
    }
}