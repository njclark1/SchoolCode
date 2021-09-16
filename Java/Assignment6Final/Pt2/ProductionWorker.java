import java.text.DecimalFormat;

public class ProductionWorker extends Employee {
	
	//constants for day and night
	public static final int DAY_SHIFT = 1;
	public static final int NIGHT_SHIFT = 2;
	
	//declare variables
	private int shift;
	private double payRate;
	
	//constructor
	public ProductionWorker(String n, String num, String date, int sh, double rate) {
		super(n, num, date);
		shift = DAY_SHIFT;
		payRate = rate;
	}
	
	//shift setter
	public void setShift(int s)
	{
		shift = s;
	}
	
	//pay rate setter
	public void setPayRate(double r) {
		payRate = r;
	}
	
	//shift getter
	public int getShift()
	{
		return shift;
	}
	
	//pay rate getter
	public double getPayRate() {
		return payRate;
	}

	//Create output string
	public String toString() {
		DecimalFormat dollar = new DecimalFormat("#, ##0.00");
		String string = super.toString();
		string += "\nShift: ";
		if (shift == DAY_SHIFT)
			string += "Day";
		else if (shift == NIGHT_SHIFT)
			string += "Night";
		else 
			string += "Not a shift";
		string += ("\nHourly Pay Rate: $" + dollar.format(payRate));
		return string;
	}
	

}
