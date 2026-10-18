# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_04:03:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,825 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Norwood — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 04:03:09 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:03:01 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | -0.091 |  |
| 2026-10-19 04:02:47 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:02:46 | Thalgahagoda (Nilwala Ganga) | 1.99 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-19 04:02:16 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.060 |  |
| 2026-10-19 04:02:08 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-10-19 04:02:07 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-19 04:02:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-19 04:01:53 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 04:01:49 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-10-19 04:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:01:48 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:01:44 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.050 |  |
| 2026-10-19 04:01:38 | Ellagawa (Kalu Ganga) | 7.33 | 🟢 Normal | -0.036 |  |
| 2026-10-19 04:01:20 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:01:00 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.021 |  |
| 2026-10-19 04:00:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:00:19 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:54:13 | Putupaula (Kalu Ganga) | 1.73 | 🟢 Normal | -0.011 |  |
| 2026-10-19 03:30:14 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.008 |  |
| 2026-10-19 03:22:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | -0.672 |  |
| 2026-10-19 03:20:07 | Panadugama (Nilwala Ganga) | 5.65 | 🟡 Alert | -0.069 |  |
| 2026-10-19 03:18:36 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.024 |  |
| 2026-10-19 03:17:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.51 | 🟢 Normal | -0.672 |  |
| 2026-10-19 03:15:58 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 04:02:46 | Thalgahagoda (Nilwala Ganga) | 1.99 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-19 03:30:14 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.008 |  |
| 2026-10-19 03:20:07 | Panadugama (Nilwala Ganga) | 5.65 | 🟡 Alert | -0.069 |  |
| 2026-10-19 03:02:22 | Hanwella (Kelani Ganga) | 3.78 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-19 04:02:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-19 04:02:07 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-19 03:02:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-19 04:01:53 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 03:05:18 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-19 04:00:19 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:02:47 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:03:09 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:01:48 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-10-19 04:00:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 03:03:04 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:04:49 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:01:20 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-19 04:01:48 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-19 03:54:13 | Putupaula (Kalu Ganga) | 1.73 | 🟢 Normal | -0.011 |  |
| 2026-10-19 03:09:59 | Dunamale (Aththanagalu Oya) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-10-19 03:04:54 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.020 |  |
| 2026-10-19 04:01:00 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.021 |  |
| 2026-10-19 04:02:08 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.021 |  |
| 2026-10-19 03:05:08 | Baddegama (Gin Ganga) | 2.82 | 🟢 Normal | -0.021 |  |
| 2026-10-19 03:18:36 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.024 |  |
| 2026-10-19 03:12:41 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.027 |  |
| 2026-10-19 03:02:17 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.030 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-19 04:01:38 | Ellagawa (Kalu Ganga) | 7.33 | 🟢 Normal | -0.036 |  |
| 2026-10-19 04:01:49 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | -0.040 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-19 04:01:44 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.050 |  |
| 2026-10-19 04:02:16 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.060 |  |
| 2026-10-19 03:04:45 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | -0.060 |  |
| 2026-10-19 04:03:01 | Moragaswewa (Deduru Oya) | 2.25 | 🟢 Normal | -0.091 |  |
| 2026-10-19 03:22:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | -0.672 |  |
| 2026-10-19 03:08:39 | Rathnapura (Kalu Ganga) | 4.07 | 🟢 Normal | -5.143 |  |
| 2026-10-19 03:05:05 | Glencourse (Kelani Ganga) | 11.91 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)