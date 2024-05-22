import java.awt.*;
import javax.swing.*;
import manual.ManualWidget; // Adjust package name if necessary
import tracking.TrackingWidget;

class Interface {

    void create_interface() {
        JFrame frame = new JFrame();
        frame.setSize(800, 600);
        frame.setLayout(new BorderLayout()); // Set BorderLayout

        // Create panel for Enib icon and title
        JPanel iconTitlePanel = new JPanel(new FlowLayout(FlowLayout.LEFT)); // Left-aligned flow layout
        frame.getContentPane().add(iconTitlePanel, BorderLayout.NORTH);

        // Add Enib icon
        ImageIcon enibIcon = new ImageIcon("./Icons/Logo_ENIB.png");
        Image originalEnibImage = enibIcon.getImage();
        Image scaledEnibImage = originalEnibImage.getScaledInstance(100, 50, Image.SCALE_SMOOTH);
        ImageIcon scaledEnibIcon = new ImageIcon(scaledEnibImage);
        JLabel enibimageLabel = new JLabel(scaledEnibIcon);
        iconTitlePanel.add(enibimageLabel);

        // Add title
        JLabel titleText = new JLabel("Robot Controller");
        titleText.setFont(new Font("Arial", Font.BOLD, 20));
        iconTitlePanel.add(titleText);

        // Create and add stacked widgets
        StackedWidgets stackedWidgets = new StackedWidgets();
        frame.getContentPane().add(stackedWidgets.getPanel(), BorderLayout.SOUTH); // Add to SOUTH

        frame.setVisible(true);
    }

    public static void main(String[] args) {
        Interface gui = new Interface();
        gui.create_interface();
    }
}


// Stacked widgets class
class StackedWidgets {
    private JPanel panel;
    public boolean manualVisible = true;
    public boolean trackingVisible = false;

    StackedWidgets() {
        panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS)); // Set layout to vertical

        // Add first widget if firstVisible is true
        if (manualVisible) {
            ManualWidget firstWidget = new ManualWidget("First Widget");
            panel.add(firstWidget.getPanel());
        }

        // Add second widget if secondVisible is true
        if (trackingVisible) {
            TrackingWidget secondWidget = new TrackingWidget("Second Widget");
            panel.add(secondWidget.getPanel());
        }
    }

    public void setManualVisible(boolean set_visible) {
        this.manualVisible = set_visible;
    }

    public void setTrackingVisible(boolean set_visible) {
        this.trackingVisible = set_visible;
    }

    JPanel getPanel() {
        return panel;
    }
}
