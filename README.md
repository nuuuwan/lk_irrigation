# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--08_16:15:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **282,405 measurements** from **39** stations.
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
| 2026-10-08 16:15:25 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:15:24 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-08 16:14:11 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-10-08 16:13:47 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.050 |  |
| 2026-10-08 16:12:16 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.094 |  |
| 2026-10-08 16:09:52 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 16:08:32 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.033 |  |
| 2026-10-08 16:06:42 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.040 |  |
| 2026-10-08 16:06:06 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.070 |  |
| 2026-10-08 16:06:00 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-10-08 16:06:00 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.141 |  |
| 2026-10-08 16:05:31 | Ellagawa (Kalu Ganga) | 5.37 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-08 16:05:18 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | -0.096 |  |
| 2026-10-08 16:05:15 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.049 |  |
| 2026-10-08 16:05:01 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-08 16:04:52 | Thawalama (Gin Ganga) | 2.61 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-10-08 16:04:38 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-08 16:04:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.73 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-08 16:04:33 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-08 16:04:33 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.048 |  |
| 2026-10-08 16:04:23 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:04:03 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 16:03:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 16:03:52 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.087 |  |
| 2026-10-08 16:03:20 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:03:07 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-10-08 16:02:50 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:02:23 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-10-08 16:02:04 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.069 |  |
| 2026-10-08 16:02:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:01:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-10-08 16:01:45 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:01:41 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:01:33 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:01:30 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:01:21 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.010 |  |
| 2026-10-08 16:01:11 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 16:00:55 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:00:34 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-08 16:04:52 | Thawalama (Gin Ganga) | 2.61 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-10-08 16:02:23 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-10-08 16:04:33 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-08 16:04:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.73 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-08 16:06:00 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-10-08 16:05:31 | Ellagawa (Kalu Ganga) | 5.37 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-08 16:15:24 | Thalgahagoda (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-08 16:03:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-08 16:01:11 | Moragaswewa (Deduru Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 16:04:03 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-08 16:09:52 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-08 16:01:41 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:02:01 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:15:25 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:03:20 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:01:45 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:04:23 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:02:50 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:01:30 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:00:55 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:01:33 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-08 16:14:11 | Magura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.010 |  |
| 2026-10-08 16:04:38 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-10-08 16:05:01 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-08 16:01:52 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-10-08 16:01:21 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.010 |  |
| 2026-10-08 16:00:34 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.012 |  |
| 2026-10-08 16:03:07 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-10-08 16:08:32 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | -0.033 |  |
| 2026-10-08 16:06:42 | Putupaula (Kalu Ganga) | 0.89 | 🟢 Normal | -0.040 |  |
| 2026-10-08 16:04:33 | Giriulla (Maha Oya) | 1.67 | 🟢 Normal | -0.048 |  |
| 2026-10-08 16:05:15 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.049 |  |
| 2026-10-08 16:13:47 | Panadugama (Nilwala Ganga) | 3.79 | 🟢 Normal | -0.050 |  |
| 2026-10-08 16:02:04 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.069 |  |
| 2026-10-08 16:06:06 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.070 |  |
| 2026-10-08 16:03:52 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.087 |  |
| 2026-10-08 16:12:16 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | -0.094 |  |
| 2026-10-08 16:05:18 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | -0.096 |  |
| 2026-10-08 16:06:00 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)