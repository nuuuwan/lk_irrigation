# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--18_15:16:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **236,900 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 15:16:41 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:10:23 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:06:59 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:06:29 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:06:18 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:06:15 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:05:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.53 | 🟢 Normal | -0.068 |  |
| 2026-08-18 15:04:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-08-18 15:04:29 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.068 |  |
| 2026-08-18 15:04:12 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.083 |  |
| 2026-08-18 15:04:11 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:04:07 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:03:46 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-18 15:03:39 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-08-18 15:03:26 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:03:23 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:03:22 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:03:12 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-08-18 15:03:09 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.030 |  |
| 2026-08-18 15:03:03 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:03:02 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:02:52 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:02:50 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:02:48 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:02:45 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:02:34 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-08-18 15:02:15 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:02:11 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:02:02 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.049 |  |
| 2026-08-18 15:01:56 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-18 15:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:01:52 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:01:42 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:01:42 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2026-08-18 15:01:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:01:33 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.107 |  |
| 2026-08-18 15:01:10 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:00:17 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:00:10 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-18 15:04:31 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-08-18 15:01:56 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-18 15:03:46 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-18 15:01:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:02:45 | Wellawaya (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:00:17 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:06:15 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:02:50 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:00:10 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:01:42 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:03:22 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:06:59 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:06:18 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:01:10 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:04:07 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:03:02 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:16:41 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:04:11 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:01:52 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:03:26 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:02:48 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-18 15:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:03:03 | Thanamalwila (Kirindi Oya) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:06:29 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:03:23 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:10:23 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:02:11 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:02:15 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:02:52 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-18 15:01:42 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | -0.011 |  |
| 2026-08-18 15:03:39 | Magura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.019 |  |
| 2026-08-18 15:02:34 | Hanwella (Kelani Ganga) | 1.52 | 🟢 Normal | -0.020 |  |
| 2026-08-18 15:03:12 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-08-18 15:03:09 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.030 |  |
| 2026-08-18 15:02:02 | Ellagawa (Kalu Ganga) | 5.95 | 🟢 Normal | -0.049 |  |
| 2026-08-18 15:04:29 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.068 |  |
| 2026-08-18 15:05:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.53 | 🟢 Normal | -0.068 |  |
| 2026-08-18 15:04:12 | Rathnapura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.083 |  |
| 2026-08-18 15:01:33 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.107 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)