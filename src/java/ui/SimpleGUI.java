package java.ui;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.*;

public class SimpleGUI extends JPanel implements ActionListener 
{
   JFrame jf = null;
   JButton button;
   JButton button1;
   JLabel label1;
   
   public static void main(String[] args)
   {
      SimpleGUI mdp = new SimpleGUI();
      mdp.go();
   }
   
   public void go()
   {
      jf = new JFrame();
      jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      
      button = new JButton();
      button.setText("Change Color");
      button.addActionListener(new ColorListener());
      
      button1 = new JButton("Change text");
      button1.addActionListener(new LabelListener());
      
      label1= new JLabel("this is it");
      
      MyDrawPanel drawPanel = new MyDrawPanel();
      JLabel name = new JLabel("Vishal");
      jf.getContentPane().add(BorderLayout.NORTH, name);
      jf.getContentPane().add(BorderLayout.SOUTH, button);
      jf.getContentPane().add(BorderLayout.CENTER, drawPanel);
      jf.getContentPane().add(BorderLayout.EAST, button1);
      jf.getContentPane().add(BorderLayout.WEST, label1);
      
      Dimension d = new Dimension(500,500);      
      jf.setSize(d);
      
      jf.setVisible(true);
   }

   class LabelListener implements ActionListener
   {
      public void actionPerformed(ActionEvent arg0)
      {
         label1.setText("this was not it");
      }
   }
   
   class ColorListener implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {
         jf.repaint();
      }
   }

   @Override
   public void actionPerformed(ActionEvent e)
   {
   }
}
