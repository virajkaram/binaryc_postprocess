from binaryc_postprocess.lightcurve_models.base_lightcurve_models import BaseModelLightcurve


class MatsumotoMetzger_Recombination(BaseModelLightcurve):
    def __init__(self, rho_i: float = 1e-11, f_ad: float = 0.3):
        super().__init__()
        self.rho_i = rho_i
        self.f_ad = f_ad

    def calc_peak_luminosity(self, Mej: float, ve: float):
        """
        Calculate the peak luminosity of the lightcurve.
        :param Mej: Ejected mass in solar masses
        :param ve: Ejecta velocity in km/s
        :return: Peak luminosity in erg/s
        """
        return (4.8e38 * (self.f_ad/0.3) * (self.rho_i/1e-11) ** (1./3.)
                * Mej**(2./3.) * (ve/300))

    def calc_peak_time(self, Mej: float, ve: float):
        """
        Calculate the peak time of the lightcurve.
        :param Mej: Ejected mass in solar masses
        :param ve: Ejecta velocity in km/s
        :return:
        """
        return 140 * (self.rho_i/1e-11) ** (-1. / 3.) * Mej**(1. / 3.) * (ve / 300)**(-1.)


class MatsumotoMetzger_Shock(BaseModelLightcurve):
    def __init__(self, rho_i: float = 1e-11, f_ad: float = 0.3):
        super().__init__()
        self.rho_i = rho_i
        self.f_ad = f_ad

    def calc_peak_time(self, Mej: float, ve: float):
        """
        Calculate the peak time of the lightcurve.
        :param Mej: Ejected mass in solar masses
        :param ve: Ejecta velocity in km/s
        :return:
        """
        return 140 * (self.rho_i/1e-11) ** (-1. / 3.) * Mej**(1. / 3.) * (ve / 300)**(-1.)

    def calc_peak_luminosity(self, Mej: float, ve: float, Mpre: float):
        """
        Calculate the peak luminosity of the lightcurve Eq. 31 of Matsumoto-Metzger.
        :param Mej: Ejected mass in solar masses
        :param ve: Ejecta velocity in km/s
        :param Mpre: Pre-explosion mass in solar masses
        :return: Peak luminosity in erg/s
        """
        return (7e39 * (self.rho_i/1e-11)**(1./3.) * (Mpre/0.1) *
                (ve/300)**3 * Mej**(2./3.))
