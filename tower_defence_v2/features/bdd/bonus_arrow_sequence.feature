Feature: Mini juego de flechas entre oleadas
  Scenario: El jugador acierta la secuencia correcta de flechas
    Given el juego está en ejecución
    And se muestra una secuencia de flechas como mini juego
    When el jugador presiona las flechas en el orden correcto
    Then el juego reconoce la secuencia como correcta

  Scenario: El jugador falla la secuencia de flechas
    Given el juego está en ejecución
    And se muestra una secuencia de flechas como mini juego
    When el jugador presiona una flecha incorrecta
    Then el juego reconoce la secuencia como incorrecta
