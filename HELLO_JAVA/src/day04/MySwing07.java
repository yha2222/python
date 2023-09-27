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

public class MySwing07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_mine;
	private JTextField tf_com;
	private JTextField tf_result;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing07 frame = new MySwing07();
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
	public MySwing07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 353, 442);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		// 전역변수static 쓰면 메모리 낭비
		JLabel lbl_mine = new JLabel("나:");
		lbl_mine.setBounds(32, 27, 57, 15);
		contentPane.add(lbl_mine);
		
		JLabel lbl_com = new JLabel("컴:");
		lbl_com.setBounds(32, 80, 57, 15);
		contentPane.add(lbl_com);
		
		JLabel lbl_result = new JLabel("결과: ");
		lbl_result.setBounds(32, 128, 57, 15);
		contentPane.add(lbl_result);
		
		tf_mine = new JTextField();
		tf_mine.setBounds(124, 24, 57, 21);
		contentPane.add(tf_mine);
		tf_mine.setColumns(10);
		
		tf_com = new JTextField();
		tf_com.setColumns(10);
		tf_com.setBounds(124, 77, 57, 21);
		contentPane.add(tf_com);
		
		tf_result = new JTextField();
		tf_result.setColumns(10);
		tf_result.setBounds(124, 125, 57, 21);
		contentPane.add(tf_result);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myclick();
			}
		});
		btn.setBounds(32, 168, 149, 23);
		contentPane.add(btn);
	}
	
	private void myclick() {
		String mine = tf_mine.getText();
		String com = "";
		String result = "";
		
		double rnd = Math.random();
		if(rnd > 0.66) {
			com = "가위";
		}else if(rnd > 0.33) {
			com = "바위";
		}else {
			com = "보";
		}
		
		if(com.equals("가위") && mine.equals("가위")) result = "비김";
		if(com.equals("가위") && mine.equals("바위")) result = "이김";
		if(com.equals("가위") && mine.equals("보")) result = "짐";
		
		if(com.equals("바위") && mine.equals("가위")) result = "짐";
		if(com.equals("바위") && mine.equals("바위")) result = "비김";
		if(com.equals("바위") && mine.equals("보")) result = "이김";
		
		if(com.equals("보") && mine.equals("가위")) result = "이김";
		if(com.equals("보") && mine.equals("바위")) result = "짐";
		if(com.equals("보") && mine.equals("보")) result = "비김";
		
		tf_com.setText(com);
		tf_result.setText(result);
	};
}
