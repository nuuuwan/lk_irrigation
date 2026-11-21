# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_14:31:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,887 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 14:31:20 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:20:03 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.008 |  |
| 2026-11-21 14:15:10 | Panadugama (Nilwala Ganga) | 5.02 | 🟡 Alert | -0.049 |  |
| 2026-11-21 14:12:50 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:10:25 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.058 |  |
| 2026-11-21 14:09:44 | Dunamale (Aththanagalu Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:09:19 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:08:49 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-21 14:08:33 | Moraketiya (Walawe Ganga) | 2.94 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:06:15 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-21 14:06:00 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 14:05:35 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 14:05:27 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.107 |  |
| 2026-11-21 14:04:40 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 14:04:10 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.181 |  |
| 2026-11-21 14:04:06 | Giriulla (Maha Oya) | 3.80 | 🟢 Normal | -0.226 |  |
| 2026-11-21 14:04:02 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 14:04:02 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.163 |  |
| 2026-11-21 14:03:43 | Badalgama (Maha Oya) | 4.49 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-11-21 14:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-11-21 14:03:28 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 14:02:49 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2026-11-21 14:02:35 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 14:02:34 | Kuda Oya (Kirindi Oya) | 2.26 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-21 14:02:29 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 14:02:25 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.042 |  |
| 2026-11-21 14:02:18 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:02:16 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-11-21 14:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.020 |  |
| 2026-11-21 14:01:49 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.101 |  |
| 2026-11-21 14:01:45 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 14:01:38 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:01:09 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | -0.022 |  |
| 2026-11-21 14:00:58 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:00:51 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:00:36 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | -0.090 |  |
| 2026-11-21 14:00:13 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 14:15:10 | Panadugama (Nilwala Ganga) | 5.02 | 🟡 Alert | -0.049 |  |
| 2026-11-21 14:03:43 | Badalgama (Maha Oya) | 4.49 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-11-21 14:02:34 | Kuda Oya (Kirindi Oya) | 2.26 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-21 14:02:29 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 14:02:35 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 14:04:02 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 14:06:00 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 14:03:28 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 14:04:40 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 14:01:45 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 14:05:35 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 14:06:15 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-21 14:31:20 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:01:38 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:00:58 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:09:19 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:12:50 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:08:33 | Moraketiya (Walawe Ganga) | 2.94 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:02:18 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:09:44 | Dunamale (Aththanagalu Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:00:51 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:20:03 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.008 |  |
| 2026-11-21 14:00:13 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-21 14:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-11-21 14:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.020 |  |
| 2026-11-21 14:08:49 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-21 14:01:09 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | -0.022 |  |
| 2026-11-21 14:02:16 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-11-21 14:02:25 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.042 |  |
| 2026-11-21 14:10:25 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.058 |  |
| 2026-11-21 14:02:49 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2026-11-21 14:00:36 | Weraganthota (Mahaweli Ganga) | -2.34 | 🟢 Normal | -0.090 |  |
| 2026-11-21 14:01:49 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.101 |  |
| 2026-11-21 14:05:27 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.107 |  |
| 2026-11-21 13:10:00 | Pitabeddara (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.115 |  |
| 2026-11-21 14:04:02 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.163 |  |
| 2026-11-21 14:04:10 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.181 |  |
| 2026-11-21 14:04:06 | Giriulla (Maha Oya) | 3.80 | 🟢 Normal | -0.226 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)