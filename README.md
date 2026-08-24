# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_20:10:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,477 measurements** from **39** stations.
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
| 2026-08-24 20:10:56 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.012 |  |
| 2026-08-24 20:09:37 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:09:18 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.085 |  |
| 2026-08-24 20:09:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-24 20:07:21 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:07:18 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-08-24 20:05:47 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-24 20:05:30 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:05:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-24 20:04:57 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:04:52 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.026 |  |
| 2026-08-24 20:04:38 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:04:28 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-24 20:04:21 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-08-24 20:03:53 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:03:42 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.059 |  |
| 2026-08-24 20:03:30 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:03:19 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:03:09 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-24 20:03:08 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:03:06 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:03:04 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:02:37 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:02:22 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-24 20:02:18 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 20:02:10 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-08-24 20:02:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:01:47 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:01:44 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:01:24 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:01:09 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:00:38 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:00:21 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 20:04:21 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-08-24 20:03:09 | Glencourse (Kelani Ganga) | 9.51 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-24 20:09:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-24 20:02:22 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-24 20:05:47 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-24 20:02:18 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 20:04:28 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-24 20:03:53 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:00:38 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:05:30 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:01:44 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:02:44 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:03:06 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 18:02:21 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:00:21 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:03:19 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:07:21 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:04:38 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:03:04 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:02:37 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:03:08 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:03:30 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:02:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:04:57 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:01:09 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:09:37 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-24 19:03:44 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:01:24 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-24 20:01:47 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 18:01:27 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-24 20:05:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-08-24 20:10:56 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.012 |  |
| 2026-08-24 20:07:18 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.019 |  |
| 2026-08-24 20:02:10 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-08-24 20:04:52 | Thawalama (Gin Ganga) | 1.38 | 🟢 Normal | -0.026 |  |
| 2026-08-24 20:03:42 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.059 |  |
| 2026-08-24 20:09:18 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.085 |  |
| 2026-08-24 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)