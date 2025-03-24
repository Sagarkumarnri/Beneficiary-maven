package com.benificiary.namecheck;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;

import jakarta.annotation.PreDestroy;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class FastAPILauncher implements CommandLineRunner {

    private Process fastAPIProcess;

    @Override
    public void run(String... args) {
        startFastAPI();
    }

    private void startFastAPI() {
        try {
            // 🔥 Start FastAPI script
            ProcessBuilder processBuilder = new ProcessBuilder("python", "app.py");

            // Redirect output to see logs in Spring Boot console
            processBuilder.redirectErrorStream(true);
            fastAPIProcess = processBuilder.start();

            // Read and print FastAPI logs
            new Thread(() -> {
                try (InputStream inputStream = fastAPIProcess.getInputStream();
                     BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream))) {
                    String line;
                    while ((line = reader.readLine()) != null) {
                        System.out.println("[FastAPI] " + line);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }).start();

            System.out.println("✅ FastAPI server started successfully.");
        } catch (IOException e) {
            e.printStackTrace();
            System.err.println("❌ Failed to start FastAPI.");
        }
    }

    // Stop FastAPI when Spring Boot shuts down
    @PreDestroy
    public void stopFastAPI() {
        if (fastAPIProcess != null) {
            fastAPIProcess.destroy();
            System.out.println("🛑 FastAPI server stopped.");
        }
    }
}
