 
#include <FreeRTOS.h>
#include <task.h>
#include <queue.h>
#include <stdio.h>
#include "pico/stdlib.h"

#define LED_1   0U
#define BUTTON  14U
#define LED_15  15U

static QueueHandle_t xQueue = NULL;
const uint LED_PIN = PICO_DEFAULT_LED_PIN;

void init_pins() {
    gpio_init(LED_1);
    gpio_init(LED_15);
    gpio_init(BUTTON);
    gpio_set_dir(LED_1,  GPIO_OUT);
    gpio_set_dir(LED_15, GPIO_OUT);
    gpio_set_dir(BUTTON, GPIO_IN);
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
}

void boardLED_task(void *pvParameters)
{
    uint sendVal = 0;
    const uint LED_PIN = PICO_DEFAULT_LED_PIN;
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    while (true) {
        gpio_put(LED_PIN, 1);
        //gpio_put(LED_15, 1);
        vTaskDelay(100);

        gpio_put(LED_PIN, 0);
        //gpio_put(LED_15, 0);
        vTaskDelay(100);

    }
}

void touchSensor_task(void *pvParameters) {
  uint pin_val;
  for ( ;; ) {
    xQueueReceive(xQueue, &pin_val, portMAX_DELAY);
    if (pin_val == 1) {
      gpio_put(LED_1, 0);
      printf(">> LED STATUS\n   ON --> OFF");
    }
    if (pin_val == 0) {
      gpio_put(LED_1, 1);
      printf(">> LED STATUS\n   OFF --> ON");
    }
  }
}

void button_task(void *pvParameters) {
    uint pin_val;
    while (1) {
        xQueueReceive(xQueue, &pin_val, portMAX_DELAY);
        if (pin_val == 1) {
            if (gpio_get(LED_1) == 1) { // if already toggled
                gpio_put(LED_1, 0);
            } else {
                gpio_put(LED_1, 1);
            }
        }
    }
}


int main()
{
    stdio_init_all();
    //init_pins();
    xTaskCreate(boardLED_task, "boardLED_task", 256, NULL, 1, NULL);
    //xTaskCreate(touchSensor_task, "touchSensor_task", 256, NULL, 1, NULL);
    //xTaskCreate(button_task, "button_task", 256, NULL, 1, NULL);
    vTaskStartScheduler();

    while (1) { };
}
