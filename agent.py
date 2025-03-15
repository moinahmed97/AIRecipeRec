from __future__ import annotations as _annotations

import asyncio
from dotenv import load_dotenv
import os
from dataclasses import dataclass
from typing import Any, List

from httpx import AsyncClient
from pydantic_ai import Agent, ModelRetry, RunContext

load_dotenv()

@dataclass
class Deps:
    client: AsyncClient
    recipe_api_key: str | None

recipe_agent = Agent(
    'openai:gpt-4o',
    system_prompt=(
        'You are a recipe recommendation assistant. '
        'Based on given ingredients, recommend a recipe and provide cooking instructions.'
    ),
    deps_type=Deps,
    retries=2,
)

@recipe_agent.tool
async def get_recipes(ctx: RunContext[Deps], ingredients: List[str]) -> List[dict[str, Any]]:
    """Get recipe recommendations based on ingredients.

    Args:
        ctx: The context.
        ingredients: A list of ingredients provided by the user.

    Returns:
        A list of recipe recommendations.
    """
    if ctx.deps.recipe_api_key is None:
        # If no recipe API key is provided, return a default response.
        return [{'title': 'Unknown Recipe', 'instructions': 'No instructions available.'}]

    params = {
        'api_key': ctx.deps.recipe_api_key,
        'ingredients': ','.join(ingredients),
    }

    response = await ctx.deps.client.get('https://api.spoonacular.com/recipes/findByIngredients', params=params)

    if response.status_code != 200:
        raise ModelRetry('Error fetching recipes from the API.')

    return response.json()

async def main():
    async with AsyncClient() as client:
        recipe_api_key = os.getenv('RECIPE_API_KEY')
        deps = Deps(client=client, recipe_api_key=recipe_api_key)

        result = await recipe_agent.run(
            'Can you suggest a recipe with chicken and broccoli?', deps=deps
        )

        print('Response:', result.data)

if __name__ == '__main__':
    asyncio.run(main())