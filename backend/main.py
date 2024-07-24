import os
from fastapi import FastAPI, HTTPException
import uuid
import random
import psycopg
from psycopg.rows import dict_row
from faker import Faker
import requests
from fastapi.middleware.cors import CORSMiddleware


# Initialize FastAPI app
app = FastAPI()
faker = Faker()

# Allow our local frontend to make requests to our backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Endpoint to get a new UUID
@app.get("/id")
async def get_id():
    return uuid.uuid4()

# Endpoint to detect the tone of the user biography
@app.get("/tone")
async def get_tone():
    tones = ["humorous", "ironic", "cynical"]
    return random.choice(tones)

# Endpoint to create a new user
@app.post("/user")
async def create_user():

    # Simulate 50% chance
    if random.randint(0, 100) < 50:
        raise HTTPException(status_code=500, detail="Internal Server Error")

    conn = psycopg.connect(os.getenv("DATABASE_URL"))

    cur = conn.cursor()

    new_user = {
        "id": uuid.uuid4(),
        "name": faker.name(),
        "email": faker.email(),
        "phone_number": faker.phone_number(),
        "company": faker.company(),
        "biography": faker.text(),
        "tone": random.choice(["humorous", "ironic", "cynical"]),
    }


    cur.execute("""
        INSERT INTO chefs (id, name, email, phonenumber, company, biography, tone)
        VALUES (%(id)s, %(name)s, %(email)s, %(phone_number)s, %(company)s, %(biography)s, %(tone)s)
    """, new_user)

    conn.commit()
    cur.close()
    conn.close()
    return {"status": "success", "userId": new_user["id"]}


# Endpoint to get user details by ID
@app.get("/user/{id}")
async def get_user(id: str):
    conn = psycopg.connect(os.getenv("DATABASE_URL"))

    cur = conn.cursor(row_factory=dict_row)
    cur.execute("SELECT * FROM chefs WHERE id = %s", (str(id),))
    user = cur.fetchone()

    cur.close()
    conn.close()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
