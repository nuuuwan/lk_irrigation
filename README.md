# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_22:11:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,852 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 22:11:24 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-21 22:08:23 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-21 22:08:19 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-21 22:07:16 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-21 22:06:46 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:06:39 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:06:38 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-21 22:05:52 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:05:32 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:05:27 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-08-21 22:04:48 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-21 22:04:39 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:04:03 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-21 22:03:55 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:03:44 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:03:42 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:02:49 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-08-21 22:02:43 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.040 |  |
| 2026-08-21 22:02:37 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-08-21 22:02:18 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:02:12 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-08-21 22:02:10 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:02:02 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:01:53 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-08-21 22:01:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-08-21 22:00:57 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:00:45 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:00:29 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:00:10 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 22:05:27 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-08-21 22:04:03 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-21 22:04:48 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-21 22:08:19 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-21 22:08:23 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-21 22:11:24 | Panadugama (Nilwala Ganga) | 2.60 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-21 22:07:16 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-21 22:06:38 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-21 18:01:38 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:00:10 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:02:10 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:00:57 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:01:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:03:55 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:00:45 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:04:24 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:06:39 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:03:44 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:00:29 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:03:42 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:02:20 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:02:22 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:06:46 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:02:22 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:05:52 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:04:39 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:10 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:05:32 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:02:18 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:02:02 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 22:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:05:06 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.009 |  |
| 2026-08-21 22:02:49 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-08-21 22:02:12 | Hanwella (Kelani Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-08-21 22:01:53 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-08-21 21:04:03 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.012 |  |
| 2026-08-21 22:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-08-21 22:02:37 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-08-21 22:02:43 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)