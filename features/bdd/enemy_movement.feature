Feature: Movimiento de enemigo
  Scenario: El enemigo se mueve al actualizar el juego
    Given un enemigo está en la posición inicial del camino
    When el juego actualiza su estado
    Then el enemigo debe moverse hacia la siguiente posición











