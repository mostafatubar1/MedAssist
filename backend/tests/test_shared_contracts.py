import re
from pathlib import Path

from backend import models
from shared.python import schemas


CORE = [
    "User", "Patient", "Question", "Answer", "PainReport",
    "ConversationMemory", "AuditLogEntry", "ConsentSetting",
]

ORM = {
    "User": models.UserModel,
    "Patient": models.PatientModel,
    "Question": models.QuestionModel,
    "Answer": models.AnswerModel,
    "PainReport": models.PainReportModel,
    "ConversationMemory": models.ConversationMemoryModel,
    "AuditLogEntry": models.AuditLogEntryModel,
    "ConsentSetting": models.ConsentSettingModel,
}


def _ts_fields(interface_name: str) -> set[str]:
    source = Path("shared/types/index.ts").read_text(encoding="utf-8")
    match = re.search(rf"export interface {interface_name} \{{(.*?)\n\}}", source, re.S)
    assert match, f"Missing TypeScript interface: {interface_name}"
    return set(re.findall(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\??:", match.group(1), re.M))


def test_core_sqlalchemy_pydantic_and_typescript_contract_fields_match():
    for name in CORE:
        python_fields = set(getattr(schemas, name).model_fields)
        sqlalchemy_fields = set(ORM[name].__table__.columns.keys())
        typescript_fields = _ts_fields(name)
        assert python_fields == sqlalchemy_fields == typescript_fields, f"Contract drift in {name}"
