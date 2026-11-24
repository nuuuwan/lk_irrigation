# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_05:18:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,174 measurements** from **39** stations.
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
| 2026-11-24 05:18:13 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:10:57 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.147 |  |
| 2026-11-24 05:09:24 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:08:35 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.126 |  |
| 2026-11-24 05:08:20 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-11-24 05:08:18 | Ellagawa (Kalu Ganga) | 5.16 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-11-24 05:07:47 | Urawa (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.240 |  |
| 2026-11-24 05:07:23 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.043 |  |
| 2026-11-24 05:06:01 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 05:05:32 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.077 |  |
| 2026-11-24 05:05:02 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-24 05:04:48 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | -0.029 |  |
| 2026-11-24 05:04:43 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-24 05:04:24 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-24 05:04:22 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:04:00 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-24 05:03:56 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.135 |  |
| 2026-11-24 05:03:50 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.039 |  |
| 2026-11-24 05:03:39 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-11-24 05:02:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:02:35 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.212 |  |
| 2026-11-24 05:02:26 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:02:24 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 05:02:13 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | -0.073 |  |
| 2026-11-24 05:02:12 | Giriulla (Maha Oya) | 4.20 | 🟢 Normal | -0.238 |  |
| 2026-11-24 05:02:09 | Badalgama (Maha Oya) | 4.37 | 🟢 Normal | 0.638 | 🔺 Rising |
| 2026-11-24 05:01:17 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:01:08 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:00:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.152 |  |
| 2026-11-24 05:00:39 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-24 05:00:27 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.105 |  |
| 2026-11-24 05:00:23 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 05:08:20 | Ellagawa (Kalu Ganga) | 5.26 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-11-24 05:02:09 | Badalgama (Maha Oya) | 4.37 | 🟢 Normal | 0.638 | 🔺 Rising |
| 2026-11-24 04:05:53 | Hanwella (Kelani Ganga) | 2.50 | 🟢 Normal | 0.522 | 🔺 Rising |
| 2026-11-24 04:12:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-24 05:04:24 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-24 05:04:00 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-24 05:00:39 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-24 05:05:02 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-24 05:04:43 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-11-24 05:02:24 | Moragaswewa (Deduru Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 05:06:01 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 04:06:15 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 05:01:08 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:09:24 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:01:17 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 18:05:14 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:02:26 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:02:51 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-24 05:18:13 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-24 04:03:59 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-11-24 05:03:39 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | -0.020 |  |
| 2026-11-23 18:02:13 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-11-24 05:00:23 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 05:04:48 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | -0.029 |  |
| 2026-11-24 05:03:50 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.039 |  |
| 2026-11-24 05:07:23 | Rathnapura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.043 |  |
| 2026-11-23 18:00:35 | Weraganthota (Mahaweli Ganga) | -2.49 | 🟢 Normal | -0.050 |  |
| 2026-11-24 04:07:26 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.066 |  |
| 2026-11-24 05:02:13 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | -0.073 |  |
| 2026-11-24 05:05:32 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.077 |  |
| 2026-11-24 05:00:27 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.105 |  |
| 2026-11-24 05:08:35 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.126 |  |
| 2026-11-24 05:03:56 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | -0.135 |  |
| 2026-11-24 05:10:57 | Holombuwa (Kelani Ganga) | 1.05 | 🟢 Normal | -0.147 |  |
| 2026-11-24 05:00:54 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.152 |  |
| 2026-11-24 05:02:35 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | -0.212 |  |
| 2026-11-24 05:02:12 | Giriulla (Maha Oya) | 4.20 | 🟢 Normal | -0.238 |  |
| 2026-11-24 05:07:47 | Urawa (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.240 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)