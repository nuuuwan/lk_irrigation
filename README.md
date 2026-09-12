# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_02:04:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,341 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 02:04:39 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:04:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-13 02:04:30 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-13 02:04:29 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-13 02:04:22 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 02:04:08 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.141 |  |
| 2026-09-13 02:04:05 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:04:05 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-09-13 02:03:30 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:03:17 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:03:03 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:02:52 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 02:02:22 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-09-13 02:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-13 02:01:49 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:01:36 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:01:24 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:01:13 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:01:08 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-09-13 02:01:02 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:00:36 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 02:02:22 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-09-13 02:04:05 | Glencourse (Kelani Ganga) | 9.06 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-09-13 02:04:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-13 02:04:30 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-13 00:05:43 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-13 01:17:32 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-13 02:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-13 02:04:22 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 02:02:52 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-13 00:07:11 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-13 02:04:29 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-13 01:07:29 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-13 01:12:36 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-13 02:03:17 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-09-12 18:00:50 | Weraganthota (Mahaweli Ganga) | -3.57 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:01:02 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:00:36 | Nakkala (Kumbukkan Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:03:03 | Moragaswewa (Deduru Oya) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 01:04:22 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:01:49 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-12 18:03:01 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-13 01:16:22 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:03:30 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:01:13 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:01:24 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:04:39 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:00:57 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:04:05 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 01:07:47 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 00:02:25 | Manampitiya (Mahaweli Ganga) | -0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-12 18:00:45 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-13 02:01:36 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 01:01:58 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 01:08:52 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.009 |  |
| 2026-09-13 02:01:08 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | -0.010 |  |
| 2026-09-13 01:13:50 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-09-13 00:02:16 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-09-13 02:04:08 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)