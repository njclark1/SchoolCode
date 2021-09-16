package com.example.gradecalculator;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;
import android.content.Intent;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    //intent to launch main activity 2
    public void launch2GradeTypes(View view) {
        Intent launchTwo = new Intent(this, MainActivity2.class);
        startActivity(launchTwo);
    }

    //intent to launch main activity 3
    public void launch3GradeTypes(View view) {
        Intent launchThree = new Intent(this, MainActivity3.class);
        startActivity(launchThree);
    }

    //intent to launch main activity 4
    public void launch4GradeTypes(View view) {
        Intent launchFour = new Intent(this, MainActivity4.class);
        startActivity(launchFour);
    }

    //intent to launch main activity 5
    public void launch5GradeTypes(View view) {
        Intent launchFive = new Intent(this, MainActivity5.class);
        startActivity(launchFive);
    }
}