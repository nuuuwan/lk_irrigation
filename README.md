# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_05:03:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,439 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 05:03:01 | Yaka Wewa (Ma Oya) | 1.62 | 🟢 Normal | 1.194 | 🔺 Rising |
| 2026-09-13 05:02:24 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:02:21 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:02:16 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:02:14 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:02:09 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.040 |  |
| 2026-09-13 05:02:07 | Manampitiya (Mahaweli Ganga) | -0.49 | 🟢 Normal | -0.105 |  |
| 2026-09-13 05:02:06 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.031 |  |
| 2026-09-13 05:01:48 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-09-13 05:01:45 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:01:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:01:25 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-13 05:01:15 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:00:59 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:00:43 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:00:41 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:00:23 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.132 |  |
| 2026-09-13 04:52:03 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-13 04:38:35 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-13 04:22:19 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-13 04:21:06 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 04:00:32 | Magura (Kalu Ganga) | 2.85 | 🟢 Normal | 1.278 | 🔺 Rising |
| 2026-09-13 05:03:01 | Yaka Wewa (Ma Oya) | 1.62 | 🟢 Normal | 1.194 | 🔺 Rising |
| 2026-09-13 04:09:03 | Glencourse (Kelani Ganga) | 9.56 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-09-13 04:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-09-13 04:22:19 | Rathnapura (Kalu Ganga) | 1.54 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-13 04:07:04 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-13 05:01:25 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-09-13 04:02:25 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-13 04:04:01 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-09-13 04:02:49 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-13 04:38:35 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-13 04:52:03 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-13 04:16:12 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 03:05:42 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-13 05:02:21 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-12 18:00:50 | Weraganthota (Mahaweli Ganga) | -3.57 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:00:59 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 04:00:26 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:01:45 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:02:14 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 04:00:10 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-12 18:03:01 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:02:16 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:01:32 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:00:43 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-13 04:03:46 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-13 04:03:49 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 04:06:19 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-12 18:00:45 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:01:15 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 05:02:24 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 04:21:06 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.008 |  |
| 2026-09-13 04:08:28 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.012 |  |
| 2026-09-13 04:04:56 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-09-13 05:01:48 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-09-13 05:02:06 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.031 |  |
| 2026-09-13 05:02:09 | Hanwella (Kelani Ganga) | 0.67 | 🟢 Normal | -0.040 |  |
| 2026-09-13 05:02:07 | Manampitiya (Mahaweli Ganga) | -0.49 | 🟢 Normal | -0.105 |  |
| 2026-09-13 05:00:23 | Peradeniya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)