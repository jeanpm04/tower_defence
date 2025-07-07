Feature: Tiempo de aparición entre enemigos
  Scenario: Los enemigos aparecen con un intervalo determinado
    Given el juego está en ejecución
    When el tiempo de aparición supera el umbral
    Then aparece un nuevo enemigo en pantalla