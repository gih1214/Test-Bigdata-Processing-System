package site.metacoding.mongocrud.domain;

import java.time.LocalDateTime;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
@Document(collection = "naverss") // 몽고DB greendb-naverss라는 컬렉션에 매핑된다.
public class Naver {
    // 몽고DB의 _id는 String이다.
    // 사실 몽고 ObjectId의 정확한 타입은 자바스크립트 오브젝트 타입이다.
    @Id
    private String _id;
    private String company;
    private String title;
    private LocalDateTime createdAt;

    // 몽고는 타임지 설정이 안 됨. 그래서 직접 현재 시간을 표시해줘야 한다.
    public LocalDateTime getCreatedAt() {
        return createdAt.minusHours(9);
    }
}
