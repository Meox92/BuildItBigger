package com.udacity.gradle.builditbigger;

import android.content.Intent;
import android.support.test.espresso.ViewInteraction;
import android.support.test.espresso.intent.rule.IntentsTestRule;
import android.support.test.filters.LargeTest;
import android.support.test.runner.AndroidJUnit4;
import android.support.test.rule.ActivityTestRule;


import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.intent.matcher.ComponentNameMatchers.hasClassName;
import static android.support.test.espresso.intent.matcher.IntentMatchers.hasComponent;
import static android.support.test.espresso.intent.matcher.IntentMatchers.hasExtra;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.core.IsEqual.equalTo;
import static android.support.test.espresso.intent.Intents.intended;
import static org.hamcrest.core.IsNull.notNullValue;

import com.example.androidjokelibrary.JokeTellerActivity;
import com.udacity.gradle.builditbigger.EndpointsAsyncTask;


@LargeTest
@RunWith(AndroidJUnit4.class)
public class MainActivityIntentTest {
    @Rule
    public IntentsTestRule<MainActivity> mActivityTestRule = new IntentsTestRule<>(MainActivity.class);

    @Test
    public void checkIntent() {
        onView(allOf(withId(R.id.tell_joke_button))).perform(click());
        intended(hasComponent(hasClassName(JokeTellerActivity.class.getName())));
        intended(hasExtra(equalTo("JOKE"), notNullValue()));
        onView(allOf(withId(R.id.ajl_joke_textview))).check(matches(withText("This is totally a funny joke")));
    }

}
