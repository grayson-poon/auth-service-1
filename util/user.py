from firebase_admin.auth import UserRecord

def create_user_response(user: UserRecord) -> dict[str, str | int | bool]:
	response = {
		"message": "Successfully created user.",
		"uid": user.uid,
		"email": user.email,
		"email_verified": user.email_verified,
		"phone_number": user.phone_number
	}
	return response