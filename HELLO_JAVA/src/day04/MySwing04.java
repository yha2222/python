package day04;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;

public class MySwing04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf01;
	private JTextField tf02;
	private JTextField tf03;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing04 frame = new MySwing04();
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
	public MySwing04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf01 = new JTextField();
		tf01.setBounds(50, 58, 80, 21);
		contentPane.add(tf01);
		tf01.setColumns(10);
		
		tf02 = new JTextField();
		tf02.setColumns(10);
		tf02.setBounds(160, 58, 80, 21);
		contentPane.add(tf02);
		
		tf03 = new JTextField();
		tf03.setColumns(10);
		tf03.setBounds(320, 58, 80, 21);
		contentPane.add(tf03);
		
		JLabel lbl = new JLabel("+");
		lbl.setBounds(142, 61, 57, 15);
		contentPane.add(lbl);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				hap();
			}
		});
		btn.setBounds(252, 58, 57, 21);
		contentPane.add(btn);
	}

	public void hap() {
		int a = Integer.parseInt(tf01.getText());
		int b = Integer.parseInt(tf02.getText());
		int c = a + b;
		tf03.setText(c+"");
		
	}
}
