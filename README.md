# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_06:12:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,362 measurements** from **39** stations.
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
| 2026-11-04 06:12:30 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:09:59 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-11-04 06:09:56 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-04 06:07:39 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-11-04 06:06:41 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:05:32 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-04 06:05:16 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-11-04 06:04:52 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:04:45 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.060 |  |
| 2026-11-04 06:04:31 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-11-04 06:04:19 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:04:03 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:03:41 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.049 |  |
| 2026-11-04 06:03:41 | Moragaswewa (Deduru Oya) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:03:36 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.038 |  |
| 2026-11-04 06:03:26 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | 0.001 |  |
| 2026-11-04 06:03:17 | Urawa (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.098 |  |
| 2026-11-04 06:03:07 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:02:42 | Giriulla (Maha Oya) | 3.45 | 🟢 Normal | -0.102 |  |
| 2026-11-04 06:02:33 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.068 |  |
| 2026-11-04 06:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.022 |  |
| 2026-11-04 06:02:25 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | -0.131 |  |
| 2026-11-04 06:02:20 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-04 06:02:20 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:02:17 | Badalgama (Maha Oya) | 4.27 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-04 06:02:01 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:01:57 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:01:53 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.041 |  |
| 2026-11-04 06:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 1.063 | 🔺 Rising |
| 2026-11-04 06:01:39 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-04 06:01:33 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-04 06:01:31 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | -0.110 |  |
| 2026-11-04 06:01:29 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-11-04 06:01:24 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.231 |  |
| 2026-11-04 06:01:18 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.119 |  |
| 2026-11-04 06:01:10 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.031 |  |
| 2026-11-04 06:00:22 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-11-04 06:00:16 | Rathnapura (Kalu Ganga) | 3.64 | 🟢 Normal | -0.073 |  |
| 2026-11-04 05:45:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.47 | 🟢 Normal | 1.063 | 🔺 Rising |
| 2026-11-04 05:35:32 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | 0.046 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 06:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.76 | 🟢 Normal | 1.063 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-04 06:01:39 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-04 06:01:33 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-04 06:09:56 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-04 06:02:17 | Badalgama (Maha Oya) | 4.27 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-04 06:02:20 | Ellagawa (Kalu Ganga) | 6.70 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-04 06:05:32 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-04 06:03:26 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | 0.001 |  |
| 2026-11-04 06:06:41 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:03:41 | Moragaswewa (Deduru Oya) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:03:07 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:12:30 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:04:52 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:02:20 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:04:03 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:01:57 | Thalgahagoda (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 06:07:39 | Padiyathalawa (Maduru Oya) | 0.64 | 🟢 Normal | -0.009 |  |
| 2026-11-04 06:04:31 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-11-04 06:00:22 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-11-04 06:01:29 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-11-04 06:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.022 |  |
| 2026-11-04 06:01:10 | Horowpothana (Yan Oya) | 3.07 | 🟢 Normal | -0.031 |  |
| 2026-11-04 06:09:59 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-11-04 06:03:36 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.038 |  |
| 2026-11-04 06:01:53 | Pitabeddara (Nilwala Ganga) | 2.08 | 🟢 Normal | -0.041 |  |
| 2026-11-04 06:03:41 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.049 |  |
| 2026-11-04 06:05:16 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.050 |  |
| 2026-11-04 06:04:45 | Norwood (Kelani Ganga) | 1.26 | 🟢 Normal | -0.060 |  |
| 2026-11-04 06:02:33 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.068 |  |
| 2026-11-04 06:00:16 | Rathnapura (Kalu Ganga) | 3.64 | 🟢 Normal | -0.073 |  |
| 2026-11-04 06:03:17 | Urawa (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.098 |  |
| 2026-11-04 06:02:42 | Giriulla (Maha Oya) | 3.45 | 🟢 Normal | -0.102 |  |
| 2026-11-04 06:01:31 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | -0.110 |  |
| 2026-11-04 06:01:18 | Kuda Oya (Kirindi Oya) | 1.76 | 🟢 Normal | -0.119 |  |
| 2026-11-04 06:02:25 | Glencourse (Kelani Ganga) | 11.07 | 🟢 Normal | -0.131 |  |
| 2026-11-04 05:00:17 | Thawalama (Gin Ganga) | 3.24 | 🟢 Normal | -0.210 |  |
| 2026-11-04 06:01:24 | Magura (Kalu Ganga) | 3.39 | 🟢 Normal | -0.231 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)