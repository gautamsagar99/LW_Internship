from fastapi import FastAPI, HTTPException, Form, Request
from pydantic import BaseModel, EmailStr
from fastapi.middleware.cors import CORSMiddleware
from passlib.hash import bcrypt
from datetime import date

app = FastAPI()

origins ="*" # Add your frontend URLs here
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple data structure to store user registrations
user_data = []


class UserRegistration(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
    confirmPassword: str
    dob: str
    gender: str
    country: str
    termsAndConditions: str

    



@app.post("/register")
async def register(request: Request):
    
    data = await request.json()
    print(data)

    user = UserRegistration(**data["user"])
    # Validate email format
    if not user.email:
        raise HTTPException(status_code=400, detail="Email is required.")
    
    # Validate password complexity
    if len(user.password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long.")

    # Simulate server-side validation for email format
    if "@" not in user.email:
        raise HTTPException(status_code=400, detail="Invalid email format.")

    # Simulate server-side validation for password complexity
    if not any(char.isdigit() for char in user.password) or not any(char.isalpha() for char in user.password):
        raise HTTPException(status_code=400, detail="Password must contain both letters and numbers.")

    # Hash the password
    hashed_password = bcrypt.hash(user.password)

    # Simulate storing user registration data
    user_data.append({
        "firstName": user.firstName,
        "lastName": user.lastName,
        "email": user.email,
        "hashed_password": hashed_password,
        "dob": user.dob,
        "gender": user.gender,
        "country": user.country,
        "termsAndConditions": user.termsAndConditions
    })

    return {"message": f"Registration successful"}

@app.get("/test")
async def register():
    return {"string": "hello"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
