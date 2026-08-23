# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_19:11:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **241,551 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 19:11:21 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:10:05 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.018 |  |
| 2026-08-23 19:05:35 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.016 |  |
| 2026-08-23 19:05:16 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-23 19:05:10 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-08-23 19:05:10 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-23 19:05:04 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:04:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:04:38 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:04:12 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:04:09 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-23 19:03:45 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:03:19 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:03:17 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:02:42 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:02:41 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.057 |  |
| 2026-08-23 19:02:33 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:02:26 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:02:23 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:02:23 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:02:19 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | -0.050 |  |
| 2026-08-23 19:02:09 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-08-23 19:02:09 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:01:42 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:01:39 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-23 19:01:36 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.071 |  |
| 2026-08-23 19:01:36 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:01:30 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:01:24 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-08-23 19:00:56 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:00:20 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 19:05:10 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-08-23 19:05:16 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-23 19:04:09 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-23 18:05:08 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-23 19:05:10 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-23 19:01:39 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-23 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:03:17 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:01:42 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:02:23 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:11:21 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:02:33 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:03:45 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:00:56 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-23 18:04:57 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:01:36 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:02:42 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-23 18:02:39 | Ellagawa (Kalu Ganga) | 5.01 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:04:42 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:05:04 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:04:12 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:02:26 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:02:23 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:04:38 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-23 18:01:26 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:03:19 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:01:30 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-23 19:02:09 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-23 17:22:24 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.008 |  |
| 2026-08-23 19:01:24 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-08-23 19:02:09 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-08-23 18:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -0.011 |  |
| 2026-08-23 19:05:35 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.016 |  |
| 2026-08-23 19:10:05 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.018 |  |
| 2026-08-23 19:00:20 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.035 |  |
| 2026-08-23 18:01:17 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | -0.042 |  |
| 2026-08-23 19:02:19 | Hanwella (Kelani Ganga) | 1.03 | 🟢 Normal | -0.050 |  |
| 2026-08-23 19:02:41 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.057 |  |
| 2026-08-23 19:01:36 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)