# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_13:18:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,850 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 13:18:49 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.047 |  |
| 2026-11-21 13:15:33 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:15:10 | Dunamale (Aththanagalu Oya) | 1.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-21 13:10:00 | Pitabeddara (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.115 |  |
| 2026-11-21 13:09:02 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:07:05 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | -0.028 |  |
| 2026-11-21 13:06:55 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-11-21 13:05:36 | Giriulla (Maha Oya) | 4.02 | 🟢 Normal | -0.158 |  |
| 2026-11-21 13:05:13 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:05:10 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.121 |  |
| 2026-11-21 13:05:09 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 13:04:54 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-21 13:04:38 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.221 |  |
| 2026-11-21 13:04:33 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:04:03 | Badalgama (Maha Oya) | 4.33 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-11-21 13:03:58 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.112 |  |
| 2026-11-21 13:03:52 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-21 13:03:43 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:03:32 | Moraketiya (Walawe Ganga) | 2.94 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:03:08 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-21 13:02:49 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 13:01:11 | Panadugama (Nilwala Ganga) | 5.08 | 🟡 Alert | -0.071 |  |
| 2026-11-21 13:04:03 | Badalgama (Maha Oya) | 4.33 | 🟢 Normal | 0.400 | 🔺 Rising |
| 2026-11-21 13:01:25 | Kuda Oya (Kirindi Oya) | 2.19 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-21 13:03:52 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-21 13:02:04 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-21 13:00:55 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 13:02:49 | Hanwella (Kelani Ganga) | 1.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 13:04:54 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-21 13:01:20 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 13:01:14 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 13:05:09 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 13:15:10 | Dunamale (Aththanagalu Oya) | 1.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-21 13:01:28 | Moragaswewa (Deduru Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:01:44 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:01:40 | Horowpothana (Yan Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:02:30 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:15:33 | Baddegama (Gin Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:03:32 | Moraketiya (Walawe Ganga) | 2.94 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:04:33 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:05:13 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:09:02 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:03:43 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-11-21 13:03:08 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-21 13:06:55 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-11-21 13:00:12 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-11-21 13:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-11-21 13:01:22 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.016 |  |
| 2026-11-21 13:07:05 | Thanamalwila (Kirindi Oya) | 1.84 | 🟢 Normal | -0.028 |  |
| 2026-11-21 13:02:31 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | -0.031 |  |
| 2026-11-21 13:18:49 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.047 |  |
| 2026-11-21 13:02:29 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.079 |  |
| 2026-11-21 13:03:58 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.112 |  |
| 2026-11-21 13:10:00 | Pitabeddara (Nilwala Ganga) | 1.79 | 🟢 Normal | -0.115 |  |
| 2026-11-21 13:05:10 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.121 |  |
| 2026-11-21 13:00:34 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.130 |  |
| 2026-11-21 13:05:36 | Giriulla (Maha Oya) | 4.02 | 🟢 Normal | -0.158 |  |
| 2026-11-21 13:04:38 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.221 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)