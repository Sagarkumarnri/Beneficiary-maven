package com.benificiary.namecheck;

import okhttp3.*;
import org.springframework.stereotype.Service;

@Service
public class NameSimilarityService {

    private final OkHttpClient client = new OkHttpClient();
    private final String API_URL = "http://127.0.0.1:8000/similarity";

    public String getSimilarity(String name1, String name2) {
        String jsonBody = String.format("{\"name1\": \"%s\", \"name2\": \"%s\"}", name1, name2);
        System.out.println(jsonBody);
        RequestBody body = RequestBody.create(jsonBody, MediaType.get("application/json"));

        Request request = new Request.Builder()
                .url(API_URL)
                .post(body)
                .addHeader("Content-Type", "application/json")
                .build();

        try (Response response = client.newCall(request).execute()) {
            return response.isSuccessful() && response.body() != null
                    ? response.body().string()
                    : "Request failed: " + response.code();
        } catch (Exception e) {
            return "Error calling API: " + e.getMessage();
        }
    }
}
