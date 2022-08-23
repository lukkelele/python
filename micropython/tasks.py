 
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
static uint led_status;

void init_pins() {
    gpio_init(LED_1);
    gpio_init(LED_15);
    gpio_init(BUTTON);
    gpio_init(LED_PIN);
    gpio_set_dir(LED_1,  GPIO_OUT);
    gpio_set_dir(LED_15, GPIO_OUT);
    gpio_set_dir(BUTTON, GPIO_IN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
}

void boardLED_task(void *pvParameters)
{
    const uint LED_PIN = PICO_DEFAULT_LED_PIN;

    while (true) {
        gpio_put(LED_PIN, 1);
        gpio_put(LED_1, 1);
        vTaskDelay(100);

        gpio_put(LED_PIN, 0);
        gpio_put(LED_1, 0);
        vTaskDelay(100);

    }
}

void button_task(void *pvParameters) {
    while (1) {
    // Check if button is pressed
        toggled = false;
        while (gpio_get(BUTTON) != 0) {
          // if HIGH -> Button pressed
          if (led_status == 0 & toggled == false) {
              gpio_put(LED_15, 1);
              led_status = 1;
              toggled = true;
          }
          if (led_status == 1 & toggled == false) {
              gpio_put(LED_15, 0);
              led_status = 0;
              toggled = true;
          }
        }
    }
}



int main()
{
    stdio_init_all();
    init_pins();
    xTaskCreate(boardLED_task, "boardLED_task", 256, NULL, 1, NULL);
    xTaskCreate(button_task, "button_task", 256, NULL, 1, NULL);
    vTaskStartScheduler();

    while (1) { };
}
