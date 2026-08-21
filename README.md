# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--21_06:38:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **239,238 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 06:38:57 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | -0.006 |  |
| 2026-08-21 06:09:28 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.907 |  |
| 2026-08-21 06:07:54 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.011 |  |
| 2026-08-21 06:07:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:07:28 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:07:18 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.045 |  |
| 2026-08-21 06:06:49 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-08-21 06:06:14 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.061 |  |
| 2026-08-21 06:06:11 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:05:55 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:05:25 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-21 06:05:03 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:04:58 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-21 06:04:42 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-21 06:04:33 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:04:26 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-21 06:04:13 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-21 06:03:33 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:03:10 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 06:02:49 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:02:48 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 06:02:46 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:02:31 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:02:14 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 06:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-21 06:01:31 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-21 06:01:30 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:01:17 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:01:13 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.475 |  |
| 2026-08-21 06:00:55 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-21 06:00:39 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-21 06:00:35 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:00:35 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:00:23 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-21 06:04:13 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-21 06:01:31 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-21 06:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-21 06:05:25 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-21 06:04:26 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-08-21 06:00:39 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-21 06:00:55 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-21 05:10:02 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-21 06:04:42 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-21 06:02:14 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 06:03:10 | Dunamale (Aththanagalu Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 06:02:48 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-21 05:00:07 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:01:30 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:00:35 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:01:13 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:04:33 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:00:35 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:05:55 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:07:28 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:02:46 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:02:49 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:01:17 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:07:51 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:05:03 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:06:11 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:03:33 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:00:23 | Rathnapura (Kalu Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-08-20 18:02:19 | Thanthirimale (Malwathu Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:02:31 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-21 06:38:57 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | -0.006 |  |
| 2026-08-21 05:05:59 | Ellagawa (Kalu Ganga) | 6.14 | 🟢 Normal | -0.009 |  |
| 2026-08-21 06:04:58 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-21 06:07:54 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | -0.011 |  |
| 2026-08-21 06:06:49 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.021 |  |
| 2026-08-21 06:07:18 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.045 |  |
| 2026-08-21 06:06:14 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.061 |  |
| 2026-08-21 06:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.475 |  |
| 2026-08-21 06:09:28 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.907 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)