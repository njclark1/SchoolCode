package com.example.nickapp;

import androidx.appcompat.app.AppCompatActivity;

import android.net.Uri;
import android.os.Bundle;
import android.widget.MediaController;
import android.widget.VideoView;

public class neverGonna extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_never_gonna);

        //videoView
        VideoView partyView = findViewById(R.id.videoView);
        String partyPath = "android.resource://" + getPackageName() + "/" + R.raw.party;
        Uri uri = Uri.parse(partyPath);
        partyView.setVideoURI(uri);
        MediaController partyController = new MediaController(this);
        partyView.setMediaController(partyController);
        partyController.setAnchorView(partyView);
    }
}