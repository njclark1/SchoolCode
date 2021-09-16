import java.text.DecimalFormat;

public class TeamLeader extends ProductionWorker {

	private double bonusPerMonth;
	private double hoursTraining;
	private double hoursTrainingAttended;
	
	//constructor
	public TeamLeader(String n, String num, String date,  
			int sh, double rate, double MonBon, double hrTrain, double hrTrainAtt){
		super(n, num, date, sh, rate);
		bonusPerMonth = MonBon;
		hoursTraining = hrTrain;
		hoursTrainingAttended = hrTrainAtt;	
}
	
//bonus per month setter
public void setBonusPerMonth(double boPerM) {
	bonusPerMonth = boPerM;
	}

//hours training setter
public void setHoursTraining(double hTr) {
	hoursTraining = hTr;
}

//hours attended setter
public void setHoursTrainingAttended(double hTrAt) {
	hoursTrainingAttended = hTrAt;
}

//bonus per month getter
public double getBonusPerMonth()
	{
	return bonusPerMonth;
	}

//hours training getter
public double getHoursTraining() {
	return hoursTraining;
}

//hours attended getter
public double getHoursTrainingAttended() {
	return hoursTrainingAttended;
}

//output string
public String toString() {
	DecimalFormat dollar = new DecimalFormat("#, ##0.00");
	String string = super.toString();
	string += "\n Bonus Per Month: " + dollar.format(bonusPerMonth);
	string += "\n Hours Training: " + hoursTraining;
	string += "\n Hours Training Attended: " + hoursTrainingAttended;
	return string;
}

}

	