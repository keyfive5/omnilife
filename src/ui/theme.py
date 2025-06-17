APP_STYLESHEET = """
QWidget {
    background-color: #23272e;
    color: #e6e6e6;
    font-family: 'Segoe UI', 'Arial', sans-serif;
    font-size: 15px;
}

QTabWidget::pane {
    border: 1px solid #444;
    border-radius: 8px;
    margin: 8px 0 0 0;
    background: #181a20;
}

QTabBar::tab {
    background: #23272e;
    color: #e6e6e6;
    border: 1px solid #444;
    border-bottom: none;
    border-radius: 8px 8px 0 0;
    min-width: 120px;
    min-height: 32px;
    margin-right: 2px;
    padding: 8px 20px;
    font-weight: 500;
    transition: background 0.2s;
}
QTabBar::tab:selected {
    background: #2d313a;
    color: #00e1d6;
    border-bottom: 2px solid #00e1d6;
}
QTabBar::tab:hover {
    background: #2d313a;
    color: #00e1d6;
}

QLabel {
    font-size: 16px;
}

QProgressBar {
    border: 1px solid #444;
    border-radius: 6px;
    background: #181a20;
    height: 18px;
    text-align: right;
}
QProgressBar::chunk {
    background-color: #00e1d6;
    border-radius: 6px;
}

QPushButton {
    background-color: #00e1d6;
    color: #181a20;
    border: none;
    border-radius: 6px;
    padding: 8px 24px;
    font-weight: 600;
    font-size: 15px;
    margin: 0 8px;
}
QPushButton:disabled {
    background-color: #444;
    color: #888;
}
QPushButton:hover:!disabled {
    background-color: #00bfae;
}

#HeaderBar {
    background: #181a20;
    border-bottom: 1px solid #333;
    min-height: 56px;
    max-height: 56px;
    padding: 0 24px;
}
#HeaderTitle {
    font-size: 24px;
    font-weight: bold;
    color: #00e1d6;
    letter-spacing: 1px;
}
""" 