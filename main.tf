provider "google"{
    project = "comentando"
    region = "us-central1"
}

resource "google_container_cluster" "cluster-cloud"{
    name = "cluster-1"
    location = "us-central1"
}