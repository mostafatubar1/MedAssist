export type UserRole = "patient" | "doctor" | "admin";
export type QuestionStatus = "pending" | "answered";
export type MessageRole = "patient" | "doctor" | "assistant" | "system";

export interface Citation {
  title: string;
  url: string;
  snippet: string | null;
}

export interface ConversationMessage {
  role: MessageRole;
  content: string;
  timestamp: string;
}

export interface User {
  id: string;
  email: string;
  role: UserRole;
  created_at: string;
}

export interface Patient {
  id: string;
  user_id: string;
  profile: Record<string, string | null>;
  created_at: string;
}

export interface Question {
  id: string;
  patient_id: string;
  doctor_id: string | null;
  text: string;
  status: QuestionStatus;
  created_at: string;
}

export interface Answer {
  id: string;
  question_id: string;
  text: string;
  sources: Citation[];
  grounding_confidence: number;
  created_at: string;
}

export interface PainReport {
  id: string;
  patient_id: string;
  body_region: string;
  pain_type: string;
  severity: number;
  duration: string;
  created_at: string;
}

export interface ConversationMemory {
  id: string;
  patient_id: string;
  doctor_id: string;
  messages: ConversationMessage[];
  updated_at: string;
}

export interface AuditLogEntry {
  id: string;
  actor_id: string;
  action: string;
  target_id: string | null;
  timestamp: string;
  prev_hash: string | null;
  hash: string;
}

export interface ConsentSetting {
  id: string;
  patient_id: string;
  data_category: string;
  shared: boolean;
}

export interface SignupRequest {
  email: string;
  password: string;
  role: UserRole;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface AuthToken {
  access_token: string;
  token_type: "bearer";
  user: User;
}

export interface QuestionCreate {
  patient_id: string;
  doctor_id: string | null;
  text: string;
}

export interface PainReportCreate {
  patient_id: string;
  body_region: string;
  pain_type: string;
  severity: number;
  duration: string;
}

export interface ConsentSettingUpdate {
  patient_id: string;
  data_category: string;
  shared: boolean;
}

export interface ApiMessage {
  message: string;
}
