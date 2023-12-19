import sys

import pytest

from svmpsp_graphnetviz.cli import entrypoint


def test_cli_entrypoint_help(monkeypatch):
    with pytest.raises(SystemExit) as system_err:
        with monkeypatch.context() as monkey_context:
            monkey_context.setattr(sys, "argv", [sys.argv[0], "-h"])
            entrypoint()
    assert system_err.value.code == 0


def test_cli_entrypoint_with_defaults(monkeypatch):
    with monkeypatch.context() as monkey_context:
        monkey_context.setattr(sys, "argv", [sys.argv[0]])
        entrypoint()
        assert True
