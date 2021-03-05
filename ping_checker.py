import multiprocessing
import subprocess

def check_host_status(host_id):
    ping_cmd = ["ping", "-c", "2", host_id]
    try:
        _ = subprocess.check_output(ping_cmd)
    except subprocess.CalledProcessError:
        host_reachable = False
    else:
        host_reachable = True

    return host_reachable


def main():
    with open('hosts_list.txt', "r") as fd:
        hosts_raw = fd.readlines()

    hosts = [h.strip() for h in hosts_raw if not h.startswith('#') and len(h.strip())]

    mp = multiprocessing.Pool()
    ping_results = mp.map(check_host_status, hosts)

    for host, host_status in zip(hosts, ping_results):
        host_availabilty = "UP" if host_status else "DOWN"
        print("[{:^4}] {}".format(host_availabilty, host))


if __name__ == "__main__":
    main()
