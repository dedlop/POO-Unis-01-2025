/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

import javax.swing.JOptionPane;

public class App
{
	public static void main(String[] args) {
		String firstNumber = 
		    JOptionPane.showInputDialog("enter your first number");
		String secondNumber = 
		    JOptionPane.showInputDialog("enter your second number");
		    
		int number1 = Integer.parseInt( firstNumber );
		int number2 = Integer.parseInt( secondNumber );
		
		int sum = number1 + number2;
		
		JOptionPane.showMessageDialog( null, "the sum is" + sum, "Sum of two Integers", JOptionPane.PLAIN_MESSAGE);
	}
}