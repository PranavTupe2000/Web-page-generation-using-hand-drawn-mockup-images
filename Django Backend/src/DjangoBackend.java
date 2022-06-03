import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;


public class DjangoBackend {
	public static void main(String[] args) throws Exception{
		GUI gui = new GUI();
	}
}

class GUI extends JFrame implements ActionListener {
	JTextField t1,t2;
	JLabel l1,l2;
	JButton b;
	
	public GUI() throws Exception{
		t1= new JTextField(20);
		l1 =new JLabel("Project Name:");
		t2= new JTextField(20);
		l2 =new JLabel("App Name:");
		b= new JButton("Generate");
		
		add(l1);
		add(t1);
		add(l2);
		add(t2);
		add(b);
		b.addActionListener(this);
		
		setLayout(new FlowLayout());
		setVisible(true);
		setSize(250, 300);
		setDefaultCloseOperation(3);
		setTitle("Django Backend Generator");
	}
	
	public void actionPerformed(ActionEvent e) {
		String p_name = t1.getText();
		String a_name = t2.getText();
		Generate g = new Generate();
		g.generate(p_name, a_name);
	}
}
