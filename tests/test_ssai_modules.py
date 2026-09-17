import pytest
import os
import sys

# Add parent directory to path so modules can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules import molecular, adme, aop, skin_models, qra, auth, export, validation, agents, hitl, batch

def test_modules_exist_and_callable():
    """Verify that all core module render functions exist and are callable."""
    assert callable(molecular.render_molecular_module)
    assert callable(adme.render_adme_module)
    assert callable(aop.render_aop_module)
    assert callable(skin_models.render_skin_models_module)
    assert callable(qra.render_qra_module)
    assert callable(batch.render_batch_module)
    assert callable(agents.render_agent_hub_module)
    assert callable(hitl.render_hitl_module)
    assert callable(validation.render_validation_module)
    assert callable(export.render_export_module)
    assert callable(auth.render_auth_module)

def test_verify_system_script():
    """Verify that the verification script runs successfully."""
    verify_script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../verify_system.py'))
    assert os.path.exists(verify_script_path)
    exit_code = os.system(f"python3 {verify_script_path}")
    assert exit_code == 0
