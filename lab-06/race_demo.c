#include <pthread.h>
#include <stdio.h>

#define THREADS 4
#define ITERS 1000000

// Спільний лічильник без засобів синхронізації
static int counter = 0;

void *worker(void *arg) {
    (void)arg;
    for (int i = 0; i < ITERS; i++) {
        // Неатомарна операція: читання в регістр -> інкремент -> запис у пам'ять
        counter++;
    }
    return NULL;
}

int main(void) {
    pthread_t threads[THREADS];

    for (int i = 0; i < THREADS; i++) {
        pthread_create(&threads[i], NULL, worker, NULL);
    }

    for (int i = 0; i < THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Очікувано: %d\n", THREADS * ITERS);
    printf("Отримано:  %d\n", counter);
    return 0;
}
