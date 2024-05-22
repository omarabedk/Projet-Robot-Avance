package manual;
import javax.swing.*;

public class ManualWidget {
    private JPanel panel;

   public ManualWidget(String content) {
        panel = new JPanel();
        JLabel label = new JLabel(content);
        panel.add(label);
    }

    public JPanel getPanel() {
        return panel;
    }
}
