public class Employee {
	
	// fields
	private String name;
	private int idNumber;
	private String department;
	private String position;
	
	// constructor
	public Employee(String n, int id, String dept, String pos) {
		name = n;
		idNumber = id;
		department = dept;
		position = pos;
	}
	
	// constructor
	public Employee(String n, int id) {
		name = n;
		idNumber = id;
		department = "";
		position = "";
	}
	
	// constructor
	public Employee() {
		name = "";
		idNumber = 0;
		department = "";
		position = "";
	}

	// name setter
	public void setName(String n) {
		name = n;
	}
	
	// idNumber setter
	public void setIdNumber(int num) {
		idNumber = num;
	}
	
	// department setter
	public void setDepartment(String dept) {
		department = dept;
	}
	
	// position setter
	public void setPosition(String pos) {
		position = pos;
	}
	
	// Name getter 
	public String getName() {
		return name;
	}
	
	// idNumber getter
	public int getIdNumber() {
		return idNumber;
	}
	
	// department getter
	public String getDepartment() {
		return department;
	}
	
	// position getter
	public String getPosition() {
		return position;
	}

}