# from datetime import datetime, timedelta, timezone

# import jwt
# import pytest

# from gamr_backend_service.auth.auth import ALGORITHM, SECRET_KEY, generate_token, get_current_user


# @pytest.fixture
# def jwt_token() -> str:
#     data = {"username": "gaston"}
#     expire = datetime.now(timezone.utc) + timedelta(minutes=30)
#     data["exp"] = expire
#     token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
#     return token


# def test_create_access_token():
#     data = "gaston"
#     token = generate_token(data)
#     decoded = jwt.decode(
#         token, SECRET_KEY, algorithms=[ALGORITHM], options={"verify_exp": False}
#     )
#     assert decoded["username"] == "gaston"


# def test_get_current_user(jwt_token: str):
#     user = get_current_user(jwt_token)
#     assert user.username == "gaston"


# def test_get_current_user_error():
#     with pytest.raises(ValueError) as ex:
#         get_current_user("")
#         assert ex == "Couldn't get username from payload"
