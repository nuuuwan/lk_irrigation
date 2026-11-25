# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_16:03:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,444 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 16:03:24 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 16:03:21 | Moraketiya (Walawe Ganga) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-11-25 16:03:01 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.090 |  |
| 2026-11-25 16:02:54 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.070 |  |
| 2026-11-25 16:02:50 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-11-25 16:02:41 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-25 16:02:35 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-25 16:02:34 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-25 16:02:20 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-25 16:02:13 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.041 |  |
| 2026-11-25 16:02:10 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-25 16:01:55 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-25 16:01:28 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-25 16:01:26 | Nawalapitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-25 16:01:23 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-11-25 16:01:09 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.037 |  |
| 2026-11-25 16:00:15 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 16:02:50 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-11-25 16:01:23 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-11-25 16:01:28 | Weraganthota (Mahaweli Ganga) | -2.02 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-25 16:02:41 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-25 16:02:10 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-25 16:02:20 | Wellawaya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-25 15:05:44 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-25 16:01:26 | Nawalapitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-25 16:02:35 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-25 15:04:30 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-25 16:03:24 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 15:04:26 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-25 15:05:28 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-25 16:01:55 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:04:19 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:04:32 | Rathnapura (Kalu Ganga) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-11-25 15:01:34 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-25 16:00:15 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-25 14:14:40 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-11-25 16:02:34 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-25 15:03:27 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-11-25 15:15:51 | Kuda Oya (Kirindi Oya) | 1.80 | 🟢 Normal | -0.018 |  |
| 2026-11-25 15:08:34 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.019 |  |
| 2026-11-25 15:05:11 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | -0.020 |  |
| 2026-11-25 14:05:03 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | -0.020 |  |
| 2026-11-25 16:03:21 | Moraketiya (Walawe Ganga) | 2.01 | 🟢 Normal | -0.020 |  |
| 2026-11-25 15:04:28 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.020 |  |
| 2026-11-25 15:01:49 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 16:01:09 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.037 |  |
| 2026-11-25 15:06:25 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | -0.038 |  |
| 2026-11-25 15:03:10 | Giriulla (Maha Oya) | 2.23 | 🟢 Normal | -0.040 |  |
| 2026-11-25 16:02:13 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.041 |  |
| 2026-11-25 15:13:26 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.047 |  |
| 2026-11-25 15:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.73 | 🟢 Normal | -0.053 |  |
| 2026-11-25 16:02:54 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.070 |  |
| 2026-11-25 16:03:01 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.090 |  |
| 2026-11-25 15:01:46 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | -0.124 |  |
| 2026-11-25 15:04:34 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -2.118 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)