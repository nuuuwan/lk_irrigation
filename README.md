# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--23_04:05:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,962 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 04:05:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | -0.019 |  |
| 2026-08-23 04:05:53 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-08-23 04:05:29 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:04:44 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-08-23 04:04:18 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:04:02 | Peradeniya (Mahaweli Ganga) | 2.91 | 🟢 Normal | -0.045 |  |
| 2026-08-23 04:03:52 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:03:43 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:03:36 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-08-23 04:03:31 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:02:57 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:02:50 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.034 |  |
| 2026-08-23 04:02:49 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:02:11 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.012 |  |
| 2026-08-23 04:01:54 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-08-23 04:01:46 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-23 04:01:39 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-08-23 04:01:34 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:01:25 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:01:11 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.022 |  |
| 2026-08-23 04:01:05 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:00:43 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-23 03:40:15 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.007 |  |
| 2026-08-23 03:32:29 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-23 03:32:22 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-23 03:22:21 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-23 03:02:29 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-08-23 04:01:54 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-08-23 04:04:44 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-08-23 04:01:46 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-23 02:01:54 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-23 04:01:25 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:00:58 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-23 03:00:23 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:01:05 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:00:43 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-23 01:03:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:03:52 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:02:07 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-23 03:03:25 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:04:18 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:03:31 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:05:29 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-23 03:10:45 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:02:11 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:03:43 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-23 03:32:22 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-23 02:46:07 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:02:49 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:56 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-23 03:19:23 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:02:57 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-23 04:01:34 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-23 03:40:15 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.007 |  |
| 2026-08-23 04:05:53 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-08-23 04:03:36 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-08-23 04:01:39 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-08-23 04:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.012 |  |
| 2026-08-23 03:18:38 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.017 |  |
| 2026-08-23 03:05:25 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-08-23 04:05:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | -0.019 |  |
| 2026-08-23 04:01:11 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.022 |  |
| 2026-08-23 03:22:21 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.025 |  |
| 2026-08-23 04:02:50 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.034 |  |
| 2026-08-23 04:04:02 | Peradeniya (Mahaweli Ganga) | 2.91 | 🟢 Normal | -0.045 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)