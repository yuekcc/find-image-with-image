from typing import List

import lancedb
import pyarrow as pa

uri = "store/main-lancedb"
db_connection = None
image_vector_table = None


async def ensure_connect():
    global db_connection, image_vector_table
    if db_connection is None:
        db_connection = await lancedb.connect_async(uri)

    if image_vector_table is None:
        image_vector_table = await db_connection.open_table("image_vectors")


class Database:
    def __init__(self):
        pass

    async def add(self, file_id: str, vectors: List[float]):
        await ensure_connect()
        await image_vector_table.add([
            {file_id: file_id, vectors: vectors}
        ])

    async def search(self, vectors: List[float]):
        await ensure_connect()
        result = await image_vector_table.vector_search(vectors)
        return result


image_vectors = Database()
