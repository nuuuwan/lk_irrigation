# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_04:34:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,374 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 04:34:42 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:30:44 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -576.000 |  |
| 2026-11-03 04:30:43 | Magura (Kalu Ganga) | 2.81 | 🟢 Normal | -576.000 |  |
| 2026-11-03 04:30:42 | Magura (Kalu Ganga) | 2.94 | 🟢 Normal | -576.000 |  |
| 2026-11-03 04:30:40 | Magura (Kalu Ganga) | 2.75 | 🟢 Normal | -576.000 |  |
| 2026-11-03 04:23:40 | Padiyathalawa (Maduru Oya) | 2.20 | 🟢 Normal | -0.470 |  |
| 2026-11-03 04:18:37 | Panadugama (Nilwala Ganga) | 4.13 | 🟢 Normal | -0.026 |  |
| 2026-11-03 04:15:47 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:15:01 | Horowpothana (Yan Oya) | 3.28 | 🟢 Normal | -0.017 |  |
| 2026-11-03 04:14:00 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-03 04:11:54 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:10:45 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.088 |  |
| 2026-11-03 04:08:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-03 04:08:07 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 04:07:06 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 04:06:39 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.022 |  |
| 2026-11-03 04:05:57 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 04:05:45 | Moragaswewa (Deduru Oya) | 2.36 | 🟢 Normal | 1.357 | 🔺 Rising |
| 2026-11-03 04:05:04 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-11-03 04:04:50 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:04:47 | Siyambalanduwa (Heda Oya) | 1.40 | 🟢 Normal | -0.028 |  |
| 2026-11-03 04:04:43 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-11-03 04:03:52 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.080 |  |
| 2026-11-03 04:03:04 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.258 |  |
| 2026-11-03 04:02:54 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-03 04:02:32 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-03 04:02:21 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal | -0.169 |  |
| 2026-11-03 04:02:17 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -1.228 |  |
| 2026-11-03 04:02:16 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.073 |  |
| 2026-11-03 04:02:10 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:02:08 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-03 04:01:44 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:01:28 | Thaldena (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.140 |  |
| 2026-11-03 04:01:09 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 04:00:12 | Wellawaya (Kirindi Oya) | 1.88 | 🟢 Normal | -1.014 |  |
| 2026-11-03 03:59:10 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 04:05:45 | Moragaswewa (Deduru Oya) | 2.36 | 🟢 Normal | 1.357 | 🔺 Rising |
| 2026-11-03 04:04:43 | Hanwella (Kelani Ganga) | 3.26 | 🟢 Normal | 0.355 | 🔺 Rising |
| 2026-11-03 04:05:04 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-11-03 04:02:32 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-03 04:14:00 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-03 04:02:54 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-03 03:09:55 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-03 04:08:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.48 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-11-03 04:08:07 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-03 04:05:57 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 04:07:06 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 03:04:46 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 04:01:09 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 04:01:44 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:34:42 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:02:10 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:01:57 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:04:50 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:15:47 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:11:54 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-03 04:15:01 | Horowpothana (Yan Oya) | 3.28 | 🟢 Normal | -0.017 |  |
| 2026-11-03 03:05:20 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-03 04:06:39 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.022 |  |
| 2026-11-03 04:18:37 | Panadugama (Nilwala Ganga) | 4.13 | 🟢 Normal | -0.026 |  |
| 2026-11-03 04:04:47 | Siyambalanduwa (Heda Oya) | 1.40 | 🟢 Normal | -0.028 |  |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-03 04:02:16 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.073 |  |
| 2026-11-03 04:03:52 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.080 |  |
| 2026-11-03 04:10:45 | Holombuwa (Kelani Ganga) | 1.42 | 🟢 Normal | -0.088 |  |
| 2026-11-03 04:01:28 | Thaldena (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.140 |  |
| 2026-11-03 04:02:21 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal | -0.169 |  |
| 2026-11-03 04:03:04 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.258 |  |
| 2026-11-03 04:23:40 | Padiyathalawa (Maduru Oya) | 2.20 | 🟢 Normal | -0.470 |  |
| 2026-11-03 04:00:12 | Wellawaya (Kirindi Oya) | 1.88 | 🟢 Normal | -1.014 |  |
| 2026-11-03 04:02:17 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -1.228 |  |
| 2026-11-03 04:30:44 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | -576.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)