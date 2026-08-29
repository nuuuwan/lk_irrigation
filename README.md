# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_05:42:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **245,954 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 05:42:10 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.105 |  |
| 2026-08-29 05:32:59 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-29 05:27:44 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:25:02 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | -0.105 |  |
| 2026-08-29 05:25:00 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.041 |  |
| 2026-08-29 05:19:22 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | -0.035 |  |
| 2026-08-29 05:18:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-29 05:11:09 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-29 05:10:54 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:08:05 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-29 05:07:37 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-08-29 05:07:26 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:06:48 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:06:01 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:05:43 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-08-29 05:05:29 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:05:26 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-29 05:05:14 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-08-29 05:04:29 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:03:47 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:03:23 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-08-29 05:02:41 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:02:34 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 05:02:32 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:02:25 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:02:13 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-29 05:02:08 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:02:08 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | -0.035 |  |
| 2026-08-29 05:02:02 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-29 05:01:54 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.081 |  |
| 2026-08-29 05:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:01:20 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:01:15 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:00:57 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:00:38 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.019 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 05:18:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.81 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-08-29 05:05:26 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-29 05:08:05 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-29 05:32:59 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-29 05:02:34 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 17:03:05 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 05:11:09 | Baddegama (Gin Ganga) | 1.61 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-29 05:02:02 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-29 05:02:08 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:00:29 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:06:01 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:38 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:03:47 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:03:44 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:04:03 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:02:32 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:01:15 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:27:44 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:02:25 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:02:41 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:04:29 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:07:26 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:05:29 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:00:57 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:10:54 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:01:20 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:06:48 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 05:05:14 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-08-29 05:02:13 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-29 03:04:09 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-08-29 05:07:37 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.011 |  |
| 2026-08-28 17:01:59 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-08-29 05:03:23 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-08-29 05:05:43 | Rathnapura (Kalu Ganga) | 1.62 | 🟢 Normal | -0.021 |  |
| 2026-08-29 05:19:22 | Hanwella (Kelani Ganga) | 1.65 | 🟢 Normal | -0.035 |  |
| 2026-08-29 05:25:00 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | -0.041 |  |
| 2026-08-29 05:01:54 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | -0.081 |  |
| 2026-08-29 05:42:10 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.105 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)