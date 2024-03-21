  """
  This module contains a Flask application for adopting pets.

  The application provides routes for browsing different types of pets and viewing individual pet details.

  Routes:
  - `/`: Returns the HTML content for the index page.
  - `/animals/<pet_type>`: Returns a list of pets of the specified type.
  - `/animals/<pet_type>/<int:pet_id>`: Returns the details of a specific pet.

  Example:
  To run the application, execute the script directly.

    $ python app.py

  """

  from flask import Flask
  from helper import pets

  app = Flask(__name__)


  @app.route('/')
  def index():
    """
    Returns the HTML content for the index page.

    Returns:
      str: The HTML content for the index page.
    """  
    return '''
    <h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend:</p>
    <ul> 
     <li><a href="/animals/dogs">Dogs</a></li>
     <li><a href="/animals/cats">Cats</a></li>
     <li><a href="/animals/rabbits">Rabbits</a></li>
    </ul>
    '''


  @app.route('/animals/<pet_type>')
  def animals(pet_type):
    """
    Returns a list of pets of the specified type.

    Args:
      pet_type (str): The type of pet.

    Returns:
      str: The HTML content for the list of pets.
    """
    html = f'<h1>List of {pet_type}</h1>'
    html += '<ul>'
    for pet in pets[pet_type]:
      html += f'<li>{pet}</li>'
    html += '</ul>'
    return html


  @app.route('/animals/<pet_type>/<int:pet_id>')
  def pet(pet_type, pet_id):
    """
    Returns the details of a specific pet.

    Args:
      pet_type (str): The type of pet.
      pet_id (int): The ID of the pet.

    Returns:
      str: The HTML content for the pet details.

    Raises:
      KeyError: If the pet type or ID is not found in the pet data.

    Example:
      >>> pet('dog', 1)
      '<h1>Buddy</h1><img src="https://example.com/buddy.jpg" alt="Buddy"><p>Buddy is a friendly dog.</p><ul><li>Golden Retriever</li><li>3 years old</li></ul>'
    """
    pet_data = pets[pet_type][pet_id]
    html = ''''''
    html += f'<h1>{pet_data["name"]}</h1>'
    html += f'<img src="{pet_data["url"]}" alt="{pet_data["name"]}">'
    html += f'<p>{pet_data["description"]}</p>'
    html += '<ul>'
    html += f'<li>{pet_data["breed"]}</li>'
    html += f'<li>{pet_data["age"]}</li>'
    html += '</ul>'

    return html


  if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
