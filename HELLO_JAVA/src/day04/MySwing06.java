package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.ActionEvent;
import javax.swing.SwingConstants;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
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
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 386);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(23, 29, 209, 21);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn1 = new JButton("1");
		btn1.setBounds(23, 60, 61, 23);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("2");
		btn2.setBounds(97, 60, 61, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("3");
		btn3.setBounds(173, 60, 61, 23);
		contentPane.add(btn3);
		
		JButton btn4 = new JButton("4");
		btn4.setBounds(23, 103, 61, 23);
		contentPane.add(btn4);
		
		JButton btn5 = new JButton("5");
		btn5.setBounds(97, 103, 61, 23);
		contentPane.add(btn5);
		
		JButton btn6 = new JButton("6");
		btn6.setBounds(173, 103, 61, 23);
		contentPane.add(btn6);
		
		JButton btn7 = new JButton("7");
		btn7.setBounds(23, 147, 61, 23);
		contentPane.add(btn7);
		
		JButton btn8 = new JButton("8");
		btn8.setBounds(97, 147, 61, 23);
		contentPane.add(btn8);
		
		JButton btn9 = new JButton("9");
		btn9.setBounds(173, 147, 61, 23);
		contentPane.add(btn9);
		
		JButton btn0 = new JButton("0");
		btn0.setBounds(23, 184, 61, 23);
		contentPane.add(btn0);
		
		JButton btn_call = new JButton("☎");
		btn_call.setBounds(97, 184, 135, 23);
		contentPane.add(btn_call);
		
		btn1.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
		btn2.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
		btn3.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
		btn4.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
		btn5.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
		btn6.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
		btn7.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
		btn8.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
		btn9.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
		btn0.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {myclick(e);}});
		
		btn_call.addMouseListener(new MouseAdapter() {public void mouseClicked(MouseEvent e) {mycall();}});
	}
	
	public void mycall() {
		String str_tel = tf.getText();
		JOptionPane.showMessageDialog(null, "Calling\n" + str_tel);
	}
	
	public void myclick(MouseEvent e) {
		JButton imsi = (JButton) e.getSource();
		String str_new = imsi.getText();
		String str_old = tf.getText();
		tf.setText(str_old+str_new);
	}
}
