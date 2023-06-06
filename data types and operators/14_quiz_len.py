given_name = "William"
middle_name = "Bradley"
family_name = "Pitt"

name_length = len(given_name) + len(middle_name) + len(family_name)
print(name_length)

driving_license_character_limit = 28
print("isPassDrivingLicenseCharacterLimit:", name_length < driving_license_character_limit)