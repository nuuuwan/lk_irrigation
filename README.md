# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_09:10:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,519 measurements** from **39** stations.
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
| 2026-08-10 09:10:24 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.048 |  |
| 2026-08-10 09:10:21 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:07:55 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.038 |  |
| 2026-08-10 09:06:30 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:06:02 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-10 09:05:59 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-10 09:05:53 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:05:45 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-08-10 09:05:28 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:05:22 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.028 |  |
| 2026-08-10 09:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.046 |  |
| 2026-08-10 09:04:47 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 09:04:35 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:04:33 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:04:20 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-10 09:04:04 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 09:03:59 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 09:03:57 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:03:54 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:03:42 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:03:35 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:03:15 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 09:03:07 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:03:01 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 09:02:37 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 09:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-10 09:02:20 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:02:14 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -0.010 |  |
| 2026-08-10 09:02:11 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-10 09:02:07 | Peradeniya (Mahaweli Ganga) | 3.71 | 🟢 Normal | -0.022 |  |
| 2026-08-10 09:02:06 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:02:06 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 09:02:05 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:01:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:01:41 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:01:38 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:01:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-10 09:00:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.054 |  |
| 2026-08-10 09:00:31 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 09:04:20 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-10 09:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-10 09:05:59 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-10 09:02:11 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-10 09:01:29 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-10 09:06:02 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-10 09:03:59 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 09:04:47 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 09:02:37 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 09:02:06 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 09:04:04 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 09:03:15 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 09:03:01 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 09:02:20 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:02:06 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:03:57 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:01:55 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:03:54 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:01:38 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:03:07 | Pitabeddara (Nilwala Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:05:53 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:01:41 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:10:21 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:04:35 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:03:35 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:03:42 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:05:28 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:06:30 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:00:31 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:04:33 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:02:05 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 09:02:14 | Ellagawa (Kalu Ganga) | 6.34 | 🟢 Normal | -0.010 |  |
| 2026-08-10 09:05:45 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-08-10 09:02:07 | Peradeniya (Mahaweli Ganga) | 3.71 | 🟢 Normal | -0.022 |  |
| 2026-08-10 09:05:22 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.028 |  |
| 2026-08-10 09:07:55 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.038 |  |
| 2026-08-10 09:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.046 |  |
| 2026-08-10 09:10:24 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.048 |  |
| 2026-08-10 09:00:42 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)