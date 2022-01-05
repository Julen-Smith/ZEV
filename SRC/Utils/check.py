def check_clase(author,ctx):
    def inner_check(message):
        if message.content == "Ladrón" :
             return message.author == author and message.content == "Ladrón"
        elif message.content == "Mago" :
            return message.author == author and message.content == "Mago"
        elif message.content == "Mercenario" :
            return message.author == author and message.content == "Mercenario"
    return inner_check