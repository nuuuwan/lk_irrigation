# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_19:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,849 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 19:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-04 19:02:47 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-11-04 19:02:43 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | -0.059 |  |
| 2026-11-04 19:02:42 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-04 19:02:30 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.058 |  |
| 2026-11-04 19:01:58 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-11-04 19:01:40 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:01:36 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:01:24 | Peradeniya (Mahaweli Ganga) | 3.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 19:01:17 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 19:00:17 | Wellawaya (Kirindi Oya) | 2.25 | 🟢 Normal | 0.661 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 18:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-04 19:00:17 | Wellawaya (Kirindi Oya) | 2.25 | 🟢 Normal | 0.661 | 🔺 Rising |
| 2026-11-04 19:02:42 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-04 18:06:23 | Urawa (Nilwala Ganga) | 1.49 | 🟢 Normal | 0.190 | 🔺 Rising |
| 2026-11-04 18:03:12 | Magura (Kalu Ganga) | 2.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-04 18:03:09 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-04 18:07:50 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-04 18:03:39 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 19:01:24 | Peradeniya (Mahaweli Ganga) | 3.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 18:00:31 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 19:01:17 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-04 18:01:12 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-04 19:01:36 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-04 19:01:40 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:04:53 | Ellagawa (Kalu Ganga) | 6.72 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:03:46 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:03:06 | Moraketiya (Walawe Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:04:53 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:04:00 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:02:49 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-11-04 19:01:58 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-11-04 18:10:33 | Moragaswewa (Deduru Oya) | 4.30 | 🟢 Normal | -0.018 |  |
| 2026-11-04 19:02:47 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-11-04 19:03:15 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-11-04 18:06:00 | Panadugama (Nilwala Ganga) | 4.23 | 🟢 Normal | -0.020 |  |
| 2026-11-04 18:03:18 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | -0.022 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:02:43 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.031 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-04 18:08:56 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.050 |  |
| 2026-11-04 18:02:32 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | -0.054 |  |
| 2026-11-04 19:02:30 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.058 |  |
| 2026-11-04 19:02:43 | Giriulla (Maha Oya) | 2.29 | 🟢 Normal | -0.059 |  |
| 2026-11-04 17:10:32 | Dunamale (Aththanagalu Oya) | 2.20 | 🟢 Normal | -0.062 |  |
| 2026-11-04 18:02:16 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | -0.064 |  |
| 2026-11-04 18:03:10 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.073 |  |
| 2026-11-04 18:03:48 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.078 |  |
| 2026-11-04 18:01:27 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)