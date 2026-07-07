"""
MyAgent Unified Router

Version: 13.0.0
"""

from core.intent_router import route
from core.project_router import route_project
from core.planner import plan_task


def decide(user):
    """
    Route a user request.

    Priority:
        1. Project commands
        2. Intent commands
        3. AI Planner
    """

    # Project commands
    plan = route_project(user)
    if plan is not None:
        return plan

    # Built-in intent commands
    plan = route(user)
    if plan is not None:
        return plan

    # AI Planner
    return plan_task(user)
