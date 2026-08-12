# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_20:23:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,748 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 20:23:58 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:21:02 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.230 |  |
| 2026-08-12 20:16:59 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.038 |  |
| 2026-08-12 20:12:09 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:12:05 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.030 |  |
| 2026-08-12 20:11:26 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:10:09 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-12 20:08:34 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:08:03 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:07:37 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:07:11 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:06:47 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-12 20:06:35 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:06:16 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-12 20:06:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-12 20:05:24 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.039 |  |
| 2026-08-12 20:05:22 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.230 |  |
| 2026-08-12 20:04:47 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.067 |  |
| 2026-08-12 20:04:27 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:04:26 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-08-12 20:04:03 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:03:58 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.031 |  |
| 2026-08-12 20:03:48 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:03:47 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:03:40 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.068 |  |
| 2026-08-12 20:03:09 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.031 |  |
| 2026-08-12 20:03:07 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.093 |  |
| 2026-08-12 20:03:04 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-08-12 20:02:58 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-12 20:02:54 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-08-12 20:02:22 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:02:18 | Peradeniya (Mahaweli Ganga) | 3.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 20:02:14 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-08-12 20:01:40 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:01:36 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:01:15 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:00:36 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-12 20:00:32 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 20:06:47 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-08-12 20:02:58 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-12 20:04:26 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-08-12 20:06:16 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-12 20:10:09 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-12 20:00:32 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-12 20:02:18 | Peradeniya (Mahaweli Ganga) | 3.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 20:06:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.73 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-12 20:02:54 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:01:36 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:04:27 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:11:26 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:23:58 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:05:42 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:12:09 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:08:34 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:06:35 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:07:11 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:02:22 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:04:03 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:07:37 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:01:40 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 18:01:39 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:08:03 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:01:15 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 20:00:36 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-12 20:03:04 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-08-12 20:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-08-12 20:02:14 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-08-12 20:12:05 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.030 |  |
| 2026-08-12 17:00:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.031 |  |
| 2026-08-12 20:03:58 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.031 |  |
| 2026-08-12 20:03:09 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.031 |  |
| 2026-08-12 20:16:59 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.038 |  |
| 2026-08-12 20:05:24 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.039 |  |
| 2026-08-12 20:04:47 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.067 |  |
| 2026-08-12 20:03:40 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.068 |  |
| 2026-08-12 20:03:07 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.093 |  |
| 2026-08-12 20:21:02 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.230 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)