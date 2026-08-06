# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_08:06:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,294 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 08:06:20 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:06:19 | Peradeniya (Mahaweli Ganga) | 4.12 | 🟢 Normal | -0.030 |  |
| 2026-08-06 08:05:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:05:07 | Glencourse (Kelani Ganga) | 11.33 | 🟢 Normal | -0.021 |  |
| 2026-08-06 08:04:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:04:32 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:04:14 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:04:08 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-08-06 08:04:02 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-08-06 08:03:50 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | -0.052 |  |
| 2026-08-06 08:03:47 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:03:27 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-06 08:03:21 | Kithulgala (Kelani Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:02:51 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-08-06 08:02:34 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-08-06 08:02:27 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:02:24 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-08-06 08:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | -0.020 |  |
| 2026-08-06 08:01:39 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:01:39 | Ellagawa (Kalu Ganga) | 7.68 | 🟢 Normal | -0.111 |  |
| 2026-08-06 08:01:28 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:01:19 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.021 |  |
| 2026-08-06 08:01:16 | Putupaula (Kalu Ganga) | 1.71 | 🟢 Normal | -0.032 |  |
| 2026-08-06 08:01:09 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-06 08:01:04 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:01:00 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 08:00:35 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-06 08:00:12 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | 0.000 |  |
| 2026-08-06 07:38:55 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.013 |  |
| 2026-08-06 07:23:07 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 08:01:09 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-06 08:01:00 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 08:03:27 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-06 07:08:18 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-06 08:03:21 | Kithulgala (Kelani Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:00:12 | Weraganthota (Mahaweli Ganga) | -3.43 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:02:27 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-06 07:01:00 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-06 07:04:52 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:05:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 07:01:53 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 07:13:35 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:04:32 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:01:04 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:04:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:01:39 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:03:47 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 07:08:32 | Badalgama (Maha Oya) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:06:20 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 07:04:02 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-06 07:23:07 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-06 07:00:20 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-06 08:01:28 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 07:05:04 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-08-06 08:04:08 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-08-06 08:02:51 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-08-06 08:00:35 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-06 08:02:24 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-08-06 08:02:34 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.012 |  |
| 2026-08-06 07:38:55 | Panadugama (Nilwala Ganga) | 2.52 | 🟢 Normal | -0.013 |  |
| 2026-08-06 08:04:02 | Magura (Kalu Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-08-06 08:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.45 | 🟢 Normal | -0.020 |  |
| 2026-08-06 08:01:19 | Nawalapitiya (Mahaweli Ganga) | 2.28 | 🟢 Normal | -0.021 |  |
| 2026-08-06 08:05:07 | Glencourse (Kelani Ganga) | 11.33 | 🟢 Normal | -0.021 |  |
| 2026-08-06 08:06:19 | Peradeniya (Mahaweli Ganga) | 4.12 | 🟢 Normal | -0.030 |  |
| 2026-08-06 08:01:16 | Putupaula (Kalu Ganga) | 1.71 | 🟢 Normal | -0.032 |  |
| 2026-08-06 08:03:50 | Hanwella (Kelani Ganga) | 3.17 | 🟢 Normal | -0.052 |  |
| 2026-08-06 07:05:32 | Rathnapura (Kalu Ganga) | 2.51 | 🟢 Normal | -0.105 |  |
| 2026-08-06 08:01:39 | Ellagawa (Kalu Ganga) | 7.68 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)