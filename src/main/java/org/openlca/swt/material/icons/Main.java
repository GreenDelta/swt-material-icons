package org.openlca.swt.material.icons;

import java.util.HashSet;

import org.eclipse.swt.SWT;
import org.eclipse.swt.graphics.Image;
import org.eclipse.swt.layout.FillLayout;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Shell;

public class Main {

  public static void main(String[] args) {
    var display = new Display();
    var shell = new Shell();
    shell.setSize(800, 500);
    shell.setLayout(new FillLayout());

    var img = MaterialIcon.LOCK.image(display);
    System.out.println(img.getImageData().data.length);

    var label = new Label(shell, SWT.NONE);
    label.setImage(img);

    var data = img.getImageData();
    var bounds = img.getBounds();
    var pixels = new HashSet<Integer>();
    var alphas = new HashSet<Integer>();
    for (int x = 0; x < bounds.width; x++) {
      for (int y = 0; y < bounds.height; y++) {
        var pixel = data.getPixel(x, y);
        data.setPixel(x, y, (140 << 16) | (20 << 8) | 74);
        var alpha = data.getAlpha(x, y);
        pixels.add(pixel);
        alphas.add(alpha);
      }
    }

    var img2 = new Image(display, data);
    var label2 = new Label(shell, SWT.NONE);
    label2.setImage(img2);

    System.out.println(pixels);
    System.out.println(alphas);
    System.out.println(bounds);

    shell.open();


    while (!shell.isDisposed()) {
      if (!display.readAndDispatch()) {
        display.sleep();
      }
    }
    display.dispose();

  }


}
