# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--28_17:10:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **245,623 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-28 17:10:34 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:09:39 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.019 |  |
| 2026-08-28 17:09:31 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-08-28 17:09:26 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-08-28 17:08:44 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-28 17:08:16 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-08-28 17:08:13 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-28 17:08:07 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:07:37 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-08-28 17:06:59 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:05:55 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-28 17:05:47 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:05:39 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:05:29 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-08-28 17:05:24 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-08-28 17:05:02 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-28 17:04:48 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:04:08 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:04:07 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-28 17:03:41 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | -0.010 |  |
| 2026-08-28 17:03:25 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.089 |  |
| 2026-08-28 17:03:20 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-28 17:03:11 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.030 |  |
| 2026-08-28 17:03:05 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 17:02:40 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-28 17:02:37 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 17:02:08 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:01:59 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-08-28 17:01:41 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:01:35 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-08-28 17:01:11 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.011 |  |
| 2026-08-28 17:00:56 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:00:36 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-08-28 17:00:29 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:00:29 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:00:22 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.020 |  |
| 2026-08-28 17:00:11 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-28 16:56:46 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-28 17:05:29 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-08-28 17:05:24 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-08-28 17:05:02 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-28 17:02:40 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-28 17:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-28 17:05:55 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-28 17:08:13 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-28 17:02:37 | Hanwella (Kelani Ganga) | 1.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 17:03:05 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 17:08:44 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-28 17:00:29 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:04:48 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:00:29 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:08:07 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:01:41 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:03:41 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:10:34 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-28 16:08:45 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:05:39 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:06:59 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:04:07 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:04:08 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:02:08 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:05:47 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:00:11 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:00:56 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:09:26 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-08-28 17:08:16 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-08-28 17:09:31 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-08-28 17:03:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.14 | 🟢 Normal | -0.010 |  |
| 2026-08-28 17:03:20 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-28 17:01:11 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.011 |  |
| 2026-08-28 17:01:59 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-08-28 17:07:37 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-08-28 17:09:39 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.019 |  |
| 2026-08-28 17:01:35 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | -0.020 |  |
| 2026-08-28 17:00:22 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.020 |  |
| 2026-08-28 17:03:11 | Glencourse (Kelani Ganga) | 9.84 | 🟢 Normal | -0.030 |  |
| 2026-08-28 17:03:25 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)