# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_04:25:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,719 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 04:25:12 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.720 |  |
| 2026-08-31 04:24:22 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.720 |  |
| 2026-08-31 04:22:25 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:20:12 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-31 04:10:34 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-31 04:10:29 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:09:18 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:09:05 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-08-31 04:08:45 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.010 |  |
| 2026-08-31 04:08:24 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-08-31 04:07:53 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | -0.030 |  |
| 2026-08-31 04:06:07 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-31 04:06:05 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-08-31 04:05:50 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:05:35 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-08-31 04:04:56 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:04:54 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:04:22 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:03:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:03:32 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:03:14 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 04:03:08 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-08-31 04:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-31 04:02:24 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:02:14 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:02:09 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:02:05 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:02:03 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 04:01:17 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:01:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:01:08 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.061 |  |
| 2026-08-31 04:00:47 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-31 04:00:41 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-08-31 04:00:08 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 03:42:09 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-08-31 04:09:05 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-08-31 02:03:15 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-31 04:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-31 04:10:34 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-31 04:06:07 | Hanwella (Kelani Ganga) | 1.21 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-31 04:00:47 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-31 04:02:03 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 04:03:14 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 18:04:01 | Weraganthota (Mahaweli Ganga) | -3.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 04:20:12 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-31 04:00:08 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:01:17 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:02:05 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:04:54 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:02:09 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:13 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:10:29 | Baddegama (Gin Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 03:01:09 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 03:05:53 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:05:50 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:02:24 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:01:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:04:56 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:09:18 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:36 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:02:14 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:22:25 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-31 04:08:24 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-08-31 04:03:08 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-08-31 04:08:45 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.010 |  |
| 2026-08-31 04:05:35 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-08-31 04:00:41 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-08-31 04:06:05 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.011 |  |
| 2026-08-31 04:07:53 | Panadugama (Nilwala Ganga) | 3.01 | 🟢 Normal | -0.030 |  |
| 2026-08-31 04:01:08 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.061 |  |
| 2026-08-31 04:25:12 | Magura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.720 |  |
| 2026-08-31 03:03:00 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | -0.857 |  |
| 2026-08-31 03:09:46 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | -3.429 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)