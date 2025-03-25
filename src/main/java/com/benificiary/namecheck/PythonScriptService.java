package com.benificiary.namecheck;

import org.springframework.stereotype.Service;
import java.io.*;

@Service
public class PythonScriptService {
    private static final String PYTHON_PATH = "python";  // Change if needed
    private static final String SCRIPT_PATH = "C:\\idea\\Beneficiary-maven\\fine_tune.py";  // Update with actual path

    public String runPythonScript( ) {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder(PYTHON_PATH, SCRIPT_PATH );
            processBuilder.redirectErrorStream(true);

            Process process = processBuilder.start();

            // Capture script output
            try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                String line;
                while ((line = reader.readLine()) != null) {
                    System.out.println("Python Log: " + line);  // Print to logs
                }
            }

            int exitCode = process.waitFor();
            return "training completed";
        } catch (IOException | InterruptedException e) {
             e.printStackTrace();
        }
        return "training failed";
    }
}
