# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_00:10:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **274,594 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 00:10:16 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:09:23 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | -0.029 |  |
| 2026-09-30 00:08:42 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:08:22 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:07:09 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:07:01 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:06:36 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-30 00:05:44 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:05:38 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:05:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:04:55 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:04:26 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:04:22 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.020 |  |
| 2026-09-30 00:04:20 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:04:06 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:03:36 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:03:33 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | -0.028 |  |
| 2026-09-30 00:02:45 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:02:37 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:02:29 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:02:26 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-30 00:02:20 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-30 00:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:02:16 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:01:51 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:01:46 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.030 |  |
| 2026-09-30 00:01:41 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:01:27 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:01:15 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:01:12 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:01:00 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-30 00:00:56 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:00:43 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:35:19 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 00:02:20 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-30 00:02:26 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-30 00:01:00 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-30 00:06:36 | Peradeniya (Mahaweli Ganga) | 3.02 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-29 18:00:18 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:01:12 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:01:41 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-09-29 22:02:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:00:44 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:04:05 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:05:38 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:07:09 | Panadugama (Nilwala Ganga) | 3.65 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:01:51 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:04:55 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:02:16 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:05:32 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:03:36 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:05:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:08:42 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:01:27 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:10:16 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-29 18:00:44 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:08:22 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:01:15 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 00:02:29 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-29 23:06:58 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -0.009 |  |
| 2026-09-30 00:05:44 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:04:20 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:04:06 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:02:45 | Giriulla (Maha Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:02:37 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:07:01 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:00:56 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-30 00:04:22 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.020 |  |
| 2026-09-30 00:03:33 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | -0.028 |  |
| 2026-09-30 00:09:23 | Baddegama (Gin Ganga) | 2.72 | 🟢 Normal | -0.029 |  |
| 2026-09-30 00:01:46 | Ellagawa (Kalu Ganga) | 5.55 | 🟢 Normal | -0.030 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)