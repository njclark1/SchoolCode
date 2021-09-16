package RetailItem;

public class RetailItem {
	
	// fields
	private String description;
	private int unitsOnHand;
	private double price;

	// constructor
	public RetailItem() {
		description = "";
		unitsOnHand = 0;
		price = 0.00;
	}
	
	// constructor
	public RetailItem(String desc, int unit, double p) {
		description = desc;
		unitsOnHand = unit;
		price = p;
	}
	
	// description setter
	public void setDescription(String desc) {
		description = desc;
	}
	
	// unitsOnHand setter
	public void setUnitsOnHand(int unit) {
		unitsOnHand = unit;
	}
	
	// unitsOnHand setter
	public void setPrice(double p) {
		price = p;
	}
	
	// description getter 
	public String getDescription() {
		return description;
	}
	
	// Units getter 
	public int getUnitsOnHand() {
		return unitsOnHand;
	}
	
	// Price getter 
	public double getPrice() {
		return price;
	}
	
}