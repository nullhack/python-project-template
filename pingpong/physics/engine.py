"""Physics engine for ball movement and collision detection."""

from __future__ import annotations

import math

from pingpong.config import DEFAULT_CONFIG, GameConfig
from pingpong.state.models import (
    Ball,
    CollisionType,
    Paddle,
    PhysicsResult,
    Player,
    Vector2D,
)


class PhysicsEngine:
    """Handles ball physics, collisions, and movement.

    Updates ball position based on velocity, detects wall and paddle
    collisions, and determines scoring events.

    Attributes:
        _config: Game configuration constants.
    """

    def __init__(self, config: GameConfig = DEFAULT_CONFIG) -> None:
        """Initialize physics engine.

        Args:
            config: Game configuration constants.
        """
        self._config = config

    def update(
        self,
        ball: Ball,
        left_paddle: Paddle,
        right_paddle: Paddle,
        delta_time: float,
    ) -> PhysicsResult:
        """Update ball position and detect collisions.

        Args:
            ball: Current ball state.
            left_paddle: Player paddle state.
            right_paddle: AI paddle state.
            delta_time: Time elapsed since last update (seconds).

        Returns:
            PhysicsResult with updated ball and collision/scoring info.
        """
        # Calculate new position
        new_position = ball.position + ball.velocity.scale(delta_time)
        new_velocity = ball.velocity

        collision_type: CollisionType | None = None
        scoring_player: Player | None = None

        # Check top wall collision
        if new_position.y - ball.radius <= 0:
            new_velocity = Vector2D(x=new_velocity.x, y=abs(new_velocity.y))
            collision_type = CollisionType.WALL_TOP

        # Check bottom wall collision
        elif new_position.y + ball.radius >= self._config.field_height:
            new_velocity = Vector2D(x=new_velocity.x, y=-abs(new_velocity.y))
            collision_type = CollisionType.WALL_BOTTOM

        # Check left paddle collision
        if self._check_paddle_collision(new_position, ball.radius, left_paddle):
            new_velocity = self._reflect_from_paddle(ball, left_paddle, is_left=True)
            collision_type = CollisionType.PADDLE_LEFT

        # Check right paddle collision
        elif self._check_paddle_collision(new_position, ball.radius, right_paddle):
            new_velocity = self._reflect_from_paddle(ball, right_paddle, is_left=False)
            collision_type = CollisionType.PADDLE_RIGHT

        # Check scoring (ball passes left or right boundary)
        if new_position.x - ball.radius <= 0:
            scoring_player = Player.RIGHT
        elif new_position.x + ball.radius >= self._config.field_width:
            scoring_player = Player.LEFT

        updated_ball = Ball(
            position=new_position, velocity=new_velocity, radius=ball.radius
        )

        return PhysicsResult(
            ball=updated_ball,
            scoring_player=scoring_player,
            collision_type=collision_type,
        )

    def _check_paddle_collision(
        self,
        ball_position: Vector2D,
        ball_radius: float,
        paddle: Paddle,
    ) -> bool:
        """Check if ball collides with paddle.

        Args:
            ball_position: Ball center position.
            ball_radius: Ball collision radius.
            paddle: Paddle to check.

        Returns:
            True if collision detected.
        """
        # Guard clauses for early exit on obvious non-collisions
        if ball_position.x + ball_radius <= paddle.position.x:
            return False
        if ball_position.x - ball_radius >= paddle.position.x + paddle.width:
            return False
        if ball_position.y + ball_radius <= paddle.position.y:
            return False

        return ball_position.y - ball_radius < paddle.position.y + paddle.height

    def _reflect_from_paddle(
        self,
        ball: Ball,
        paddle: Paddle,
        is_left: bool,
    ) -> Vector2D:
        """Calculate reflection velocity from paddle hit position.

        Args:
            ball: Ball state for velocity reference.
            paddle: Paddle that was hit.
            is_left: True if left paddle, False if right paddle.

        Returns:
            New velocity vector with adjusted angle.
        """
        # Calculate relative hit position on paddle (0.0 to 1.0)
        paddle_center_y = paddle.position.y + paddle.height / 2
        relative_y = (ball.position.y - paddle_center_y) / (paddle.height / 2)

        # Clamp to valid range
        relative_y = max(-1.0, min(1.0, relative_y))

        # Calculate new angle based on hit position
        # Top of paddle = upward angle, bottom = downward angle
        max_angle = 60  # degrees
        angle_radians = abs(relative_y) * max_angle * (math.pi / 180)

        # Preserve current speed
        current_speed = (ball.velocity.x**2 + ball.velocity.y**2) ** 0.5

        # Determine direction based on which paddle was hit
        if is_left:
            # Ball moving left, reflect to the right
            vx = abs(current_speed * 0.5)  # Mostly horizontal
            vy = current_speed * angle_radians * (1 if relative_y < 0 else -1)
        else:
            # Ball moving right, reflect to the left
            vx = -abs(current_speed * 0.5)  # Mostly horizontal (leftward)
            vy = current_speed * angle_radians * (1 if relative_y < 0 else -1)

        return Vector2D(x=vx, y=vy)
