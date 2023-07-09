import subprocess

command = './trex-console'  # Путь к исполняемому файлу trex-console
input_text = 'print("!")\n'  # Текст команды для передачи в trex-console

# Выполнение команды и передача текста ввода через stdin
process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate(input_text.encode())

# Вывод результата выполнения команды и ошибок (если есть)
print(output.decode())
print(error.decode())