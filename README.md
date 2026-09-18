# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_02:19:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,741 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 02:19:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-19 02:19:11 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2026-09-19 02:16:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:14:19 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-09-19 02:10:23 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:09:37 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -12.923 |  |
| 2026-09-19 02:07:01 | Baddegama (Gin Ganga) | 3.27 | 🟢 Normal | -12.923 |  |
| 2026-09-19 02:06:38 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -3.273 |  |
| 2026-09-19 02:06:16 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | -3.273 |  |
| 2026-09-19 02:04:57 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:03:46 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 02:03:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:03:26 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-19 02:03:19 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:03:06 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-09-19 02:03:02 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:03:01 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-19 02:02:26 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.080 |  |
| 2026-09-19 02:02:14 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-19 02:02:08 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:02:06 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:01:50 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:01:45 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:01:35 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-19 02:01:35 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-09-19 02:01:11 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:01:09 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 02:00:52 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | -0.005 |  |
| 2026-09-19 02:00:51 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-09-19 02:00:35 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:00:26 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 02:00:51 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-09-19 02:14:19 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-09-19 02:19:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-09-19 01:02:17 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-19 02:03:01 | Peradeniya (Mahaweli Ganga) | 2.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-19 02:01:35 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-19 02:03:26 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-19 01:03:55 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-19 02:01:09 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 02:03:46 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-19 01:43:50 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-09-19 02:02:08 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:00:35 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:03:31 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:01:50 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:04:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:01:11 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:03:19 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:03:02 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:01:45 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:02:06 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:04:57 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:10:23 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-19 00:04:51 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:16:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 02:00:52 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | -0.005 |  |
| 2026-09-18 18:03:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-19 02:03:06 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-09-19 02:02:14 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-19 02:00:26 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-09-19 00:11:55 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.018 |  |
| 2026-09-19 00:07:14 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-09-19 01:08:47 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.021 |  |
| 2026-09-19 02:01:35 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-09-19 02:19:11 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2026-09-19 02:02:26 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.080 |  |
| 2026-09-19 02:06:38 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -3.273 |  |
| 2026-09-19 02:09:37 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -12.923 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)