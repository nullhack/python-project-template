"""Fixed timestep game loop controller."""

from __future__ import annotations

import time
from typing import Optional

from pingpong.ai.controller import AIController
from pingpong.config import DEFAULT_CONFIG, GameConfig
from pingpong.input.handler import InputHandler
from pingpong.physics.engine import PhysicsEngine
from pingpong.render.terminal import TerminalRenderer
from pingpong.state.manager import GameStateManager, ScoreManager
from pingpong.state.models import (
    Ball,
    Difficulty,
    GameEvent,
    GameState,
    GameStateData,
    Paddle,
    Player,
    Vector2D,
)


class GameLoop:
    """Fixed timestep game loop driving update/render cycle.

    Orchestrates all game components: input handling, physics,
    AI control, scoring, and rendering.

    Attributes:
        _config: Game configuration constants.
        _state_manager: Game state machine.
        _score_manager: Score tracking.
        _input_handler: Keyboard input handler.
        _renderer: Terminal renderer.
        _physics: Physics engine.
        _ai: AI controller.
    """

    def __init__(
        self,
        config: GameConfig = DEFAULT_CONFIG,
        input_handler: Optional[InputHandler] = None,
        renderer: Optional[TerminalRenderer] = None,
    ) -> None:
        """Initialize game loop.

        Args:
            config: Game configuration constants.
            input_handler: Input handler instance.
            renderer: Terminal renderer instance.
        """
        self._config = config
        self._state_manager = GameStateManager()
        self._score_manager = ScoreManager(config.win_score)

        self._input_handler = input_handler or InputHandler()
        self._renderer = renderer or TerminalRenderer()
        self._physics = PhysicsEngine(config)
        self._ai = AIController(config)

        # Initialize game state
        self._game_state = self._create_initial_state()

        self._running = False
        self._paused = False

    def _create_initial_state(self) -> GameStateData:
        """Create initial game state with default positions."""
        ball = Ball(
            position=Vector2D(
                x=self._config.field_width / 2,
                y=self._config.field_height / 2,
            ),
            velocity=Vector2D(x=5.0, y=3.0),
        )

        left_paddle = Paddle(
            position=Vector2D(x=2.0, y=self._config.field_height / 2 - 2),
            width=1.0,
            height=4.0,
            speed=self._config.paddle_speed,
        )

        right_paddle = Paddle(
            position=Vector2D(
                x=self._config.field_width - 3.0,
                y=self._config.field_height / 2 - 2,
            ),
            width=1.0,
            height=4.0,
            speed=self._config.paddle_speed,
        )

        return GameStateData(
            ball=ball,
            left_paddle=left_paddle,
            right_paddle=right_paddle,
            left_score=0,
            right_score=0,
            game_status=GameState.MENU,
            difficulty=Difficulty.MEDIUM,
        )

    def start(self) -> None:
        """Start the game loop.

        Begins fixed-timestep update/render cycle at configured FPS.
        Runs until stop() is called or game exits.
        """
        self._running = True
        frame_time = 1.0 / self._config.fps
        last_time = time.perf_counter()

        while self._running:
            current_time = time.perf_counter()
            delta_time = current_time - last_time

            if delta_time >= frame_time:
                last_time = current_time

                self._update(delta_time)

                if self._state_manager.get_state() == GameState.PLAYING:
                    self._render()

    def stop(self) -> None:
        """Stop the game loop gracefully."""
        self._running = False

    def pause(self) -> None:
        """Pause the game loop."""
        self._paused = True

    def resume(self) -> None:
        """Resume a paused game loop."""
        self._paused = False

    def _update(self, delta_time: float) -> None:
        """Update game state for one frame.

        Args:
            delta_time: Time elapsed since last update (seconds).
        """
        inputs = self._input_handler.get_current_inputs()

        state = self._state_manager.get_state()

        # Handle state-specific inputs
        if state == GameState.MENU:
            self._handle_menu_inputs(inputs)
            return

        if state == GameState.GAME_OVER:
            self._handle_game_over_inputs(inputs)
            return

        # Handle pause inputs
        if self._handle_pause_inputs(inputs):
            return

        # Update paddles
        self._update_player_paddle(inputs, delta_time)
        self._update_ai_paddle(delta_time)

        # Update ball physics
        result = self._physics.update(
            self._game_state.ball,
            self._game_state.left_paddle,
            self._game_state.right_paddle,
            delta_time,
        )

        self._game_state.ball = result.ball

        # Handle scoring
        if result.scoring_player:
            self._handle_scoring(result.scoring_player)

    def _handle_menu_inputs(self, inputs: frozenset[str]) -> None:
        """Handle inputs in MENU state.

        Args:
            inputs: Set of currently pressed keys.
        """
        if " " in inputs or "space" in inputs:
            self._state_manager.transition(GameEvent.START_GAME)
        elif "q" in inputs or "Q" in inputs:
            self._running = False

    def _handle_game_over_inputs(self, inputs: frozenset[str]) -> None:
        """Handle inputs in GAME_OVER state.

        Args:
            inputs: Set of currently pressed keys.
        """
        if "q" in inputs or "Q" in inputs:
            self._running = False

    def _handle_pause_inputs(self, inputs: frozenset[str]) -> bool:
        """Handle pause toggle inputs.

        Args:
            inputs: Set of currently pressed keys.

        Returns:
            True if pause state changed (should skip update), False otherwise.
        """
        if self._paused:
            if "p" in inputs or "P" in inputs:
                self._paused = False
            return True

        if "p" in inputs or "P" in inputs:
            self._paused = True
            return True

        return False

    def _update_player_paddle(self, inputs: frozenset[str], delta_time: float) -> None:
        """Update player paddle based on input.

        Args:
            inputs: Set of currently pressed keys.
            delta_time: Time elapsed since last update (seconds).
        """
        if "w" in inputs or "up" in inputs:
            direction = -1
        elif "s" in inputs or "down" in inputs:
            direction = 1
        else:
            return

        self._move_paddle(self._game_state.left_paddle, direction, delta_time)

    def _update_ai_paddle(self, delta_time: float) -> None:
        """Update AI paddle based on computed move direction.

        Args:
            delta_time: Time elapsed since last update (seconds).
        """
        ai_direction = self._ai.compute_move(
            self._game_state.ball,
            self._game_state.right_paddle,
            self._game_state.difficulty,  # type: ignore
        )

        if ai_direction != 0:
            self._move_paddle(self._game_state.right_paddle, ai_direction, delta_time)

    def _move_paddle(self, paddle: Paddle, direction: int, delta_time: float) -> None:
        """Move paddle in specified direction with boundary clamping.

        Args:
            paddle: Paddle to move.
            direction: Movement direction (-1 for up, 1 for down).
            delta_time: Time elapsed since last update (seconds).
        """
        new_y = paddle.position.y + direction * paddle.speed * delta_time
        bounded_y = max(1.0, min(self._config.field_height - paddle.height - 1, new_y))
        paddle.position = Vector2D(x=paddle.position.x, y=bounded_y)

    def _handle_scoring(self, scoring_player: Player) -> None:
        """Handle scoring event.

        Args:
            scoring_player: Which player scored the point.
        """
        self._score_manager.record_point(scoring_player)

        if scoring_player == Player.LEFT:
            self._game_state.left_score = self._score_manager.get_scores()[0]
        else:
            self._game_state.right_score = self._score_manager.get_scores()[1]

        self._reset_ball()

        if self._score_manager.has_winner():
            self._state_manager.transition(GameEvent.GAME_OVER)

    def _reset_ball(self) -> None:
        """Reset ball to center with random direction."""
        import random

        direction = random.choice([-1, 1])
        self._game_state.ball = Ball(
            position=Vector2D(
                x=self._config.field_width / 2,
                y=self._config.field_height / 2,
            ),
            velocity=Vector2D(
                x=direction * self._config.ball_speed * 0.5,
                y=random.uniform(-3.0, 3.0),
            ),
        )

    def _render(self) -> None:
        """Render current game state to terminal."""
        self._renderer.render(self._game_state)
