from binaryc_postprocess.extinction.base_extinction import BaseExtinction


class MacLeodWindExtinction(BaseExtinction):
    def __init__(self, f_vir: float = 0.25, f_nu: float = 0.25, Xd: float = 5e-3, kappa_d: float = 1e3):
        """

        :param f_vir:
        :param f_nu:
        :param Xd: dust-to-gas ratio
        :param kappa_d: dust opacity cm^2/g
        """
        self.f_vir = f_vir
        self.f_nu = f_nu
        self.Xd = Xd
        self.kappa_d = kappa_d
        super().__init__()

    def calculate_Av(self, M_star: float, R_star: float,  q: float):
        """
        Calculate the extinction in the V band.
        :param M_star: Mass of the star in solar masses
        :param R_star: Radius of the star in solar radii
        :param q: mass ratio
        :return:
        """

        return (0.97 * (q/0.1) ** 1.04 * (M_star)**(-1.5) * (R_star/10)**0.5 *
                (self.Xd * self.kappa_d/5.0) * (self.f_vir/0.25)**(-2.5) *
                (self.f_nu/0.25)**0.5)


class MacLeodTorusExtinction(BaseExtinction):
    def __init__(self, Xd: float = 5e-3, kappa_d: float = 1e3):
        """
        :param Xd: dust-to-gas ratio
        :param kappa_d: dust opacity cm^2/g
        """
        self.Xd = Xd
        self.kappa_d = kappa_d
        super().__init__()

    def calculate_Av(self, M_star: float, R_star: float,  q: float):
        """
        Calculate the extinction in the V band.
        :param M_star: Mass of the star in solar masses
        :param R_star: Radius of the star in solar radii
        :param q: mass ratio
        :return:
        """

        return (0.18 * (q/0.1) ** 1.6 * M_star**(-2.8) * (R_star/10)**1.8 *
                self.Xd * self.kappa_d/5.0)
