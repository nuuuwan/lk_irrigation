# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_21:18:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,821 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 21:18:18 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-21 21:13:48 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-21 21:09:25 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:08:15 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-21 21:06:19 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-21 21:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.010 |  |
| 2026-08-21 21:05:49 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 21:03:52 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-21 21:05:14 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-08-21 21:04:51 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-21 21:08:15 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-21 21:13:48 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-21 21:02:54 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 21:06:19 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-21 21:18:18 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-21 18:01:38 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:00:15 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:00:54 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:00:52 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:02:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:03:21 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:02:53 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:04:24 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:01:44 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:02:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:01:33 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:02:20 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:02:22 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:04:19 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:02:22 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:02:59 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:09:25 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-21 18:02:10 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:05:49 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:04:40 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:03:18 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 21:05:06 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.009 |  |
| 2026-08-21 21:05:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | -0.010 |  |
| 2026-08-21 21:02:00 | Magura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-08-21 21:04:03 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | -0.012 |  |
| 2026-08-21 21:00:49 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.012 |  |
| 2026-08-21 21:02:18 | Hanwella (Kelani Ganga) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-08-21 21:03:11 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-08-21 21:02:42 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.031 |  |
| 2026-08-21 21:04:03 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)