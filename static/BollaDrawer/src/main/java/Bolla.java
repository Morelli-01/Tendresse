import com.google.gson.Gson;

import java.util.Optional;

public class Bolla {
    public String data;
    public String[] descrizioni;
    public String[] qta;
    public String[] um;
    public String[] note;
    public String lavorazione;
    public String respSpedizione;
    public String dataTrasp;
    public String aspetto;
    public destinatario dst;
    public boolean sameAddress;
    public String[] dst2;
    public String number;
    public String year;

    public static void main(String[] args) {
        Bolla bolla = new Bolla();
        bolla.data = "27/02/2023";
        bolla.descrizioni = new String[1];
        bolla.descrizioni[0] = "Filato Composizioni Diverse";
        bolla.qta = new String[1];
        bolla.qta[0] = "10";
        bolla.um = new String[1];
        bolla.um[0] = "Kg";
        bolla.note = new String[1];
        bolla.note[0] = "---";
        bolla.lavorazione = "Taglio";
        bolla.respSpedizione = "mittente";
        bolla.dataTrasp = bolla.data;
        bolla.aspetto = "visibile";
        destinatario dst = new destinatario();
        dst.setUsr("Nicola Morelli");
        dst.setRiga1("Via Giacomo Puccini 22");
        dst.setRiga2("");
        dst.setCitta("Carpi");
        dst.setProv("MO");
        dst.setCap("41012");
        dst.setPaese("Italia");
        bolla.dst = dst;
        bolla.sameAddress = true;
        bolla.dst2 = new String[1];
        bolla.number = "";
        bolla.year="2022";

        Gson gson = new Gson();
        //System.out.println(gson.toJson(bolla));
        String[] arg = new String[1];
        arg[0] = gson.toJson(bolla);
        System.out.println(arg[0]);
        publicDrawer.main(arg);

//        try {
//        } catch (Exception e) {
//            System.out.println("Error: " + e.getMessage());
//            System.out.println(e.fillInStackTrace());
//        }

    }
}
