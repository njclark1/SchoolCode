
public class Employee {
	
	// fields
	private String empName;
	private String empId;
	private String dateHired;

	//employee name setter
	public void setName(String n) {
		empName = n;
	}
	
	//employee id setter
	public void setIdNumber(String idNum) {
		empId = idNum;
	}
	
	//date hired setter
	public void setHireDate(String date) {
		dateHired = date;
	}
	
	//employee name getter 
	public String getName() {
		return empName;
	}
	
	//employee id getter
	public String getIdNumber() {
		return empId;
	}
	
	//date hired getter
	public String getHireDate() {
		return dateHired;
	}
	
	//constructor
	public Employee(String n, String idN, String date) {
		empName = n;
		empId = idN;
		dateHired = date;
	}
	
	//constructor
	public Employee() {
		empName = "";
		empId = "";
		dateHired = "";
	}
	
	//Create output string
	public String toString() {
		String string = "Name: " + empName + "\nEmployee Number: ";
		
		if (empId == "")
			string += "Invalid ID Number";
		else
			string += empId;
		string += ("\nHire Date: " + dateHired);
		return string;
	}
}