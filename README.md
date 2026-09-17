# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--18_02:05:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **263,835 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Baddegama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 02:05:40 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:05:30 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:05:22 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:05:02 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:04:50 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:04:48 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:04:19 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:04:15 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.017 |  |
| 2026-09-18 02:03:55 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:03:48 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:03:40 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.033 |  |
| 2026-09-18 02:03:37 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 02:03:13 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-18 02:02:45 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:02:30 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-09-18 02:02:28 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-18 02:02:25 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 02:02:19 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:02:18 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -1.756 |  |
| 2026-09-18 02:02:04 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-09-18 02:01:38 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:01:37 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -1.756 |  |
| 2026-09-18 02:01:25 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:01:09 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:00:53 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.185 |  |
| 2026-09-18 02:00:53 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | -0.108 |  |
| 2026-09-18 02:00:05 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-18 01:51:45 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-18 00:09:27 | Baddegama (Gin Ganga) | 3.51 | 🟡 Alert | -0.010 |  |
| 2026-09-18 02:00:53 | Magura (Kalu Ganga) | 4.92 | 🟡 Alert | -0.108 |  |
| 2026-09-18 02:02:04 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-09-18 02:02:28 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-09-18 01:04:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.29 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-18 02:03:13 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-18 02:03:37 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-18 02:02:25 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-18 02:02:30 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-09-17 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:05:40 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:01:25 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-18 01:02:20 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:05:30 | Nawalapitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-18 01:12:28 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:09:10 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-09-17 17:02:18 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:06:54 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-18 01:04:11 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:02:45 | Ellagawa (Kalu Ganga) | 4.98 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:00:05 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:05:22 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:04:19 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:01:38 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:03:55 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:05:02 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:02:19 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-17 18:01:22 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 00:05:41 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:01:09 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-09-18 02:03:48 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-18 01:03:20 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-18 01:14:30 | Dunamale (Aththanagalu Oya) | 2.11 | 🟢 Normal | -0.009 |  |
| 2026-09-18 02:04:15 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.017 |  |
| 2026-09-18 01:05:52 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.028 |  |
| 2026-09-18 02:03:40 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.033 |  |
| 2026-09-18 00:01:47 | Thawalama (Gin Ganga) | 2.21 | 🟢 Normal | -0.060 |  |
| 2026-09-18 02:00:53 | Peradeniya (Mahaweli Ganga) | 2.42 | 🟢 Normal | -0.185 |  |
| 2026-09-18 02:02:18 | Panadugama (Nilwala Ganga) | 4.51 | 🟢 Normal | -1.756 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)