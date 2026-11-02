# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_17:26:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,979 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 17:26:08 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.015 |  |
| 2026-11-02 17:16:18 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.046 |  |
| 2026-11-02 17:13:12 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.027 |  |
| 2026-11-02 17:10:22 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.035 |  |
| 2026-11-02 17:10:13 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.048 |  |
| 2026-11-02 17:09:42 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-02 17:08:33 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.038 |  |
| 2026-11-02 17:08:27 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.036 |  |
| 2026-11-02 17:08:10 | Galgamuwa (Mee Oya) | 0.86 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-11-02 17:07:26 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-02 17:07:08 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.076 |  |
| 2026-11-02 17:06:39 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-02 17:05:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-02 17:05:53 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:05:52 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-02 17:05:35 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:04:58 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-11-02 17:04:53 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:04:29 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-11-02 17:03:50 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:03:40 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.040 |  |
| 2026-11-02 17:03:29 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-02 17:03:22 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-11-02 17:03:13 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-11-02 17:03:01 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-11-02 17:02:39 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 17:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | -0.060 |  |
| 2026-11-02 17:01:36 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-02 17:01:35 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:01:34 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:01:29 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:01:16 | Moragaswewa (Deduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:01:12 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 17:00:58 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:00:25 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-11-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.083 |  |
| 2026-11-02 17:00:06 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 17:08:10 | Galgamuwa (Mee Oya) | 0.86 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-11-02 17:03:29 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-02 17:06:39 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-02 17:09:42 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-02 17:01:36 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-02 17:05:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-02 17:02:39 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 17:01:12 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 17:01:34 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:01:16 | Moragaswewa (Deduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:01:35 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:05:53 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:00:58 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:03:50 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:00:06 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:04:53 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:01:29 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:03:01 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:05:35 | Urawa (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 17:05:52 | Pitabeddara (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-02 17:07:26 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-02 17:03:22 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-11-02 17:02:50 | Nawalapitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-11-02 17:26:08 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.015 |  |
| 2026-11-02 17:04:29 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-11-02 16:07:19 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | -0.020 |  |
| 2026-11-02 17:04:58 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-11-02 17:00:25 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-11-02 17:13:12 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | -0.027 |  |
| 2026-11-02 17:03:13 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.030 |  |
| 2026-11-02 17:10:22 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | -0.035 |  |
| 2026-11-02 17:08:27 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.036 |  |
| 2026-11-02 17:08:33 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.038 |  |
| 2026-11-02 17:03:40 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | -0.040 |  |
| 2026-11-02 17:16:18 | Rathnapura (Kalu Ganga) | 2.15 | 🟢 Normal | -0.046 |  |
| 2026-11-02 17:10:13 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.048 |  |
| 2026-11-02 17:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.74 | 🟢 Normal | -0.060 |  |
| 2026-11-02 17:07:08 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.076 |  |
| 2026-11-02 17:00:16 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)