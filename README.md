# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_13:19:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,531 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 13:19:40 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.032 |  |
| 2026-11-05 13:17:02 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:15:54 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:10:37 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.073 |  |
| 2026-11-05 13:10:09 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | -0.036 |  |
| 2026-11-05 13:08:34 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.040 |  |
| 2026-11-05 13:07:51 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | -0.058 |  |
| 2026-11-05 13:07:29 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.019 |  |
| 2026-11-05 13:07:05 | Thanthirimale (Malwathu Oya) | 1.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-05 13:06:33 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:06:18 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.047 |  |
| 2026-11-05 13:05:53 | Kuda Oya (Kirindi Oya) | 2.33 | 🟢 Normal | -0.137 |  |
| 2026-11-05 13:05:23 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | -0.048 |  |
| 2026-11-05 13:05:20 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.048 |  |
| 2026-11-05 13:05:19 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-11-05 13:05:18 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:04:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:04:36 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-11-05 13:03:26 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:03:15 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:03:15 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:03:12 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-05 13:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:02:59 | Dunamale (Aththanagalu Oya) | 2.69 | 🟢 Normal | -0.059 |  |
| 2026-11-05 13:02:54 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-11-05 13:02:43 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.040 |  |
| 2026-11-05 13:02:31 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.138 |  |
| 2026-11-05 13:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.010 |  |
| 2026-11-05 13:02:27 | Ellagawa (Kalu Ganga) | 6.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-05 13:02:26 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:02:25 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:02:21 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:02:20 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.021 |  |
| 2026-11-05 13:01:48 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:01:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:01:37 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:01:30 | Moragaswewa (Deduru Oya) | 3.49 | 🟢 Normal | -0.030 |  |
| 2026-11-05 13:00:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.100 |  |
| 2026-11-05 13:00:48 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 13:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.010 |  |
| 2026-11-05 13:02:27 | Ellagawa (Kalu Ganga) | 6.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-05 13:00:48 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-05 13:07:05 | Thanthirimale (Malwathu Oya) | 1.91 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-05 12:14:20 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-05 13:01:48 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:01:37 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:03:15 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:15:54 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:03:26 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:01:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:04:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:02:21 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:02:25 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:17:02 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:05:18 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:02:26 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:03:15 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:07:29 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.019 |  |
| 2026-11-05 13:03:12 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-05 13:02:54 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-11-05 13:04:36 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-11-05 13:02:20 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.021 |  |
| 2026-11-05 13:01:30 | Moragaswewa (Deduru Oya) | 3.49 | 🟢 Normal | -0.030 |  |
| 2026-11-05 13:19:40 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.032 |  |
| 2026-11-05 13:10:09 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | -0.036 |  |
| 2026-11-05 13:02:43 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.040 |  |
| 2026-11-05 13:08:34 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.040 |  |
| 2026-11-05 13:06:18 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.047 |  |
| 2026-11-05 13:05:20 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.048 |  |
| 2026-11-05 13:05:23 | Giriulla (Maha Oya) | 2.11 | 🟢 Normal | -0.048 |  |
| 2026-11-05 13:05:19 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-11-05 13:07:51 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | -0.058 |  |
| 2026-11-05 13:02:59 | Dunamale (Aththanagalu Oya) | 2.69 | 🟢 Normal | -0.059 |  |
| 2026-11-05 13:10:37 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.073 |  |
| 2026-11-05 13:00:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.100 |  |
| 2026-11-05 13:05:53 | Kuda Oya (Kirindi Oya) | 2.33 | 🟢 Normal | -0.137 |  |
| 2026-11-05 13:02:31 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)