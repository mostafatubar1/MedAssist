"""initial shared data model

Revision ID: 0001_initial
Revises:
"""
from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("email", sa.String(320), nullable=False),
        sa.Column("role", sa.String(20), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.UniqueConstraint("email"),
    )
    op.create_index("ix_users_email", "users", ["email"])
    op.create_table("user_credentials",
        sa.Column("user_id", sa.Uuid(), sa.ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
        sa.Column("password_hash", sa.String(512), nullable=False),
    )
    op.create_table("patients",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("user_id", sa.Uuid(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("profile", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.UniqueConstraint("user_id"),
    )
    op.create_index("ix_patients_user_id", "patients", ["user_id"])
    op.create_table("questions",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("patient_id", sa.Uuid(), sa.ForeignKey("patients.id"), nullable=False),
        sa.Column("doctor_id", sa.Uuid(), sa.ForeignKey("users.id"), nullable=True),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("status", sa.String(20), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_questions_patient_id", "questions", ["patient_id"])
    op.create_index("ix_questions_doctor_id", "questions", ["doctor_id"])
    op.create_table("answers",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("question_id", sa.Uuid(), sa.ForeignKey("questions.id"), nullable=False),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("sources", sa.JSON(), nullable=False),
        sa.Column("grounding_confidence", sa.Float(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.UniqueConstraint("question_id"),
    )
    op.create_index("ix_answers_question_id", "answers", ["question_id"])
    op.create_table("pain_reports",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("patient_id", sa.Uuid(), sa.ForeignKey("patients.id"), nullable=False),
        sa.Column("body_region", sa.String(120), nullable=False),
        sa.Column("pain_type", sa.String(120), nullable=False),
        sa.Column("severity", sa.Integer(), nullable=False),
        sa.Column("duration", sa.String(120), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_pain_reports_patient_id", "pain_reports", ["patient_id"])
    op.create_table("conversation_memories",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("patient_id", sa.Uuid(), sa.ForeignKey("patients.id"), nullable=False),
        sa.Column("doctor_id", sa.Uuid(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("messages", sa.JSON(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_conversation_memories_patient_id", "conversation_memories", ["patient_id"])
    op.create_index("ix_conversation_memories_doctor_id", "conversation_memories", ["doctor_id"])
    op.create_table("audit_log_entries",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("actor_id", sa.Uuid(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("action", sa.String(255), nullable=False),
        sa.Column("target_id", sa.Uuid(), nullable=True),
        sa.Column("timestamp", sa.DateTime(timezone=True), nullable=False),
        sa.Column("prev_hash", sa.String(128), nullable=True),
        sa.Column("hash", sa.String(128), nullable=False),
    )
    op.create_index("ix_audit_log_entries_actor_id", "audit_log_entries", ["actor_id"])
    op.create_table("consent_settings",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("patient_id", sa.Uuid(), sa.ForeignKey("patients.id"), nullable=False),
        sa.Column("data_category", sa.String(120), nullable=False),
        sa.Column("shared", sa.Boolean(), nullable=False),
    )
    op.create_index("ix_consent_settings_patient_id", "consent_settings", ["patient_id"])


def downgrade() -> None:
    for table in ["consent_settings", "audit_log_entries", "conversation_memories", "pain_reports", "answers", "questions", "patients", "user_credentials", "users"]:
        op.drop_table(table)
