import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query_ids_file", type=str, required=True)

    args = parser.parse_args()

    level = args.query_ids_file.split("_")[0]
    scenario = args.query_ids_file.split("_")[1]

    with open("./data/test_query_ids/{}".format(args.query_ids_file), "r") as f:
        query_ids = json.load(f)
        query_ids = list(map(int, query_ids.keys()))
    # print(query_ids)

    outputs = []
    with open("./data/instruction/{}_query.json".format(level), "r") as f:
        data = json.load(f)
        for d in data:
            if d["query_id"] in query_ids:
                outputs.append(d)

    output_file = "./data/instruction/{}_{}_test_query.json".format(level, scenario)
    with open(output_file, "w") as f:
        json.dump(outputs, f, indent=2)
