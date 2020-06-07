# challenge 1
# task 1

# TODO: Ingredient model
# name - string (e.g. "carrots")
# description - string (e.g. "chopped")
# quantity - decimal (e.g. ".25")
# measurement_type - string (e.g. "cups")
# recipe - foreign key
class Ingredient(Model):
    name = CharField()
    description = CharField()
    quantity = DecimalField(decimal_places=2)
    measurement_type = CharField()
    recipe = ForeignKeyField(Recipe, related_name='ingredient_set')
    class Meta:
        database = DATABASE
# task 2
class IngredientList(Resource):
    def get(self):
        return "random string"
    
class Ingredient(Resource):
    def get(self, id):
        return "random string"
# challenge completed

# challenge 2
# task 1
from flask import jsonify, Blueprint
from flask.ext.restful import Resource, Api
# task 2
recipes_api = Blueprint('resources.recipes',__name__)
# task 3
api = Api(recipes_api)

api.add_resource(
    IngredientList,
    '/api/v1/ingredients',
    endpoint='ingredients'
)
api.add_resource(
    Ingredient,
    '/api/v1/ingredients/<int:id>',
    endpoint='ingredient'
)
# task 4
from resources.ingredients import ingredients_api
from resources.recipes import recipes_api
app.register_blueprint(ingredients_api)
app.register_blueprint(recipes_api)
# challenge completed

# challenge 3
# task 1
ingredient_fields={
    'name': fields.String,
    'description': fields.String,
    'measurement_type': fields.String,
    'quantity': fields.Float,
    'recipe':fields.String
}
# task 2
def get(self):
        ingredients = [marshal(ingredient, ingredient_fields)
                       for ingredient in models.Ingredient.select()]
        return {'ingredients': ingredients}

@marshal_with(ingredient_fields)
def post(self):
    args = self.reqparse.parse_args()
    ingredient = models.Ingredient.create(**args)
    return ingredient

@marshal_with(ingredient_fields)
def get(self, id):
    ingredient = models.Ingredient.get(models.Ingredient.id==id)
    return ingredient
# challenge completed

# challenge 4
# task 1
return ('', 204, {'Location': url_for('resources.recipes.recipes')})
# challenge completed