import java.text.DecimalFormat;

public class ShiftSupervisor extends Employee {

	//variables
	private double supSalary;
	private double supBonus;
	
	//constructor
	public ShiftSupervisor(String n, String num, String date, double sal, double bon) {
		super(n, num, date);
		supSalary = sal;
		supBonus = bon;
	}
	
	//salary setter
	public void setSalary(double sa)
	{
		supSalary = sa;
	}
	
	//bonus setter
	public void setBonus(double bo) {
		supBonus = bo;
	}
	
	//salary getter
	public double getSalary()
	{
		return supSalary;
	}
	
	//bonus getter
	public double getBonus() {
		return supBonus;
	}

	//Create output string
	public String toString() {
		DecimalFormat dollar = new DecimalFormat("#, ##0.00");
		String string = super.toString();
		string += "\n Salary: " + dollar.format(supSalary);
		string += "\n Bonus: " + dollar.format(supBonus);
		return string;
	}
	
}
