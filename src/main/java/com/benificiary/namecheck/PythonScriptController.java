package com.benificiary.namecheck;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import java.io.File;
import java.io.IOException;

@RestController
@RequestMapping("/api")
public class PythonScriptController {

    private final PythonScriptService pythonScriptService;

    public PythonScriptController(PythonScriptService pythonScriptService) {
        this.pythonScriptService = pythonScriptService;
    }

    @PostMapping("/train")
    public String uploadFileAndRunScript( ) {
        try {
            // Save the uploaded file to a temporary location

            // Run the Python script with the uploaded file
           return  pythonScriptService.runPythonScript( );


        } catch (Exception e) {
            return "❌ Error saving file: " + e.getMessage();
        }
    }
}
