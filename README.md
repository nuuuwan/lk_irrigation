# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_23:06:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,379 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 23:06:31 | Panadugama (Nilwala Ganga) | 4.41 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-21 23:06:20 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-10-21 23:05:37 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-21 23:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-21 23:05:11 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 23:04:52 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.055 |  |
| 2026-10-21 23:04:34 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-21 23:04:15 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-21 23:04:07 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.072 |  |
| 2026-10-21 23:04:05 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-10-21 23:04:02 | Nawalapitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-21 23:03:57 | Thalgahagoda (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-21 23:03:16 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 23:03:15 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-21 23:03:12 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-21 23:02:52 | Kithulgala (Kelani Ganga) | 2.46 | 🟢 Normal | -0.191 |  |
| 2026-10-21 23:02:41 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-10-21 23:02:39 | Deraniyagala (Kelani Ganga) | 3.18 | 🟢 Normal | 0.489 | 🔺 Rising |
| 2026-10-21 23:02:31 | Kuda Oya (Kirindi Oya) | 2.25 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-10-21 23:02:12 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | -0.130 |  |
| 2026-10-21 23:02:10 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.051 |  |
| 2026-10-21 23:02:08 | Siyambalanduwa (Heda Oya) | 3.05 | 🟢 Normal | -0.145 |  |
| 2026-10-21 23:01:35 | Horowpothana (Yan Oya) | 2.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 23:01:22 | Yaka Wewa (Ma Oya) | 1.70 | 🟢 Normal | -0.153 |  |
| 2026-10-21 23:00:31 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-21 23:00:31 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 23:00:11 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.095 |  |
| 2026-10-21 22:21:00 | Thawalama (Gin Ganga) | 1.87 | 🟢 Normal | -0.055 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 22:07:26 | Rathnapura (Kalu Ganga) | 4.39 | 🟢 Normal | 0.893 | 🔺 Rising |
| 2026-10-21 22:08:34 | Holombuwa (Kelani Ganga) | 1.89 | 🟢 Normal | 0.530 | 🔺 Rising |
| 2026-10-21 23:02:39 | Deraniyagala (Kelani Ganga) | 3.18 | 🟢 Normal | 0.489 | 🔺 Rising |
| 2026-10-21 23:02:31 | Kuda Oya (Kirindi Oya) | 2.25 | 🟢 Normal | 0.265 | 🔺 Rising |
| 2026-10-21 23:04:05 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-10-21 23:06:31 | Panadugama (Nilwala Ganga) | 4.41 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-21 23:04:02 | Nawalapitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-21 18:01:26 | Galgamuwa (Mee Oya) | 1.81 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-10-21 23:05:37 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-21 23:03:12 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-21 23:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-21 23:03:15 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-21 22:06:53 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-10-21 22:14:52 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-21 23:04:34 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-21 23:04:15 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-21 18:01:56 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-21 22:02:22 | Moragaswewa (Deduru Oya) | 1.35 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-21 23:01:35 | Horowpothana (Yan Oya) | 2.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 23:05:11 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 23:03:16 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 23:00:31 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 20:04:28 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 22:00:55 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 23:00:31 | Thaldena (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-10-21 22:04:06 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-21 23:03:57 | Thalgahagoda (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-21 23:06:20 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-10-21 23:02:41 | Manampitiya (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-10-21 22:01:52 | Pitabeddara (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.021 |  |
| 2026-10-21 23:02:10 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | -0.051 |  |
| 2026-10-21 23:04:52 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.055 |  |
| 2026-10-21 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.070 |  |
| 2026-10-21 23:04:07 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.072 |  |
| 2026-10-21 23:00:11 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.095 |  |
| 2026-10-21 23:02:12 | Thanamalwila (Kirindi Oya) | 2.10 | 🟢 Normal | -0.130 |  |
| 2026-10-21 23:02:08 | Siyambalanduwa (Heda Oya) | 3.05 | 🟢 Normal | -0.145 |  |
| 2026-10-21 23:01:22 | Yaka Wewa (Ma Oya) | 1.70 | 🟢 Normal | -0.153 |  |
| 2026-10-21 23:02:52 | Kithulgala (Kelani Ganga) | 2.46 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)