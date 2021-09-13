from typing import List

from database import query, get_connection
import models


def add_thought(thought: models.Thought):
    with get_connection() as connection:
        cursor = connection.cursor()

        # convert the thought to a tuple
        thought_record = (
            None,
            thought.title,
            thought.message,
            thought.author
        )

        # perform query
        cursor.execute(query.INSERT_THOUGHT, thought_record)
        cursor.close()


def get_thoughts() -> List[models.ResponseThought]:
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query.SELECT_ALL_THOUGHTS)
        thoughts = cursor.fetchall()

    # convert response to a list of ResponseThought objects
    return [models.ResponseThought(**thought) for thought in thoughts]
