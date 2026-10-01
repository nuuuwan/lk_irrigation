# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_08:26:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,784 measurements** from **39** stations.
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
| 2026-10-01 08:26:14 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:23:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:19:54 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:14:47 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -0.011 |  |
| 2026-10-01 08:13:13 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-10-01 08:08:52 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:08:36 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:08:35 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:08:35 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | -0.028 |  |
| 2026-10-01 08:08:34 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:07:55 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.019 |  |
| 2026-10-01 08:07:50 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-01 08:07:23 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:06:39 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:05:57 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 08:05:07 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:05:01 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.064 |  |
| 2026-10-01 08:04:23 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:04:18 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.116 |  |
| 2026-10-01 08:04:10 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 08:03:55 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:03:54 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.050 |  |
| 2026-10-01 08:03:49 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:03:47 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:03:39 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-01 08:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.061 |  |
| 2026-10-01 08:03:25 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-10-01 08:02:47 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:46 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:20 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:14 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.033 |  |
| 2026-10-01 08:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-10-01 08:02:02 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:01:54 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.070 |  |
| 2026-10-01 08:01:05 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:00:44 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.041 |  |
| 2026-10-01 08:00:43 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-10-01 08:00:28 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 08:07:50 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-01 07:05:47 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-01 08:04:10 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 08:05:57 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-01 08:01:05 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:23:59 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:04:23 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:08:35 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:46 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:20 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:08:52 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:06:39 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:03:47 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:47 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:03:49 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:03:55 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:07:23 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:08:36 | Rathnapura (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:05:07 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:19:54 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:26:14 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:02 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:13:13 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-10-01 08:03:39 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-01 08:00:43 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-10-01 08:00:28 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-01 08:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-10-01 08:14:47 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -0.011 |  |
| 2026-10-01 08:07:55 | Ellagawa (Kalu Ganga) | 5.12 | 🟢 Normal | -0.019 |  |
| 2026-10-01 08:03:25 | Thanamalwila (Kirindi Oya) | 0.27 | 🟢 Normal | -0.021 |  |
| 2026-10-01 08:08:35 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | -0.028 |  |
| 2026-10-01 08:02:14 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.033 |  |
| 2026-10-01 08:00:44 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.041 |  |
| 2026-10-01 08:03:54 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | -0.050 |  |
| 2026-10-01 08:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.061 |  |
| 2026-10-01 08:05:01 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.064 |  |
| 2026-10-01 08:01:54 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.070 |  |
| 2026-10-01 07:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.097 |  |
| 2026-10-01 08:04:18 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)