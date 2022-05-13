package site.metacoding.mongocrud.web;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import lombok.RequiredArgsConstructor;
import site.metacoding.mongocrud.domain.NaverRepository;

@RequiredArgsConstructor
@RestController
public class NaverApiController {
    private final NaverRepository naverRepository;

    // select는 OK -> 200
    // post는 CREATED -> 201

    @GetMapping("/navers")
    public ResponseEntity<?> findAll() {
        return new ResponseEntity<>(naverRepository.findAll(), HttpStatus.OK);
    }
}
