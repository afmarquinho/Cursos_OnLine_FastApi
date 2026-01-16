from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from apps.users.schemas import Current_user
from apps.users.security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/users/login")

# Funciòn que decodifica el token sin consultar la base de datos, el oauth2_schema toma el token del header
def get_current_user (token: str = Depends(oauth2_scheme)) -> Current_user:
    try:
        payload = decode_access_token(token)
        user_id: str | None = payload.get("sub")
        role: str | None = payload.get("role")
        username:str | None = payload.get("username")

        if user_id is None or role is None or username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )
        # **paylod hace uan desestructuraciòn y manda los atributos como variables separadas
        return Current_user(user_id=user_id, role=role, username=username)

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )


def check_admin (current_user: Current_user = Depends(get_current_user)) -> Current_user:
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos de administrador"
        )

    return current_user
