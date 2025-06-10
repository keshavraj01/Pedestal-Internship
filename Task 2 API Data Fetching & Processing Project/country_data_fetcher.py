import requests
import argparse
import csv
import json
from operator import itemgetter

API_URL = "https://restcountries.com/v3.1/all"

def fetch_country_data():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"❌ Error fetching data from API: {e}")
        return []

def process_data(data, region_filter=None):
    countries = []
    for country in data:
        try:
            name = country['name']['common']
            population = country.get('population', 0)
            region = country.get('region', 'Unknown')
            area = country.get('area', 0)
            if region_filter and region.lower() != region_filter.lower():
                continue
            countries.append({
                'name': name,
                'population': population,
                'region': region,
                'area': area
            })
        except KeyError:
            continue
    return countries

def display_summary(countries):
    total_population = sum(c['population'] for c in countries)
    print("\n🌍 Summary Statistics")
    print(f"Total Countries: {len(countries)}")
    print(f"Total Population: {total_population:,}")

def display_top_countries(countries, top_n=5):
    top = sorted(countries, key=itemgetter('population'), reverse=True)[:top_n]
    print(f"\n📊 Top {top_n} Countries by Population")
    for i, c in enumerate(top, 1):
        print(f"{i}. {c['name']} - {c['population']:,} people")

def save_to_csv(countries, filename="countries.csv"):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "population", "region", "area"])
        writer.writeheader()
        for c in countries:
            writer.writerow(c)
    print(f"\n💾 Data saved to {filename}")

def save_to_json(countries, filename="countries.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(countries, f, indent=4)
    print(f"\n💾 Data saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fetch and display country data from a public API.")
    parser.add_argument('--top', type=int, default=5, help='Number of top populous countries to display')
    parser.add_argument('--save', choices=['csv', 'json'], help='Save data to file')
    parser.add_argument('--region', type=str, help='Filter by region (e.g., Asia, Europe)')
    args = parser.parse_args()

    print("🌐 Fetching data from API...")
    raw_data = fetch_country_data()
    if not raw_data:
        return

    countries = process_data(raw_data, args.region)

    if not countries:
        print("⚠️ No data available after filtering.")
        return

    display_summary(countries)
    display_top_countries(countries, args.top)

    if args.save == 'csv':
        save_to_csv(countries)
    elif args.save == 'json':
        save_to_json(countries)

if __name__ == "__main__":
    main()
