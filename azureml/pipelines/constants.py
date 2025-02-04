from pathlib import Path

COMPONENTS_DIR = (Path(__file__).parent.parent / "components").absolute()

ENVIRONMENTS_DIR = (Path(__file__).parent.parent / "environments").absolute()

GUIDANCE_PROGRAMS_DIR = (
    Path(__file__).parent.parent.parent / "guidance_programs"
).absolute()

ENVIRONMENT_FILE = ENVIRONMENTS_DIR / "promptbase-env.yaml"

assert COMPONENTS_DIR.exists(), f"Did not find {COMPONENTS_DIR}"
assert ENVIRONMENT_FILE.exists(), f"Did not find {ENVIRONMENT_FILE}"
assert GUIDANCE_PROGRAMS_DIR.exists(), f"Did not find {GUIDANCE_PROGRAMS_DIR}"
