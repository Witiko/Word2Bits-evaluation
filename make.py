import logging
from os import cpu_count
import subprocess


logger = logging.getLogger(__name__)


def make(targets, num_processes=1, directory='.'):
    """Uses GNU make to produce targets.

    Parameters
    ----------
    targets : str or iterable of str
        The names of the targets. If only a string is provided, it specifies the name of the only target.
    num_processes : int or 'all', optional
        The number of threads used to produce the targets. If all, then the number of threads is equal to
        the number of available CPU cores. One thread will be used when unspecified.
    directory : str, optional
        The pathname of a directory in which the targets will be made. The current working directory will
        be used when unspecified.
    """
    
    if num_processes == 'all':
        num_processes = cpu_count()
    
    if isinstance(targets, str):
        target = targets
        logger.info(
            'Making target {}{} in directory {}/'.format(
                target,
                ' using {} threads'.format(num_processes) if num_processes > 1 else '',
                directory,
            )
        )
    else:
        targets = list(targets)
        target = ' '.join(targets)
        logger.info(
            'Making {} targets{} in directory {}/'.format(
                len(targets),
                ' using {} threads'.format(num_processes) if num_processes > 1 else '',
                directory,
            )
        )

    command = 'nice -n 19 make -j {} -C {} {}'.format(num_processes, directory, target)
    exit_code = subprocess.call(command, shell=True)
    assert exit_code == 0, 'GNU Make exited with code {}'.format(exit_code)
    logger.info('Done making targets')
