import javax.swing.JFrame;
import javax.swing.JButton;
import javax.swing.JPanel;
import javax.swing.JComboBox;

public class AddOne {
    public static void main(String[]arg) {

        JButton jbtOk = new JButton("Ok");
        JButton jbtCancel = new JButton("Cancel");
        JComboBox jcbColor = new JComboBox(new String[] {"Red", "Junior", "Senior"});


        JPanel panel = new JPanel();

        panel.add(jbtCancel);
        panel.add(jbtOk);
        panel.add(jcbColor);
        
        JFrame frame = new JFrame();
        
        frame.add(panel);
        
        frame.setTitle("Window 1");
        frame.setSize(300, 200);
        frame.setLocation(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        
    }
    
}