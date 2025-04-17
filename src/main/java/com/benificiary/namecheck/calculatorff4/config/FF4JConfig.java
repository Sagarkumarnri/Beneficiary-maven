package com.benificiary.namecheck.calculatorff4.config;




import org.ff4j.FF4j;
import org.ff4j.web.FF4jDispatcherServlet;
import org.ff4j.core.Feature;
import org.springframework.boot.web.servlet.ServletRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class FF4JConfig {

    @Bean
    public FF4j getFF4j() {
        FF4j ff4j = new FF4j();

        ff4j.createFeature(new Feature("feature-add", true));
        ff4j.createFeature(new Feature("feature-subtract", true));
        ff4j.createFeature(new Feature("feature-divide", false));

        return ff4j;
    }

    @Bean
    public ServletRegistrationBean<FF4jDispatcherServlet> ff4jServlet(FF4j ff4j) {
        FF4jDispatcherServlet ff4jServlet = new FF4jDispatcherServlet();
        ff4jServlet.setFf4j(ff4j);
        ServletRegistrationBean<FF4jDispatcherServlet> registration =
                new ServletRegistrationBean<>(ff4jServlet, "/ff4j-console/*");
        registration.setName("FF4jConsoleServlet");
        return registration;
    }
}
