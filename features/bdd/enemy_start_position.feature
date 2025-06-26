Feature: Posición inicial de enemigos
  Scenario: Todos los enemigos aparecen en la entrada del camino
    Given el juego está en ejecución
    When el jugador inicia una nueva oleada
    Then todos los enemigos aparecen en la posición inicial del camino
