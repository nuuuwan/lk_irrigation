# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--03_15:19:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **250,821 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 15:19:08 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:13:10 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:09:53 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:09:38 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-03 15:08:57 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-09-03 15:08:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:07:57 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.018 |  |
| 2026-09-03 15:07:02 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:06:26 | Thanamalwila (Kirindi Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:05:44 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:05:39 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:05:31 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:05:27 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-03 15:05:23 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:04:52 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-09-03 15:04:43 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-09-03 15:04:22 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.035 |  |
| 2026-09-03 15:04:16 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:04:05 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-03 15:04:00 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -2.372 |  |
| 2026-09-03 15:03:40 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:03:30 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.021 |  |
| 2026-09-03 15:03:25 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:03:13 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-09-03 15:03:12 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-03 15:03:07 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:02:45 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:02:44 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-03 15:02:36 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:02:26 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-09-03 15:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.122 |  |
| 2026-09-03 15:02:00 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:01:56 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-09-03 15:01:51 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:01:42 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:01:31 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:01:30 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 15:01:08 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-03 15:00:37 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:00:23 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 14:59:59 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-03 15:03:13 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-09-03 15:02:44 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-03 15:08:57 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-09-03 15:09:38 | Magura (Kalu Ganga) | 1.38 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-03 15:01:08 | Peradeniya (Mahaweli Ganga) | 2.28 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-03 15:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-03 15:05:27 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-03 15:05:44 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:19:08 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:08:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:02:36 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:00:37 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:04:43 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:02:00 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:09:53 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:03:07 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:04:16 | Ellagawa (Kalu Ganga) | 4.51 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:07:02 | Panadugama (Nilwala Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:02:45 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:01:30 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:01:42 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:05:23 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:13:10 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:05:31 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:05:39 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:00:23 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:01:31 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:06:26 | Thanamalwila (Kirindi Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-03 15:04:05 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-03 15:03:12 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-03 15:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-09-03 15:07:57 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.018 |  |
| 2026-09-03 15:04:52 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.021 |  |
| 2026-09-03 15:02:26 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-09-03 15:03:30 | Glencourse (Kelani Ganga) | 9.40 | 🟢 Normal | -0.021 |  |
| 2026-09-03 15:01:56 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-09-03 15:04:22 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.035 |  |
| 2026-09-03 15:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.122 |  |
| 2026-09-03 15:04:00 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | -2.372 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)