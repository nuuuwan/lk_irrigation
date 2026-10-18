# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_13:06:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,285 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 13:06:28 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.019 |  |
| 2026-10-18 13:06:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:05:55 | Peradeniya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.029 |  |
| 2026-10-18 13:05:22 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-10-18 13:04:55 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:04:38 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-10-18 13:03:51 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:03:51 | Rathnapura (Kalu Ganga) | 3.34 | 🟢 Normal | -0.111 |  |
| 2026-10-18 13:03:28 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.050 |  |
| 2026-10-18 13:03:27 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:03:26 | Hanwella (Kelani Ganga) | 3.77 | 🟢 Normal | -0.091 |  |
| 2026-10-18 13:03:23 | Panadugama (Nilwala Ganga) | 5.85 | 🟡 Alert | -0.045 |  |
| 2026-10-18 13:03:17 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-10-18 13:03:14 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:02:56 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.072 |  |
| 2026-10-18 13:02:55 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 13:02:52 | Weraganthota (Mahaweli Ganga) | -2.31 | 🟢 Normal | -0.048 |  |
| 2026-10-18 13:02:38 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.220 |  |
| 2026-10-18 13:02:33 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.040 |  |
| 2026-10-18 13:02:31 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-18 13:02:17 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-18 13:02:14 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-18 13:01:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:01:37 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.083 |  |
| 2026-10-18 13:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:01:29 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 13:01:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:00:49 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:00:44 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.041 |  |
| 2026-10-18 13:00:44 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 12:04:25 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 13:03:23 | Panadugama (Nilwala Ganga) | 5.85 | 🟡 Alert | -0.045 |  |
| 2026-10-18 12:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.11 | 🟡 Alert | -0.053 |  |
| 2026-10-18 13:03:17 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-10-18 13:02:17 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-18 13:00:44 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 13:01:29 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 12:02:13 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-18 13:02:55 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 13:02:31 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-18 13:01:16 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:01:34 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:01:38 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:00:49 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:03:27 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:06:51 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:03:14 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:04:59 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:03:51 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:04:55 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-18 13:06:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 12:06:31 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-18 13:02:14 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-18 12:09:56 | Putupaula (Kalu Ganga) | 1.91 | 🟢 Normal | -0.018 |  |
| 2026-10-18 13:06:28 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.019 |  |
| 2026-10-18 13:04:38 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-10-18 13:05:22 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-10-18 12:07:32 | Magura (Kalu Ganga) | 2.26 | 🟢 Normal | -0.024 |  |
| 2026-10-18 12:06:56 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.028 |  |
| 2026-10-18 13:05:55 | Peradeniya (Mahaweli Ganga) | 2.89 | 🟢 Normal | -0.029 |  |
| 2026-10-18 13:02:33 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.040 |  |
| 2026-10-18 13:00:44 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.041 |  |
| 2026-10-18 13:02:52 | Weraganthota (Mahaweli Ganga) | -2.31 | 🟢 Normal | -0.048 |  |
| 2026-10-18 13:03:28 | Glencourse (Kelani Ganga) | 11.40 | 🟢 Normal | -0.050 |  |
| 2026-10-18 13:02:56 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.072 |  |
| 2026-10-18 13:01:37 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.083 |  |
| 2026-10-18 13:03:26 | Hanwella (Kelani Ganga) | 3.77 | 🟢 Normal | -0.091 |  |
| 2026-10-18 13:03:51 | Rathnapura (Kalu Ganga) | 3.34 | 🟢 Normal | -0.111 |  |
| 2026-10-18 13:02:38 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.220 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)