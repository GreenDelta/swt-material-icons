package org.openlca.swt.material.icons;

import java.io.IOException;

import org.eclipse.swt.graphics.Image;
import org.eclipse.swt.graphics.ImageData;
import org.eclipse.swt.graphics.ImageLoader;
import org.eclipse.swt.graphics.RGB;
import org.eclipse.swt.widgets.Display;

public record MaterialIcon(String name) {

  public boolean exists() {
    return MaterialIcon.class.getResource(name) != null;
  }

  public ImageData data() {
    try (var stream = MaterialIcon.class.getResourceAsStream(name)) {
      var data = new ImageLoader().load(stream);
      var imageData = data.length == 0
        ? null
        : data[0];
      return imageData;
    } catch (IOException e) {
      throw new RuntimeException("failed to load image data of " + this, e);
    }
  }

  public ImageData data(RGB color) {
    var raw = data();
    if (raw == null)
      return null;
    var data = (ImageData) raw.clone();
    for (int x = 0; x < data.width; x++) {
      for (int y = 0; y < data.height; y++) {
        data.setPixel(x, y, (color.red << 16) | (color.green << 8) | (color.blue));
      }
    }
    return data;
  }

  public Image image(Display display) {
    return new Image(display, data());
  }

  public Image image(Display display, RGB rgb) {
    return new Image(display, data(rgb));
  }

}
