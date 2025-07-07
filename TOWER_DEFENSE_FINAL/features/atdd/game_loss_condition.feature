Feature: Condición de derrota del jugador

  Scenario: El jugador pierde al permitir que enemigos crucen el camino
    Given el jugador tiene 1 punto de vida
    And un enemigo alcanza el final del camino
    When el juego actualiza el estado del jugador
    Then el juego muestra un mensaje de derrota
    And el juego termina
