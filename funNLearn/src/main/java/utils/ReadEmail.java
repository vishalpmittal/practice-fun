package utils;

import java.util.Arrays;
import java.util.Properties;

import javax.mail.Address;
import javax.mail.Folder;
import javax.mail.Message;
import javax.mail.Session;
import javax.mail.Store;

public class ReadEmail {

    public static void main(String[] args) throws Exception {

        Properties props = new Properties();
        props.setProperty("mail.smtp.host", "smtp.gmail.com");
        props.setProperty("mail.smtp.socketFactory.port", "465");
        props.setProperty("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
        props.setProperty("mail.smtp.auth", "true");
        props.setProperty("mail.smtp.port", "465");

        Session session = Session.getDefaultInstance(props, null);
        Store store = session.getStore("imaps");
        store.connect("smtp.gmail.com", "your_email", "your_password");
        System.out.println(store);

        Folder inbox = store.getFolder("inbox");
        inbox.open(Folder.READ_ONLY);

        int messageCount = inbox.getMessageCount();
        System.out.println("Total Messages: " + messageCount);

        int endMessage = messageCount;
        int startMessage = messageCount >= 10 ? endMessage - 10 : 0;

        while (startMessage >= 0) {
            Message[] messages = inbox.getMessages(startMessage, endMessage);

            for (Message message : messages) {
                Address[] fromAdd = message.getFrom();
                for (Address add : fromAdd) {
                    String[] recruiter = add.toString().split("[<>]");
                    System.out.print(Arrays.toString(recruiter) + "  |  ");
                }
                System.out.println(message.getSubject());
            }

            endMessage -= 10;
            if (startMessage == 0)
                break;
            startMessage = endMessage - 10;
            if (startMessage < 10) {
                startMessage = 0;
            }
        }

        inbox.close(true);
        store.close();
    }
}