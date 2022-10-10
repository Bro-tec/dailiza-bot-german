"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"geht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"Ich brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],

    [r"Ich möchte (.*)",
    ["Warum möchtest du {0}?",
    "Würde {0} dich denn wirklich glücklich machen?",
    "Ich kann dich verstehen, manchmal möchte ich ebenfalls  {0}."]],


    [r"Ich lerne gerade (.*)",
    ["Lernst du gerne {0}?",
    "Ist {0} dein Lieblingsthema? ",
    "Ich wäre auch gerne ein {0} Profi."]],




]
