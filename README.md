# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_04:02:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **245,901 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 04:02:46 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.079 |  |
| 2026-08-29 04:02:39 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:38 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:29 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-08-29 04:02:21 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:48 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:37 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:22 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:17 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:10 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 04:01:08 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-29 03:53:56 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-29 03:49:44 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.006 |  |
| 2026-08-29 03:24:49 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:15:59 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 03:06:42 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-29 03:03:50 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-29 03:03:37 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-29 03:02:22 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-29 03:53:56 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-29 04:01:08 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-29 02:06:22 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-29 04:01:10 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 17:03:05 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 03:06:25 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 03:06:14 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-28 17:00:29 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:08:55 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:38 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:17 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:01:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:02:57 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:03:44 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:04:03 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:02:56 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:39 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:05:48 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:03:11 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:29 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:21 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:37 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:15:59 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:22 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-29 02:06:03 | Magura (Kalu Ganga) | 1.78 | 🟢 Normal | -0.005 |  |
| 2026-08-29 03:49:44 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.006 |  |
| 2026-08-29 03:06:10 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-08-29 03:04:09 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-08-28 17:01:59 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-08-29 03:06:19 | Padiyathalawa (Maduru Oya) | 0.00 | 🟢 Normal | -0.017 |  |
| 2026-08-29 03:06:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.75 | 🟢 Normal | -0.036 |  |
| 2026-08-29 04:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-08-29 03:08:15 | Glencourse (Kelani Ganga) | 10.28 | 🟢 Normal | -0.047 |  |
| 2026-08-29 04:02:46 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)