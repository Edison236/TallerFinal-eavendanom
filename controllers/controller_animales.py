from flask import Blueprint, render_template, request, jsonify
from databases.db import db
from models.guarderia import Guarderia,insert_animals

guarderia_bp = Blueprint('daycare', __name__, url_prefix='/daycare')

@guarderia_bp.route('/upload_animals', methods = ['GET','POST'])
def upload_info_animals():
    animals = Guarderia.query.count()
    print(animals)
    if animals.__eq__(0):
        insert_animals()
    else:
        return jsonify({"mensaje": "Los datos ya fueron cargados."})
    return get_list_animal()

@guarderia_bp.route('/get_animals', methods= ['GET'])
def get_list_animal():
    animals = Guarderia.query.all()
    return jsonify([{'id': animal.id,'name': animal.name, 'type': animal.type, 'breed': animal.breed, 'age': animal.age, 'sound': animal.sound} for animal in animals]), 200

@guarderia_bp.route('/update_animals/<int:id>', methods= ['PATCH'])
def update_animal(id):
    animal = Guarderia.query.get(id)
    if animal:
        data = request.get_json()
        print(data.get('name'))
        animal.name = data.get('name')
        db.session.commit()
    return  jsonify({"mensaje": "Datos actualizados correctamente."}), 200 

@guarderia_bp.route('/delete_animals/<int:id>', methods = ["DELETE"])
def delete_animals(id):
    animal = Guarderia.query.get(id)
    if animal:
        db.session.delete(animal)
        db.session.commit()
    return  jsonify({"mensaje": f"El animal {animal.name} se borro correctamente."}), 200 

@guarderia_bp.route('/create_animal', methods = ['POST'])
def create_animal():
    animal = request.get_json()
    create = Guarderia(name = animal['name'] ,type = animal['type'] ,breed = animal['breed'] ,age = animal['age'] ,sound = animal['sound'])
    db.session.add(create)
    db.session.commit()
    return  jsonify({"mensaje": f"El animal {animal['name']} fue creado correctamente."}), 200 

@guarderia_bp.route('/get_animal/<string:name>', methods= ['GET'])
def get_animal_name(name):
    animals = Guarderia.query.filter(Guarderia.name == name).all()
    print(animals)
    return jsonify([{'id': animal.id,'name': animal.name, 'type': animal.type, 'breed': animal.breed, 'age': animal.age, 'sound': animal.sound} for animal in animals]), 200