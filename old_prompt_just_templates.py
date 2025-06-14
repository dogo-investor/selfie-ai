import json

# Load the presets from a JSON file
with open("presets.json", "r") as f:
    presets = json.load(f)

# Template with variable keys
template = """
A cinematic handheld {camera_style} medium shot, set in a {location} in the {time_of_day}. {main_character} in {main_character_outfit} holds the camera at arm’s length, {face_visibility}, as sunlight glistens in from {light_source}. His {outfit_material} is glossy and shining. Behind him, {background_setting} – {background_activity}. The {location_description}. {main_character} slowly pans the camera sideways, revealing {secondary_character} {secondary_action_description}. Sun glistens off his frame as it shines through the window. Back on camera, {main_character} yells with a sense of urgency: “{dialogue_line}”
"""

def generate_prompt(universe_key):
    key = universe_key.strip().lower()
    if key not in presets:
        return f"❌ No preset available for '{universe_key}'. Try one of: {', '.join(presets.keys())}"
    
    return template.format(**presets[key]).strip()

# Command-line test
if __name__ == "__main__":
    user_input = input("🎥 Enter a movie/show title (e.g., Barbie, Toy Story, Star Wars): ")
    print("\nGenerated Prompt:\n")
    print(generate_prompt(user_input))
