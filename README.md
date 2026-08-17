# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_06:15:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,668 measurements** from **39** stations.
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
| 2026-08-17 06:15:23 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:12:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:12:44 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:11:32 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.001 |  |
| 2026-08-17 06:09:41 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:08:33 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:08:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.067 |  |
| 2026-08-17 06:08:06 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:08:01 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.023 |  |
| 2026-08-17 06:07:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.132 |  |
| 2026-08-17 06:07:30 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-17 06:07:25 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-17 06:06:49 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:06:01 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 06:05:35 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:05:11 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:05:07 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-17 06:04:48 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:04:47 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.028 |  |
| 2026-08-17 06:04:41 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | -0.022 |  |
| 2026-08-17 06:04:27 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:04:09 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-17 06:03:31 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:03:25 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-17 06:03:15 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:02:59 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:02:55 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-17 06:02:34 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:02:34 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-08-17 06:02:31 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 06:02:26 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:02:25 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.024 |  |
| 2026-08-17 06:02:22 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:02:12 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.021 |  |
| 2026-08-17 06:02:08 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:01:35 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-17 06:01:05 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.021 |  |
| 2026-08-17 06:00:46 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:00:10 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 06:01:35 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-17 06:04:09 | Hanwella (Kelani Ganga) | 1.32 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-17 06:02:31 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-17 06:05:07 | Dunamale (Aththanagalu Oya) | 0.39 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-17 06:07:25 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-08-17 06:03:25 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-17 06:06:01 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-17 06:11:32 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.001 |  |
| 2026-08-17 06:02:34 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:02:26 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 05:00:37 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:05:11 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:12:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:02:59 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:04:27 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:57 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:04:48 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:05:35 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:15:23 | Ellagawa (Kalu Ganga) | 5.03 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:02:22 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:09:41 | Moraketiya (Walawe Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:06:49 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:08:33 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:00:46 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:12:44 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:00:10 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:03:15 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:03:31 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-17 06:07:30 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-17 06:02:55 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-17 06:02:34 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-08-17 06:01:05 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.021 |  |
| 2026-08-17 06:02:12 | Panadugama (Nilwala Ganga) | 2.56 | 🟢 Normal | -0.021 |  |
| 2026-08-17 06:04:41 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | -0.022 |  |
| 2026-08-17 06:08:01 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.023 |  |
| 2026-08-17 06:02:25 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.024 |  |
| 2026-08-17 06:04:47 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.028 |  |
| 2026-08-17 06:08:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | -0.067 |  |
| 2026-08-17 06:07:59 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.132 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)