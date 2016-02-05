package java.ui;

import java.awt.Color;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;

import javax.sound.midi.ControllerEventListener;
import javax.sound.midi.ShortMessage;
import javax.swing.*;

public class MyDrawPanel extends JPanel implements ControllerEventListener
{
   boolean msg = false;
   public void controlChange(ShortMessage event)
   {
      msg = true;
      repaint();
   }
   
   public void paintComponent(Graphics g)
   {
      if (msg)
      {
         int red = (int) (Math.random() *250);
         int green = (int) (Math.random() *250);
         int blue = (int) (Math.random() *250);
         
         g.setColor(new Color(red, green, blue));
         
         int ht = (int)((Math.random() *120) + 10);
         int width = (int) ((Math.random() * 120)+ 10);
         
         int x = (int) ((Math.random() *40 )+10);
         int y = (int) ((Math.random() *40 ) + 10);
         
         g.fillRect(x, y, ht, width);
         msg = false;
      }
   }
}
