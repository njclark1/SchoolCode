package RetailItem;

public class RetailItemDemo {

	public static void main(String[] args) {
		// Item1
		RetailItem item1 = new RetailItem();
		item1.setDescription("Jacket");
		item1.setUnitsOnHand(12);
		item1.setPrice(59.95);
		
		// Item2
		RetailItem item2 = new RetailItem();
		item2.setDescription("Designer Jeans");
		item2.setUnitsOnHand(40);
		item2.setPrice(34.95);
		
		// Item3 
		RetailItem item3 = new RetailItem();
		item3.setDescription("Shirt");
		item3.setUnitsOnHand(20);
		item3.setPrice(24.95);
	}

}
