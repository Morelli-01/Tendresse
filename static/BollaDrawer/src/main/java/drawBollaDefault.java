import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.pdmodel.PDPageContentStream;
import org.apache.pdfbox.pdmodel.font.PDFont;
import org.apache.pdfbox.pdmodel.font.PDType1Font;
import org.apache.pdfbox.pdmodel.graphics.image.PDImageXObject;

import java.io.IOException;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class drawBollaDefault {
    public static DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd/MM/yyyy");
    public static PDFont font;

    static {
        try {
            font = new PDType1Font(PDType1Font.COURIER_BOLD.getCOSObject());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    //public static PDFont newfont = new PDType1Font();
    public static void addLogo(String path, PDDocument document) throws IOException {
        if (document.getNumberOfPages()<1)
            throw new IndexOutOfBoundsException();
        PDPage firstPage = document.getPage(0);
        PDImageXObject logo = PDImageXObject.createFromFile(path, document);
        PDPageContentStream contentStream = new PDPageContentStream(document, firstPage);
        contentStream.drawImage(logo, 10,670, 240,120);

        contentStream.close();
    }
    public static void drawTransportInfo(Integer number, PDDocument document) throws IOException {
        if (document.getNumberOfPages()<1)
            throw new IndexOutOfBoundsException();
        PDPage firstPage = document.getPage(0);
        PDPageContentStream contentStream = new PDPageContentStream(document, firstPage, PDPageContentStream.AppendMode.APPEND, false);
        int cellHeight = 15;
        int cellWidth = 250;
        int initx = 315;
        int inity = 770;
        for(int i = 0; i<2; i++){
            contentStream.addRect(initx,inity,cellWidth,cellHeight);
            inity -= cellHeight;
        }

        contentStream.stroke();
        contentStream.beginText();

        contentStream.setFont(font, 12);
        contentStream.setLeading(15);
        contentStream.newLineAtOffset(320,775);
        contentStream.showText("Documento di Trasporto");
        contentStream.newLine();
        contentStream.showText("N "+number+"/"+ LocalDateTime.now().getYear()+" - "+
                dtf.format(LocalDate.now()));
        contentStream.endText();

        cellHeight = 15;
        cellWidth = 250;
        initx = 315;
        inity = 740;
        contentStream.addRect(initx,inity,cellWidth,cellHeight);
        inity =680;
        cellHeight = 60;
        contentStream.addRect(initx,inity,cellWidth,cellHeight);
        contentStream.stroke();

        contentStream.beginText();
        contentStream.setFont(font, 12);
        contentStream.setLeading(15);
        contentStream.newLineAtOffset(320,745);
        contentStream.showText("Destinatario");
        contentStream.endText();

        cellHeight=15;
        inity = 650;
        contentStream.addRect(initx,inity,cellWidth,cellHeight);
        inity -= cellHeight;
        contentStream.addRect(initx,inity,cellWidth,cellHeight);
        contentStream.stroke();

        contentStream.beginText();
        contentStream.newLineAtOffset(320,655);
        contentStream.showText("Luogo di Destinazione");
        contentStream.endText();
        contentStream.close();

    }
    public static void drawCausaleTrasporto(String input, PDDocument document) throws IOException {
        if (document.getNumberOfPages()<1)
            throw new IndexOutOfBoundsException();
        PDPage firstPage = document.getPage(0);
        PDPageContentStream contentStream = new PDPageContentStream(document, firstPage, PDPageContentStream.AppendMode.APPEND, false);
        int cellHeight = 15;
        int cellWidth = 250;
        int initx = 10;
        int inity = 650;

        contentStream.addRect(initx,inity,cellWidth,cellHeight);
        inity -= cellHeight;
        contentStream.addRect(initx,inity,cellWidth,cellHeight);
        contentStream.stroke();

        contentStream.beginText();
        contentStream.setFont(font, 12);
        contentStream.setLeading(15);
        contentStream.newLineAtOffset(13, 655);
        contentStream.showText("Causale del Trasporto");
        contentStream.newLine();
        contentStream.showText(input);
        contentStream.endText();
        contentStream.close();
    }
    public static void drawMerce(int n, PDDocument document) throws IOException {
        if (document.getNumberOfPages()<1)
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
        contentStream.setFont(font, 15);
        contentStream.newLineAtOffset(15, 590);
        contentStream.showText("Descrizione Merce");
        contentStream.newLineAtOffset(300, 0);
        contentStream.showText("Q.ta'");
        contentStream.newLineAtOffset(50, 0);
        contentStream.showText("U.M.");
        contentStream.newLineAtOffset(50, 0);
        contentStream.showText("Note");
        contentStream.endText();

        for(int i = 0; i<n; i++){
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
        contentStream.close();
        drawLavorazioni(inity, document);
    }
    public static void drawLavorazioni( int inity, PDDocument document) throws IOException {
        if (document.getNumberOfPages()<1)
            throw new IndexOutOfBoundsException();
        PDPage firstPage = document.getPage(0);
        PDPageContentStream contentStream = new PDPageContentStream(document, firstPage, PDPageContentStream.AppendMode.APPEND, false);
        int cellHeight = 30;
        int cellWidth = 555;
        inity -= 30;
        contentStream.addRect(10, inity, cellWidth, cellHeight);
        contentStream.stroke();
        contentStream.beginText();
        contentStream.setFont(font, 15);
        contentStream.newLineAtOffset(15, inity+10);
        contentStream.showText("Lavorazioni da Effettuare");
        contentStream.endText();
        inity -= 30;
        contentStream.addRect(10, inity, cellWidth, cellHeight);
        contentStream.stroke();

        contentStream.close();
    }
    public static void drawFooter(PDDocument document) throws IOException {
        if (document.getNumberOfPages()<1)
            throw new IndexOutOfBoundsException();
        PDPage firstPage = document.getPage(0);
        PDPageContentStream contentStream = new PDPageContentStream(document, firstPage, PDPageContentStream.AppendMode.APPEND, false);
        int cellHeight = 40;
        int cellWidth = 185;
        int initx = 10;
        int inity = 80;

        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        initx+=cellWidth;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        initx+=cellWidth;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        contentStream.stroke();
        contentStream.beginText();
        contentStream.setFont(font, 10);
        contentStream.newLineAtOffset(10, 110);
        contentStream.showText("Trasporto a cura del");

        contentStream.newLineAtOffset(186,0);
        contentStream.showText("Data inizio Trasporto");

        contentStream.newLineAtOffset(186,0);
        contentStream.showText("Aspetto esteriore dei Beni");
        contentStream.endText();

        inity -= cellHeight;
        initx = 10;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        initx+=cellWidth;
        contentStream.addRect(initx, inity, cellWidth, cellHeight);
        contentStream.stroke();

        contentStream.beginText();
        contentStream.newLineAtOffset(10, 70);
        contentStream.showText("Firma Conducente");

        contentStream.newLineAtOffset(186,0);
        contentStream.showText("Firma Destinatario");

        contentStream.newLineAtOffset(186,5);
        contentStream.setLeading(7);
        contentStream.setFont(font, 6);
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
//     public static void main(String[] args) throws IOException {
//         PDDocument document = new PDDocument();
//         PDPage firstPage = new PDPage();
//         document.addPage(firstPage);
//         addLogo("C:\\Users\\nicol\\Desktop\\bolle\\tendresseLogo.png", document);
//         drawTransportInfo(0, document);
//         drawCausaleTrasporto("c/lavorazione in subfornitura", document);
//         drawMerce(13, document);
//         drawFooter(document);
//         document.save("C:\\Users\\nicol\\Desktop\\bolle\\bolla.pdf");
//         document.close();
//     }
}
