Feature: Condición de victoria del jugador

  Scenario: El jugador gana al derrotar a todos los enemigos
    Given el jugador está en el último nivel del juego
    And todos los enemigos han sido derrotados
    When el juego verifica el estado final
    Then el juego muestra un mensaje de victoria
    And el jugador no pierde vidas
