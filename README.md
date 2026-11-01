# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_13:02:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,880 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 13:02:46 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-01 13:02:43 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:02:38 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-01 13:02:11 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:01:55 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:01:52 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-11-01 13:01:18 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 13:01:06 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-01 13:00:52 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-01 13:00:43 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:00:34 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:00:33 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.011 |  |
| 2026-11-01 13:00:24 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:00:15 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 12:04:28 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-11-01 12:06:15 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | 0.945 | 🔺 Rising |
| 2026-11-01 13:02:38 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-01 12:02:00 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-01 13:02:46 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-01 12:04:38 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 13:00:52 | Nagalagam Street (Kelani Ganga) | 0.62 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-01 13:01:06 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-01 13:01:18 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 13:01:52 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:00:34 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 12:01:43 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:01:55 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:00:43 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:00:15 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:02:43 | Hanwella (Kelani Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 12:04:30 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 12:01:29 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:00:24 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 12:03:09 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-01 12:11:06 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-11-01 12:01:28 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:02:11 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-01 12:05:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 13:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-11-01 12:01:16 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-11-01 12:05:47 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.010 |  |
| 2026-11-01 12:03:01 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-11-01 13:00:33 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.011 |  |
| 2026-11-01 12:02:52 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.011 |  |
| 2026-11-01 12:09:03 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.011 |  |
| 2026-11-01 12:02:54 | Galgamuwa (Mee Oya) | 1.03 | 🟢 Normal | -0.012 |  |
| 2026-11-01 12:04:21 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.026 |  |
| 2026-11-01 12:04:59 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.026 |  |
| 2026-11-01 12:09:31 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.028 |  |
| 2026-11-01 12:01:57 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | -0.028 |  |
| 2026-11-01 12:07:33 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.029 |  |
| 2026-11-01 12:03:09 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.031 |  |
| 2026-11-01 12:06:11 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)