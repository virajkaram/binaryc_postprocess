from binaryc_postprocess.lightcurve_models.base_lightcurve_models import BaseModelLightcurve
import numpy as np


class MetzgerPejcha(BaseModelLightcurve):
    def __init__(self, xi:float,  trun_torb:float, f_omega:float, kappa: float = 0.3):
        self.xi = xi
        self.f_omega = f_omega
        self.trun_torb = trun_torb
        self.kappa = kappa
        super().__init__()

    def calc_peak_luminosity(self, M_w, vej, a_Rms, Mej, M, vesc, vw):
        """
        Calculate the peak luminosity of the lightcurve.
        :param M_w:
        :param vej: Ejected velocity
        :param a_Rms: orbital separation in terms of main sequence radius
        :param Mej:
        :param M:
        :param vesc:
        :param vw:
        :return:
        """
        exponent = np.exp(3 * self.xi**0.5 * (self.kappa/0.3)**0.5 *
                          (self.trun_torb/10)**(-1) * (Mej/0.1)**(1./2.) *
                          (vej/vesc)**(-0.5) * M**(-0.25) * (a_Rms/10)**(-5./4.))
        return (9e40 * self.xi ** 3 * (self.f_omega/0.3) ** (-1.0) * (M_w / 0.1) *
                (vw/(vesc/4)) ** (-1) * (vej/vesc) ** 3 * (self.trun_torb/10) ** (-1) *
                (M) ** (5./2.) * (a_Rms/10) ** (-2.5) * exponent)

    def calc_peak_time(self,Mej, vej, M, a_Rms, vesc):
        """
        Calculate the peak time of the lightcurve.
        :param Mej:
        :param vej:
        :param M:
        :param a_Rms:
        :param vesc:
        :return:
        """
        return (27 * (self.kappa/0.3)**(0.5) * self.xi**(-0.5) *
                (Mej/0.1)**0.5 * (vej/vesc) ** (-0.5) * M ** (9./20.) *
                (a_Rms/10)**0.25)
