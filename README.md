# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_16:02:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,998 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 16:02:50 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.019 |  |
| 2026-11-01 16:02:43 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-01 16:02:30 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:02:12 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:01:44 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.051 |  |
| 2026-11-01 16:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:01:25 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:01:22 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-01 16:01:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:01:12 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 16:01:06 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-11-01 16:01:05 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:00:13 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 15:02:29 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | -0.011 |  |
| 2026-11-01 15:02:14 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-01 16:01:22 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-01 15:01:59 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-01 15:03:50 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-01 16:02:43 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-01 15:05:12 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 16:01:12 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 16:01:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 15:01:44 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:01:25 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 15:00:21 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 15:03:10 | Galgamuwa (Mee Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-01 15:07:15 | Magura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-11-01 15:03:58 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 15:10:30 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | 0.000 |  |
| 2026-11-01 15:18:30 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:02:12 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:00:13 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 15:12:55 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:02:30 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:01:05 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-01 15:02:07 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-11-01 15:08:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-11-01 15:06:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | -0.013 |  |
| 2026-11-01 15:02:52 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.013 |  |
| 2026-11-01 15:13:58 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.016 |  |
| 2026-11-01 15:03:53 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-11-01 16:02:50 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.019 |  |
| 2026-11-01 15:03:07 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-11-01 15:01:34 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.023 |  |
| 2026-11-01 16:01:06 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-11-01 15:04:26 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.041 |  |
| 2026-11-01 15:02:39 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.049 |  |
| 2026-11-01 16:01:44 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.051 |  |
| 2026-11-01 15:01:33 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.062 |  |
| 2026-11-01 15:01:19 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.103 |  |
| 2026-11-01 15:07:37 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)