# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_18:15:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,269 measurements** from **39** stations.
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
| 2026-08-31 18:15:29 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:12:44 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:09:34 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:07:55 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-08-31 18:07:10 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.036 |  |
| 2026-08-31 18:06:49 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 18:06:48 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-31 18:06:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.103 |  |
| 2026-08-31 18:05:29 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-31 18:05:19 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:04:56 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-08-31 18:04:53 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:04:40 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:04:36 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -36.000 |  |
| 2026-08-31 18:04:35 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -36.000 |  |
| 2026-08-31 18:04:34 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:04:33 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -36.000 |  |
| 2026-08-31 18:03:50 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:03:12 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:02:57 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.053 |  |
| 2026-08-31 18:02:56 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:02:53 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-08-31 18:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-08-31 18:02:41 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:02:34 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-08-31 18:02:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:02:00 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:01:49 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:01:46 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-31 18:01:34 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.011 |  |
| 2026-08-31 18:01:24 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-31 18:01:15 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:01:09 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:01:06 | Manampitiya (Mahaweli Ganga) | -0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:00:47 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:00:46 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-31 18:00:43 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-31 18:00:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -0.113 |  |
| 2026-08-31 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 18:01:24 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-31 18:05:29 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-31 18:01:46 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-31 18:06:49 | Holombuwa (Kelani Ganga) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:01:09 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:01:15 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:02:00 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:01:49 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:04:51 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:04:34 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:02:56 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:03:12 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:15:29 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | 0.000 |  |
| 2026-08-31 17:01:10 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:03:50 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:09:34 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:04:40 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:02:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:02:41 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:01:06 | Manampitiya (Mahaweli Ganga) | -0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:00:47 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:05:19 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:12:44 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 18:07:55 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-08-31 18:04:56 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-08-31 17:03:18 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-08-31 18:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-08-31 18:06:48 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-31 18:00:46 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-31 18:00:43 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-08-31 18:01:34 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.011 |  |
| 2026-08-31 18:02:34 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-08-31 18:02:53 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.031 |  |
| 2026-08-31 18:07:10 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.036 |  |
| 2026-08-31 18:02:57 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.053 |  |
| 2026-08-31 18:06:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.103 |  |
| 2026-08-31 18:00:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -0.113 |  |
| 2026-08-31 18:04:36 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)