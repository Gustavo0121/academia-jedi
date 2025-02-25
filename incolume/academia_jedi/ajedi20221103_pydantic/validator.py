from pydantic import BaseModel, ValidationError, validator


class UserModel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    @validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            msg = 'must contain a space'
            raise ValueError(msg)
        return v.title()

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            msg = 'passwords do not match'
            raise ValueError(msg)
        return v

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v


if __name__ == '__main__':  # pragma: no cover

    user = UserModel(
        name='samuel colvin',
        username='scolvin',
        password1='zxcvbn',
        password2='zxcvbn',
    )
    print(user)
    # > name='Samuel Colvin' username='scolvin' password1='zxcvbn'

    try:
        UserModel(
            name='samuel',
            username='scolvin',
            password1='zxcvbn',
            password2='zxcvbn2',
        )
    except ValidationError as e:
        print(e)

        """
        2 validation errors for UserModel
        name
          must contain a space (type=value_error)
        password2
          passwords do not match (type=value_error)
        """
