# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_21:13:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **242,515 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 21:13:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:11:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:10:35 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:10:15 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.028 |  |
| 2026-08-24 21:09:57 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:09:32 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:07:46 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.011 |  |
| 2026-08-24 21:07:17 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:06:56 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:06:41 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:05:56 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 21:04:32 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-08-24 21:04:24 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-08-24 21:04:21 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-08-24 21:03:48 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-24 21:03:11 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:03:03 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-24 21:03:01 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:57 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:53 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:50 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:48 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-08-24 21:02:41 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:41 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-08-24 21:02:34 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:33 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:28 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.034 |  |
| 2026-08-24 21:02:24 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:22 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.164 |  |
| 2026-08-24 21:02:17 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:12 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:03 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 21:01:35 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:00:55 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | -0.010 |  |
| 2026-08-24 21:00:27 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-24 21:00:25 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-24 21:04:32 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-08-24 21:03:03 | Deraniyagala (Kelani Ganga) | 0.69 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-24 21:00:27 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-24 21:03:48 | Glencourse (Kelani Ganga) | 9.53 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-24 21:02:00 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 21:05:56 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-24 21:00:25 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:41 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:03 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:12 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:57 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-24 18:02:21 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:09:32 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:09:57 | Ellagawa (Kalu Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:17 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:50 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:06:41 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:03:01 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:24 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:03:11 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:53 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:33 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:10:35 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:06:56 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:07:17 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:01:35 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:34 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:13:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-24 21:02:48 | Magura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-08-24 18:01:27 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-24 21:00:55 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | -0.010 |  |
| 2026-08-24 21:04:21 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-08-24 21:07:46 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.011 |  |
| 2026-08-24 21:02:41 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-08-24 21:04:24 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-08-24 21:10:15 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.028 |  |
| 2026-08-24 21:02:28 | Putupaula (Kalu Ganga) | 0.38 | 🟢 Normal | -0.034 |  |
| 2026-08-24 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.119 |  |
| 2026-08-24 21:02:22 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)