package com.example.androidjokelibrary;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.widget.TextView;

public class JokeTellerActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.ajl_activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);


        Intent intent = getIntent();
        String joke = intent.getStringExtra("JOKE");

        TextView textView = (TextView) findViewById(R.id.ajl_joke_textview);

        if(!joke.isEmpty()){
            textView.setText(joke);
        } else {
            textView.setText("No joke provided");
        }

    }

}

