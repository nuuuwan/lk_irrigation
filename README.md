# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_20:07:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,680 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 20:07:05 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-22 20:06:10 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:05:22 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:05:21 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:04:22 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:04:19 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:03:28 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.060 |  |
| 2026-08-22 20:03:15 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-22 20:03:04 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:02:48 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:02:43 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.059 |  |
| 2026-08-22 20:02:35 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:02:34 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:02:15 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 20:02:11 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.042 |  |
| 2026-08-22 20:02:06 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:01:43 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:01:21 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-22 20:01:21 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:01:19 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:00:32 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:00:31 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-22 19:46:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 19:24:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 20:01:21 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-22 20:03:15 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-22 20:07:05 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-22 20:02:15 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 18:00:58 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:00:31 | Wellawaya (Kirindi Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:01:19 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:01:21 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:04:22 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:03:04 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:02:34 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:07:20 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 19:05:22 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:04:19 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:05:22 | Glencourse (Kelani Ganga) | 9.35 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:02:48 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 19:02:08 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-22 19:06:30 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:02:35 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:05:21 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:06:10 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:02:06 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-22 18:01:56 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:00:32 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-22 19:14:23 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 19:04:30 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-22 20:01:43 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-22 19:03:59 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | -0.009 |  |
| 2026-08-22 19:04:21 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-22 18:05:09 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.010 |  |
| 2026-08-22 19:24:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.015 |  |
| 2026-08-22 19:08:15 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.018 |  |
| 2026-08-22 19:06:09 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.038 |  |
| 2026-08-22 20:02:11 | Hanwella (Kelani Ganga) | 1.17 | 🟢 Normal | -0.042 |  |
| 2026-08-22 19:07:04 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.047 |  |
| 2026-08-22 20:02:43 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.059 |  |
| 2026-08-22 20:03:28 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.060 |  |
| 2026-08-22 19:16:53 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | -13.277 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)