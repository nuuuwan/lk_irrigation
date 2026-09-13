# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--13_12:20:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **259,736 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 12:20:57 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:18:22 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:15:24 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.064 |  |
| 2026-09-13 12:14:09 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:13:01 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:10:24 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.286 |  |
| 2026-09-13 12:07:24 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.023 |  |
| 2026-09-13 12:07:13 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:06:52 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-13 12:06:46 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:06:26 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.056 |  |
| 2026-09-13 12:05:54 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:05:43 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-09-13 12:05:33 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-09-13 12:05:33 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-09-13 12:05:06 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-09-13 12:04:52 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 12:04:14 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:04:12 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-13 12:04:11 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:04:10 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-13 12:03:59 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:03:58 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.129 |  |
| 2026-09-13 12:03:24 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:03:04 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-09-13 12:02:57 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.080 |  |
| 2026-09-13 12:02:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:02:33 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:02:24 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | -0.045 |  |
| 2026-09-13 12:02:23 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:02:21 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-13 12:02:09 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.084 |  |
| 2026-09-13 12:01:52 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-09-13 12:01:49 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | -0.010 |  |
| 2026-09-13 12:01:38 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:01:38 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:01:33 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:01:14 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-13 12:00:46 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:00:29 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:59:59 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-13 12:05:43 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-09-13 12:03:04 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-09-13 12:06:52 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-13 12:02:21 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-13 12:04:10 | Ellagawa (Kalu Ganga) | 4.95 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-13 12:04:12 | Rathnapura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-13 12:01:14 | Manampitiya (Mahaweli Ganga) | -0.43 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-13 12:04:52 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-13 12:02:33 | Weraganthota (Mahaweli Ganga) | -3.64 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:03:24 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:00:46 | Nakkala (Kumbukkan Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:01:38 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:02:23 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:01:33 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:03:59 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:13:01 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:20:57 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:02:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:18:22 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:05:54 | Dunamale (Aththanagalu Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-13 11:59:59 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:04:14 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:04:11 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:00:29 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:07:13 | Kuda Oya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-09-13 12:05:33 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-09-13 12:05:33 | Thanamalwila (Kirindi Oya) | 0.09 | 🟢 Normal | -0.009 |  |
| 2026-09-13 12:05:06 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-09-13 12:01:49 | Moragaswewa (Deduru Oya) | -0.31 | 🟢 Normal | -0.010 |  |
| 2026-09-13 12:01:52 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-09-13 12:07:24 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.023 |  |
| 2026-09-13 12:02:24 | Thawalama (Gin Ganga) | 2.24 | 🟢 Normal | -0.045 |  |
| 2026-09-13 12:06:26 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.056 |  |
| 2026-09-13 12:15:24 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.064 |  |
| 2026-09-13 12:02:57 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.080 |  |
| 2026-09-13 12:02:09 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.084 |  |
| 2026-09-13 12:03:58 | Magura (Kalu Ganga) | 3.40 | 🟢 Normal | -0.129 |  |
| 2026-09-13 12:10:24 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.286 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)