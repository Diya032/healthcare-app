# healthcare-app

 ## Repo Structure (Reference)

```bash
healthcare-system/
│
├── infra/                         # Infrastructure as code (Bicep/Terraform/ARM, deployment scripts)
│
├── patient_service/               # Backend service: Patient API
│   ├── requirements.txt           # Dependencies for patient service
│   ├── app/                       # Main application package (Python package)
│   │   ├── __init__.py            # Marks `app/` as a package
│   │   ├── main.py                # FastAPI entrypoint (creates FastAPI app, mounts routers)
│   │   ├── crud.py                # DB operations logic
│   │   ├── config.py              # Config/env settings
│   │   ├── models.py              # SQLAlchemy models
│   │   ├── schemas.py             # Pydantic schemas
│   │   ├── routers/               # API route handlers
│   │   │   ├── __init__.py        # Marks routers as package
│   │   │   └── patients.py        # Example router
│   │   └── tests/                 # Unit/integration tests for patient service
│   │       └── test_patients.py
│
├── appointments_service/          # Backend service: Appointments API
│   ├── requirements.txt           # Dependencies for appointments service
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── crud.py
│   │   ├── config.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   └── appointments.py
│   │   ├── notifications/         # Placeholder (notification API can live here later)
│   │   │   └── __init__.py
│   │   └── tests/
│   │       └── test_appointments.py
│
├── frontend/                      # Placeholder for frontend app (React, Next.js, etc.)
│
└── requirements.txt               # Top-level (dev/test tools, linting, common deps if needed)

```


## Notes for the Team

* __init__.py rules:

  ** Add inside app/ and its subfolders (routers/, notifications/, etc.) → needed to treat them as packages.
  
  ** Do not add at service root (patient_service/, appointments_service/) → services talk via REST, not imports.
  
  ** Do not add in infra/ or frontend/.

* requirements.txt:

  ** Each service has its own → for deployment into its own App Service.
  
  ** Root requirements.txt → optional, for dev dependencies (pytest, black, mypy, etc.).

* Service extensibility:

  ** Appointments service can extend with notifications/ or other modules.

  ** Use patient service as a reference baseline.
