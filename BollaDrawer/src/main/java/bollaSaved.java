public class bollaSaved implements Comparable<bollaSaved>{
    int anno;
    int numero;

    @Override
    public String toString() {
        return "bollaSaved{" +
                "anno=" + anno +
                ", numero=" + numero +
                '}';
    }

    public int getAnno() {
        return anno;
    }

    public void setAnno(int anno) {
        this.anno = anno;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public bollaSaved(){}

    public bollaSaved(int anno, int numero) {
        this.anno = anno;
        this.numero = numero;
    }

    @Override
    public int compareTo(bollaSaved o) {
        return  o.getNumero() - this.numero;
    }
}
