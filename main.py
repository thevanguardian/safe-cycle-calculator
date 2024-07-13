import json
import argparse

def find_optimal_ips_to_remove(ip_app_dict, retain_percentage):
    app_count = {}
    for apps in ip_app_dict.values():
        for app in apps:
            if app in app_count:
                app_count[app] += 1
            else:
                app_count[app] = 1

    required_capacity = {app: max(1, int(count * retain_percentage / 100)) for app, count in app_count.items()}

    ip_contribution = []
    for ip, apps in ip_app_dict.items():
        contribution = sum([1 for app in apps if app_count[app] > required_capacity[app]])
        ip_contribution.append((ip, contribution))

    ip_contribution.sort(key=lambda x: x[1], reverse=True)

    removed_ips = []
    retained_capacity = app_count.copy()

    for ip, contribution in ip_contribution:
        can_remove = True
        for app in ip_app_dict[ip]:
            if retained_capacity[app] -1 < required_capacity[app]:
                can_remove = False
                break
            if can_remove:
                removed_ips.append(ip)
                for app in ip_app_dict[ip]:
                    retained_capacity[app] -= 1

    return removed_ips

def load_ip_app_dict_from_file(file_path):
    with open(file_path, 'r') as file:
        ip_app_dict = json.load(file)
    return ip_app_dict

def main():
    parser = argparse.ArgumentParser(description="Find optimal IPs to remove while retaining desired capacity. Will output JSON object containing safe to remove IP addresses and their associated applications.")
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the JSON file containing IP and application data.')
    parser.add_argument('-r', '--retain_percentage', type=int, default=50, help='Percentage of capacity to retain. (default: 50)')
    args=parser.parse_args()

    ip_app_dict = load_ip_app_dict_from_file(args.file)
    removed_ips = find_optimal_ips_to_remove(ip_app_dict, args.retain_percentage)

    removed_ip_dict = {ip: ip_app_dict[ip] for ip in removed_ips}
    print(json.dumps(removed_ip_dict, indent=4))

if __name__ == '__main__':
    main()
