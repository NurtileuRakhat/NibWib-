export interface AuthToken {
    access: string;
};

export interface Register {
    username: string;
    password: string;
    password2: string;
    email: string;
    first_name: string;
    last_name: string;
};