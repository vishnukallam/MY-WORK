package com.example.calucator;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    double firstNumber;
    double secondNumber;
    String operator;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Buttons Numbers
        Button num0 = findViewById(R.id.numbers0);
        Button num1 = findViewById(R.id.numbers1);
        Button num2 = findViewById(R.id.numbers2);
        Button num3 = findViewById(R.id.numbers3);
        Button num4 = findViewById(R.id.numbers4);
        Button num5 = findViewById(R.id.numbers5);
        Button num6 = findViewById(R.id.numbers6);
        Button num7 = findViewById(R.id.numbers7);
        Button num8 = findViewById(R.id.numbers8);
        Button num9 = findViewById(R.id.numbers9);

        // Button On and Off
        Button on = findViewById(R.id.on);
        Button off = findViewById(R.id.off);

        // Buttons AllClear and Delete
        Button ac = findViewById(R.id.ac);
        Button del = findViewById(R.id.del);

        // Button Operators
        Button div = findViewById(R.id.div);
        Button mul = findViewById(R.id.times);
        Button sub = findViewById(R.id.minus);
        Button add = findViewById(R.id.plus);
        Button equals = findViewById(R.id.equal);
        Button dot = findViewById(R.id.dot);

        // Text Screen
        TextView screen = findViewById(R.id.screen);

        // AC resets everything
        ac.setOnClickListener(view -> {
            firstNumber = 0;
            secondNumber = 0;
            operator = "";
            screen.setText("0");
        });

        // On/Off visibility
        off.setOnClickListener(view -> screen.setVisibility(view.GONE));
        on.setOnClickListener(view -> {
            screen.setVisibility(view.VISIBLE);
            screen.setText("0");
        });

        // Append number buttons
        ArrayList<Button> num = new ArrayList<>();
        num.add(num0);
        num.add(num1);
        num.add(num2);
        num.add(num3);
        num.add(num4);
        num.add(num5);
        num.add(num6);
        num.add(num7);
        num.add(num8);
        num.add(num9);

        for (Button b : num) {
            b.setOnClickListener(view -> {
                String current = screen.getText().toString();
                if (current.equals("0")) {
                    screen.setText(b.getText().toString());
                } else {
                    screen.setText(current + b.getText().toString());
                }
            });
        }

        // Operator buttons
        ArrayList<Button> operators = new ArrayList<>();
        operators.add(div);
        operators.add(mul);
        operators.add(sub);
        operators.add(add);

        for (Button b : operators) {
            b.setOnClickListener(view -> {
                try {
                    firstNumber = Double.parseDouble(screen.getText().toString());
                    operator = b.getText().toString();
                    screen.setText(formatNumber(firstNumber) + " " + operator + " ");
                } catch (NumberFormatException e) {
                    screen.setText("ERROR");
                }
            });
        }

        // Dot (decimal point)
        dot.setOnClickListener(view -> {
            String current = screen.getText().toString();
            if (!current.endsWith(".")) {
                screen.setText(current + ".");
            }
        });

        // Delete
        del.setOnClickListener(view -> {
            String number = screen.getText().toString();
            if (number.length() > 1) {
                screen.setText(number.substring(0, number.length() - 1));
            } else {
                screen.setText("0");
            }
        });

        // Equals
        equals.setOnClickListener(view -> {
            String currentText = screen.getText().toString();
            String[] parts = currentText.split(" ");

            if (parts.length < 3) {
                screen.setText("ERROR");
                return;
            }

            try {
                firstNumber = Double.parseDouble(parts[0]);
                operator = parts[1];
                secondNumber = Double.parseDouble(parts[2]);
            } catch (Exception e) {
                screen.setText("ERROR");
                return;
            }

            double result;
            String output;

            switch (operator) {
                case "/":
                    result = firstNumber / secondNumber;
                    output = formatNumber(result);
                    break;
                case "x":
                    result = firstNumber * secondNumber;
                    output = formatNumber(result);
                    break;
                case "-":
                    result = firstNumber - secondNumber;
                    output = formatNumber(result);
                    break;
                case "+":
                    result = firstNumber + secondNumber;
                    output = formatNumber(result);
                    break;
                default:
                    output = "ERROR";
                    screen.setText(output);
                    return;
            }

            screen.setText(output);
            firstNumber = result;
        });
    }


    private String formatNumber(double num) {
        if (num == (int) num) {
            return String.valueOf((int) num);
        } else {
            return String.valueOf(num);
        }
    }
}
