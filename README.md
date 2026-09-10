# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--10_07:10:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **256,844 measurements** from **39** stations.
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
| 2026-09-10 07:10:50 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:08:36 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:07:52 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-10 07:07:33 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.124 |  |
| 2026-09-10 07:06:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.038 |  |
| 2026-09-10 07:06:27 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.036 |  |
| 2026-09-10 07:06:25 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -1.800 |  |
| 2026-09-10 07:06:23 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.115 |  |
| 2026-09-10 07:05:54 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:05:02 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-10 07:05:01 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-10 07:04:45 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | -1.800 |  |
| 2026-09-10 07:04:04 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.057 |  |
| 2026-09-10 07:03:53 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-09-10 07:03:22 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.021 |  |
| 2026-09-10 07:03:05 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.033 |  |
| 2026-09-10 07:03:02 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 07:03:00 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:02:56 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 07:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-10 07:02:45 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-09-10 07:02:43 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-10 07:02:39 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:02:35 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:02:27 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:02:10 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-10 07:01:57 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.049 |  |
| 2026-09-10 07:01:56 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.030 |  |
| 2026-09-10 07:01:44 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:01:20 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 07:01:09 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:01:04 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.095 |  |
| 2026-09-10 07:00:43 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:38:27 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:30:29 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-10 07:02:10 | Deraniyagala (Kelani Ganga) | 0.62 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-10 07:07:52 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-09-10 06:03:16 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-09 18:02:14 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-10 07:05:02 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-10 07:01:20 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 07:02:56 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 07:03:02 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-10 07:02:35 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:05:54 | Moragaswewa (Deduru Oya) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:01:44 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:10:50 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:02:30 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:03:19 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:02:39 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:08:36 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:04:31 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:00:43 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:01:09 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:02:27 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:03:00 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-10 06:04:29 | Kuda Oya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-10 07:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-10 07:02:43 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-09-10 07:05:01 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-10 07:03:53 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-09-10 07:02:45 | Hanwella (Kelani Ganga) | 0.88 | 🟢 Normal | -0.021 |  |
| 2026-09-10 07:03:22 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.021 |  |
| 2026-09-10 07:01:56 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | -0.030 |  |
| 2026-09-10 07:03:05 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.033 |  |
| 2026-09-10 07:06:27 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.036 |  |
| 2026-09-10 07:06:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.038 |  |
| 2026-09-10 06:03:27 | Glencourse (Kelani Ganga) | 9.17 | 🟢 Normal | -0.040 |  |
| 2026-09-10 07:01:57 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.049 |  |
| 2026-09-10 07:04:04 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.057 |  |
| 2026-09-10 07:01:04 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.095 |  |
| 2026-09-10 07:06:23 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.115 |  |
| 2026-09-10 07:07:33 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.124 |  |
| 2026-09-10 07:06:25 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -1.800 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)