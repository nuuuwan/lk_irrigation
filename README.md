# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_04:38:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,519 measurements** from **39** stations.
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
| 2026-08-08 04:38:21 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.026 |  |
| 2026-08-08 04:30:23 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.040 |  |
| 2026-08-08 04:28:07 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.007 |  |
| 2026-08-08 04:22:53 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-08 04:19:25 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.035 |  |
| 2026-08-08 04:15:28 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:08:12 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.009 |  |
| 2026-08-08 04:07:23 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 04:07:06 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-08 04:07:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:05:40 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:05:39 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 04:04:53 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:04:33 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-08 04:04:29 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:03:57 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.031 |  |
| 2026-08-08 04:03:45 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-08 04:03:35 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 04:03:16 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:03:12 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:02:57 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | -0.022 |  |
| 2026-08-08 04:02:53 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.039 |  |
| 2026-08-08 04:02:37 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.022 |  |
| 2026-08-08 04:02:07 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:02:06 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.040 |  |
| 2026-08-08 04:01:56 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:01:55 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.040 |  |
| 2026-08-08 04:01:12 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 04:01:10 | Padiyathalawa (Maduru Oya) | 0.01 | 🟢 Normal | -0.047 |  |
| 2026-08-08 04:01:03 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:01:02 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 04:05:39 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 04:07:06 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-08 04:03:35 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 04:01:12 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 04:07:23 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 04:22:53 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-07 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:01:02 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:04:29 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:07:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:03:12 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:01:55 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-07 18:10:22 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:05:40 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:02:07 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:01:03 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:15:28 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:04:53 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:01:56 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-07 18:01:27 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:03:16 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 03:01:22 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 03:03:37 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:28:07 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.007 |  |
| 2026-08-08 04:08:12 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.009 |  |
| 2026-08-08 03:11:06 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-08 04:03:45 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-08 04:04:33 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-08-08 04:02:57 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | -0.022 |  |
| 2026-08-08 04:02:37 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.022 |  |
| 2026-08-08 04:38:21 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.026 |  |
| 2026-08-08 04:03:57 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.031 |  |
| 2026-08-08 04:19:25 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.035 |  |
| 2026-08-08 04:02:53 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | -0.039 |  |
| 2026-08-08 04:30:23 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.040 |  |
| 2026-08-08 04:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.040 |  |
| 2026-08-08 04:02:06 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.040 |  |
| 2026-08-08 04:01:10 | Padiyathalawa (Maduru Oya) | 0.01 | 🟢 Normal | -0.047 |  |
| 2026-08-08 03:12:16 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)