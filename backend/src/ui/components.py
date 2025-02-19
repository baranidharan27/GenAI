# src/ui/components.py
import streamlit as st
from typing import List, Callable, Tuple
from src.config.settings import UIConfig

class UIComponents:
    @staticmethod
    def setup_page_config(config: UIConfig):
        st.set_page_config(
            page_title=config.page_title,
            page_icon=config.page_icon,
            layout=config.layout
        )
    
    @staticmethod
    def create_sidebar(config: UIConfig) -> Tuple[int, str]:
        st.sidebar.title("Settings")
        
        max_length = st.sidebar.slider(
            "Maximum Length",
            min_value=config.min_length,
            max_value=config.max_length,
            value=config.default_length,
            step=config.length_step
        )
        
        theme = st.sidebar.radio(
            "Theme",
            options=config.available_themes,
            index=0
        )
        
        return max_length, theme
    
    @staticmethod
    def create_main_content() -> str:
        st.title("Content Generator")
        st.subheader("Easily generate factual answers to your questions!")
        st.write("Enter a query below to get a direct and concise response.")
        return st.text_input("Your Question:")
    
    @staticmethod
    def show_examples(config: UIConfig, callback: Callable):
        st.subheader("Example Prompts")
        selected = st.radio(
            "Select an example:",
            options=config.default_examples
        )
        if st.button("Use Example"):
            callback(selected)