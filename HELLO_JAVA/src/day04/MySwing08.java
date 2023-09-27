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

public class MySwing08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf01;
	private JTextField tf02;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing08 frame = new MySwing08();
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
	public MySwing08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 353, 442);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		JLabel lbl_mine = new JLabel("첫째별수:");
		lbl_mine.setBounds(32, 27, 57, 15);
		contentPane.add(lbl_mine);
		
		JLabel lbl_com = new JLabel("끝별수:");
		lbl_com.setBounds(32, 80, 57, 15);
		contentPane.add(lbl_com);
		
		tf01 = new JTextField();
		tf01.setBounds(124, 24, 68, 21);
		contentPane.add(tf01);
		tf01.setColumns(10);
		
		tf02 = new JTextField();
		tf02.setColumns(10);
		tf02.setBounds(124, 77, 68, 21);
		contentPane.add(tf02);
		
		JButton btn = new JButton("별그리기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(32, 122, 160, 23);
		contentPane.add(btn);
		
		ta = new JTextArea();
		ta.setBounds(32, 158, 160, 212);
		contentPane.add(ta);
	}
	
	public String getStar(int cnt) {
		String ret = "";
		for(int i = 0; i < cnt; i++) {
			ret += "*";
		}
		ret += "\n";
		return ret;
	}
	
	public void myclick() {
		String str = tf01.getText();
		String end = tf02.getText();
		
		int s = Integer.parseInt(str);
		int e = Integer.parseInt(end);
		
		String txt = "";
		
		for(int i = s; i <= e; i++) {			
			txt += getStar(i);
		}
		
		ta.setText(txt);
	}
	
}
