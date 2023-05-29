import pytest
from sta_que.stack_and_queue import Stack, Queue , PseudoQueue

def test_stack_push_one_value():
    stack = Stack()
    stack.push(1)
    assert stack.top.value == 1


def test_stack_push_multiple_values():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.top.value == 3


def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    value = stack.pop()
    assert value == 2
    assert stack.top.value == 1

def test_stack_empty_after_multiple_pops():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.is_empty()


def test_stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    value = stack.peek()
    assert value == 2
    assert stack.top.value == 2


def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty()


def test_stack_pop_on_empty_stack_raises_exception():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()


def test_stack_peek_on_empty_stack_raises_exception():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()


# Queue tests
def test_queue_enqueue_one_value():
    queue = Queue()
    queue.enqueue(1)
    assert queue.front.value == 1
    assert queue.back.value == 1


def test_queue_enqueue_multiple_values():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.front.value == 1
    assert queue.back.value == 3


def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    value = queue.dequeue()
    assert value == 1
    assert queue.front.value == 2


def test_queue_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    value = queue.peek()
    assert value == 1
    assert queue.front.value == 1


def test_queue_empty_after_multiple_dequeues():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty()


def test_queue_is_empty():
    queue = Queue()
    assert queue.is_empty()


def test_queue_dequeue_on_empty_queue_raises_exception():
    queue = Queue()
    with pytest.raises(Exception):
        queue.dequeue()


def test_queue_peek_on_empty_queue_raises_exception():
    queue = Queue()
    with pytest.raises(Exception):
        queue.peek()    




def test_pseudo_queue_happy_path():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() == 5
    assert queue.dequeue() == 6


def test_pseudo_queue_empty():
    queue = PseudoQueue()
    with pytest.raises(Exception):
        queue.dequeue()
