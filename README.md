# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_19:26:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,075 measurements** from **39** stations.
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
| 2026-11-21 19:26:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | -0.036 |  |
| 2026-11-21 19:25:35 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.016 |  |
| 2026-11-21 19:15:28 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-21 19:15:08 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.052 |  |
| 2026-11-21 19:14:09 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:11:08 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.060 |  |
| 2026-11-21 19:09:03 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.129 |  |
| 2026-11-21 19:08:56 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-21 19:07:49 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.028 |  |
| 2026-11-21 19:06:56 | Badalgama (Maha Oya) | 4.22 | 🟢 Normal | -0.155 |  |
| 2026-11-21 19:06:47 | Moraketiya (Walawe Ganga) | 2.97 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-21 19:06:26 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.037 |  |
| 2026-11-21 19:06:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-21 19:05:31 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.022 |  |
| 2026-11-21 19:05:17 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.040 |  |
| 2026-11-21 19:04:33 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.059 |  |
| 2026-11-21 19:04:19 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-21 19:03:58 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-21 19:03:39 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.029 |  |
| 2026-11-21 19:03:35 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:03:33 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:03:23 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-21 19:03:18 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-11-21 19:02:26 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.347 |  |
| 2026-11-21 19:02:22 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.161 |  |
| 2026-11-21 19:02:02 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:01:56 | Kuda Oya (Kirindi Oya) | 2.25 | 🟢 Normal | -0.030 |  |
| 2026-11-21 19:01:49 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:01:39 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:01:31 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.022 |  |
| 2026-11-21 19:01:15 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-21 19:00:45 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-21 19:00:20 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-11-21 19:00:12 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 19:04:19 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-21 19:03:58 | Thaldena (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-21 19:15:28 | Urawa (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-21 19:08:56 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-21 19:06:04 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-21 19:03:23 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-21 19:00:12 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-21 19:06:47 | Moraketiya (Walawe Ganga) | 2.97 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-21 19:00:45 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-21 18:00:46 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:02:02 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:01:39 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:19 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:01:15 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:03:35 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:01:49 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:02:22 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:14:09 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-21 19:00:20 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-11-21 19:01:06 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-21 19:03:18 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-11-21 19:25:35 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.016 |  |
| 2026-11-21 19:05:31 | Baddegama (Gin Ganga) | 1.84 | 🟢 Normal | -0.022 |  |
| 2026-11-21 19:01:31 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.022 |  |
| 2026-11-21 19:07:49 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.028 |  |
| 2026-11-21 19:03:39 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.029 |  |
| 2026-11-21 19:01:56 | Kuda Oya (Kirindi Oya) | 2.25 | 🟢 Normal | -0.030 |  |
| 2026-11-21 19:26:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.51 | 🟢 Normal | -0.036 |  |
| 2026-11-21 19:06:26 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.037 |  |
| 2026-11-21 19:05:17 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.040 |  |
| 2026-11-21 19:15:08 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.052 |  |
| 2026-11-21 19:04:33 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | -0.059 |  |
| 2026-11-21 19:11:08 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.060 |  |
| 2026-11-21 18:02:21 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | -0.079 |  |
| 2026-11-21 19:09:03 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | -0.129 |  |
| 2026-11-21 19:06:56 | Badalgama (Maha Oya) | 4.22 | 🟢 Normal | -0.155 |  |
| 2026-11-21 19:02:22 | Glencourse (Kelani Ganga) | 9.62 | 🟢 Normal | -0.161 |  |
| 2026-11-21 19:02:26 | Giriulla (Maha Oya) | 2.55 | 🟢 Normal | -0.347 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)