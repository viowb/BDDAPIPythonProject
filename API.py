import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

import org.junit.Test;

public class APITest {

@Test
    public void testGetUser() {
        given()
            .baseUri("https://api.example.com")
        .when()
            .get("/users/1")
        .then()
            .statusCode(200)
            .body("name", equalTo("John"))
            .body("id", equalTo(1));
    }
}