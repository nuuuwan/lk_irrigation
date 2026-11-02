# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_04:03:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,351 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2026-11-03 03:59:10 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | -0.118 |  |
| 2026-11-03 03:39:48 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.085 |  |
| 2026-11-03 03:15:55 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.290 |  |
| 2026-11-03 03:13:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:13:44 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | 0.049 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 00:15:17 | Magura (Kalu Ganga) | 2.38 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-11-03 04:02:32 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-03 03:05:30 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-11-03 03:04:53 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-03 03:06:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-03 03:04:44 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-03 03:02:57 | Moragaswewa (Deduru Oya) | 0.94 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-02 18:02:49 | Galgamuwa (Mee Oya) | 0.91 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-11-03 04:02:54 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-03 03:09:55 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-03 03:03:43 | Horowpothana (Yan Oya) | 3.30 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-03 03:06:28 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 03:00:08 | Siyambalanduwa (Heda Oya) | 1.43 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 03:04:46 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 04:01:09 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 04:01:44 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 04:02:10 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:07:56 | Badalgama (Maha Oya) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:01:57 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-02 18:01:45 | Thanthirimale (Malwathu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:01:52 | Thalgahagoda (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:13:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-11-03 03:08:58 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | -0.009 |  |
| 2026-11-03 04:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-03 03:06:13 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-11-03 03:05:20 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-02 18:00:17 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.030 |  |
| 2026-11-03 03:03:30 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.061 |  |
| 2026-11-03 04:02:16 | Glencourse (Kelani Ganga) | 11.93 | 🟢 Normal | -0.073 |  |
| 2026-11-03 03:39:48 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.085 |  |
| 2026-11-03 03:59:10 | Rathnapura (Kalu Ganga) | 3.62 | 🟢 Normal | -0.118 |  |
| 2026-11-03 04:01:28 | Thaldena (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.140 |  |
| 2026-11-03 04:02:21 | Nakkala (Kumbukkan Oya) | 1.78 | 🟢 Normal | -0.169 |  |
| 2026-11-03 04:03:04 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.258 |  |
| 2026-11-03 03:15:55 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.290 |  |
| 2026-11-03 04:00:12 | Wellawaya (Kirindi Oya) | 1.88 | 🟢 Normal | -1.014 |  |
| 2026-11-03 04:02:17 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | -1.228 |  |
| 2026-11-03 03:08:32 | Panadugama (Nilwala Ganga) | 4.16 | 🟢 Normal | -9.600 |  |
| 2026-11-03 03:07:06 | Padiyathalawa (Maduru Oya) | 2.80 | 🟢 Normal | -127.059 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)