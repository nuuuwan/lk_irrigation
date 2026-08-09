# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_07:16:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,541 measurements** from **39** stations.
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
| 2026-08-09 07:16:52 | Panadugama (Nilwala Ganga) | 4.86 | 🟢 Normal | -0.061 |  |
| 2026-08-09 07:15:19 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.025 |  |
| 2026-08-09 07:11:28 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.034 |  |
| 2026-08-09 07:09:27 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:09:17 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | -0.002 |  |
| 2026-08-09 07:08:50 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-08-09 07:07:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-09 07:07:22 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.037 |  |
| 2026-08-09 07:06:19 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-09 07:05:44 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 07:05:43 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-09 07:05:35 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.029 |  |
| 2026-08-09 07:05:21 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.020 |  |
| 2026-08-09 07:05:03 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-09 07:04:59 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:04:51 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-08-09 07:04:50 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:04:36 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:04:25 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-09 07:03:29 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:03:16 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:02:57 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 07:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-08-09 07:02:16 | Kithulgala (Kelani Ganga) | 2.28 | 🟢 Normal | -0.073 |  |
| 2026-08-09 07:02:15 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:02:02 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:01:52 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:01:50 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:01:29 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-09 07:01:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:01:13 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.043 |  |
| 2026-08-09 07:00:53 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:00:39 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:00:26 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.138 |  |
| 2026-08-09 07:00:19 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:00:16 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.044 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 07:03:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.90 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-09 07:07:51 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-09 07:05:03 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-09 07:01:29 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-09 07:05:43 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-09 07:02:57 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-09 06:11:58 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-09 07:05:44 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 07:02:15 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:02:02 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:01:52 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:01:50 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:04:50 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:00:39 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 18:03:38 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:03:29 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:09:27 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:01:13 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:00:19 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:04:25 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:04:59 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:00:53 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:04:36 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:03:16 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-09 07:09:17 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | -0.002 |  |
| 2026-08-09 07:08:50 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.009 |  |
| 2026-08-09 07:06:19 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-08-09 07:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-08-09 07:05:21 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | -0.020 |  |
| 2026-08-09 07:15:19 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.025 |  |
| 2026-08-09 07:05:35 | Hanwella (Kelani Ganga) | 2.26 | 🟢 Normal | -0.029 |  |
| 2026-08-09 07:04:51 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.029 |  |
| 2026-08-09 07:11:28 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | -0.034 |  |
| 2026-08-09 07:07:22 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.037 |  |
| 2026-08-09 07:01:13 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.043 |  |
| 2026-08-09 07:00:16 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.044 |  |
| 2026-08-09 07:16:52 | Panadugama (Nilwala Ganga) | 4.86 | 🟢 Normal | -0.061 |  |
| 2026-08-09 07:02:16 | Kithulgala (Kelani Ganga) | 2.28 | 🟢 Normal | -0.073 |  |
| 2026-08-09 07:00:26 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)