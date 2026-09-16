# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_22:06:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,813 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 22:06:27 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:06:01 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:05:39 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.049 |  |
| 2026-09-16 22:05:30 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-16 22:04:58 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.206 |  |
| 2026-09-16 22:04:51 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-09-16 22:04:27 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-09-16 22:04:17 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-16 22:04:13 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:03:53 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-16 22:03:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 22:03:09 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-16 22:02:58 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-16 22:02:46 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:02:44 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 22:02:44 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 22:02:34 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.032 |  |
| 2026-09-16 22:02:33 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-16 22:02:29 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-16 22:02:25 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-16 22:02:21 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:02:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:02:14 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:02:11 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-16 22:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:01:56 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-09-16 22:01:30 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.068 |  |
| 2026-09-16 22:01:17 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:00:34 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-16 21:38:14 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-16 21:20:50 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 22:02:11 | Glencourse (Kelani Ganga) | 10.04 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-09-16 22:02:29 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-16 22:03:53 | Magura (Kalu Ganga) | 3.19 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-16 22:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-16 22:02:25 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-16 21:09:14 | Thawalama (Gin Ganga) | 2.43 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-16 22:03:09 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-16 22:05:30 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-16 21:38:14 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-16 22:02:58 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-16 21:04:03 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-16 22:02:33 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-16 22:02:44 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 21:05:37 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 22:02:44 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 22:03:13 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 18:02:49 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:06:27 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:02:46 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:02:21 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:00:34 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:06 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-16 21:17:05 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:04:13 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:02:14 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:01:17 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:02:17 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:06:01 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-09-16 22:04:51 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:00:42 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-16 22:01:56 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-09-16 22:04:27 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -0.010 |  |
| 2026-09-16 22:04:17 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-16 22:02:34 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.032 |  |
| 2026-09-16 21:06:46 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | -0.040 |  |
| 2026-09-16 22:05:39 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -0.049 |  |
| 2026-09-16 22:01:30 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.068 |  |
| 2026-09-16 22:04:58 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.206 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)