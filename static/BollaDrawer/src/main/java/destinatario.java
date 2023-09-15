import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class destinatario implements Iterable<String>{
    String usr, riga1, riga2, citta, cap, prov, paese;

    public String getUsr() {
        return usr;
    }

    public void setUsr(String usr) {
        this.usr = usr;
    }

    public String getRiga1() {
        return riga1;
    }

    public void setRiga1(String riga1) {
        this.riga1 = riga1;
    }

    public String getRiga2() {
        return riga2;
    }

    public void setRiga2(String riga2) {
        this.riga2 = riga2;
    }

    public String getCitta() {
        return citta;
    }

    public void setCitta(String citta) {
        this.citta = citta;
    }

    public String getCap() {
        return cap;
    }

    public void setCap(String cap) {
        this.cap = cap;
    }

    public String getProv() {
        return prov;
    }

    public void setProv(String prov) {
        this.prov = prov;
    }

    public String getPaese() {
        return paese;
    }

    public void setPaese(String paese) {
        this.paese = paese;
    }

    public destinatario(){}

    public destinatario(String usr, String riga1, String riga2, String citta, String cap, String prov, String paese) {
        this.usr = usr;
        this.riga1 = riga1;
        this.riga2 = riga2;
        this.citta = citta;
        this.cap = cap;
        this.prov = prov;
        this.paese = paese;
    }

    @Override
    public String toString() {
        return "destinatario{" +
                "usr='" + usr + '\'' +
                ", riga1='" + riga1 + '\'' +
                ", riga2='" + riga2 + '\'' +
                ", citta='" + citta + '\'' +
                ", cap='" + cap + '\'' +
                ", prov='" + prov + '\'' +
                ", paese='" + paese + '\'' +
                '}';
    }

    @Override
    public Iterator<String> iterator() {
        List<String> elements = new ArrayList<>(List.of(usr, riga1, riga2, citta, cap, prov, paese));
        return elements.iterator();
    }
}
