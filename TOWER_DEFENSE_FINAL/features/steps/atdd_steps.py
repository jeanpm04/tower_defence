from behave import given, when, then
from tower_defence.src.game_logic import check_game_end
from tower_defence.src.game_state import GameState

@given('el jugador está en el último nivel del juego')
def step_impl(context):
    context.game_state = GameState()
    context.game_state.level = context.game_state.max_level

@given('todos los enemigos han sido derrotados')
def step_impl(context):
    context.game_state.enemies_remaining = 0

@when('el juego verifica el estado final')
def step_impl(context):
    context.result = check_game_end(context.game_state)

@then('el juego muestra un mensaje de victoria')
def step_impl(context):
    assert context.result == "victory"

@then('el jugador no pierde vidas')
def step_impl(context):
    assert context.game_state.lives > 0


@given('el jugador tiene 1 punto de vida')
def step_impl(context):
    context.game_state = GameState()
    context.game_state.lives = 1

@given('un enemigo alcanza el final del camino')
def step_impl(context):
    context.game_state.enemies_crossed = 1

@when('el juego actualiza el estado del jugador')
def step_impl(context):
    context.result = check_game_end(context.game_state)

@then('el juego muestra un mensaje de derrota')
def step_impl(context):
    assert context.result == "defeat"

@then('el juego termina')
def step_impl(context):
    assert context.game_state.running is False
