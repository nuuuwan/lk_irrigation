# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--07_16:13:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,086 measurements** from **39** stations.
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
| 2026-08-07 16:13:53 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:11:15 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:10:01 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.017 |  |
| 2026-08-07 16:07:42 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:07:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-08-07 16:07:11 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | 0.884 | 🔺 Rising |
| 2026-08-07 16:06:59 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.064 |  |
| 2026-08-07 16:06:03 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:05:43 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-08-07 16:05:04 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.061 |  |
| 2026-08-07 16:05:01 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-08-07 16:05:01 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.019 |  |
| 2026-08-07 16:05:01 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-07 16:04:53 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:04:40 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:03:52 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:03:49 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | -0.117 |  |
| 2026-08-07 16:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-07 16:03:40 | Glencourse (Kelani Ganga) | 11.14 | 🟢 Normal | -0.031 |  |
| 2026-08-07 16:03:18 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:03:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:03:11 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-07 16:03:01 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:02:25 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:02:23 | Nawalapitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-08-07 16:02:10 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 16:02:02 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | -0.020 |  |
| 2026-08-07 16:01:39 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-08-07 16:01:27 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-07 16:01:22 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:01:09 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-07 16:01:07 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-08-07 16:01:02 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-07 16:00:54 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-07 16:00:47 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 16:00:28 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-08-07 16:00:28 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:00:12 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:00:11 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-07 16:07:11 | Rathnapura (Kalu Ganga) | 2.93 | 🟢 Normal | 0.884 | 🔺 Rising |
| 2026-08-07 16:00:54 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-07 16:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.76 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-07 16:03:11 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-07 15:02:36 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-07 16:01:27 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-07 16:01:02 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-07 16:01:09 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-07 16:05:01 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-07 16:02:10 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 16:00:47 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-07 16:02:25 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:00:12 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:03:52 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:00:11 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:13:53 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:07:42 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:11:15 | Hanwella (Kelani Ganga) | 2.78 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:06:03 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:03:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:04:53 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:03:01 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:01:22 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:00:28 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:04:40 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-07 16:07:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-08-07 16:05:43 | Badalgama (Maha Oya) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-08-07 16:01:39 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-08-07 16:02:23 | Nawalapitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-08-07 16:01:07 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-08-07 16:05:01 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-08-07 16:00:28 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | -0.011 |  |
| 2026-08-07 16:10:01 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.017 |  |
| 2026-08-07 16:05:01 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.019 |  |
| 2026-08-07 16:02:02 | Ellagawa (Kalu Ganga) | 5.74 | 🟢 Normal | -0.020 |  |
| 2026-08-07 16:03:40 | Glencourse (Kelani Ganga) | 11.14 | 🟢 Normal | -0.031 |  |
| 2026-08-07 16:05:04 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.061 |  |
| 2026-08-07 16:06:59 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.064 |  |
| 2026-08-07 16:03:49 | Kithulgala (Kelani Ganga) | 2.41 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)