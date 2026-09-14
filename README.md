# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_14:12:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **260,712 measurements** from **39** stations.
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
| 2026-09-14 14:12:40 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:10:34 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.017 |  |
| 2026-09-14 14:08:48 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-09-14 14:08:42 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:07:19 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:07:13 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.055 |  |
| 2026-09-14 14:07:02 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:06:45 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.019 |  |
| 2026-09-14 14:06:41 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:06:23 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:04:49 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-14 14:04:11 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:04:00 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-09-14 14:03:17 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.040 |  |
| 2026-09-14 14:03:12 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-14 14:03:00 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-09-14 14:02:54 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:43 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:42 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:40 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.029 |  |
| 2026-09-14 14:02:34 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:17 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.042 |  |
| 2026-09-14 14:02:16 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-09-14 14:02:06 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:01:59 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:01:56 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-14 14:01:30 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:01:24 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-14 14:01:22 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | -0.033 |  |
| 2026-09-14 14:01:09 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:00:41 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:00:19 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.015 |  |
| 2026-09-14 14:00:06 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:44:28 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 14:04:00 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-09-14 14:04:49 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-14 13:05:02 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-14 14:06:23 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:54 | Wellawaya (Kirindi Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:00:06 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:01:30 | Moragaswewa (Deduru Oya) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:02 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:16 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:08:42 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:01:59 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:04:11 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:07:19 | Baddegama (Gin Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:07:02 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:06 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:12:40 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:01:56 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:01:09 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:43 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:06:41 | Badalgama (Maha Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:42 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:02:34 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 13:00:40 | Thanthirimale (Malwathu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:00:41 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-14 14:08:48 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-09-14 11:01:27 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-09-14 14:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-09-14 14:01:46 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-14 14:03:00 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-09-14 14:03:12 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-14 14:01:24 | Manampitiya (Mahaweli Ganga) | -0.36 | 🟢 Normal | -0.010 |  |
| 2026-09-14 14:00:19 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.015 |  |
| 2026-09-14 14:10:34 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.017 |  |
| 2026-09-14 14:06:45 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.019 |  |
| 2026-09-14 14:02:40 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.029 |  |
| 2026-09-14 14:01:22 | Glencourse (Kelani Ganga) | 9.34 | 🟢 Normal | -0.033 |  |
| 2026-09-14 14:03:17 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.040 |  |
| 2026-09-14 14:02:17 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | -0.042 |  |
| 2026-09-14 14:07:13 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.055 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)