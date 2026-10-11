# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_09:08:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,819 measurements** from **39** stations.
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
| 2026-10-11 09:08:44 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 09:08:26 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.041 |  |
| 2026-10-11 09:07:26 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.138 |  |
| 2026-10-11 09:07:21 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-10-11 09:07:19 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | -0.009 |  |
| 2026-10-11 09:07:18 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.094 |  |
| 2026-10-11 09:06:50 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.012 |  |
| 2026-10-11 09:06:44 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | -0.009 |  |
| 2026-10-11 09:06:38 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:06:32 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:06:14 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:06:09 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.040 |  |
| 2026-10-11 09:06:02 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.058 |  |
| 2026-10-11 09:05:52 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.009 |  |
| 2026-10-11 09:05:48 | Magura (Kalu Ganga) | 3.41 | 🟢 Normal | -0.087 |  |
| 2026-10-11 09:05:43 | Moragaswewa (Deduru Oya) | 2.50 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-10-11 09:05:32 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.070 |  |
| 2026-10-11 09:05:29 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-11 09:04:45 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.207 |  |
| 2026-10-11 09:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 09:04:21 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.089 |  |
| 2026-10-11 09:03:47 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.015 |  |
| 2026-10-11 09:03:26 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:03:22 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-10-11 09:03:13 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.031 |  |
| 2026-10-11 09:02:57 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.073 |  |
| 2026-10-11 09:02:46 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | -0.060 |  |
| 2026-10-11 09:02:41 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:02:24 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-11 09:02:23 | Giriulla (Maha Oya) | 2.73 | 🟢 Normal | -0.070 |  |
| 2026-10-11 09:02:17 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-10-11 09:01:52 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-10-11 09:01:37 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-11 09:01:29 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.060 |  |
| 2026-10-11 09:01:26 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:01:06 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:00:18 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.031 |  |
| 2026-10-11 09:00:11 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.060 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 09:05:43 | Moragaswewa (Deduru Oya) | 2.50 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-10-11 09:01:37 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-11 09:00:11 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-11 09:02:24 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-11 09:05:29 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-11 09:04:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 09:08:44 | Baddegama (Gin Ganga) | 2.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 09:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:03:26 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:06:32 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:02:41 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:06:38 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:06:14 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:01:26 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-11 09:06:44 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | -0.009 |  |
| 2026-10-11 09:05:52 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.009 |  |
| 2026-10-11 09:07:19 | Panadugama (Nilwala Ganga) | 3.99 | 🟢 Normal | -0.009 |  |
| 2026-10-11 09:07:21 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-10-11 09:02:17 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-10-11 09:06:50 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.012 |  |
| 2026-10-11 09:03:47 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.015 |  |
| 2026-10-11 09:01:52 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-10-11 09:03:22 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-10-11 08:05:31 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-10-11 09:03:13 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.031 |  |
| 2026-10-11 09:00:18 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.031 |  |
| 2026-10-11 09:06:09 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.040 |  |
| 2026-10-11 09:08:26 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.041 |  |
| 2026-10-11 09:06:02 | Hanwella (Kelani Ganga) | 2.98 | 🟢 Normal | -0.058 |  |
| 2026-10-11 09:02:46 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | -0.060 |  |
| 2026-10-11 09:01:29 | Kithulgala (Kelani Ganga) | 2.04 | 🟢 Normal | -0.060 |  |
| 2026-10-11 09:02:23 | Giriulla (Maha Oya) | 2.73 | 🟢 Normal | -0.070 |  |
| 2026-10-11 09:05:32 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.070 |  |
| 2026-10-11 09:02:57 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.073 |  |
| 2026-10-11 09:05:48 | Magura (Kalu Ganga) | 3.41 | 🟢 Normal | -0.087 |  |
| 2026-10-11 09:04:21 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.089 |  |
| 2026-10-11 09:07:18 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.094 |  |
| 2026-10-11 09:07:26 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.138 |  |
| 2026-10-11 09:04:45 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)