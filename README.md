# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--09_10:14:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **228,663 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 10:14:47 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.017 |  |
| 2026-08-09 10:12:59 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:12:54 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-09 10:12:51 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-09 10:11:21 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:10:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-09 10:09:37 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:09:20 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:09:19 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:09:01 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-09 10:08:52 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-09 10:08:32 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:07:16 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.107 |  |
| 2026-08-09 10:06:39 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:06:23 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-08-09 10:06:23 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:06:05 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:05:50 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-08-09 10:05:32 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | -0.165 |  |
| 2026-08-09 10:05:11 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:04:55 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:04:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:03:43 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:03:33 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:03:25 | Peradeniya (Mahaweli Ganga) | 3.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-09 10:03:02 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-08-09 10:02:23 | Kithulgala (Kelani Ganga) | 2.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-09 10:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-08-09 10:02:22 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:02:06 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:01:58 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-09 10:01:57 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-09 10:09:01 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-09 10:08:52 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-09 10:02:23 | Kithulgala (Kelani Ganga) | 2.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-09 10:03:25 | Peradeniya (Mahaweli Ganga) | 3.67 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-09 10:10:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.92 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-08-09 10:12:51 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-08-09 10:00:54 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 10:01:29 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-09 10:01:30 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:01:01 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:04:23 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:06:39 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:02:06 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:09:37 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:09:20 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:03:33 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:01:31 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:04:55 | Glencourse (Kelani Ganga) | 10.70 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:06:05 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:01:10 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:02:22 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:03:43 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:05:11 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:06:23 | Badalgama (Maha Oya) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:08:32 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:12:59 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:11:21 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:09:19 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:01:33 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-09 10:12:54 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-09 10:01:58 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-09 10:03:02 | Hanwella (Kelani Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-08-09 10:02:22 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-08-09 10:14:47 | Rathnapura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.017 |  |
| 2026-08-09 10:06:23 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.019 |  |
| 2026-08-09 10:05:50 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-08-09 10:01:57 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.040 |  |
| 2026-08-09 10:07:16 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.107 |  |
| 2026-08-09 10:05:32 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | -0.165 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)