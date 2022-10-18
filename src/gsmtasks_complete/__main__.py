import asyncio
import datetime as dt
import logging
from typing import Optional

import asyncclick as click
import pytz
from gsmtasks.client import ApiClient
from gsmtasks.components.schemas.action_enum import ActionEnum
from gsmtasks.components.schemas.account_role import AccountRole
from gsmtasks.components.schemas.nested_address import NestedAddress
from gsmtasks.components.schemas.task_command import TaskCommand
from gsmtasks.components.schemas.task_serializer_v2 import TaskSerializerV2
from gsmtasks.components.schemas.task_state_enum import TaskStateEnum
from gsmtasks.paths.tasks_list.param_model import TasksListState

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

tz = pytz.timezone('Europe/Vienna')


@click.command()
@click.option('--token', type=click.STRING, envvar='TOKEN')
@click.option('--account_id', type=click.STRING, required=False, envvar='ACCOUNT')
async def main(token: str, account_id: Optional[str]):
    client = ApiClient(token)

    if account_id is None:
        account = (await client.accounts_list(q_page_size=1))[0]
        account_id = str(account.id)

    account_url = f'https://api.gsmtasks.com/accounts/{account_id}/'
    account_role = (await client.account_roles_list(q_account=account_id, q_is_active=True, q_is_worker="true"))[0]

    await process_tasks(account_role, account_url, client)


async def process_tasks(account_role: AccountRole, account_url: str, client: ApiClient):
    new_task = TaskSerializerV2(
        account=account_url,
        category='assignment',
        description='test task',
        address=NestedAddress(raw_address="Bahnstrasse 83A, 2120 Wolkersdprf im Weinviertel, Österreich"),
        assignee=account_role.user,
    )

    tasks = await client.tasks_create([new_task] * 2)
    logger.debug('Created tasks %s',
                 [task_.id for task_ in await client.tasks_list(q_id__in=[task_.id for task_ in tasks])])

    task = tasks[0]
    logger.info('Working with %s', task.id)

    await client.task_commands_create(TaskCommand(
        account=account_url,
        task=task.url,
        time=dt.datetime.now(),
        action=ActionEnum.complete,
    ))

    await wait_until_completed(task, client)

    since = tz.localize(dt.datetime.combine(dt.date.today(), dt.time.min)) - dt.timedelta(days=3)
    logger.debug('Since: %s', since.isoformat(timespec='seconds'))

    task_list = await client.tasks_list(
        q_state=TasksListState.completed,
        q_ordering='last_completed_at',
        q_updated_at__gte=since.isoformat(timespec='seconds')
    )
    logger.info('%s%s found', task.id, '' if task.id in [task_.id for task_ in task_list] else ' NOT')

    logger.debug('Found %s',[task_.id for task_ in task_list])


async def wait_until_completed(task: TaskSerializerV2, client: ApiClient) -> None:
    # make sure task is completed
    while True:
        task_completed = await client.tasks_retrieve(p_id=task.id)
        logger.info(task_completed.state)

        if task_completed.state == TaskStateEnum.completed.value:
            break

        await asyncio.sleep(1.)


if __name__ == '__main__':
    logging.basicConfig()
    main()
