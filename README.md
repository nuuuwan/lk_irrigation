# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_16:06:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,952 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 16:06:01 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:05:39 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 16:05:11 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-09-02 16:04:32 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:04:28 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:04:06 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:03:52 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-09-02 16:03:35 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:03:32 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-02 16:03:23 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.043 |  |
| 2026-09-02 16:03:22 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.012 |  |
| 2026-09-02 16:03:18 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:03:18 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:03:13 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:03:07 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:03:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-02 16:02:59 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-09-02 16:02:50 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 16:02:40 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:02:35 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-02 16:02:10 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:02:07 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:02:07 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:01:57 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.088 |  |
| 2026-09-02 16:01:49 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-02 16:01:37 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-09-02 16:01:29 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:01:15 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-09-02 16:00:15 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 15:13:06 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.952 | 🔺 Rising |
| 2026-09-02 16:01:49 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-02 16:03:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-02 16:02:35 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-02 15:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 16:02:50 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 16:05:39 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 16:02:07 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 15:01:04 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:01:37 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:01:29 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:02:07 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 15:04:42 | Galgamuwa (Mee Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 15:10:44 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:03:18 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:04:28 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:03:13 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:03:35 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:04:32 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:17:26 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:00:15 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 15:03:06 | Siyambalanduwa (Heda Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:02:40 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:03:18 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:04:06 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:06:01 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:02:10 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:03:07 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 16:05:11 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-09-02 16:03:32 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-02 16:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-09-02 16:01:15 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-09-02 15:02:26 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-02 16:03:52 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-09-02 16:03:22 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.012 |  |
| 2026-09-02 16:02:59 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.019 |  |
| 2026-09-02 15:07:34 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-09-02 16:03:23 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | -0.043 |  |
| 2026-09-02 16:01:57 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)