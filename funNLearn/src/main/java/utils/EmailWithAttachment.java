package utils;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.Reader;
import java.util.Properties;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;
import org.apache.commons.mail.DefaultAuthenticator;
import org.apache.commons.mail.EmailAttachment;
import org.apache.commons.mail.EmailException;
import org.apache.commons.mail.MultiPartEmail;

public class EmailWithAttachment {
    private static Properties props = new Properties();

    static void readProperties(String filePath) {
        InputStream input = null;
        try {
            input = new FileInputStream(filePath);

            // load a properties file
            props.load(input);
        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            if (input != null) {
                try {
                    input.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    static void sendEmail(String toFName, String toLName, String toEmail) {
        System.out.print("Sending email to " + toFName + " " + toLName + " @" + toEmail + " ");
        System.out.print(".");

        // Create the email message
        MultiPartEmail email = new MultiPartEmail();
        email.setHostName(props.getProperty("emailServer"));
        email.setSmtpPort(Integer.parseInt(props.getProperty("emailServerPort")));
        email.setAuthenticator(new DefaultAuthenticator(props.getProperty("userName"), props.getProperty("password")));
        email.setSSL(true);
        System.out.print(".");

        // Create the attachment
        EmailAttachment attachment = new EmailAttachment();
        attachment.setPath(props.getProperty("attachFile"));
        attachment.setDisposition(EmailAttachment.ATTACHMENT);
        attachment.setDescription(props.getProperty("attachDesc"));
        attachment.setName(props.getProperty("attachDesc"));
        System.out.print(".");

        try {
            email.setFrom(props.getProperty("email"), props.getProperty("name"));
            email.addTo(toEmail, toFName + " " + toLName);

            email.setSubject(props.getProperty("emailSubject"));
            email.setMsg(props.getProperty("emailContent").replaceFirst("TODO_RECEIVER", toFName));

            System.out.print(".");
            // add the attachment
            email.attach(attachment);

            System.out.print(".");
            // send the email
            email.send();

            System.out.println("done");
        } catch (EmailException e) {
            e.printStackTrace();
        }
    }

    static void sendEmails(String csvFilePath) {
        Reader in = null;
        Iterable<CSVRecord> records = null;
        try {
            in = new FileReader(csvFilePath);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        try {
            records = CSVFormat.EXCEL.withHeader().parse(in);
        } catch (IOException e) {
            e.printStackTrace();
        }
        for (CSVRecord record : records) {
            String firstName = record.get("FirstName").trim();
            firstName = firstName.substring(0, 1).toUpperCase() + firstName.substring(1).toLowerCase();
            String lastName = record.get("LastName").trim();
            lastName = lastName.substring(0, 1).toUpperCase() + lastName.substring(1).toLowerCase();
            String email = record.get("EmailID").trim();
            // System.out.println(firstName + lastName + email);
            sendEmail(firstName, lastName, email);
        }
    }

    public static void main(String[] args) {
        readProperties("src/main/java/utils/EmailWithAttachment.properties");
        // sendEmail("xyz", "Ml", "xyzml@gmail.com");
        sendEmails(props.getProperty("toEmailsCSVFile"));
    }
}
