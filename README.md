# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_16:30:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,024 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 16:30:05 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-01 16:23:03 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.007 |  |
| 2026-11-01 16:13:57 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-01 16:09:41 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-11-01 16:09:32 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:08:59 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:08:56 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-01 16:08:47 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-11-01 16:07:47 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-01 16:07:38 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | -0.011 |  |
| 2026-11-01 16:07:05 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:06:31 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.081 |  |
| 2026-11-01 16:06:29 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-11-01 16:06:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:06:09 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-01 16:05:35 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:05:13 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-01 16:04:59 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:04:45 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-01 16:04:26 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:04:21 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 16:04:01 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:03:57 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-01 16:03:39 | Galgamuwa (Mee Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:03:37 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:03:31 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.096 | 🔺 Rising |
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
| 2026-11-01 16:30:05 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | 0.000 |  |
| 2026-11-01 16:08:47 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.241 | 🔺 Rising |
| 2026-11-01 16:04:45 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-01 16:05:13 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-01 16:03:31 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-01 16:01:22 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-01 16:08:56 | Magura (Kalu Ganga) | 2.14 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-01 16:02:43 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-01 16:06:09 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-01 16:04:21 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-01 16:03:57 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-01 16:07:47 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-01 16:13:57 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-01 16:01:12 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-01 16:01:21 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:04:01 | Moragaswewa (Deduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:01:25 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:09:32 | Panadugama (Nilwala Ganga) | 4.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:08:59 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:02:12 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:00:13 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:05:35 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:04:26 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:02:30 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:03:37 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 16:23:03 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.007 |  |
| 2026-11-01 16:09:41 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-11-01 16:07:05 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:04:59 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:03:39 | Galgamuwa (Mee Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:06:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:01:05 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-01 16:07:38 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | -0.011 |  |
| 2026-11-01 16:06:29 | Pitabeddara (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-11-01 16:02:50 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | -0.019 |  |
| 2026-11-01 16:01:06 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-11-01 16:01:44 | Moraketiya (Walawe Ganga) | 1.09 | 🟢 Normal | -0.051 |  |
| 2026-11-01 16:06:31 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.081 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)