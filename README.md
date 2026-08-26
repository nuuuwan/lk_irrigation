# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--27_03:23:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **244,476 measurements** from **39** stations.
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
| 2026-08-27 03:23:54 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.005 |  |
| 2026-08-27 03:17:05 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.018 |  |
| 2026-08-27 03:15:04 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.016 |  |
| 2026-08-27 03:13:09 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:11:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-27 03:08:40 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:06:23 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.019 |  |
| 2026-08-27 03:05:56 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-27 03:05:43 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 03:05:01 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-27 03:04:36 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:04:33 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.031 |  |
| 2026-08-27 03:04:24 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:04:04 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:04:04 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-27 03:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.176 |  |
| 2026-08-27 03:03:29 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:03:29 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:03:16 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.003 |  |
| 2026-08-27 03:03:11 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:03:06 | Ellagawa (Kalu Ganga) | 6.49 | 🟢 Normal | -0.010 |  |
| 2026-08-27 03:02:47 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-27 03:02:38 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 03:02:33 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.090 |  |
| 2026-08-27 03:02:25 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:02:23 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-27 03:02:11 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:01:42 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:01:31 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:01:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:00:39 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-27 03:04:04 | Glencourse (Kelani Ganga) | 10.43 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-27 03:02:47 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-08-27 03:11:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-27 03:05:01 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-27 03:02:23 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-27 03:05:56 | Thawalama (Gin Ganga) | 1.89 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-27 01:16:23 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-27 01:07:15 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 03:05:43 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 03:02:38 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-27 02:05:57 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:00:39 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:01:25 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:04:04 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:04:36 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-08-26 18:03:09 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-27 02:04:18 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:13:09 | Norwood (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:02:11 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:01:42 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:01:31 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:03:11 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:03:29 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:08:40 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:02:25 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-27 02:03:04 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:04:24 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-27 03:03:16 | Baddegama (Gin Ganga) | 1.82 | 🟢 Normal | -0.003 |  |
| 2026-08-27 03:23:54 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.005 |  |
| 2026-08-27 03:03:06 | Ellagawa (Kalu Ganga) | 6.49 | 🟢 Normal | -0.010 |  |
| 2026-08-26 18:01:52 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-27 03:15:04 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.016 |  |
| 2026-08-27 03:17:05 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.018 |  |
| 2026-08-27 03:06:23 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.019 |  |
| 2026-08-26 18:01:25 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.020 |  |
| 2026-08-27 03:04:33 | Kithulgala (Kelani Ganga) | 1.91 | 🟢 Normal | -0.031 |  |
| 2026-08-27 01:13:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.22 | 🟢 Normal | -0.034 |  |
| 2026-08-27 03:02:33 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.090 |  |
| 2026-08-27 03:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.176 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)