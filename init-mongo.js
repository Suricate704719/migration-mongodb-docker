db.getSiblingDB('hopital').createUser({
    user: "data_worker",
    pwd: "WorkerPassword2026!",
    roles: [{ role: "readWrite", db: "hopital" }]
});