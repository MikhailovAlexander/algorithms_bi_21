from typing import Union
import math


from task import Task
from custom_exception import ScheduleArgumentException,\
    InternalScheduleException


TASK = 'task'
PART = 'part'
DOWNTIME = 'downtime'


class Schedule:
    """A class for calculating the optimal schedule for a list of tasks and the
    number of executors.

    Properties
    ----------
    tasks(self) -> tuple[Task]:
        Returns the source task tuple.

    task_count(self) -> int:
        Returns the source task count.

    executor_count(self) -> int:
        Returns the executor count.

    duration(self) -> int:
        Returns the schedule duration.

    downtime(self) -> int:
        Returns the downtime duration for all executors.

    Methods
    -------
    get_downtime_for_executor(self, executor_idx: int) -> int:
        Returns the downtime duration for the executor.

    get_schedule_for_executor(self, executor_idx: int) -> str:
        Returns the schedule for the executor.
    """
    def __init__(self, tasks: list[Task], executor_count: int):
        """Schedule class constructor to initialize the object.

        :param tasks: a source task list.
        :param executor_count: a number of executors for tasks.
        :raise ScheduleArgumentException: when the tasks parameter is not a
            list, when the task list is empty, when the task list contains
            not a Task object.
        """
        error_msg = Schedule.__get_param_error(tasks)
        if error_msg is not None:
            raise ScheduleArgumentException(error_msg)
        self.__tasks: list[Task] = tasks
        self.__executor_count: int = executor_count
        self.__executor_tasks: list[list[dict[str:Task, str: int]]] =\
            [[] for i in range(executor_count)]
        self.__duration: int = self.__calculate_duration()
        self.__distribute_tasks()

    @property
    def tasks(self) -> tuple[Task]:
        """Returns the source task tuple."""
        return tuple(self.__tasks)

    @property
    def task_count(self) -> int:
        """Returns the source task count."""
        return len(self.__tasks)

    @property
    def executor_count(self) -> int:
        """Returns the executor count."""
        return self.__executor_count

    @property
    def duration(self) -> int:
        """Returns the schedule duration."""
        return self.__calculate_duration()

    @property
    def downtime(self) -> int:
        """Returns the downtime duration for all executors."""
        total = 0
        for task in self.__tasks:
            total += task.duration
        return self.__duration * self.__executor_count - total

    def get_downtime_for_executor(self, executor_idx: int) -> int:
        """Returns the downtime duration for the executor.

        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the downtime duration for the executor.
        """
        if executor_idx + 1 != self.__executor_count:
            return 0
        return self.downtime

    def get_schedule_for_executor(self, executor_idx: int) -> str:
        """Returns the schedule for the executor.

        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the schedule for the executor.
        """
        task_number = 0
        s = ""
        point = 0
        for task in self.__executor_tasks[executor_idx]:
            s += f'{task_number + 1}. task: {task.name} from {point} to {point + task.duration}\n'
            task_number += 1
            point += task.duration
        return s

    def __calculate_duration(self) -> int:
        maximum = 0
        s = 0
        for task in self.__tasks:
            maximum = max(maximum, task.duration)
            s += task.duration

        if s % self.__executor_count != 0:
            s = int(s/self.__executor_count) + 1
        else:
            s /= self.__executor_count

        return max(maximum, s)

    def __distribute_tasks(self) -> None:
        taskNumber = 0
        timeLeft = 0
        for exNumber in range(self.__executor_count):
            duration = self.__duration
            while duration > 0 and taskNumber < self.task_count:
                currentTask = self.tasks[taskNumber]
                if timeLeft > 0:
                    timeForEx = timeLeft
                    timeLeft = 0
                    duration -= timeForEx
                elif currentTask.duration <= duration:
                    timeForEx = currentTask.duration
                    duration -= timeForEx
                else:
                    timeForEx = duration
                    timeLeft = currentTask.duration - duration
                    duration = 0
                    taskNumber -= 1
                self.__executor_tasks[exNumber].append(Task(f'{currentTask.name}', timeForEx))
                #self.__executor_tasks[exNumber].append({TASK: currentTask, PART: timeForEx})
                taskNumber += 1
        return

    @staticmethod
    def __get_param_error(tasks: list[Task]) -> Union[str, None]:
        pass

    def __get_executor_idx_error(self, executor_idx: int) -> Union[str, None]:
        pass


def main():
    tasks = [Task('a', 3), Task('b', 4), Task('c', 6), Task('d', 7),
             Task('e', 7), Task('f', 9), Task('g', 10), Task('h', 12),
             Task('i', 17)]
    schedule = Schedule(tasks, 5)
    print(f'Total duration: {schedule.duration}')
    print(f'Total downtime: {schedule.downtime}')
    for i in range(schedule.executor_count):
        print(f'\nExecutor # {i + 1}:')
        print(f'Downtime:  {schedule.get_downtime_for_executor(i)}')
        print(schedule.get_schedule_for_executor(i))


if __name__ == '__main__':
    main()
