# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--13_20:10:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,637 measurements** from **39** stations.
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
| 2026-08-13 20:10:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:09:42 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:09:19 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:08:29 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.009 |  |
| 2026-08-13 20:07:53 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:06:57 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:06:24 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-13 20:05:39 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | -0.029 |  |
| 2026-08-13 20:05:33 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:05:31 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:04:34 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.046 |  |
| 2026-08-13 20:04:23 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:04:18 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:04:14 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-08-13 20:03:20 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:03:13 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:03:07 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:02:57 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.030 |  |
| 2026-08-13 20:02:50 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-08-13 20:02:41 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 20:02:31 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.033 |  |
| 2026-08-13 20:02:30 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:02:25 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.050 |  |
| 2026-08-13 20:02:20 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:02:19 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-13 20:02:12 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-08-13 20:02:07 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.013 |  |
| 2026-08-13 20:01:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:01:37 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.091 |  |
| 2026-08-13 20:01:31 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:01:31 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-13 20:01:07 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-08-13 20:00:46 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:00:20 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-08-13 19:56:42 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-13 20:02:19 | Rathnapura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-08-13 20:01:31 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-13 20:06:24 | Glencourse (Kelani Ganga) | 9.95 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-13 20:02:41 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-13 20:02:30 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:01:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:03:07 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:02:20 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:13:34 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:04:23 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:04:14 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:07:53 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:03:13 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:04:18 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:01:31 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:04:34 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:05:33 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:09:42 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:06:57 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:09:19 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:06:46 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:05:31 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:10:29 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:03:20 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:00:46 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-13 20:08:29 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.009 |  |
| 2026-08-13 20:01:07 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-08-13 20:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-08-13 20:00:20 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-08-13 20:02:07 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.013 |  |
| 2026-08-13 20:02:12 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-08-13 20:02:50 | Hanwella (Kelani Ganga) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-08-13 20:05:39 | Ellagawa (Kalu Ganga) | 4.83 | 🟢 Normal | -0.029 |  |
| 2026-08-13 20:02:57 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.030 |  |
| 2026-08-13 20:02:31 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.033 |  |
| 2026-08-13 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.040 |  |
| 2026-08-13 20:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.046 |  |
| 2026-08-13 20:02:25 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.050 |  |
| 2026-08-13 20:01:37 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)