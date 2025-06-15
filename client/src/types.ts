export interface Customer{
    id: number;
    first_name: string;
    surname: string;
    middle_name?: string;
    date_of_birth: string;
    home_address: string;
    date_of_registration: string;
    matric_field: string;
}

export interface NewCustomer {
  first_name: string;
  surname: string;
  middle_name?: string;
  date_of_birth: string;
  home_address: string;
  date_of_registration: string;
  matric_field: string;
}
