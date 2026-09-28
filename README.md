# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_15:17:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,359 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 15:17:21 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.008 |  |
| 2026-09-28 15:15:33 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.043 |  |
| 2026-09-28 15:14:49 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-28 15:10:02 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:08:33 | Baddegama (Gin Ganga) | 3.87 | 🟡 Alert | -0.036 |  |
| 2026-09-28 15:08:05 | Nagalagam Street (Kelani Ganga) | 0.81 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-28 15:07:39 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-09-28 15:05:59 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.019 |  |
| 2026-09-28 15:05:42 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:05:38 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:05:19 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | -0.029 |  |
| 2026-09-28 15:05:16 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-09-28 15:04:45 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:04:38 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | -0.059 |  |
| 2026-09-28 15:04:18 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.060 |  |
| 2026-09-28 15:04:10 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:04:04 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:04:00 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.030 |  |
| 2026-09-28 15:03:52 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.041 |  |
| 2026-09-28 15:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.59 | 🟢 Normal | -0.120 |  |
| 2026-09-28 15:03:17 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:03:15 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:03:14 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:03:00 | Dunamale (Aththanagalu Oya) | 1.89 | 🟢 Normal | -0.024 |  |
| 2026-09-28 15:02:47 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-09-28 15:02:26 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:02:24 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:02:17 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:02:00 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:01:44 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:01:44 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-09-28 15:01:25 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:01:21 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.032 |  |
| 2026-09-28 15:01:16 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:01:07 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:01:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:00:34 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 15:05:19 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | -0.029 |  |
| 2026-09-28 15:08:33 | Baddegama (Gin Ganga) | 3.87 | 🟡 Alert | -0.036 |  |
| 2026-09-28 15:08:05 | Nagalagam Street (Kelani Ganga) | 0.81 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-28 15:14:49 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-28 15:02:26 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:00:34 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:01:25 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:01:16 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:02:25 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:02:00 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:05:42 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:04:45 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 14:06:21 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:02:24 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:04:10 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:01:44 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:01:44 | Peradeniya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:01:07 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-28 15:17:21 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.008 |  |
| 2026-09-28 15:07:39 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | -0.009 |  |
| 2026-09-28 15:03:14 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:03:15 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:04:04 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:10:02 | Panadugama (Nilwala Ganga) | 4.54 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:05:38 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:01:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:02:17 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-09-28 15:05:16 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-09-28 15:05:59 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | -0.019 |  |
| 2026-09-28 15:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-09-28 15:02:47 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-09-28 15:03:00 | Dunamale (Aththanagalu Oya) | 1.89 | 🟢 Normal | -0.024 |  |
| 2026-09-28 15:04:00 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.030 |  |
| 2026-09-28 15:01:21 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.032 |  |
| 2026-09-28 15:03:52 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.041 |  |
| 2026-09-28 15:15:33 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.043 |  |
| 2026-09-28 15:04:38 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | -0.059 |  |
| 2026-09-28 15:04:18 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.060 |  |
| 2026-09-28 15:03:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.59 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)