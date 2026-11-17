#!/usr/bin/env bash
set -euo pipefail

mkdir -p data backup reports

cat > data/measurements.txt <<'EOF'
12.5 sensor-a
14.0 sensor-b
11.2 sensor-a
13.8 sensor-b
10.9 sensor-a
EOF

echo "перший запис" > data/readings.txt
cp data/readings.txt backup/readings-renamed.txt

{
  echo "=== Відсортовані значення ==="
  cat data/measurements.txt | sort -n
  echo "=== Кількість рядків ==="
  cat data/measurements.txt | wc -l
} > reports/report.txt

echo "Готово. Створено data/measurements.txt (рядків: $(wc -l < data/measurements.txt))."
