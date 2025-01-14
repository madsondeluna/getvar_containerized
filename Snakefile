rule all:
    input:
        "flask_running"

rule install_dependencies:
    output:
        "dependencies_installed"
    shell:
        """
        pip install -r requirements.txt && touch dependencies_installed
        """

rule run_flask:
    input:
        "dependencies_installed"
    output:
        "flask_running"
    shell:
        """
        python3 main.py
        """

