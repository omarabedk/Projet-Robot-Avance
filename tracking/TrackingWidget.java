package tracking;
import javax.swing.*;

public class TrackingWidget {
    private JPanel panel;

   public TrackingWidget(String content) {
        panel = new JPanel();
        JLabel label = new JLabel(content);
        panel.add(label);
    }

    public  JPanel getPanel() {
        return panel;
    }
}
