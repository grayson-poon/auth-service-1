from firebase_admin.auth import UserRecord

def user_details(user: UserRecord) -> dict[str, str | int | bool]:
	details = {
		"uid": user.uid,
		"display_name": user.display_name,
		"email": user.email,
		"email_verified": user.email_verified,
		"phone_number": user.phone_number,
		"photo_url": user.photo_url,
		"disabled": user.disabled
	}
	return details