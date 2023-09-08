import com.google.gson.Gson;

import java.nio.file.Path;
import java.nio.file.Paths;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.pdmodel.PDPageContentStream;

import java.io.File;
import java.io.IOException;
import java.sql.SQLException;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;


public class publicDrawer {
    private static final DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd/MM/yyyy");
    private static String path = System.getProperty("user.dir") + System.getProperty("file.separator") + "Bolle";

    public void saveBollaFromJson(String json) {
        Gson gson = new Gson();
        Bolla bolla = gson.fromJson(json, Bolla.class);
        saveBollaAdapter(bolla);
    }

    public void saveBollaAdapter(Bolla bolla) {
        try {
            this.saveBolla(bolla.data, bolla.descrizioni, bolla.qta, bolla.um, bolla.note, bolla.lavorazione, bolla.respSpedizione,
                    bolla.dataTrasp, bolla.aspetto, bolla.dst, bolla.sameAddress, bolla.dst2, bolla.number, bolla.year);
        } catch (IOException | SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public void saveBolla(String data,
                          String[] descrizioni, String[] qta, String[] um, String[] note, String lavorazione,
                          String respSpedizione, String dataTrasp, String aspetto, destinatario dst, boolean sameAddress,
                          String[] dst2, String number, String year) throws IOException, SQLException {

        String anno = data.substring(6);
        if (year.equals("")) {
            year = anno;
        } else {
            anno = year;
        }
        String final_anno = anno;
        List<bollaSaved> bolleList = new ArrayList<>();
        Integer num = Integer.valueOf(number);
//        if (number.equals("")) {
//            try {
//                List<bollaSaved> tmp = dbConn.getBolle();
//                if (tmp.size() == 0) {
//                    num = 1;
//                } else {
//                    tmp.forEach(bolla -> {
//                        if (String.valueOf(bolla.getAnno()).equals(final_anno)) {
//                            bolleList.add(bolla);
//                        }
//                    });
//                    if (bolleList.size() == 0) {
//                        num = 1;
//                    } else {
//                        num = bolleList.get(0).getNumero() + 1;
//                    }
//                }
//
//            } catch (SQLException e) {
//                System.out.println(e.getMessage());
//                throw new RuntimeException(e);
//            }
//        } else {
//            num = Integer.valueOf(number);
//        }


        PDDocument document = new PDDocument();
        PDPage firstPage = new PDPage();
        document.addPage(firstPage);
        String pathSeparator = File.separator;
        System.out.println(System.getProperty("user.dir") + pathSeparator + "Tendresse" + pathSeparator + "static" + pathSeparator + "images" + pathSeparator + "tendresseLogo.png");
        drawBollaDefault.addLogo(System.getProperty("user.dir") + pathSeparator + "Tendresse" + pathSeparator + "static" + pathSeparator + "images" + pathSeparator + "tendresseLogo.png", document);
//        drawBollaDefault.addLogo("/images/tendresseLogo.png", document);
        if (sameAddress) {
            drawTransportInfoSameAddress(num, document, data);
        } else {
            drawTransportInfoDifferentAddress(num, document, data, dst2);
        }
        drawBollaDefault.drawCausaleTrasporto("c/lavorazione in subfornitura", document);
        drawMerce(descrizioni.length, document, descrizioni, qta, um, note, lavorazione);
        drawFooter(document, respSpedizione, dataTrasp, aspetto);
        drawDestnatario(document, dst, sameAddress);
        createDir();
        document.save(System.getProperty("user.dir") + pathSeparator + "Tendresse" + pathSeparator + "static" + pathSeparator + "Bolle" + pathSeparator + num + "-" + year + ".pdf");
        System.out.println(System.getProperty("user.dir") + pathSeparator + "Tendresse" + pathSeparator + "static" + pathSeparator + "Bolle" + pathSeparator + num + "-" + year + ".pdf");
        document.close();
//        dbConn.addBolla(new bollaSaved(Integer.parseInt(year), num));

    }

    public void drawTransportInfoSameAddress(Integer number, PDDocument document, String data) throws IOException {
        if (document.getNumberOfPages() < 1)
            throw new IndexOutOfBoundsException();
        PDPage firstPage = document.getPage(0);
        PDPageContentStream contentStream = new PDPageContentStream(document, firstPage, PDPageContentStream.AppendMode.APPEND, false);
        int cellHeight = 15;
        int cellWidth = 250;
        int initx = 315;
        int inity = 770;
        for (int i = 0; i < 2; i++) {
            contentStream.addRect(initx, inity, cellWidth, cellHeight);
            inity -= cellHeight;
        }

        contentStream.stroke();
        contentStream.beginText();

        contentStream.setFont(drawBollaDefault.font, 12);
        contentStream.setLeading(15);
        contentStream.newLineAtOffset(320, 775);
        contentStream.showText("Documento di Trasporto");
        contentStream.newLine();
        contentStream.showText("N " + number + "/" + LocalDateTime.now().getYear() + " - " +
                data);
        contentStream.endText();

        cellHeight = 15;
        cellWidth = 250;
        initx = 315;
        inity = 740;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        inity = 680;
        cellHeight = 60;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        contentStream.stroke();

        contentStream.beginText();
        contentStream.setFont(drawBollaDefault.font, 12);
        contentStream.setLeading(15);
        contentStream.newLineAtOffset(320, 745);
        contentStream.showText("Destinatario");
        contentStream.endText();

        cellHeight = 15;
        inity = 650;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        inity -= cellHeight;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        contentStream.stroke();

        contentStream.beginText();
        contentStream.newLineAtOffset(320, 655);
        contentStream.showText("Luogo di Destinazione");
        contentStream.endText();
        contentStream.close();

    }

    public void drawTransportInfoDifferentAddress(Integer number, PDDocument document, String data, String[] destinazione) throws IOException {
        if (document.getNumberOfPages() < 1)
            throw new IndexOutOfBoundsException();
        PDPage firstPage = document.getPage(0);
        PDPageContentStream contentStream = new PDPageContentStream(document, firstPage, PDPageContentStream.AppendMode.APPEND, false);
        int cellHeight = 15;
        int cellWidth = 250;
        int initx = 315;
        int inity = 770;
        for (int i = 0; i < 2; i++) {
            contentStream.addRect(initx, inity, cellWidth, cellHeight);
            inity -= cellHeight;
        }

        contentStream.stroke();
        contentStream.beginText();

        contentStream.setFont(drawBollaDefault.font, 12);
        contentStream.setLeading(15);
        contentStream.newLineAtOffset(320, 775);
        contentStream.showText("Documento di Trasporto");
        contentStream.newLine();
        contentStream.showText("N " + number + "/" + LocalDateTime.now().getYear() + " - " +
                data);
        contentStream.endText();

        cellHeight = 15;
        cellWidth = 250;
        initx = 315;
        inity = 740;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        inity = 690;
        cellHeight = 50;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        contentStream.stroke();

        contentStream.beginText();
        contentStream.setFont(drawBollaDefault.font, 12);
        contentStream.setLeading(15);
        contentStream.newLineAtOffset(320, 745);
        contentStream.showText("Destinatario");
        contentStream.endText();

        cellHeight = 15;
        inity = 670;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        cellHeight = 50;
        inity -= cellHeight;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        contentStream.stroke();

        contentStream.beginText();
        contentStream.newLineAtOffset(320, 674);
        contentStream.setLeading(13);
        contentStream.showText("Luogo di Destinazione");
        contentStream.newLine();
        contentStream.showText(destinazione[0]);
        contentStream.newLine();
        contentStream.showText(destinazione[1]);
        contentStream.newLine();
        contentStream.showText(destinazione[2] + " - " + destinazione[3]);
        contentStream.newLine();
        contentStream.showText(destinazione[4]);


        contentStream.endText();
        contentStream.close();

    }

    public void drawMerce(int n, PDDocument document, String[] descrizioni, String[] qta, String[] um, String[] note, String lavorazione) throws IOException {
        if (document.getNumberOfPages() < 1)
            throw new IndexOutOfBoundsException();
        PDPage firstPage = document.getPage(0);
        PDPageContentStream contentStream = new PDPageContentStream(document, firstPage, PDPageContentStream.AppendMode.APPEND, false);
        int cellHeight = 30;
        int cellWidth = 300;
        int initx = 10;
        int inity = 580;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        initx += cellWidth;
        cellWidth = 50;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        initx += cellWidth;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        initx += cellWidth;
        cellWidth = 155;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        contentStream.stroke();

        contentStream.beginText();
        contentStream.setFont(drawBollaDefault.font, 15);
        contentStream.newLineAtOffset(15, 590);
        contentStream.showText("Descrizione Merce");
        contentStream.newLineAtOffset(300, 0);
        contentStream.showText("Q.ta'");
        contentStream.newLineAtOffset(50, 0);
        contentStream.showText("U.M.");
        contentStream.newLineAtOffset(50, 0);
        contentStream.showText("Note");
        contentStream.endText();

        for (int i = 0; i < n; i++) {
            initx = 10;
            cellWidth = 300;
            inity -= 30;
            contentStream.addRect(initx, inity, cellWidth, cellHeight);
            initx += cellWidth;
            cellWidth = 50;
            contentStream.addRect(initx, inity, cellWidth, cellHeight);
            initx += cellWidth;
            contentStream.addRect(initx, inity, cellWidth, cellHeight);
            initx += cellWidth;
            cellWidth = 155;
            contentStream.addRect(initx, inity, cellWidth, cellHeight);
            contentStream.stroke();
        }

        inity = 585;

        for (int i = 0; i < n; i++) {
            contentStream.beginText();
            initx = 12;
            cellWidth = 300;
            inity -= 30;
            contentStream.newLineAtOffset(initx, inity);
            contentStream.showText(descrizioni[i]);
            contentStream.newLineAtOffset(cellWidth, 0);
            contentStream.showText(qta[i]);
            cellWidth = 50;
            contentStream.newLineAtOffset(cellWidth, 0);
            contentStream.showText(um[i]);
            contentStream.newLineAtOffset(cellWidth, 0);
            contentStream.showText(note[i]);
            contentStream.endText();
        }
        inity = 580 - 30 * n;
        contentStream.close();
        drawLavorazioni(inity, document, lavorazione);
    }

    public void drawFooter(PDDocument document, String respSpedizione, String dataTrasp, String aspetto) throws IOException {
        if (document.getNumberOfPages() < 1)
            throw new IndexOutOfBoundsException();
        PDPage firstPage = document.getPage(0);
        PDPageContentStream contentStream = new PDPageContentStream(document, firstPage, PDPageContentStream.AppendMode.APPEND, false);
        int cellHeight = 40;
        int cellWidth = 185;
        int initx = 10;
        int inity = 80;

        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        initx += cellWidth;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        initx += cellWidth;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        contentStream.stroke();
        /*nomi colonne*/
        contentStream.beginText();
        contentStream.setFont(drawBollaDefault.font, 10);
        contentStream.newLineAtOffset(10, 110);
        contentStream.showText("Trasporto a cura del");

        contentStream.newLineAtOffset(186, 0);
        contentStream.showText("Data inizio Trasporto");

        contentStream.newLineAtOffset(186, 0);
        contentStream.showText("Aspetto esteriore dei Beni");
        contentStream.endText();
        /*--------------*/
        /*valori colonne*/
        contentStream.setFont(drawBollaDefault.font, 15);
        contentStream.beginText();
        contentStream.newLineAtOffset(12, 90);
        contentStream.showText(respSpedizione);

        contentStream.newLineAtOffset(186, 0);
        contentStream.showText(dataTrasp);

        contentStream.newLineAtOffset(186, 0);
        contentStream.showText(aspetto);
        contentStream.endText();
        /*--------------*/
        inity -= cellHeight;
        initx = 10;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        initx += cellWidth;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        contentStream.stroke();

        contentStream.setFont(drawBollaDefault.font, 10);
        contentStream.beginText();
        contentStream.newLineAtOffset(10, 70);
        contentStream.showText("Firma Conducente");

        contentStream.newLineAtOffset(186, 0);
        contentStream.showText("Firma Destinatario");

        contentStream.newLineAtOffset(186, 5);
        contentStream.setLeading(7);
        contentStream.setFont(drawBollaDefault.font, 6);
        contentStream.showText("La merce trasportata a mezzo vettore o mittente, relativa ");
        contentStream.newLine();
        contentStream.showText("al presente documento di trasporto, è coperta da assicurazione");
        contentStream.newLine();
        contentStream.showText("furto e pertanto viaggia a rischio del mittente fino al ");
        contentStream.newLine();
        contentStream.showText("magazzino del destinatario. E' condizione indispensabile");
        contentStream.newLine();
        contentStream.showText("che ogni mancanza o manomissione venga segnalata al ");
        contentStream.newLine();
        contentStream.showText("trasportatore al momento del ritiro. Nel caso in cui non venga ");
        contentStream.newLine();
        contentStream.showText("ripettato quanto sopra, ogni responsabilità viene ");
        contentStream.newLine();
        contentStream.showText("considerata a completo carico del destinatario");
        contentStream.endText();

        contentStream.close();
    }

    public void drawDestnatario(PDDocument document, destinatario dst, boolean sameAddress) throws IOException {
        if (document.getNumberOfPages() < 1)
            throw new IndexOutOfBoundsException();
        PDPage firstPage = document.getPage(0);
        PDPageContentStream contentStream = new PDPageContentStream(document, firstPage, PDPageContentStream.AppendMode.APPEND, false);
        contentStream.beginText();
        contentStream.setLeading(12);
        contentStream.setFont(drawBollaDefault.font, 12);
        contentStream.newLineAtOffset(320, 730);
        contentStream.showText(dst.getUsr());
        contentStream.newLine();
        contentStream.showText(dst.getRiga1());
        contentStream.newLine();
        if (dst.getRiga2() != null && !dst.getRiga2().equals("") && sameAddress == true) {
            contentStream.showText(dst.getRiga2());
            contentStream.newLine();
        }
        contentStream.showText(dst.getCitta() + " - " + dst.getCap());
        contentStream.newLine();
        contentStream.showText(dst.getProv() + " - " + dst.getPaese());


        contentStream.endText();
        contentStream.close();
    }

    public void drawLavorazioni(int inity, PDDocument document, String lavorazione) throws IOException {
        if (document.getNumberOfPages() < 1)
            throw new IndexOutOfBoundsException();
        PDPage firstPage = document.getPage(0);
        PDPageContentStream contentStream = new PDPageContentStream(document, firstPage, PDPageContentStream.AppendMode.APPEND, false);
        int cellHeight = 30;
        int cellWidth = 555;
        inity -= 35;
        contentStream.addRect(10, inity, cellWidth, cellHeight);
        contentStream.stroke();
        contentStream.beginText();
        contentStream.setFont(drawBollaDefault.font, 15);
        contentStream.setLeading(30);
        contentStream.newLineAtOffset(15, inity + 10);
        contentStream.showText("Lavorazioni da Effettuare");
        contentStream.newLine();
        contentStream.showText(lavorazione);
        contentStream.endText();
        inity -= 30;
        contentStream.addRect(10, inity, cellWidth, cellHeight);
        contentStream.stroke();

        contentStream.close();
    }

    public void createDir() {
        new File(path).mkdirs();
    }

    public static void main(String[] args) {

        if (args.length < 1) {
            System.err.println("Missing Parameter");
            System.exit(1);
        }
        Gson gson = new Gson();
//
//        for (int i = 0; i < args.length; i++) {
//            System.out.println(args[i]);
//        }
        Bolla bolla = gson.fromJson(args[0], Bolla.class);

        publicDrawer drawer = new publicDrawer();
        try {
            drawer.saveBollaAdapter(bolla);
            System.out.println("Bolla successfully created and saved");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
