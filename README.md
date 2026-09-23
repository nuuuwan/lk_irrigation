# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_10:15:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,666 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 10:15:42 | Ellagawa (Kalu Ganga) | 8.14 | 🟢 Normal | -0.025 |  |
| 2026-09-23 10:13:53 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.009 |  |
| 2026-09-23 10:13:17 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.020 |  |
| 2026-09-23 10:12:46 | Thalgahagoda (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:10:20 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-23 10:09:50 | Rathnapura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.020 |  |
| 2026-09-23 10:08:11 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:08:02 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | 0.000 |  |
| 2026-09-23 10:07:19 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-09-23 10:06:25 | Nawalapitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-23 10:06:04 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-09-23 10:05:55 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:05:46 | Baddegama (Gin Ganga) | 3.81 | 🟡 Alert | -0.031 |  |
| 2026-09-23 10:05:37 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-09-23 10:05:24 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.210 |  |
| 2026-09-23 10:05:19 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:04:55 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:04:06 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:04:02 | Glencourse (Kelani Ganga) | 12.84 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:03:58 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:03:49 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:03:46 | Kithulgala (Kelani Ganga) | 2.32 | 🟢 Normal | -0.050 |  |
| 2026-09-23 10:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-23 10:03:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:03:25 | Hanwella (Kelani Ganga) | 4.83 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:03:21 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.021 |  |
| 2026-09-23 10:03:00 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:02:49 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:02:47 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:02:27 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:02:25 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 10:02:07 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:01:15 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:00:52 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:00:52 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-23 10:00:47 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:00:37 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:00:06 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 10:03:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-23 10:08:02 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | 0.000 |  |
| 2026-09-23 10:05:46 | Baddegama (Gin Ganga) | 3.81 | 🟡 Alert | -0.031 |  |
| 2026-09-23 10:00:52 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-23 10:06:25 | Nawalapitiya (Mahaweli Ganga) | 2.23 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-23 10:10:20 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-23 10:02:25 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 10:03:58 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:01:15 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:02:27 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:00:37 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:03:25 | Hanwella (Kelani Ganga) | 4.83 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:03:00 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:05:19 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:00:52 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:03:33 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:04:06 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:02:49 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:12:46 | Thalgahagoda (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:03:49 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:02:07 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:13:53 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.009 |  |
| 2026-09-23 10:07:19 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-09-23 10:04:55 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:08:11 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:00:06 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:00:47 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:02:47 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:05:55 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:04:02 | Glencourse (Kelani Ganga) | 12.84 | 🟢 Normal | -0.010 |  |
| 2026-09-23 10:05:37 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | -0.011 |  |
| 2026-09-23 10:13:17 | Panadugama (Nilwala Ganga) | 4.39 | 🟢 Normal | -0.020 |  |
| 2026-09-23 10:06:04 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-09-23 10:09:50 | Rathnapura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.020 |  |
| 2026-09-23 10:03:21 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | -0.021 |  |
| 2026-09-23 10:15:42 | Ellagawa (Kalu Ganga) | 8.14 | 🟢 Normal | -0.025 |  |
| 2026-09-23 10:03:46 | Kithulgala (Kelani Ganga) | 2.32 | 🟢 Normal | -0.050 |  |
| 2026-09-23 10:05:24 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)