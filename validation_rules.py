from marshmallow import Schema, fields

# validations rules
class FizzBuzzSchema(Schema):
	int1 	= 	fields.Int(required=True)
	int2 	= 	fields.Int(required=True)
	limit 	= 	fields.Int(required=True)
	str1 	= 	fields.Str(required=True)
	str2 	= 	fields.Str(required=True)