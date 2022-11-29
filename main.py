from typing import Union, List, Tuple
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
    def __init__(self, tasks: List[Task], executor_count: int):
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
        self.__tasks: List[Task] = tasks
        self.__executor_count: int = executor_count
        self.__executor_tasks: List[List[dict[str:Task, str: int]]] =\
            [[] for i in range(executor_count)]
        self.__totaltime: int = self.__calculate_totaltime()
        self.__duration: int = self.__calculate_duration()
        self.__downtime: int = self.__calculate_downtime()
        self.__distribute_tasks()

    @property
    def tasks(self) -> Tuple[Task]:
        return tuple(self.__tasks)

    @property
    def task_count(self) -> int:
        return len(self.__tasks)

    @property
    def executor_count(self) -> int:
        return self.__executor_count

    @property
    def duration(self) -> int:
        return self.__duration

    @property
    def downtime(self) -> int:
        return self.__downtime

    @property
    def totaltime(self) -> int:
        return self.__totaltime

    def get_downtime_for_executor(self, executor_idx: int) -> int:
        """Returns the downtime duration for the executor.

        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the downtime duration for the executor.
        """
        if type(executor_idx) != int:
            raise InternalScheduleException
        if executor_idx + 1 > self.executor_count:
            raise InternalScheduleException

        s = self.totaltime - (executor_idx + 1) * self.duration
        if s > 0:
            return 0
        else:
            return 0 - s

    def get_schedule_for_executor(self, executor_idx: int) -> str:
        """Returns the schedule for the executor.

        :param executor_idx: the index for executor.
        :raise InternalScheduleException: when the executor_idx parameter is
            not int, when the executor_idx parameter value is greater ot equal
            than the number of the executors.
        :return: the schedule for the executor.
        """
        if type(executor_idx) != int:
            raise InternalScheduleException
        if executor_idx + 1 > self.executor_count:
            raise InternalScheduleException

        start = self.duration * executor_idx
        end = start + self.duration
        current = 0
        s = ''
        t = 0
        j = 1
        for task in self.__tasks:
            current += task.duration
            if current > start and current - task.duration < end :
                time = current - start
                if time > self.duration:
                    time = self.duration
                s += str(j) + '. task: ' + task.name + ' from ' + str(t) +' to ' + str(time) + '\n'
                j+=1
                t = time
        if t < self.duration:
            s += str(j) + '. task: downtime from ' + str(t) + ' to ' + str(self.duration) + '\n'
        return s

    def __calculate_totaltime(self) -> int:
        s = 0
        for task in self.__tasks:
            s += task.duration
        return s

    def __calculate_duration(self) -> int:
        m = 0
        for task in self.__tasks :
            m = max(m,task.duration)
        s = self.totaltime / self.__executor_count
        s = math.ceil(s)

        return max(s,m)

    def __calculate_downtime(self) -> int:
        return self.duration * self.__executor_count - self.totaltime

    def __distribute_tasks(self) -> None:
        pass

    @staticmethod
    def __get_param_error(tasks: List[Task]) -> Union[str, None]:
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
