# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_15:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **328,047 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 15:03:15 | Badalgama (Maha Oya) | 3.75 | 🟢 Normal | -0.058 |  |
| 2026-11-28 15:03:14 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-11-28 15:03:07 | Moragaswewa (Deduru Oya) | 2.19 | 🟢 Normal | -0.020 |  |
| 2026-11-28 15:03:05 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-28 15:03:00 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.051 |  |
| 2026-11-28 15:02:50 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 15:02:49 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-28 15:02:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 15:02:31 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 15:02:12 | Thanamalwila (Kirindi Oya) | 2.01 | 🟢 Normal | -0.049 |  |
| 2026-11-28 15:02:02 | Ellagawa (Kalu Ganga) | 6.84 | 🟢 Normal | -0.100 |  |
| 2026-11-28 15:01:55 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-11-28 15:01:40 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-28 15:01:27 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-11-28 15:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-11-28 15:01:01 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -1.147 |  |
| 2026-11-28 15:00:45 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 14:07:58 | Dunamale (Aththanagalu Oya) | 4.00 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-28 14:05:30 | Moraketiya (Walawe Ganga) | 3.13 | 🟡 Alert | 0.000 |  |
| 2026-11-28 14:02:53 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | -0.020 |  |
| 2026-11-28 14:13:58 | Panadugama (Nilwala Ganga) | 5.22 | 🟡 Alert | -0.025 |  |
| 2026-11-28 15:03:14 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-11-28 14:06:43 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-11-28 14:03:43 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-28 14:05:22 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-28 15:02:50 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-28 14:03:15 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 14:03:41 | Manampitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 15:02:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 15:00:45 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-11-28 14:10:49 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-28 15:03:05 | Baddegama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-28 15:02:49 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-28 15:01:55 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-11-28 15:02:31 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 14:15:44 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | -0.008 |  |
| 2026-11-28 14:02:32 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-11-28 15:01:40 | Siyambalanduwa (Heda Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-11-28 14:15:00 | Urawa (Nilwala Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-11-28 14:02:48 | Wellawaya (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-28 15:03:07 | Moragaswewa (Deduru Oya) | 2.19 | 🟢 Normal | -0.020 |  |
| 2026-11-28 15:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-11-28 14:06:00 | Rathnapura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.021 |  |
| 2026-11-28 14:03:55 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-11-28 14:04:24 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | -0.021 |  |
| 2026-11-28 15:01:27 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | -0.031 |  |
| 2026-11-28 15:02:12 | Thanamalwila (Kirindi Oya) | 2.01 | 🟢 Normal | -0.049 |  |
| 2026-11-28 15:03:00 | Holombuwa (Kelani Ganga) | 1.21 | 🟢 Normal | -0.051 |  |
| 2026-11-28 15:03:15 | Badalgama (Maha Oya) | 3.75 | 🟢 Normal | -0.058 |  |
| 2026-11-28 14:05:00 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.075 |  |
| 2026-11-28 14:04:35 | Giriulla (Maha Oya) | 2.56 | 🟢 Normal | -0.079 |  |
| 2026-11-28 15:02:02 | Ellagawa (Kalu Ganga) | 6.84 | 🟢 Normal | -0.100 |  |
| 2026-11-28 14:03:20 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | -0.109 |  |
| 2026-11-28 14:13:08 | Magura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.117 |  |
| 2026-11-28 14:02:50 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | -0.126 |  |
| 2026-11-28 15:01:01 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -1.147 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)