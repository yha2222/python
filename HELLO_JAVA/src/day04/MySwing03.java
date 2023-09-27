package day04;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	
	JLabel lbl01, lbl02, lbl03, lbl04, lbl05, lbl06;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl01 = new JLabel("__");
		lbl01.setBounds(32, 52, 35, 15);
		contentPane.add(lbl01);
		
		lbl02 = new JLabel("__");
		lbl02.setBounds(99, 52, 35, 15);
		contentPane.add(lbl02);
		
		lbl03 = new JLabel("__");
		lbl03.setBounds(166, 52, 35, 15);
		contentPane.add(lbl03);
		
		lbl04 = new JLabel("__");
		lbl04.setBounds(233, 52, 35, 15);
		contentPane.add(lbl04);
		
		lbl05 = new JLabel("__");
		lbl05.setBounds(300, 52, 35, 15);
		contentPane.add(lbl05);
		
		lbl06 = new JLabel("__");
		lbl06.setBounds(367, 52, 35, 15);
		contentPane.add(lbl06);
		
		JButton btn = new JButton("로또 생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		
		btn.setBounds(32, 98, 347, 23);
		contentPane.add(btn);
	}
	
	public void myclick() {
		int[] arr = {
		             1, 2, 3, 4, 5,       6, 7, 8, 9, 10,
		             11, 12, 13, 14, 15,  16, 17, 18, 19, 20,
		             21, 22, 23, 24, 25,  26, 27, 28, 29, 30,
		             31, 32, 33, 34, 35,  36, 37, 38, 39, 40,
		             41, 42, 43, 44, 45
					};
		
		 for(int i = 0; i < 1000; i++) { 
			 int ran = (int)(Math.random()*45);
			 	int a = arr[0];
			    arr[0] = arr[ran];
			    arr[ran] = a;
		 }
		 
		 lbl01.setText(arr[0]+"");
		 lbl02.setText(arr[1]+"");
		 lbl03.setText(arr[2]+"");
		 lbl04.setText(arr[3]+"");
		 lbl05.setText(arr[4]+"");
		 lbl06.setText(arr[5]+"");
		 
	}

}
