from flask import Flask, render_template
  app = Flask(__name__)

  @app.route('/')
  def index():
    return '''''
    
    <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
<ul> 

<li><a herf=" /animals/dogs">Dogs</a></li>
<li><a herf=" /animals/cats">Cats</a></li>
<li><a herf=" /animals/rabbits">Rabbitts</a></li>


</ul>
'''
    
@app.route('/animals/<pet_type>')
def animals(pet_type):
  pet_list = pets.get(pet_type,  [])
  

html = f'<h1>List of {pet_type.capitalize()}:</h1> </h1>'
for pet_id, pet in enumerate(pet_list):
  html += f'<li><a href="/animals/{pet_type}/{pet_id">{pet["name"]}</a></li>'

html +='</ul>'


return html

@app.route('/animals/<pet_type>/<int:pet_id>/')
def pet(pet_type, pet_id):
  pet_list = pet.get(pet_type, [])
if 0 <=pet_id< len(pet_list):
  pet_data = pet_list[pet_id]

html= f'<h1>{pet_data["name"]}</h1>'
html += f'<img src="{pet_data["url"]}" alt="{pet_data["name"]}">'
html += f'<p>{pet_data["description"]}</p>'
html += '<ul>'
html += f'<li>breed:{pet_data["breed]}</li>'
html += '</ul>'

return html
else:
return'pet not found.'

pets={
  'dogs':[
    {'name': 'Buddy','age': '3 years', 'breed': 'Labrador', 'description': 'Friendly and playful.', 'url':'buddy.jpg'},
  ],
  'cats':[
    {'name': 'Buddy','age': '2 years', 'breed': 'Siamese', 'description': 'Independet and curious.', 'url':'whiskers.jpg'},
  ],
  'rabbits':[
    {'name': 'Snowball','age': '1 years', 'breed': 'Holland Lop', 'description': 'Adorable and fluffy.', 'url': 'snowball.jpg'},
  ]
}

if __name__ == '__main__':
  app.run(debug=true)
app.run(debug=True, host="0.0.0.0")
