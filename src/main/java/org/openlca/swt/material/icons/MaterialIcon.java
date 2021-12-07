package org.openlca.swt.material.icons;

import java.io.IOException;

import org.eclipse.swt.graphics.Image;
import org.eclipse.swt.graphics.ImageData;
import org.eclipse.swt.graphics.ImageLoader;
import org.eclipse.swt.widgets.Display;

public enum MaterialIcon {

  LOCK("lock.png");

  private final String file;

  MaterialIcon(String file) {
    this.file = file;
  }

  Image image(Display display) {
    return new Image(display, data());
  }

  ImageData data() {
    try (var stream = MaterialIcon.class.getResourceAsStream(file)) {
      var data = new ImageLoader().load(stream);
      return data.length == 0
        ? null
        : data[0];
    } catch (IOException e) {
      throw new RuntimeException("failed to load image data of " + this, e);
    }
  }

}
