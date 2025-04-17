package com.benificiary.namecheck.calculatorff4;



import org.ff4j.FF4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CalculatorService {

    @Autowired
    private FF4j ff4j;

    public int add(int a, int b) {
        if (ff4j.check("feature-add")) {
            return a + b;
        } else {
            throw new UnsupportedOperationException("Add operation is disabled");
        }
    }

    public int subtract(int a, int b) {
        if (ff4j.check("feature-subtract")) {
            return a - b;
        } else {
            throw new UnsupportedOperationException("Subtract operation is disabled");
        }
    }

    public int divide(int a, int b) {
        if (ff4j.check("feature-divide")) {
            if (b == 0) throw new ArithmeticException("Division by zero");
            return a / b;
        } else {
            throw new UnsupportedOperationException("Divide operation is disabled");
        }
    }
}
