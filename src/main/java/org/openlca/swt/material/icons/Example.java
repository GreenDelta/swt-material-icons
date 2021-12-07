package org.openlca.swt.material.icons;

import org.eclipse.swt.SWT;
import org.eclipse.swt.graphics.RGB;
import org.eclipse.swt.layout.FillLayout;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.Shell;

public class Example {

  public static void main(String[] args) {
    var display = new Display();
    var shell = new Shell();
    shell.setSize(60 * 16, 500);
    shell.setLayout(new FillLayout());

    var com = new Composite(shell, SWT.NONE);
    com.setBackground(display.getSystemColor(SWT.COLOR_WHITE));
    com.setLayout(new GridLayout(60, true));

    for (var icon : MaterialIcon.values()) {
      var img = icon.image(display, new RGB(0, 121, 107));
      var label = new Label(com, SWT.NONE);
      label.setBackground(display.getSystemColor(SWT.COLOR_WHITE));
      label.setImage(img);
      label.setToolTipText(icon.name());
    }

    shell.open();

    while (!shell.isDisposed()) {
      if (!display.readAndDispatch()) {
        display.sleep();
      }
    }
    display.dispose();

  }

}
