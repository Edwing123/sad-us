CREATE TABLE thought
(
    thought_id SMALLINT UNSIGNED AUTO_INCREMENT,
    title VARCHAR(150),
    message TEXT,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    author VARCHAR(80),
    CONSTRAINT pk_thought PRIMARY KEY (thought_id)
)
