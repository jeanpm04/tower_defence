Feature: Inicio de oleada en el juego
  Scenario: El jugador inicia una nueva oleada
    Given el juego está en ejecución
    When el jugador inicia una nueva oleada
    Then aparece al menos un enemigo en pantalla