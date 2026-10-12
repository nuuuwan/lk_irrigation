# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_21:10:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,181 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Urawa — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 21:10:20 | Panadugama (Nilwala Ganga) | 5.47 | 🟡 Alert | 0.228 | 🔺 Rising |
| 2026-10-12 21:08:31 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:07:58 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:07:21 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-10-12 21:07:05 | Urawa (Nilwala Ganga) | 2.82 | 🟡 Alert | 0.366 | 🔺 Rising |
| 2026-10-12 21:06:37 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.412 | 🔺 Rising |
| 2026-10-12 21:06:31 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.191 |  |
| 2026-10-12 21:06:17 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-12 21:05:24 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-10-12 21:04:58 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.040 |  |
| 2026-10-12 21:04:53 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.015 |  |
| 2026-10-12 21:04:51 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-12 21:04:48 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:04:35 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 21:04:24 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-12 21:03:52 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:03:50 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:03:50 | Dunamale (Aththanagalu Oya) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-10-12 21:03:49 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-12 21:03:26 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-12 21:03:25 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.029 |  |
| 2026-10-12 21:03:17 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 21:02:51 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | -0.031 |  |
| 2026-10-12 21:02:43 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:02:42 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:02:12 | Hanwella (Kelani Ganga) | 3.72 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-12 21:01:59 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-10-12 21:01:52 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:01:47 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 21:01:46 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:01:14 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-12 21:00:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-12 20:58:14 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.044 |  |
| 2026-10-12 20:30:40 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 21:07:05 | Urawa (Nilwala Ganga) | 2.82 | 🟡 Alert | 0.366 | 🔺 Rising |
| 2026-10-12 21:10:20 | Panadugama (Nilwala Ganga) | 5.47 | 🟡 Alert | 0.228 | 🔺 Rising |
| 2026-10-12 21:00:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-12 21:06:37 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.412 | 🔺 Rising |
| 2026-10-12 20:08:50 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-10-12 21:07:21 | Thawalama (Gin Ganga) | 3.20 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-10-12 21:01:59 | Magura (Kalu Ganga) | 2.78 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-10-12 21:03:26 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-12 21:02:12 | Hanwella (Kelani Ganga) | 3.72 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-12 21:06:17 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-10-12 21:04:24 | Ellagawa (Kalu Ganga) | 6.90 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-12 21:04:51 | Glencourse (Kelani Ganga) | 11.73 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-12 21:04:35 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 21:03:17 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-12 20:07:01 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-12 21:01:47 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 18:02:58 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:01:46 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:01:52 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:02:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:08:31 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:04:48 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:03:52 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:03:50 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-12 20:01:29 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:02:43 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:07:58 | Thanamalwila (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-10-12 21:03:49 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-12 21:01:14 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-12 21:04:53 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.015 |  |
| 2026-10-12 21:05:24 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.019 |  |
| 2026-10-12 21:03:50 | Dunamale (Aththanagalu Oya) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-10-12 21:03:25 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.029 |  |
| 2026-10-12 21:02:51 | Badalgama (Maha Oya) | 3.10 | 🟢 Normal | -0.031 |  |
| 2026-10-12 21:04:58 | Baddegama (Gin Ganga) | 2.45 | 🟢 Normal | -0.040 |  |
| 2026-10-12 20:58:14 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.044 |  |
| 2026-10-12 20:06:52 | Putupaula (Kalu Ganga) | 1.79 | 🟢 Normal | -0.053 |  |
| 2026-10-12 21:06:31 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)