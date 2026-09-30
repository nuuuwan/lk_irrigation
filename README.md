# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--30_15:08:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,156 measurements** from **39** stations.
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
| 2026-09-30 15:08:39 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | -0.020 |  |
| 2026-09-30 15:07:54 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 15:06:23 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | -0.010 |  |
| 2026-09-30 15:05:39 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:05:35 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-09-30 15:05:26 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 15:05:15 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-09-30 15:05:02 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.058 |  |
| 2026-09-30 15:04:28 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:04:28 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:04:16 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | -0.019 |  |
| 2026-09-30 15:04:02 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:04:00 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.021 |  |
| 2026-09-30 15:03:57 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.069 |  |
| 2026-09-30 15:03:23 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | -0.060 |  |
| 2026-09-30 15:03:09 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-30 15:02:54 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:02:52 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.062 |  |
| 2026-09-30 15:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 15:02:46 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.010 |  |
| 2026-09-30 15:02:43 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-09-30 15:02:39 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:02:32 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-09-30 15:02:26 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:02:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:02:23 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-30 15:02:18 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-30 15:02:00 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.061 |  |
| 2026-09-30 15:02:00 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.025 |  |
| 2026-09-30 15:01:34 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-30 15:00:41 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:00:36 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-30 15:00:23 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:00:22 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 15:03:09 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-30 15:00:36 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-30 15:02:18 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-30 15:05:26 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-30 15:02:48 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 15:07:54 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-30 15:02:54 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:02:26 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:01:52 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:02:39 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:00:23 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:02:26 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:06:37 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:04:28 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:03:57 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:04:02 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:05:39 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:04:28 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:00:41 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 14:03:36 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:00:22 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-30 15:05:35 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-09-30 15:02:23 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-30 15:02:32 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-09-30 15:01:34 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-30 15:06:23 | Panadugama (Nilwala Ganga) | 3.39 | 🟢 Normal | -0.010 |  |
| 2026-09-30 15:02:46 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.010 |  |
| 2026-09-30 14:13:44 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.016 |  |
| 2026-09-30 15:04:16 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | -0.019 |  |
| 2026-09-30 15:08:39 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | -0.020 |  |
| 2026-09-30 15:02:43 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-09-30 15:05:15 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-09-30 15:04:00 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.021 |  |
| 2026-09-30 15:02:00 | Magura (Kalu Ganga) | 1.81 | 🟢 Normal | -0.025 |  |
| 2026-09-30 15:05:02 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.058 |  |
| 2026-09-30 15:03:23 | Glencourse (Kelani Ganga) | 10.41 | 🟢 Normal | -0.060 |  |
| 2026-09-30 15:02:00 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | -0.061 |  |
| 2026-09-30 15:02:52 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.062 |  |
| 2026-09-30 15:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)