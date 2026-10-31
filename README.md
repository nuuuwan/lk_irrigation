# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_02:03:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,472 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 02:03:42 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-11-01 02:03:34 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.030 |  |
| 2026-11-01 02:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -0.049 |  |
| 2026-11-01 02:03:18 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | -0.051 |  |
| 2026-11-01 02:03:16 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 02:03:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-11-01 02:02:53 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-11-01 02:02:49 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-11-01 02:02:39 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.005 |  |
| 2026-11-01 02:02:26 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 02:02:21 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-01 02:02:21 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.005 |  |
| 2026-11-01 02:02:04 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-01 02:01:43 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 02:01:29 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 02:00:15 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-01 02:00:13 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-01 02:00:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:36:19 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.014 |  |
| 2026-11-01 01:29:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.215 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 02:00:15 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-01 02:03:08 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.215 | 🔺 Rising |
| 2026-11-01 01:05:36 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-01 01:04:13 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-01 01:04:50 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-01 02:02:04 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-01 02:00:13 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-01 01:04:01 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-01 02:01:29 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 02:00:07 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 02:03:16 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 02:02:26 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:09:38 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:18:57 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.000 |  |
| 2026-11-01 02:01:43 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:03:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:07:54 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:58 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-01 02:02:21 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-01 02:02:21 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.005 |  |
| 2026-11-01 02:02:39 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.005 |  |
| 2026-11-01 01:05:21 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-11-01 01:05:56 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:06:44 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-01 02:02:53 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-11-01 02:03:42 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:02:27 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-11-01 01:36:19 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.014 |  |
| 2026-11-01 01:05:33 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-11-01 02:02:49 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-10-31 18:04:44 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.020 |  |
| 2026-11-01 02:03:34 | Moragaswewa (Deduru Oya) | 0.99 | 🟢 Normal | -0.030 |  |
| 2026-11-01 01:06:11 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | -0.039 |  |
| 2026-11-01 01:03:00 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.041 |  |
| 2026-11-01 02:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.94 | 🟢 Normal | -0.049 |  |
| 2026-11-01 02:03:18 | Putupaula (Kalu Ganga) | 1.39 | 🟢 Normal | -0.051 |  |
| 2026-11-01 01:04:12 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)