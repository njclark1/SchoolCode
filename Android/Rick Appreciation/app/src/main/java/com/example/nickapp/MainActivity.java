package com.example.nickapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.constraintlayout.widget.ConstraintsChangedListener;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Adapter;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.RadioGroup;
import android.widget.Spinner;
import android.widget.Toast;
import android.widget.CompoundButton.OnCheckedChangeListener;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Spinner spinner = findViewById(R.id.timesThanked);
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.thanked, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);
        spinner.setOnItemSelectedListener(this);
    }

    public void launchPageTwo(View view){
        Intent launchTwo = new Intent(this, Activity2.class);
        startActivity(launchTwo);
        Toast.makeText(this, "What a guy!", Toast.LENGTH_SHORT).show();
    }

    public void launchPageThree(View view) {
        Intent launchThree = new Intent(this, neverGonna.class);
        startActivity(launchThree);
        Toast.makeText(this, "Please Enjoy", Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        String text = parent.getItemAtPosition(position).toString();
        Toast.makeText(parent.getContext(), "Correct, he is a ten", Toast.LENGTH_SHORT).show();

    }
    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }

    public void appreciate(View view) {
        Toast.makeText(this, "Me too", Toast.LENGTH_SHORT).show();
    }
}
//test2