# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_15:02:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,908 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 15:02:55 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.088 |  |
| 2026-11-21 15:02:54 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-21 15:02:51 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-21 15:02:48 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-21 15:02:40 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-21 15:02:20 | Moraketiya (Walawe Ganga) | 3.00 | 🟡 Alert | 0.067 | 🔺 Rising |
| 2026-11-21 15:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-21 15:02:14 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.052 |  |
| 2026-11-21 15:02:10 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-21 15:02:07 | Kuda Oya (Kirindi Oya) | 2.38 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-11-21 15:02:04 | Panadugama (Nilwala Ganga) | 4.95 | 🟢 Normal | -0.090 |  |
| 2026-11-21 15:02:02 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-21 15:02:02 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.039 |  |
| 2026-11-21 15:01:47 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 15:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 15:01:15 | Giriulla (Maha Oya) | 3.61 | 🟢 Normal | -0.199 |  |
| 2026-11-21 15:01:09 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.023 |  |
| 2026-11-21 15:01:09 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-11-21 15:00:52 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-11-21 14:59:34 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 14:37:46 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.075 |  |
| 2026-11-21 14:31:20 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 15:02:20 | Moraketiya (Walawe Ganga) | 3.00 | 🟡 Alert | 0.067 | 🔺 Rising |
| 2026-11-21 14:03:43 | Badalgama (Maha Oya) | 4.49 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-11-21 15:02:07 | Kuda Oya (Kirindi Oya) | 2.38 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-11-21 15:02:40 | Hanwella (Kelani Ganga) | 1.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-21 14:04:02 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 14:06:00 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 14:03:28 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 15:02:51 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-21 14:59:34 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 14:04:40 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 15:01:47 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 14:05:35 | Glencourse (Kelani Ganga) | 10.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 14:06:15 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-21 14:31:20 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-21 15:01:20 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 15:02:02 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:12:50 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:02:18 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:09:44 | Dunamale (Aththanagalu Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-11-21 15:02:10 | Thanamalwila (Kirindi Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-21 14:20:03 | Norwood (Kelani Ganga) | 0.87 | 🟢 Normal | -0.008 |  |
| 2026-11-21 15:02:48 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-21 15:02:54 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-11-21 15:01:09 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-11-21 15:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-21 14:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.78 | 🟢 Normal | -0.020 |  |
| 2026-11-21 15:00:52 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-11-21 15:01:09 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.023 |  |
| 2026-11-21 15:02:02 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.039 |  |
| 2026-11-21 15:02:14 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.052 |  |
| 2026-11-21 14:10:25 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.058 |  |
| 2026-11-21 14:02:49 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.060 |  |
| 2026-11-21 14:37:46 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.075 |  |
| 2026-11-21 15:02:55 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.088 |  |
| 2026-11-21 15:02:04 | Panadugama (Nilwala Ganga) | 4.95 | 🟢 Normal | -0.090 |  |
| 2026-11-21 14:05:27 | Rathnapura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.107 |  |
| 2026-11-21 14:04:02 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | -0.163 |  |
| 2026-11-21 15:01:15 | Giriulla (Maha Oya) | 3.61 | 🟢 Normal | -0.199 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)