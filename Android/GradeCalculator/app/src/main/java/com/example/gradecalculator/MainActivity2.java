package com.example.gradecalculator;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity2 extends AppCompatActivity {


    //variables
    private EditText pointsPossible1;
    private EditText pointsPossible2;
    private EditText pointsEarned1;
    private EditText pointsEarned2;
    private EditText percentageOfGrade1;
    private EditText percentageOfGrade2;
    private TextView resultView;
    private TextView encourageView;
    private Button calcButton;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        //set variables to interface items
        pointsPossible1 = (EditText) findViewById(R.id.editTextNumber3);
        pointsPossible2 = (EditText) findViewById(R.id.editTextNumber2);
        pointsEarned1 = (EditText) findViewById(R.id.editTextNumberDecimal5);
        pointsEarned2 = (EditText) findViewById(R.id.editTextNumberDecimal3);
        percentageOfGrade1 = (EditText) findViewById(R.id.editTextNumberDecimal6);
        percentageOfGrade2 = (EditText) findViewById(R.id.editTextNumberDecimal4);
        resultView = (TextView) findViewById(R.id.resultView);
        encourageView = (TextView) findViewById(R.id.textView36);
        calcButton = findViewById(R.id.button);

        //button click listener
        calcButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                //points possible
                double pp1 = Double.parseDouble(pointsPossible1.getText().toString());
                double pp2 = Double.parseDouble(pointsPossible2.getText().toString());

                //points earned
                double pe1 = Double.parseDouble(pointsEarned1.getText().toString());
                double pe2 = Double.parseDouble(pointsEarned2.getText().toString());

                //percentage of grade
                double percent1 = Double.parseDouble(percentageOfGrade1.getText().toString());
                double percent2 = Double.parseDouble(percentageOfGrade2.getText().toString());

                //percentage of each grade type earned
                double type1Percentage = (pe1/pp1);
                double type2Percentage = (pe2/pp2);

                //points earned per grade type
                double type1PointsEarned = type1Percentage * (percent1);
                double type2PointsEarned = type2Percentage * (percent2);

                //total points earned
                double totalPointsEarned = type1PointsEarned + type2PointsEarned;

                //display results to user
                String finalResults = String.format("%.2f", totalPointsEarned);
                resultView.setText(finalResults);

                // format results text color
                if (totalPointsEarned < 59.999) {
                    resultView.setTextColor(Color.parseColor("#E74C3C"));
                    encourageView.setText("Don't give up! If you work hard, you can do this!");
                } else if (totalPointsEarned >= 59.999 && totalPointsEarned < 69.999) {
                    resultView.setTextColor(Color.parseColor("#D35400"));
                    encourageView.setText("Keep pushing! You've got this!");
                } else if (totalPointsEarned >= 69.999 && totalPointsEarned < 79.999) {
                    resultView.setTextColor(Color.parseColor("#F1C40F"));
                    encourageView.setText("You're getting there! Keep up the effort!");
                } else if (totalPointsEarned >= 79.999 && totalPointsEarned < 89.999) {
                    resultView.setTextColor(Color.parseColor("#3498DB"));
                    encourageView.setText("Great job! Keep it up!");
                } else if (totalPointsEarned >= 89.999) {
                    resultView.setTextColor(Color.parseColor("#2ECC71"));
                    encourageView.setText("Wow! You're killing it!");
                }
            }
        });
    }


}