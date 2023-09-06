

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class dbConn {
    List<destinatario> destinatari = new ArrayList<>();

    public List<destinatario> getCredentials() {
        return destinatari;
    }

    public List<String> getUsrList() {
        List<String> users = new ArrayList<>();
        for (destinatario dst : destinatari) {
            users.add(dst.getUsr());
        }

        return users;
    }

    public static void remAddress(destinatario dst) throws SQLException {
        Connection connection = null;
        Statement statement = null;

        DBManager.setConnection(DBManager.JDBC_Driver_MySQL, DBManager.JDBC_URL_MySQL);
        connection = DBManager.getConnection();
        statement = connection.createStatement();
        statement.executeUpdate("delete from indirizzi where Username like '"+ dst.getUsr() +"';");
        //System.out.println("inject frame:");
        //System.out.println("delete from indirizzi where Username like '"+ dst.getUsr() +"';");
    }

    public static void addAddress(destinatario dst) throws SQLException {
        Connection connection = null;
        Statement statement = null;

        DBManager.setConnection(DBManager.JDBC_Driver_MySQL, DBManager.JDBC_URL_MySQL);
        connection = DBManager.getConnection();
        statement = connection.createStatement();
        statement.executeUpdate("insert into indirizzi values(\"" + dst.getUsr() + "\", \"" +
                dst.getRiga1() + "\", \"" +
                dst.getRiga2() + "\", \"" +
                dst.getCitta() + "\", \"" +
                dst.getCap() + "\", \"" +
                dst.getProv() + "\", \"" +
                dst.getPaese() + "\"); ");
        //System.out.println("inject frame:");
        //System.out.println("insert into indirizzi values(\"" + dst.getUsr() + "\", \"" +
//                dst.getRiga1() + "\", \"" +
//                dst.getRiga2() + "\", \"" +
//                dst.getCitta() + "\", \"" +
//                dst.getCap() + "\", \"" +
//                dst.getProv() + "\", \"" +
//                dst.getPaese() + "\"); ");
    }

    public dbConn() {
        Connection connection = null;
        Statement statement = null;
        try {
            DBManager.setConnection(DBManager.JDBC_Driver_MySQL, DBManager.JDBC_URL_MySQL);
            connection = DBManager.getConnection();
            statement = connection.createStatement();

            //database di prova creato sul momento
            try {
                statement.executeQuery("SELECT * FROM Indirizzi LIMIT 1");
                //System.out.println("database ok");
            } catch (SQLException e) {
                statement.executeUpdate("DROP TABLE IF EXISTS Indirizzi");
                statement.executeUpdate("CREATE TABLE Indirizzi (Username VARCHAR(50) not null," +
                        "Riga1 varchar(50) not null, " +
                        "Riga2 varchar(50), " +
                        "Citta varchar(50) not null, " +
                        "CAP varchar(50) not null, " +
                        "prov varchar(50) not null references sigleprovincie, " +
                        "Paese varchar(50) not null, " +
                        "primary key (Username))");

            }
            ResultSet rs = statement.executeQuery("select * from Indirizzi");
            int userindex = rs.findColumn("Username");
            int riga1index = rs.findColumn("Riga1");
            int riga2index = rs.findColumn("Riga2");
            int cittaindex = rs.findColumn("Citta");
            int capindex = rs.findColumn("CAP");
            int provindex = rs.findColumn("prov");
            int paeseindex = rs.findColumn("Paese");
            while (rs.next()) {
                destinatario dst = new destinatario();
                dst.setUsr(rs.getString(userindex));
                dst.setRiga1(rs.getString(riga1index));
                dst.setRiga2(rs.getString(riga2index));
                dst.setCitta(rs.getString(cittaindex));
                dst.setCap(rs.getString(capindex));
                dst.setProv(rs.getString(provindex));
                dst.setPaese(rs.getString(paeseindex));
                this.destinatari.add(dst);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());

        } /*finally {
            if (connection != null) {
                try {
                    statement.close();
                    connection.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }

            }
        }*/
    }

    public static void main(String[] args) {
        /*dbConn C = new dbConn();
        for (destinatario dst : C.destinatari) {
            System.out.println(dst);
        }*/
        List<bollaSaved> l = new ArrayList<>();
        try {
            l = getBolle();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        for(bollaSaved bls : l){
            System.out.println(bls);
        }
    }

    public static List<bollaSaved> getBolle() throws SQLException{

        Connection connection = null;
        Statement statement = null;

        DBManager.setConnection(DBManager.JDBC_Driver_MySQL, DBManager.JDBC_URL_MySQL);
        connection = DBManager.getConnection();
        statement = connection.createStatement();

        try {
            statement.executeQuery("SELECT * FROM bolleSalvate LIMIT 1");
            //System.out.println("database ok");
        } catch (SQLException e) {
            statement.executeUpdate("DROP TABLE IF EXISTS bolleSalvate");
            statement.executeUpdate(
                    "CREATE TABLE bolleSalvate (" +
                    "numero int, " +
                    "anno int, " +
                    "primary key (numero, anno));");
        }
        ResultSet rs = statement.executeQuery("select * from bolleSalvate;");
        List<bollaSaved> bolleList = new ArrayList<>();
        int numeroIndex = rs.findColumn("numero");
        int annoIndex = rs.findColumn("anno");
        while(rs.next()){
            bollaSaved bls = new bollaSaved();
            bls.setAnno(rs.getInt(annoIndex));
            bls.setNumero(rs.getInt(numeroIndex));
            bolleList.add(bls);
        }
        Collections.sort(bolleList);
        return bolleList;
    }

    public static void addBolla(bollaSaved bls) throws SQLException {
        Connection connection = null;
        Statement statement = null;

        DBManager.setConnection(DBManager.JDBC_Driver_MySQL, DBManager.JDBC_URL_MySQL);
        connection = DBManager.getConnection();
        statement = connection.createStatement();
        statement.executeUpdate("insert into bolleSalvate values("+ bls.getNumero() +","+ bls.getAnno() +");");
       // System.out.println("frame injected:");
       // System.out.println("insert into bolleSalvate values("+ bls.getNumero() +","+ bls.getAnno() +");");

    }

    public static void remBolla(bollaSaved bls)throws SQLException{
        Connection connection = null;
        Statement statement = null;

        DBManager.setConnection(DBManager.JDBC_Driver_MySQL, DBManager.JDBC_URL_MySQL);
        connection = DBManager.getConnection();
        statement = connection.createStatement();
        System.out.println("frame injected:");
        System.out.println("delete from bolleSalvate where numero ="+ bls.getNumero() +" and anno = "+ bls.getAnno() +";");
        statement.executeUpdate("delete from bolleSalvate where numero ="+ bls.getNumero() +" and anno = "+ bls.getAnno() +";");

    }
}
