# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_02:10:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,351 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 02:10:47 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.009 |  |
| 2026-08-09 02:09:50 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -8.260 |  |
| 2026-08-09 02:08:51 | Rathnapura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.028 |  |
| 2026-08-09 02:06:49 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-08-09 02:06:34 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-08-09 02:06:06 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.029 |  |
| 2026-08-09 02:05:44 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:05:11 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.005 |  |
| 2026-08-09 02:04:51 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.021 |  |
| 2026-08-09 02:03:43 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:03:34 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.010 |  |
| 2026-08-09 02:03:01 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-09 02:02:46 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-08-09 02:02:29 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:02:28 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-09 02:02:26 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:02:12 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:02:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:02:08 | Giriulla (Maha Oya) | 2.09 | 🟢 Normal | -8.260 |  |
| 2026-08-09 02:02:05 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:01:56 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 02:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-09 02:01:38 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-08-09 02:00:51 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:00:39 | Peradeniya (Mahaweli Ganga) | 3.62 | 🟢 Normal | -0.121 |  |
| 2026-08-09 01:53:26 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:53:24 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:44:28 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 01:04:30 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-08-09 02:02:28 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-09 02:01:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-09 01:00:43 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-09 00:02:45 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 02:03:01 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-09 02:01:56 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:02:26 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:02:05 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:00:51 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:03:57 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 23:06:40 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:03:38 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:05:44 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-09 00:02:57 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:03:04 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:44:28 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:02:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:03:43 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-09 01:01:10 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:01:56 | Thanthirimale (Malwathu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:02:12 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:02:29 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-09 02:05:11 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.005 |  |
| 2026-08-09 01:16:27 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.009 |  |
| 2026-08-09 02:10:47 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | -0.009 |  |
| 2026-08-09 02:06:49 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.010 |  |
| 2026-08-09 01:02:06 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-08-09 02:02:46 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-08-09 02:03:34 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.010 |  |
| 2026-08-09 02:06:34 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-08-09 02:04:51 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.021 |  |
| 2026-08-09 02:08:51 | Rathnapura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.028 |  |
| 2026-08-09 02:06:06 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.029 |  |
| 2026-08-09 02:01:38 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-08-09 00:06:38 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | -0.079 |  |
| 2026-08-09 02:00:39 | Peradeniya (Mahaweli Ganga) | 3.62 | 🟢 Normal | -0.121 |  |
| 2026-08-09 02:09:50 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -8.260 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)