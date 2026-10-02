# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_03:06:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,385 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 03:06:15 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.018 |  |
| 2026-10-03 03:05:54 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.087 |  |
| 2026-10-03 03:05:36 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:05:33 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-10-03 03:05:03 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-10-03 03:04:54 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:04:50 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-03 03:04:43 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -16.941 |  |
| 2026-10-03 03:04:39 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:04:35 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-03 03:04:09 | Thawalama (Gin Ganga) | 2.76 | 🟢 Normal | -16.941 |  |
| 2026-10-03 03:04:07 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:03:38 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.021 |  |
| 2026-10-03 03:03:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-03 03:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:03:11 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-03 03:03:01 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.147 |  |
| 2026-10-03 03:02:56 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:01:54 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:01:50 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-10-03 03:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:01:36 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-03 03:01:12 | Ellagawa (Kalu Ganga) | 6.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 03:00:37 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-03 02:32:48 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.005 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 01:01:15 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-10-03 03:03:17 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-03 03:04:35 | Badalgama (Maha Oya) | 2.24 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-03 02:06:36 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-03 03:00:37 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-03 02:09:55 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-03 01:02:24 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-03 03:03:11 | Dunamale (Aththanagalu Oya) | 1.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-03 03:01:36 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-03 01:06:51 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-03 03:01:12 | Ellagawa (Kalu Ganga) | 6.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-03 02:00:59 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:04:07 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:04:39 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:01:39 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:05:36 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:08:06 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-03 00:01:11 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:04:54 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:02:56 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:03:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:09:49 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-02 18:06:13 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:01:54 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-03 01:06:23 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-03 03:03:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-10-03 02:32:48 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.005 |  |
| 2026-10-03 03:05:03 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-10-03 03:04:50 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | -0.010 |  |
| 2026-10-03 03:06:15 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.018 |  |
| 2026-10-03 02:06:24 | Pitabeddara (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-10-03 03:01:50 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-10-03 03:05:33 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.021 |  |
| 2026-10-03 03:03:38 | Rathnapura (Kalu Ganga) | 2.43 | 🟢 Normal | -0.021 |  |
| 2026-10-03 02:08:01 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.086 |  |
| 2026-10-03 03:05:54 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | -0.087 |  |
| 2026-10-03 03:03:01 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.147 |  |
| 2026-10-03 03:04:43 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -16.941 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)