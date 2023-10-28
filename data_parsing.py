import csv
import re
from pathlib import Path


def ossl_csv_to_dict(file: Path) -> list[dict[float, float]]:
    """Converts a CSV file to a list of dictionaries of wavelengths and reflectance.

    This takes data from the Open Soil Spectral Library (OSSL) CSVs and converts it
    into Python dictionaries. This function only parses the NIR 
    """
    with file.open("r", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)  # Skipping the header line
        headers_of_interest = header[1835:2910]
        r = re.compile("scan_visnir\.(\d+)_ref")
        wavelengths = [int(r.match(x).groups()[0]) for x in headers_of_interest]
        data: list[dict[float, float]] = []
        for row in reader:
            data_of_interest = row[1835:2910]
            reflectances = []
            for x in data_of_interest:
                try:
                    reflectances.append(float(x))
                except ValueError:
                    pass
            data.append(dict(zip(wavelengths, reflectances)))
    return data
        
        
