# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_20:02:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,065 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 20:02:59 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-02 20:02:42 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-02 20:02:34 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | -0.030 |  |
| 2026-11-02 20:02:33 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.050 |  |
| 2026-11-02 20:02:29 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-02 20:01:48 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2026-11-02 20:01:43 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-02 20:01:23 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 20:00:56 | Thalgahagoda (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-02 20:00:18 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 20:01:48 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2026-11-02 19:05:18 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.299 | 🔺 Rising |
| 2026-11-02 19:04:11 | Padiyathalawa (Maduru Oya) | 0.35 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-11-02 19:12:31 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-11-02 19:02:55 | Norwood (Kelani Ganga) | 1.12 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-02 19:07:44 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-11-02 19:08:46 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-02 19:00:25 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-02 19:06:39 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 19:09:03 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-02 20:01:23 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 19:05:15 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-02 20:00:18 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 19:02:06 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-11-02 20:01:43 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:04:26 | Giriulla (Maha Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:05:42 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:02:27 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 20:02:29 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:04:23 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-02 20:02:59 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:03:25 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-02 19:07:55 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-11-02 20:02:42 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-02 19:07:59 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.018 |  |
| 2026-11-02 19:05:49 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.019 |  |
| 2026-11-02 20:00:56 | Thalgahagoda (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-02 19:09:48 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.028 |  |
| 2026-11-02 19:09:13 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.029 |  |
| 2026-11-02 19:02:30 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | -0.030 |  |
| 2026-11-02 20:02:34 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | -0.030 |  |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-02 19:04:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-11-02 19:05:20 | Panadugama (Nilwala Ganga) | 4.45 | 🟢 Normal | -0.034 |  |
| 2026-11-02 20:02:33 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.050 |  |
| 2026-11-02 19:05:45 | Ellagawa (Kalu Ganga) | 6.02 | 🟢 Normal | -0.057 |  |
| 2026-11-02 19:07:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)