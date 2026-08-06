# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_10:14:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,383 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 10:14:36 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-08-06 10:11:16 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-08-06 10:10:39 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | -0.027 |  |
| 2026-08-06 10:10:16 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:09:54 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-08-06 10:08:46 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.009 |  |
| 2026-08-06 10:07:24 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:07:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-08-06 10:06:24 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-08-06 10:06:22 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:06:06 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.085 |  |
| 2026-08-06 10:05:44 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-06 10:05:23 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:05:14 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.039 |  |
| 2026-08-06 10:04:43 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:04:13 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:04:12 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:03:12 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | -0.021 |  |
| 2026-08-06 10:03:08 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-06 10:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.030 |  |
| 2026-08-06 10:02:52 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:02:31 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:02:09 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:02:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:02:05 | Hanwella (Kelani Ganga) | 3.09 | 🟢 Normal | -0.041 |  |
| 2026-08-06 10:02:03 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 10:01:54 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:01:50 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | -0.134 |  |
| 2026-08-06 10:01:33 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:01:29 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:01:28 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:01:12 | Kithulgala (Kelani Ganga) | 2.52 | 🟢 Normal | -0.050 |  |
| 2026-08-06 10:00:54 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:00:44 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-06 10:00:28 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:00:17 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 10:03:08 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-06 10:00:44 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-06 10:02:03 | Horowpothana (Yan Oya) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 10:00:17 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:04:43 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:01:28 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-06 09:09:25 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:01:33 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:02:09 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:02:31 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:04:13 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-06 09:09:53 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:02:52 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:02:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:07:24 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:01:29 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:04:12 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:06:22 | Holombuwa (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:00:54 | Thanthirimale (Malwathu Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:10:16 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:05:23 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:00:28 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:01:54 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 10:11:16 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-08-06 10:06:24 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-08-06 10:08:46 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | -0.009 |  |
| 2026-08-06 10:05:44 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-06 10:09:54 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-08-06 09:10:08 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-08-06 10:14:36 | Panadugama (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.010 |  |
| 2026-08-06 10:03:12 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | -0.021 |  |
| 2026-08-06 10:10:39 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | -0.027 |  |
| 2026-08-06 10:07:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-08-06 10:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.030 |  |
| 2026-08-06 10:05:14 | Putupaula (Kalu Ganga) | 1.65 | 🟢 Normal | -0.039 |  |
| 2026-08-06 10:02:05 | Hanwella (Kelani Ganga) | 3.09 | 🟢 Normal | -0.041 |  |
| 2026-08-06 10:01:12 | Kithulgala (Kelani Ganga) | 2.52 | 🟢 Normal | -0.050 |  |
| 2026-08-06 10:06:06 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.085 |  |
| 2026-08-06 10:01:50 | Ellagawa (Kalu Ganga) | 7.44 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)