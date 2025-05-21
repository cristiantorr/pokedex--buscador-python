# Importando las librerias necesarias

import flet as ft
import requests
import base64
from urllib.request import urlopen
from PIL import Image
from io import BytesIO

# Este es un programa que consulta la API de Pokemon y muestra la imagen del Pokemon buscado

def main(page):
  logo_pokedex = ft.Image(
    src=f"logo.png",
    width=350,
    height=170
  )
  nombre = ft.TextField(label="Nombre", autofocus=True)
  submit = ft.ElevatedButton("Consultar")

  poke_image = ft.Image(
    src=f"background.png",
    width=350,
    height=350
  )

# Definimos la funcion que se ejecutara al hacer click en el boton
  def btn_click(e):
    api_url_pokemon = f'https://pokeapi.co/api/v2/pokemon/{nombre.value}'
    result = requests.get(api_url_pokemon)
    if result.status_code == 200:
      poke_data = result.json()
      url_image = poke_data['sprites']['other']['official-artwork']['front_default']
      im = Image.open(urlopen(url_image))
      buffer = BytesIO()
      im.save(buffer, format="png")
      image_base64 = base64.b64encode(buffer.getvalue()).decode()
      poke_image.src_base64 = image_base64
      poke_image.update()

  submit.on_click = btn_click

  # Agregamos el logo y el boton a la pagina
  page.add(
      logo_pokedex,
      nombre,
      submit,
      poke_image
    )

ft.app(target=main)