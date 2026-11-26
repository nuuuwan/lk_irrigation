# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_13:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,186 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 13:03:15 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:03:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-26 13:03:02 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.110 |  |
| 2026-11-26 13:02:49 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.070 |  |
| 2026-11-26 13:02:49 | Moragaswewa (Deduru Oya) | 4.45 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-26 13:02:39 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | -0.010 |  |
| 2026-11-26 13:02:31 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:02:07 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-11-26 13:01:56 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:01:50 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-11-26 13:01:48 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:01:40 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 13:01:28 | Galgamuwa (Mee Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-26 13:01:06 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 12:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.09 | 🟡 Alert | -0.020 |  |
| 2026-11-26 12:01:15 | Dunamale (Aththanagalu Oya) | 3.84 | 🟡 Alert | -0.042 |  |
| 2026-11-26 13:03:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-26 13:02:49 | Moragaswewa (Deduru Oya) | 4.45 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-26 13:01:40 | Thanthirimale (Malwathu Oya) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 11:07:53 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.001 |  |
| 2026-11-26 13:01:56 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-26 12:07:15 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:01:48 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:03:15 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-26 12:07:37 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:02:31 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-26 12:16:35 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-26 13:02:39 | Weraganthota (Mahaweli Ganga) | -1.99 | 🟢 Normal | -0.010 |  |
| 2026-11-26 13:01:06 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-11-26 12:00:54 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-11-26 12:19:32 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-26 13:01:28 | Galgamuwa (Mee Oya) | 1.25 | 🟢 Normal | -0.011 |  |
| 2026-11-26 12:11:12 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-26 12:11:13 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.017 |  |
| 2026-11-26 12:01:10 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-11-26 12:00:26 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-26 13:01:50 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-11-26 12:09:55 | Ellagawa (Kalu Ganga) | 6.06 | 🟢 Normal | -0.027 |  |
| 2026-11-26 13:02:07 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.030 |  |
| 2026-11-26 12:00:55 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.030 |  |
| 2026-11-26 12:04:02 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.031 |  |
| 2026-11-26 12:03:27 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.031 |  |
| 2026-11-26 12:05:19 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.032 |  |
| 2026-11-26 12:06:24 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.038 |  |
| 2026-11-26 12:01:15 | Peradeniya (Mahaweli Ganga) | 3.05 | 🟢 Normal | -0.060 |  |
| 2026-11-26 12:05:21 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.060 |  |
| 2026-11-26 12:04:20 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.061 |  |
| 2026-11-26 12:05:27 | Badalgama (Maha Oya) | 4.19 | 🟢 Normal | -0.062 |  |
| 2026-11-26 13:02:49 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.070 |  |
| 2026-11-26 12:01:16 | Manampitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | -0.074 |  |
| 2026-11-26 12:04:12 | Glencourse (Kelani Ganga) | 10.86 | 🟢 Normal | -0.105 |  |
| 2026-11-26 13:03:02 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.110 |  |
| 2026-11-26 12:10:02 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)