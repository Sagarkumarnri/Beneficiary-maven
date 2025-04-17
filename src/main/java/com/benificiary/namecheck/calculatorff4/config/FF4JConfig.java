package com.benificiary.namecheck.calculatorff4.config;

import org.springframework.context.annotation.Bean;

import org.ff4j.FF4j;
import org.ff4j.core.Feature;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class FF4JConfig {
    @Bean
    public FF4j getFF4j() {
        FF4j ff4j = new FF4j();

        // Define features
        ff4j.createFeature(new Feature("feature-add", true));
        ff4j.createFeature(new Feature("feature-subtract", true));
        ff4j.createFeature(new Feature("feature-divide", false)); // disabled by default

        return ff4j;
    }
}
