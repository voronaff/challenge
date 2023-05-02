#!/bin/bash

WORKSPACE="$(cd "$(dirname "$0")" && pwd -P)"
IMG_NAME=${1:-"$(basename "$WORKSPACE")"}
IMG_TAG=${2:-'latest'}

docker build -t "${IMG_NAME}:${IMG_TAG}" -f "${WORKSPACE}/Dockerfile" "${WORKSPACE}"