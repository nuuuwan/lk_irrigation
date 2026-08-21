# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_16:12:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,633 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 16:12:57 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:11:27 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.027 |  |
| 2026-08-21 16:10:18 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:10:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:08:41 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-08-21 16:08:17 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:08:06 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.009 |  |
| 2026-08-21 16:07:45 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:07:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:07:36 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-21 16:07:22 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:07:12 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:06:18 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:06:02 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-21 16:05:50 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:05:30 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 16:04:33 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.050 |  |
| 2026-08-21 16:04:17 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-08-21 16:04:13 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:03:49 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-21 16:03:06 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:02:59 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 16:02:56 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-21 16:02:49 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 16:02:39 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:02:26 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 16:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.09 | 🟢 Normal | -0.010 |  |
| 2026-08-21 16:02:17 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:02:16 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-21 16:02:09 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 16:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-21 16:01:47 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:01:40 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-08-21 16:01:39 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | -0.010 |  |
| 2026-08-21 16:01:29 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:01:24 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-08-21 16:01:22 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:01:14 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:01:12 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:01:06 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 16:08:41 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-08-21 16:02:56 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-08-21 16:07:36 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-21 16:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-21 16:02:26 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 16:02:16 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-21 16:05:30 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 16:02:09 | Hanwella (Kelani Ganga) | 1.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 16:02:49 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 16:02:59 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 16:06:02 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-21 16:06:18 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:04:13 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:02:39 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:12:57 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:07:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:01:14 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:01:29 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:07:22 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:01:47 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:01:06 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:03:06 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:05:50 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:10:16 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:07:45 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:01:12 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:07:12 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:08:17 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:10:18 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:01:22 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 16:08:06 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.009 |  |
| 2026-08-21 16:01:39 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | -0.010 |  |
| 2026-08-21 16:04:17 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-08-21 16:01:40 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-08-21 16:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.09 | 🟢 Normal | -0.010 |  |
| 2026-08-21 16:03:49 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-08-21 16:01:24 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-08-21 16:11:27 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.027 |  |
| 2026-08-21 16:04:33 | Glencourse (Kelani Ganga) | 9.80 | 🟢 Normal | -0.050 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)