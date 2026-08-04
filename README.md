# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_00:11:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,120 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Rathnapura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 00:11:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | -0.059 |  |
| 2026-08-05 00:11:02 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:10:12 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:09:34 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:09:31 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-05 00:08:27 | Kithulgala (Kelani Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:07:19 | Hanwella (Kelani Ganga) | 5.05 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-05 00:07:11 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:06:23 | Peradeniya (Mahaweli Ganga) | 4.55 | 🟢 Normal | -0.029 |  |
| 2026-08-05 00:06:13 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.114 |  |
| 2026-08-05 00:05:42 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:05:28 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-05 00:04:53 | Deraniyagala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.138 |  |
| 2026-08-05 00:04:27 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:04:22 | Nawalapitiya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -0.020 |  |
| 2026-08-05 00:04:14 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.047 |  |
| 2026-08-05 00:04:12 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:04:08 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:04:05 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.021 |  |
| 2026-08-05 00:04:00 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-08-05 00:04:00 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:03:54 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.031 |  |
| 2026-08-05 00:03:32 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:03:21 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:03:12 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:02:53 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:02:45 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:02:44 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.021 |  |
| 2026-08-05 00:02:10 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-08-05 00:01:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:01:39 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:01:38 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-05 00:01:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:01:31 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.071 |  |
| 2026-08-05 00:01:20 | Rathnapura (Kalu Ganga) | 5.71 | 🟡 Alert | -0.112 |  |
| 2026-08-04 23:44:02 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 00:11:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.00 | 🟡 Alert | -0.059 |  |
| 2026-08-05 00:01:20 | Rathnapura (Kalu Ganga) | 5.71 | 🟡 Alert | -0.112 |  |
| 2026-08-05 00:07:19 | Hanwella (Kelani Ganga) | 5.05 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-05 00:09:31 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-05 00:01:38 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-05 00:05:28 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-05 00:08:27 | Kithulgala (Kelani Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:03:21 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:05:42 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:01:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:00:57 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:04:08 | Pitabeddara (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:03:12 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:01:35 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:03:32 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:11:02 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:04:12 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:02:53 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:02:45 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 23:03:02 | Putupaula (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:04:00 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:07:11 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-04 18:01:32 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:10:12 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:09:34 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:04:27 | Thanamalwila (Kirindi Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-05 00:04:00 | Thalgahagoda (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-08-05 00:02:10 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-08-05 00:04:22 | Nawalapitiya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -0.020 |  |
| 2026-08-05 00:04:05 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | -0.021 |  |
| 2026-08-05 00:02:44 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.021 |  |
| 2026-08-05 00:06:23 | Peradeniya (Mahaweli Ganga) | 4.55 | 🟢 Normal | -0.029 |  |
| 2026-08-05 00:03:54 | Thawalama (Gin Ganga) | 1.93 | 🟢 Normal | -0.031 |  |
| 2026-08-05 00:04:14 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.047 |  |
| 2026-08-05 00:01:31 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.071 |  |
| 2026-08-05 00:06:13 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.114 |  |
| 2026-08-04 18:04:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.115 |  |
| 2026-08-05 00:04:53 | Deraniyagala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)