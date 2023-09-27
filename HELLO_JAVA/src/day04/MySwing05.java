package day04;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;

public class MySwing05 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JLabel lbl;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing05 frame = new MySwing05();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 465);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl = new JLabel("출력단수:");
		lbl.setBounds(25, 29, 57, 15);
		contentPane.add(lbl);
		
		tf = new JTextField();
		tf.setText("");
		tf.setBounds(129, 26, 67, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(25, 54, 172, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(25, 87, 172, 316);
		contentPane.add(ta);
	}
	
	public void myclick() {
		int dan = Integer.parseInt(tf.getText());
		String a = "";
		
		for(int i = 1; i <= 9; i++) { 
			a += dan + " * " + i + " = " + dan*i + "\n" ; 
		}
	
		System.out.println(a);
		ta.setText(a);
	}
	
}
