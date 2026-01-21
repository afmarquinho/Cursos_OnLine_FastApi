from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from apps.users.schemas import CurrentUser
from apps.users.security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/users/login")

# Funciòn que decodifica el token sin consultar la base de datos, el oauth2_schema toma el token del header
def get_current_user (token: str = Depends(oauth2_scheme)) -> CurrentUser:
    try:
        payload = decode_access_token(token)
        user_id: int | None = int(payload.get("sub"))
        role: str | None = payload.get("role")
        username:str | None = payload.get("username")
        is_active:bool | None = bool(payload.get("is_active"))

        if user_id is None or role is None or username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )
        # **paylod hace uan desestructuraciòn y manda los atributos como variables separadas
        return CurrentUser(user_id=user_id, role=role, username=username, is_active=is_active)

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )

def role_required(roles: list):
    def wrapper (CurrentUser: CurrentUser = Depends(get_current_user)):
        if CurrentUser.role not in roles :
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No tienes permisos"
            )
        return CurrentUser
    return wrapper

def check_admin (CurrentUser: CurrentUser = Depends(get_current_user)) -> CurrentUser:
    if CurrentUser.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos de administrador"
        )

    return CurrentUser

