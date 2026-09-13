# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_07:31:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,538 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 07:31:10 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-13 07:26:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-09-13 07:12:08 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:09:58 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:09:38 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-13 07:08:40 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.100 |  |
| 2026-09-13 07:07:53 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2026-09-13 07:06:45 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-13 07:06:44 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-13 07:06:06 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:06:03 | Magura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.047 |  |
| 2026-09-13 07:05:58 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-09-13 07:05:44 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:05:36 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 07:05:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.191 |  |
| 2026-09-13 07:05:01 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:04:50 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-13 07:04:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:04:32 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 07:03:51 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-09-13 07:03:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:03:31 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-13 07:03:26 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-09-13 07:03:17 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:03:11 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:02:55 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:02:36 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:02:23 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-09-13 07:02:23 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-13 07:02:04 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-13 07:01:52 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:01:23 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-13 07:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-09-13 07:01:18 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:01:12 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | -0.002 |  |
| 2026-09-13 07:01:01 | Manampitiya (Mahaweli Ganga) | -0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:00:56 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:00:23 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:00:14 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:00:07 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 07:07:53 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2026-09-13 07:26:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.50 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-09-13 07:03:26 | Hanwella (Kelani Ganga) | 0.96 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-09-13 07:05:58 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-09-13 07:06:44 | Glencourse (Kelani Ganga) | 10.27 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-09-13 07:06:45 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-13 07:02:04 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-13 07:03:31 | Ellagawa (Kalu Ganga) | 4.36 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-13 07:01:23 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-13 07:02:23 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-13 07:04:50 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-13 07:09:38 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-13 07:31:10 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-09-13 07:04:32 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 07:05:36 | Baddegama (Gin Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 07:05:01 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:00:07 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:01:18 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:02:36 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:09:58 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:00:56 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:03:11 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:00:14 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:12:08 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:04:34 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:01:52 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:03:17 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:06:06 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:05:44 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:01:01 | Manampitiya (Mahaweli Ganga) | -0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:00:23 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:02:55 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 07:01:12 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | -0.002 |  |
| 2026-09-13 07:02:23 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-09-13 07:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-09-13 07:03:51 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-09-13 07:06:03 | Magura (Kalu Ganga) | 3.95 | 🟢 Normal | -0.047 |  |
| 2026-09-13 07:08:40 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.100 |  |
| 2026-09-13 07:05:17 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)