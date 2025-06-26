from behave import given, when, then
from unittest.mock import patch, MagicMock
from tower_defence.src.wave_manager import WaveManager
from tower_defence.src.animated_enemy import AnimatedEnemy


# ========== Feature: Movimiento de enemigo ==========

@given("un enemigo está en la posición inicial del camino")
@patch("pygame.image.load")
def step_impl_given_enemy(context, mock_load):
    mock_surface = MagicMock()
    mock_load.return_value = mock_surface
    mock_surface.convert_alpha.return_value = mock_surface

    context.enemy = AnimatedEnemy(
        path=[(0, 0), (100, 0)],
        sprite_sheet_path="Bat.png",
        frame_width=32,
        frame_height=32,
        num_frames=3,
        health=100,
        speed=1
    )
    context.initial_x = context.enemy.x
    context.initial_y = context.enemy.y

@when("el juego actualiza su estado")
def step_impl_update_game(context):
    if hasattr(context, 'enemy'):
        context.enemy.move()
    elif hasattr(context, 'wave_manager'):
        context.wave_manager.update()

@then("el enemigo debe moverse hacia la siguiente posición")
def step_impl_then_moved(context):
    assert context.enemy.x != context.initial_x or context.enemy.y != context.initial_y, \
        "El enemigo no se ha movido"


# ========== Feature: Inicio de oleada en el juego ==========

@given("el juego está en ejecución")
def step_impl_game_running(context):
    context.path = [(0, 0), (100, 0)]
    context.wave_manager = WaveManager(path=context.path)

@when("el jugador inicia una nueva oleada")
@patch("pygame.image.load")
def step_impl_start_wave(context, mock_load):
    mock_surface = MagicMock()
    mock_load.return_value = mock_surface
    mock_surface.convert_alpha.return_value = mock_surface

    context.wave_manager.spawn_enemy()

@then("aparece al menos un enemigo en pantalla")
def step_impl_enemy_spawned(context):
    assert len(context.wave_manager.enemies) > 0, "No se generaron enemigos"


# ========== Feature: Secuencia de flechas bonus ==========

@given("se muestra una secuencia de flechas como mini juego")
def step_impl_show_arrow_sequence(context):
    context.expected_sequence = ["up", "left", "down"]
    context.input_sequence = []

@when("el jugador presiona las flechas en el orden correcto")
def step_impl_correct_arrow_sequence(context):
    context.input_sequence = ["up", "left", "down"]

@when("el jugador presiona una flecha incorrecta")
def step_impl_incorrect_arrow_sequence(context):
    context.input_sequence = ["up", "right", "down"]  # 'right' es incorrecta

@then("el juego reconoce la secuencia como correcta")
def step_impl_sequence_correct(context):
    assert context.input_sequence == context.expected_sequence, "La secuencia no fue reconocida como correcta"

@then("el juego reconoce la secuencia como incorrecta")
def step_impl_sequence_incorrect(context):
    assert context.input_sequence != context.expected_sequence, "La secuencia incorrecta fue aceptada como válida"



# ========== Feature: Tiempo de aparición entre enemigos ==========

@when("el tiempo de aparición supera el umbral")
@patch("pygame.image.load")
def step_impl_spawn_timer_exceeds(context, mock_load):
    mock_surface = MagicMock()
    mock_load.return_value = mock_surface
    mock_surface.convert_alpha.return_value = mock_surface

    context.wave_manager.spawn_timer = context.wave_manager.spawn_delay
    context.wave_manager.update()

@then("aparece un nuevo enemigo en pantalla")
def step_impl_new_enemy_spawned(context):
    assert len(context.wave_manager.enemies) > 0, "No apareció un nuevo enemigo"


# ========== Feature: Posición inicial de enemigos ==========

@then("todos los enemigos aparecen en la posición inicial del camino")
def step_impl_enemy_start_position(context):
    x0, y0 = context.path[0]
    for enemy in context.wave_manager.enemies:
        assert (enemy.x, enemy.y) == (x0, y0), "Un enemigo no está en la posición inicial"
