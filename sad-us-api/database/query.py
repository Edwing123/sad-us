# insert thought
INSERT_THOUGHT = """
INSERT INTO thought
(
    thought_id,
    title,
    message,
    author
)

VALUES(%s, %s, %s, %s);
"""


SELECT_ALL_THOUGHTS = """
SELECT * FROM thought;
"""
