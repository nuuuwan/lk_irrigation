# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_15:15:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,593 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 15:15:07 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:12:44 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:07:27 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.009 |  |
| 2026-08-21 15:07:18 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-21 15:07:16 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:06:55 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-21 15:06:49 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-08-21 15:06:24 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:06:05 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:05:37 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:05:18 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:05:11 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:05:07 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:04:55 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.063 |  |
| 2026-08-21 15:04:47 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:04:36 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.049 |  |
| 2026-08-21 15:04:32 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-08-21 15:04:32 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:04:25 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.039 |  |
| 2026-08-21 15:04:15 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-21 15:04:03 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:03:55 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.060 |  |
| 2026-08-21 15:03:36 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.031 |  |
| 2026-08-21 15:03:34 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:03:27 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-21 15:03:18 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:03:15 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:03:09 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 15:03:08 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-21 15:02:52 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.010 |  |
| 2026-08-21 15:02:19 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 15:01:55 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:01:41 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:01:28 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:01:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-08-21 15:01:07 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.031 |  |
| 2026-08-21 15:00:54 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-21 15:00:33 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 15:01:28 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-08-21 15:07:18 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-08-21 15:03:08 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-21 15:00:54 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-21 15:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-21 15:06:55 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-21 15:03:09 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 15:04:15 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-21 15:06:05 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:01:41 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:02:19 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:01:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:05:07 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:03:18 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:02:52 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:06:24 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:03:15 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:04:03 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:00:33 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:04:32 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:01:55 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:12:44 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:05:37 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:05:18 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:01:28 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:07:16 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:05:11 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:15:07 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-21 15:07:27 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.009 |  |
| 2026-08-21 15:06:49 | Putupaula (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-08-21 15:04:32 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-08-21 15:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.010 |  |
| 2026-08-21 15:03:27 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-21 15:01:07 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | -0.031 |  |
| 2026-08-21 15:03:36 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | -0.031 |  |
| 2026-08-21 15:04:25 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.039 |  |
| 2026-08-21 15:04:36 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.049 |  |
| 2026-08-21 15:03:55 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.060 |  |
| 2026-08-21 15:04:55 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)