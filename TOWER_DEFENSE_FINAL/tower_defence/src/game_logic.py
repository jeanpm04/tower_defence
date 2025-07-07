def check_game_end(game_state):
    if game_state.enemies_remaining <= 0 and game_state.level >= game_state.max_level:
        game_state.status = "victory"
        game_state.running = False
        return "victory"

    if game_state.lives <= 0 or game_state.enemies_crossed >= game_state.lives:
        game_state.status = "defeat"
        game_state.running = False
        return "defeat"

    return "playing"
