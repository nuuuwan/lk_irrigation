# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--31_14:17:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,045 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 14:17:53 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-10-31 14:10:40 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal | -0.052 |  |
| 2026-10-31 14:10:30 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | -0.026 |  |
| 2026-10-31 14:08:46 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-10-31 14:08:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-31 14:07:11 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.028 |  |
| 2026-10-31 14:06:39 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:06:15 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-31 14:05:32 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 14:05:20 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:04:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:04:18 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.019 |  |
| 2026-10-31 14:03:48 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-31 14:03:44 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-10-31 14:03:44 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-31 14:03:40 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-31 14:03:29 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-31 14:03:25 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.030 |  |
| 2026-10-31 14:03:21 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.81 | 🟢 Normal | -0.088 |  |
| 2026-10-31 14:02:53 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.108 |  |
| 2026-10-31 14:02:46 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.101 |  |
| 2026-10-31 14:02:39 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | -0.020 |  |
| 2026-10-31 14:02:29 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.013 |  |
| 2026-10-31 14:02:28 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:02:26 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-10-31 14:02:14 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-10-31 14:02:13 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | -0.099 |  |
| 2026-10-31 14:02:12 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.030 |  |
| 2026-10-31 14:02:12 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-10-31 14:01:54 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-31 14:01:44 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:01:34 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.044 |  |
| 2026-10-31 14:01:31 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:00:55 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-31 14:00:28 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.139 |  |
| 2026-10-31 14:00:14 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.051 |  |
| 2026-10-31 14:00:09 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-31 14:02:39 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | -0.020 |  |
| 2026-10-31 14:06:15 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-31 14:08:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-31 14:03:48 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-31 14:03:29 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-31 14:03:40 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-31 14:00:55 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-31 14:05:32 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-31 14:00:09 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:01:44 | Moragaswewa (Deduru Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:04:21 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:06:39 | Galgamuwa (Mee Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:02:28 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:05:20 | Rathnapura (Kalu Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:01:31 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:03:21 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-31 14:17:53 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-10-31 14:02:26 | Dunamale (Aththanagalu Oya) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-10-31 14:03:44 | Hanwella (Kelani Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-10-31 14:02:14 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-10-31 14:01:54 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-31 14:03:44 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-10-31 14:02:29 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | -0.013 |  |
| 2026-10-31 14:04:18 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.019 |  |
| 2026-10-31 14:02:12 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-10-31 14:10:30 | Panadugama (Nilwala Ganga) | 4.66 | 🟢 Normal | -0.026 |  |
| 2026-10-31 14:07:11 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.028 |  |
| 2026-10-31 14:02:12 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | -0.030 |  |
| 2026-10-31 14:03:25 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.030 |  |
| 2026-10-31 14:08:46 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.032 |  |
| 2026-10-31 14:01:34 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.044 |  |
| 2026-10-31 14:00:14 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.051 |  |
| 2026-10-31 14:10:40 | Baddegama (Gin Ganga) | 2.49 | 🟢 Normal | -0.052 |  |
| 2026-10-31 14:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.81 | 🟢 Normal | -0.088 |  |
| 2026-10-31 14:02:13 | Putupaula (Kalu Ganga) | 2.11 | 🟢 Normal | -0.099 |  |
| 2026-10-31 14:02:46 | Ellagawa (Kalu Ganga) | 6.48 | 🟢 Normal | -0.101 |  |
| 2026-10-31 14:02:53 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.108 |  |
| 2026-10-31 14:00:28 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)