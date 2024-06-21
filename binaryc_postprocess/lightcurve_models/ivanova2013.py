from binaryc_postprocess.lightcurve_models.base_lightcurve_models import BaseModelLightcurve


class Ivanova2013(BaseModelLightcurve):
    def __init__(self, kappa: float,
                 Trec: float):
        self.kappa = kappa
        self.Trec = Trec
        super().__init__()

    def calc_peak_luminosity(self, Munb: float, Rinit: float, Ek: float):
        """
        Calculate the peak luminosity of the lightcurve.
        :param Munb: float Unbound mass in solar masses
        :param Rinit: float Initial radius in solar radii
        :param Ek: float Kinetic energy in erg
        :return: float Peak luminosity in erg/s
        """
        return (1.7e4 * (Rinit/3.5)**(2./3.) * (Ek/1e46)**(5./6.)
                * (Munb/0.03)**(-1./2.) * (self.kappa/0.32)**(-1./3.)
                * (self.Trec/4500)**(4./3.))

    def calc_peak_time(self, Munb: float, Rinit: float, Ek: float):
        """
        Calculate the peak time of the lightcurve.
        """
        return (17 * (Rinit/3.5)**(1./6.) * (Ek/1e46)**(-1./6.) * (Munb/0.03)**(1./2.)
                * (self.kappa/0.32)**(1./6.) * (self.Trec/4500)**(-2./3.))
