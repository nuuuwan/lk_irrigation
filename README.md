# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_16:25:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,297 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 16:25:27 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:16:02 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.008 |  |
| 2026-08-30 16:12:34 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:12:29 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.018 |  |
| 2026-08-30 16:12:20 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:11:58 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-08-30 16:06:42 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:06:41 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.033 |  |
| 2026-08-30 16:05:24 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:05:20 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.048 |  |
| 2026-08-30 16:05:03 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 16:04:53 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-08-30 16:04:35 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:04:15 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:04:03 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-08-30 16:03:40 | Weraganthota (Mahaweli Ganga) | -3.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-30 16:03:40 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.020 |  |
| 2026-08-30 16:03:26 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 16:03:26 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-08-30 16:03:19 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:03:02 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-08-30 16:02:50 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:02:45 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-08-30 16:02:43 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:02:43 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:02:37 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-30 16:02:30 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 16:02:29 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-30 16:02:28 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 16:02:27 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.020 |  |
| 2026-08-30 16:02:24 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:55 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:46 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:33 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:12 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:00:33 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:00:17 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 16:02:29 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-30 16:02:30 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 16:02:28 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 16:03:40 | Weraganthota (Mahaweli Ganga) | -3.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-30 16:05:03 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 16:03:26 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 16:02:43 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:00:17 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:25:27 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:55 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:02:24 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:00:33 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:02:43 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:03:19 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:12:20 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:12 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:02:50 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:04:15 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:06:42 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:46 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:07:34 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:04:35 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:05:24 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:08:30 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:12:34 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:01:33 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-30 16:16:02 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.008 |  |
| 2026-08-30 16:11:58 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-08-30 16:04:53 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-08-30 16:03:02 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-08-30 16:02:37 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-08-30 16:02:45 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-08-30 16:04:03 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-08-30 16:03:26 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.011 |  |
| 2026-08-30 16:12:29 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -0.018 |  |
| 2026-08-30 16:03:40 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.020 |  |
| 2026-08-30 16:02:27 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | -0.020 |  |
| 2026-08-30 16:06:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | -0.033 |  |
| 2026-08-30 16:05:20 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.048 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)