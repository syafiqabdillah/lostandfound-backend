from utils.executor import execute_get, execute_post
from utils.auth import get_current_time, generate_id
from fastapi import HTTPException

def create(category, description):
    query = """
            INSERT INTO report (id, category, description, created_date)
            VALUES (%s, %s, %s, %s) RETURNING id
            """
    id = generate_id()
    created_date = get_current_time()
    return execute_post(query, (id, category, description, created_date))

def getAll(q):
    q_ = f"%{q.lower()}%"
    query = "select id, category, description, created_date from report where lower(description) like %s order by created_date desc"
    results = execute_get(query, (q_, ))
    return [
        {
            "id": result[0],
            "category": result[1],
            "description": result[2],
            "created_date": result[3]
        } for result in results
    ]