from fastapi import FastAPI
from app.api import pokemons

"""
"""
app = FastAPI()
# To include routes to Pokemons API search
app.include_router(pokemons.router)
