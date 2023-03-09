from models.user import User as UserModel
from schemas.user import User as UserSchema


class UserService():

    def __init__(self,db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).all()
        return result

    def get_user(self,id:int):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result

    def get_user_by_username(self,username:str):
        result = self.db.query(UserModel).filter(UserModel.username == username).all()
        return result      
    
    def get_user_by_email(self,email:str):
        result = self.db.query(UserModel).filter(UserModel.email()== email).all()
        return result      

    def create_user(self, user:UserSchema):
        new_user = UserModel(
        name=user.name,
        lastname = user.lastname,
        email = user.email,
        username = user.username,
        password = user.password,
        cohabitation_agreement = user.cohabitation_agreement,
        status = user.status,
        description = user.description,
        knowledge_interest = user.knowledge_interest,
        create_at = user.create_at,
        update_at = user.update_at,
        forgot_password = user.forgot_password,
        image_profile = user.image_profile,
        phone_number = user.phone_number

        )
        self.db.add(new_user)
        self.db.commit()
        return 



    def update_user(self,id:int, data:UserSchema):
        user = self.db.query(UserModel).get(id)
        if user:
            user.name=data.name
            user.lastname = data.lastname
            user.email = data.email
            user.username = data.username
            user.password = data.password
            user.cohabitation_agreement = data.cohabitation_agreement
            user.status = data.status
            user.description = data.description
            user.knowledge_interest = data.knowledge_interest
            user.create_at = data.create_at
            user.update_at = data.update_at
            user.forgot_password = data.forgot_password
            user.image_profile = data.image_profile
            user.phone_number = data.phone_number
            self.db.commit()
            return True
        return False

    def delete_user(self,id:int):
        user = self.get_user_by_id(id)
        if not user:
            return None
        self.db.delete(user)
        self.db.commit()
        return user
    
    def get_user_by_id(self,id:int):
        return self.db.query(UserModel).filter(UserModel.id == id).first()



