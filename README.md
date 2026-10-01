# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_09:12:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,822 measurements** from **39** stations.
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
| 2026-10-01 09:12:36 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | -0.019 |  |
| 2026-10-01 09:12:04 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:11:15 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -1.463 |  |
| 2026-10-01 09:09:12 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -1.463 |  |
| 2026-10-01 09:08:39 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.028 |  |
| 2026-10-01 09:08:02 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-01 09:07:37 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:07:26 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.009 |  |
| 2026-10-01 09:06:57 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-10-01 09:06:35 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 09:06:33 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:05:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:05:14 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:05:11 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:04:51 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-01 09:04:37 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:04:31 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-10-01 09:04:05 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.122 |  |
| 2026-10-01 09:03:53 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-01 09:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:03:18 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -2.919 |  |
| 2026-10-01 09:02:54 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-01 09:02:53 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.092 |  |
| 2026-10-01 09:02:49 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-01 09:02:46 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.020 |  |
| 2026-10-01 09:02:44 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:02:33 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-01 09:02:28 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:02:25 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:02:09 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:02:07 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.011 |  |
| 2026-10-01 09:02:04 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -2.919 |  |
| 2026-10-01 09:01:51 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:01:51 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-01 09:01:22 | Moragaswewa (Deduru Oya) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-10-01 09:01:08 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-01 09:00:46 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-10-01 09:00:36 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 09:03:53 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-01 09:02:54 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-01 09:01:51 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-01 09:06:35 | Glencourse (Kelani Ganga) | 10.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 07:05:47 | Thanthirimale (Malwathu Oya) | 0.54 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-01 09:02:33 | Peradeniya (Mahaweli Ganga) | 2.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-01 09:08:02 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-01 09:00:36 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:02:28 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:05:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:02:44 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:06:33 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:01:51 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:05:11 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:12:04 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:07:37 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-01 08:02:47 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:04:37 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:05:14 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:02:25 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:02:09 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:03:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-10-01 09:07:26 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | -0.009 |  |
| 2026-10-01 09:04:51 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-01 09:01:08 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-01 09:01:22 | Moragaswewa (Deduru Oya) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-10-01 09:00:46 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-10-01 09:02:49 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-10-01 09:04:31 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-10-01 09:02:07 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.011 |  |
| 2026-10-01 08:14:47 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | -0.011 |  |
| 2026-10-01 09:06:57 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-10-01 09:12:36 | Baddegama (Gin Ganga) | 1.79 | 🟢 Normal | -0.019 |  |
| 2026-10-01 09:02:46 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.020 |  |
| 2026-10-01 09:08:39 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.028 |  |
| 2026-10-01 09:02:53 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.092 |  |
| 2026-10-01 09:04:05 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.122 |  |
| 2026-10-01 09:11:15 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -1.463 |  |
| 2026-10-01 09:03:18 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -2.919 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)