package com.benificiary.namecheck;

import com.benificiary.namecheck.NameSimilarityService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
public class NameSimilarityController {

    @Autowired
    private NameSimilarityService nameSimilarityService;

    @PostMapping("/similarity")
    public String checkSimilarity(@RequestBody NameRequest request) {
        return nameSimilarityService.getSimilarity(request.getName1(), request.getName2());
    }
}

// DTO class
class NameRequest {
    private String name1;
    private String name2;

    public String getName1() { return name1; }
    public void setName1(String name1) { this.name1 = name1; }

    public String getName2() { return name2; }
    public void setName2(String name2) { this.name2 = name2; }
}
