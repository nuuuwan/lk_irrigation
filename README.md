# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_13:15:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,782 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 13:15:28 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:14:45 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.025 |  |
| 2026-08-09 13:13:30 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:12:47 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.008 |  |
| 2026-08-09 13:11:31 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-09 13:11:11 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:10:36 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-09 13:10:31 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -0.129 |  |
| 2026-08-09 13:09:38 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:09:30 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.018 |  |
| 2026-08-09 13:07:26 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:07:04 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.018 |  |
| 2026-08-09 13:06:52 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:06:12 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-08-09 13:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | -0.077 |  |
| 2026-08-09 13:05:14 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:04:52 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-08-09 13:04:31 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-08-09 13:03:52 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:03:01 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-08-09 13:03:01 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-09 13:02:57 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:02:56 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:02:51 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:02:40 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-09 13:02:33 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:02:28 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:02:15 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:02:14 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-09 13:02:06 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-09 13:01:59 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:01:38 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 13:01:25 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:01:22 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:01:21 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 13:01:12 | Thanthirimale (Malwathu Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 13:00:39 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:00:08 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:59:27 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:28:04 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 13:02:40 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-09 13:02:14 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-09 13:10:36 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-09 13:03:01 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-09 13:01:38 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 13:01:21 | Ellagawa (Kalu Ganga) | 5.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 13:01:12 | Thanthirimale (Malwathu Oya) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 13:11:31 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-09 13:02:15 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:15:28 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:01:59 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:09:38 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:00:39 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:11:11 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:02:56 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:02:51 | Hanwella (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 12:19:06 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:02:33 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:02:28 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:01:25 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:00:08 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:01:22 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:03:52 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:06:52 | Rathnapura (Kalu Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:05:14 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:13:30 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:02:57 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 13:12:47 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.008 |  |
| 2026-08-09 13:06:12 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-08-09 13:04:31 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-08-09 13:02:06 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-09 13:09:30 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.018 |  |
| 2026-08-09 13:07:04 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.018 |  |
| 2026-08-09 12:15:49 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-08-09 13:03:01 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-08-09 13:04:52 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-08-09 13:14:45 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.025 |  |
| 2026-08-09 13:05:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.82 | 🟢 Normal | -0.077 |  |
| 2026-08-09 13:10:31 | Panadugama (Nilwala Ganga) | 4.07 | 🟢 Normal | -0.129 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)