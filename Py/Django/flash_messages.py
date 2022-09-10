#f lash messages

messages.success(request, 'Login successful')
messages.error(request, 'Login error')

# Message tags
# debug, info, success, warning and error

# Display flash in template 
{% if messages %} 
    {% for message in messages %} 
        {% message %} 
        {% message.tags %}