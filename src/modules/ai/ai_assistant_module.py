from core.base_module import BaseModule
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt6.QtCore import Qt
import os

try:
    import openai
except ImportError:
    openai = None

try:
    import ollama
except ImportError:
    ollama = None

class AIAssistantModule(BaseModule):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.use_openai = openai and self.api_key
        self.use_ollama = (not self.use_openai) and ollama
        self.ollama_model = "llama2"
        super().__init__("AI Assistant")
        if openai and self.api_key:
            openai.api_key = self.api_key

    def _init_ui(self):
        layout = QVBoxLayout(self.widget)
        layout.setContentsMargins(32, 24, 32, 24)
        layout.setSpacing(16)

        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.chat_history.setPlaceholderText("Ask me anything... e.g. 'Summarize this text', 'What's the weather?', 'Give me a productivity tip.'")
        layout.addWidget(self.chat_history)

        input_layout = QHBoxLayout()
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type your question or command...")
        input_layout.addWidget(self.input_box)
        self.ask_button = QPushButton("Ask AI")
        input_layout.addWidget(self.ask_button)
        layout.addLayout(input_layout)

        self.status_label = QLabel("")
        layout.addWidget(self.status_label)

        self.ask_button.clicked.connect(self.ask_ai)
        self.input_box.returnPressed.connect(self.ask_ai)

        if not self.use_openai and not self.use_ollama:
            self.status_label.setText("No AI backend available. Install ollama (pip install ollama) and run 'ollama run llama2'.")

    def ask_ai(self):
        user_text = self.input_box.text().strip()
        if not user_text:
            return
        self.chat_history.append(f"<b>You:</b> {user_text}")
        self.input_box.clear()
        self.status_label.setText("Thinking...")
        self.ask_button.setEnabled(False)
        self.widget.repaint()

        if self.use_openai:
            self._ask_openai(user_text)
        elif self.use_ollama:
            self._ask_ollama(user_text)
        else:
            self.chat_history.append("<span style='color:#ff5555'><b>AI:</b> No AI backend available. Please install and run Ollama, or set OPENAI_API_KEY.</span>")
            self.status_label.setText("")
            self.ask_button.setEnabled(True)

    def _ask_openai(self, user_text):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_text}],
                max_tokens=256,
                temperature=0.7,
            )
            ai_text = response.choices[0].message.content.strip()
            self.chat_history.append(f"<b>AI:</b> {ai_text}")
        except Exception as e:
            self.chat_history.append(f"<span style='color:#ff5555'><b>AI:</b> Error: {e}</span>")
        self.status_label.setText("")
        self.ask_button.setEnabled(True)

    def _ask_ollama(self, user_text):
        try:
            response = ollama.chat(model=self.ollama_model, messages=[{"role": "user", "content": user_text}])
            ai_text = response['message']['content'].strip()
            self.chat_history.append(f"<b>AI:</b> {ai_text}")
        except Exception as e:
            self.chat_history.append(f"<span style='color:#ff5555'><b>AI:</b> Ollama error: {e}</span>")
        self.status_label.setText("")
        self.ask_button.setEnabled(True)

    def start(self):
        pass
    def stop(self):
        pass
    def get_status(self):
        status = super().get_status()
        status.update({
            "openai": self.use_openai,
            "ollama": self.use_ollama
        })
        return status 