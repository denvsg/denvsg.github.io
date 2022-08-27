#
import asyncio
import time
from random import randint


@asyncio.coroutine
def start_state():
    print("start state called")
    input_value = randint(0, 1)
    time.sleep(1)
    if input_value == 0:
        result = yield from state2(input_value)
    else:
        result = yield from state1(input_value)
    print("resume of the Transition:")
    print(f"start calling {result}")


@asyncio.coroutine
def state1(transition_value):
    output_value = str(f"state 1 with translation value= {transition_value}")
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating...")
    if input_value == 0:
        result = yield from state3(input_value)
    else:
        result = yield from state2(input_value)

    result = f"state 1 calling {result}"
    return output_value + str(result)


@asyncio.coroutine
def state2(transition_value):
    output_value = str(f"state 2 with translation value= {transition_value}")
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating...")
    if input_value == 0:
        result = yield from state1(input_value)
    else:
        result = yield from state3(input_value)

    result = f"state 2 calling {result}"
    return output_value + str(result)


@asyncio.coroutine
def state3(transition_value):
    output_value = str(f"state 3 with translation value= {transition_value}")
    input_value = randint(0, 1)
    time.sleep(1)
    print("...Evaluating...")
    if input_value == 0:
        result = yield from state1(input_value)
    else:
        result = yield from state_end(input_value)

    result = f"state 3 calling {result}"
    return output_value + str(result)


@asyncio.coroutine
def state_end(transition_value):
    output_value = str(f"state END with translation value= {transition_value}")
    time.sleep(1)
    print("...STOP Computation...")
    return output_value


if __name__ == "__main__":
    print("Finite state machine simulation with Asyncio Coroutine")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_state())
    loop.close()
