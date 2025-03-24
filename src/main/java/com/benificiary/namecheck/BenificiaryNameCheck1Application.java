package com.benificiary.namecheck;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class BenificiaryNameCheck1Application {



	public static void main(String[] args) {
		SpringApplication.run(BenificiaryNameCheck1Application.class, args);
		FastAPILauncher fastAPILauncher=new FastAPILauncher();
		fastAPILauncher.run();
	}


}