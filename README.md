# Операційні системи. Лабораторні роботи №1–6

**Предмет:** Операційні системи  
**Спеціальність:** Інженерія програмного забезпечення  
**Група:** ІПЗ-41  
**Виконала:** Єва Якимчук  
**Платформа курсу:** [omc-learning.online — Операційні системи](https://www.omc-learning.online/courses/operational_systems)

---

## Структура репозиторію

```
operational-systems/
├── README.md                                # Головний опис та інструкції компіляції
├── lab-01/                                  # Лабораторна №1: GNU Bash та фільтри
│   ├── data/
│   │   ├── readings.txt
│   │   └── measurements.txt
│   ├── backup/
│   │   └── readings-renamed.txt
│   ├── reports/
│   │   └── report.txt
│   ├── setup.sh                             # Ідемпотентний скрипт розгортання
│   └── README.md                            # Звіт з детальним аналізом
├── lab-02/                                  # Лабораторна №2: Системні виклики та файлові дескриптори
│   ├── fd_demo.c                            # Демонстрація open, write, read, lseek, close
│   ├── copy_file.c                          # Буферизований копіювач файлів (4 КБ)
│   ├── notes.txt
│   ├── notes-copy.txt
│   └── README.md
├── lab-03/                                  # Лабораторна №3: Керування процесами
│   ├── process_demo.c                       # fork, exec (execlp), waitpid, WEXITSTATUS
│   ├── worker_children.c                    # Множинні нащадки, SIGABRT, аналіз кодів
│   └── README.md
├── lab-04/                                  # Лабораторна №4: Потоки POSIX Threads
│   ├── threads_demo.c                       # pthread_create, pthread_join, аргументи
│   ├── sum_array.c                          # Паралельне сумування зрізів масиву (1..100)
│   └── README.md
├── lab-05/                                  # Лабораторна №5: Планування процесора
│   ├── scheduler_sim.c                      # Симулятор C: FCFS, SJF, Round-Robin (q=1,2,4)
│   ├── scheduler_sim.py                     # Симулятор Python із розширенням P5
│   ├── results.txt                          # Зведені таблиці метрик W, T, R
│   └── README.md
└── lab-06/                                  # Лабораторна №6: Синхронізація (м'ютекси, семафори)
    ├── race_demo.c                          # Відтворення стану гонитви (Race Condition)
    ├── race_fixed.c                         # Захист критичної секції м'ютексом
    ├── semaphore_demo.c                     # Лічильний семафор POSIX (MAX_ACTIVE=2)
    └── README.md
```

---

## Зведена таблиця лабораторних робіт та інструкції запуску

| № | Назва роботи | Ключові технології | Команди компіляції та запуску |
|---|---|---|---|
| **1** | Навігація, маніпулювання файловою ієрархією та базова фільтрація даних у GNU Bash | `bash`, `cat`, `grep`, `sort`, `cut`, `uniq`, `wc`, `tail`, `pipeline` | `cd lab-01`<br>`chmod +x setup.sh && ./setup.sh` |
| **2** | Системні виклики ядра Linux для роботи з файловими дескрипторами | `open`, `read`, `write`, `lseek`, `close`, `errno`, `strace` | `cd lab-02`<br>`gcc -Wall -Wextra -pedantic -o fd_demo fd_demo.c && ./fd_demo`<br>`gcc -Wall -Wextra -pedantic -o copy_file copy_file.c && ./copy_file notes.txt notes-copy.txt` |
| **3** | Керування життєвим циклом процесів у C/Linux | `fork`, `execlp`, `waitpid`, `WIFEXITED`, `WIFSIGNALED`, `SIGABRT` | `cd lab-03`<br>`gcc -Wall -Wextra -pedantic -o process_demo process_demo.c && ./process_demo`<br>`gcc -Wall -Wextra -pedantic -o worker_children worker_children.c && ./worker_children` |
| **4** | Створення та керування потоками POSIX Threads | `pthread_create`, `pthread_join`, `void*` arguments, `Data Race Freedom` | `cd lab-04`<br>`gcc -Wall -Wextra -pedantic -pthread -o threads_demo threads_demo.c && ./threads_demo`<br>`gcc -Wall -Wextra -pedantic -pthread -o sum_array sum_array.c && ./sum_array` |
| **5** | Моделювання алгоритмів планування процесора | `FCFS`, `SJF`, `Round-Robin`, метрики `Waiting Time`, `Turnaround`, `Response` | `cd lab-05`<br>`gcc -Wall -Wextra -pedantic -o scheduler_sim scheduler_sim.c && ./scheduler_sim`<br>`python3 scheduler_sim.py` |
| **6** | Синхронізація потоків м'ютексами та семафорами | `Data Race`, `pthread_mutex_t`, `Mutual Exclusion`, `sem_t`, `Counting Semaphore` | `cd lab-06`<br>`gcc -Wall -Wextra -pedantic -pthread -o race_demo race_demo.c && ./race_demo`<br>`gcc -Wall -Wextra -pedantic -pthread -o race_fixed race_fixed.c && ./race_fixed`<br>`gcc -Wall -Wextra -pedantic -pthread -o semaphore_demo semaphore_demo.c && ./semaphore_demo` |

---

## Вимоги до середовища
* Операційна система: GNU/Linux (Ubuntu/Debian, Arch, Fedora або Windows Subsystem for Linux WSL2);
* Компілятор: GCC 9+ із підтримкою стандарту POSIX.1-2008 (`-Wall -Wextra -pedantic -pthread`);
* Інтерпретатор Python 3.8+ (для симулятора `lab-05`).
