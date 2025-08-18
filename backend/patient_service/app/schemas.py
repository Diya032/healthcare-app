# app/schemas.py
# ---------------------------------------------------------
# Pydantic models for request/response validation.
# We keep "Auth-related" and "Patient-related" schemas
# separate because in production Azure AD B2C will manage
# users & authentication, while Patients remain our
# domain-specific entity stored in our DB.
# ---------------------------------------------------------

from typing import Optional, Literal
from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date, datetime


# -------------------------
# PATIENT SCHEMAS (Domain)
# -------------------------

class PatientBase(BaseModel):
    """Shared base fields for patient records."""
    name: str
    age: int
    dob: date
    gender: str
    contact_number: str
    email: EmailStr
    address: Optional[str] = None


class PatientCreate(PatientBase):
    """Payload for creating a new patient record (POST /patients).
    Notice: No password field. Auth is managed separately.
    """
    pass


class PatientUpdate(BaseModel):
    """Payload for partial patient updates (PATCH /patients).
    All fields optional so clients can send only what changes.
    """
    name: Optional[str] = None
    age: Optional[int] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    contact_number: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None


class PatientOut(PatientBase):
    """Response model returned to clients after reading patients."""
    id: int
    # Pydantic v2 config: allow ORM → Pydantic conversion
    model_config = ConfigDict(from_attributes=True)


# -------------------------
# AUTH SCHEMAS (Users/JWT)
# -------------------------
# These are temporary while we mock login/signup.
# Later replaced by Azure AD B2C-issued JWTs.
# -------------------------

class UserCreate(BaseModel):
    """Signup payload (used only if we manage auth locally)."""
    email: EmailStr
    password: str  # Will be hashed before storage, don't double hash (mistake)

class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    # NOT included password field for security


class LoginSchema(BaseModel):
    """Login payload: exchange email+password for JWT."""
    email: EmailStr
    password: str


class Token(BaseModel):
    """JWT access token returned after login."""
    access_token: str
    token_type: Literal["bearer"] = "bearer"


class TokenData(BaseModel):
    """Payload extracted from JWT (e.g. user_id or email)."""
    email: Optional[str] = None
