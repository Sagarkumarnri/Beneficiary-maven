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
        return nameSimilarityService.getSimilarity(request.getGivenName(), request.getActualName ());
    }
}

// DTO class
class NameRequest {
    public String getGivenName() {
		return givenName;
	}
	public void setGivenName(String givenName) {
		this.givenName = givenName;
	}
	public String getActualName() {
		return actualName;
	}
	public void setActualName(String actualName) {
		this.actualName = actualName;
	}
	private String givenName;
    private String actualName;

   
}
