import psutil
from terminaltables import AsciiTable
from termcolor import colored

def get_remote_connections():
    remote_connections = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.raddr:
            remote_connections.append([conn.pid, conn.status, conn.laddr, conn.raddr])
    return remote_connections

def get_running_commands():
    running_commands = []
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        cmdline = process.info['cmdline']
        if cmdline:
            running_commands.append([process.info['pid'], process.info['name'], ' '.join(list(cmdline))])
        else:
            running_commands.append([process.info['pid'], process.info['name'], ''])
    return running_commands


def get_server_traffic():
    sent = psutil.net_io_counters().bytes_sent
    received = psutil.net_io_counters().bytes_recv
    return sent, received

def main():
    print(colored('\n[ Remote Connections ]\n', 'yellow'))
    remote_connections = get_remote_connections()
    table_data = [['PID', 'Status', 'Local Address', 'Remote Address']]
    for conn in remote_connections:
        table_data.append(conn)
    table = AsciiTable(table_data)
    print(table.table)

    print(colored('\n[ Running Commands ]\n', 'yellow'))
    running_commands = get_running_commands()
    table_data = [['PID', 'Name', 'Command Line']]
    for command in running_commands:
        table_data.append(command)
    table = AsciiTable(table_data)
    print(table.table)

    print(colored('\n[ Server Traffic ]\n', 'yellow'))
    sent, received = get_server_traffic()
    table_data = [['Bytes Sent', 'Bytes Received'], [sent, received]]
    table = AsciiTable(table_data)
    print(table.table)

if __name__ == '__main__':
    main()
