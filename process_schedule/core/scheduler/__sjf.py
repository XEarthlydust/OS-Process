from .__scheduler import Scheduler as __Scheduler


class SJF(__Scheduler):
    from .. import PCB as __PCB

    def __call__(self, time: int,
                 ready_queue: list[__PCB]):

        shortest_pcb = ready_queue[0]
        for pcb_time_check in ready_queue:
            if pcb_time_check.is_running:
                shortest_pcb = pcb_time_check
            elif shortest_pcb.remain_time > pcb_time_check.remain_time:
                shortest_pcb = pcb_time_check

        pcb = shortest_pcb
        if pcb.is_running:
            return pcb.remain_time

        if pcb.is_ready:
            return pcb.run(time)
