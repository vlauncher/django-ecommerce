#!/bin/bash

echo "🔍 Running tests with coverage..."
coverage run -m pytest

echo "📊 Generating coverage report..."
coverage report

echo "🌍 Generating HTML coverage report..."
coverage html

# Automatically open the report based on OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open coverage_html_report/index.html
elif [[ "$OSTYPE" == "darwin"* ]]; then
    open coverage_html_report/index.html
elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    start coverage_html_report/index.html
else
    echo "❗ Please open coverage_html_report/index.html manually."
fi

echo "✅ Coverage process completed!"
