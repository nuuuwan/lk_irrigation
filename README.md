# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_16:30:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,198 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 16:30:31 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:27:44 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:13:50 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:09:59 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.063 |  |
| 2026-09-30 16:08:17 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-09-30 16:07:59 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-09-30 16:06:37 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-09-30 16:06:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:06:16 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:06:00 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.087 |  |
| 2026-09-30 16:05:42 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.019 |  |
| 2026-09-30 16:05:31 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-09-30 16:05:17 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-30 16:04:45 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:04:17 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.039 |  |
| 2026-09-30 16:03:54 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.020 |  |
| 2026-09-30 16:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.090 |  |
| 2026-09-30 16:03:08 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-09-30 16:03:06 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.012 |  |
| 2026-09-30 16:02:58 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:02:53 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:02:53 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:02:50 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-09-30 16:02:46 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:02:43 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-30 16:02:07 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 16:02:06 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:02:00 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 16:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-09-30 16:01:50 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-09-30 16:01:45 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:01:40 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-30 16:01:25 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.020 |  |
| 2026-09-30 16:00:43 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.020 |  |
| 2026-09-30 16:00:41 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:00:40 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-09-30 16:00:36 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:00:32 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:00:05 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 16:02:43 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-30 16:01:40 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-30 16:05:17 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-30 16:02:07 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 16:02:00 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 16:00:36 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:00:32 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:02:46 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:06:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:02:53 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:01:45 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:27:44 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:00:41 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:02:06 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:04:45 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:30:31 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:00:41 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:02:58 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:00:05 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:13:50 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:06:16 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-30 16:06:37 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-09-30 16:08:17 | Panadugama (Nilwala Ganga) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-09-30 16:05:31 | Badalgama (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-09-30 16:01:54 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-09-30 16:01:50 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-09-30 16:00:40 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.011 |  |
| 2026-09-30 16:03:06 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.012 |  |
| 2026-09-30 16:05:42 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.019 |  |
| 2026-09-30 16:03:54 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | -0.020 |  |
| 2026-09-30 16:03:08 | Hanwella (Kelani Ganga) | 2.24 | 🟢 Normal | -0.020 |  |
| 2026-09-30 16:07:59 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-09-30 16:00:43 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.020 |  |
| 2026-09-30 16:01:25 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.020 |  |
| 2026-09-30 16:02:50 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-09-30 16:04:17 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.039 |  |
| 2026-09-30 16:09:59 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.063 |  |
| 2026-09-30 16:06:00 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.087 |  |
| 2026-09-30 16:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)