#!/usr/bin/env python3
"""
Test runner for MathModel project.

This script provides a convenient way to run tests with different options.
"""

import argparse
import logging
import os
import subprocess
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> int:
    """Run the tests with the specified options."""
    parser = argparse.ArgumentParser(description="Run tests for MathModel project")
    parser.add_argument(
        "--coverage", "-c", action="store_true", help="Run tests with coverage report"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Run tests with verbose output"
    )
    parser.add_argument("--test", "-t", help="Run specific test file or test function")
    parser.add_argument(
        "--xml",
        "-x",
        action="store_true",
        help="Generate XML report for CI integration",
    )
    parser.add_argument(
        "--html",
        "-m",
        action="store_true",
        help="Generate HTML report",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        default="test-results",
        help="Output directory for reports",
    )

    args = parser.parse_args()

    # Create output directory if it doesn't exist
    if args.html or args.xml:
        os.makedirs(args.output_dir, exist_ok=True)
        logger.info(f"Created output directory: {args.output_dir}")

    # Base command
    cmd = ["poetry", "run", "pytest"]

    # Add options
    if args.verbose:
        cmd.append("-v")

    if args.coverage:
        cmd.extend(["--cov=mathmodel", "--cov-report=term-missing"])
        if args.html:
            cmd.append(f"--cov-report=html:{args.output_dir}/coverage")

    if args.xml:
        cmd.append(f"--junitxml={args.output_dir}/test-results.xml")

    if args.html:
        cmd.append(f"--html={args.output_dir}/report.html")
        cmd.append("--self-contained-html")

    if args.test:
        cmd.append(args.test)

    # Run tests
    logger.info(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd)

    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
