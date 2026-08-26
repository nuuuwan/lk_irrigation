# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_17:13:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **244,139 measurements** from **39** stations.
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
| 2026-08-26 17:13:38 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.125 |  |
| 2026-08-26 17:12:06 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:10:56 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.066 |  |
| 2026-08-26 17:10:45 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-08-26 17:09:44 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-08-26 17:09:00 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:07:58 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-08-26 17:06:01 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.115 |  |
| 2026-08-26 17:05:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:05:06 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:05:02 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.109 |  |
| 2026-08-26 17:04:55 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.019 |  |
| 2026-08-26 17:04:49 | Rathnapura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.098 |  |
| 2026-08-26 17:04:39 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:04:33 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 17:04:32 | Ellagawa (Kalu Ganga) | 6.73 | 🟢 Normal | -0.030 |  |
| 2026-08-26 17:04:22 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | -0.021 |  |
| 2026-08-26 17:04:06 | Thanthirimale (Malwathu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:03:51 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:03:49 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-26 17:03:36 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-26 17:03:19 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:03:17 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-26 17:02:55 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-08-26 17:02:51 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2026-08-26 17:02:40 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-26 17:02:36 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:02:24 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:02:12 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:02:10 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.021 |  |
| 2026-08-26 17:02:07 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:02:05 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:01:24 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 17:00:55 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.080 |  |
| 2026-08-26 17:00:32 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:00:15 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:00:12 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 17:03:17 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-08-26 17:03:49 | Putupaula (Kalu Ganga) | 1.29 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-26 17:02:40 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-26 17:04:33 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 17:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 17:03:19 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:00:12 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:02:36 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:02:07 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:03:51 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:04:39 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:02:24 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:12:06 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:00:32 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:02:12 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:05:06 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:00:15 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:04:06 | Thanthirimale (Malwathu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:01:24 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:09:00 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:05:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.41 | 🟢 Normal | 0.000 |  |
| 2026-08-26 17:09:44 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-08-26 17:07:58 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | -0.009 |  |
| 2026-08-26 17:10:45 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-08-26 17:03:36 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-26 17:02:55 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-08-26 17:04:55 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.019 |  |
| 2026-08-26 17:04:22 | Panadugama (Nilwala Ganga) | 3.22 | 🟢 Normal | -0.021 |  |
| 2026-08-26 17:02:10 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.021 |  |
| 2026-08-26 17:04:32 | Ellagawa (Kalu Ganga) | 6.73 | 🟢 Normal | -0.030 |  |
| 2026-08-26 16:05:46 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.040 |  |
| 2026-08-26 17:02:51 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | -0.040 |  |
| 2026-08-26 17:10:56 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.066 |  |
| 2026-08-26 17:00:55 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.080 |  |
| 2026-08-26 17:04:49 | Rathnapura (Kalu Ganga) | 2.89 | 🟢 Normal | -0.098 |  |
| 2026-08-26 17:05:02 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.109 |  |
| 2026-08-26 17:06:01 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.115 |  |
| 2026-08-26 17:13:38 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)