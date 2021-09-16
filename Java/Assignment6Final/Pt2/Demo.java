
public class Demo {

	public static void main(String[] args) {
		
		//employee output
		System.out.println("Employee Output:");
		Employee emp1 = new Employee("Biggie Cheese", "123CM", "01-01-1994");
		System.out.println(emp1);
		
		//production worker output
		System.out.println("\nProduction Worker Output:");
		ProductionWorker proWor1 = new ProductionWorker("Big Papi", "456PU", "02-02-1995", 500, 7.25);
		System.out.println(proWor1);
		
		//shift supervisor output
		System.out.println("\nShift Supervisor Output:");
		ShiftSupervisor Shifty1 = new ShiftSupervisor("Biggie Smalls", "789NK", "03-03-1996", 234, 564235);
		System.out.println(Shifty1);
		
		//team leader output
		System.out.println("\nTeam Leader Output:");
		TeamLeader Lead1 = new TeamLeader("Biggs Wedge", "101RX", "04-04-1997", 1, 150, 2300, 20, 10.00);
		System.out.println(Lead1);
	}

}
