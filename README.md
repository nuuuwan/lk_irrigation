# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_23:05:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,439 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 23:05:10 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-10 23:05:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:04:31 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.030 |  |
| 2026-10-10 23:03:58 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:03:54 | Hanwella (Kelani Ganga) | 2.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 23:03:04 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:02:53 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | 1.993 | 🔺 Rising |
| 2026-10-10 23:02:45 | Nakkala (Kumbukkan Oya) | 2.03 | 🟢 Normal | -0.309 |  |
| 2026-10-10 23:02:44 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-10 23:02:43 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.150 |  |
| 2026-10-10 23:02:23 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-10 23:02:22 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:01:51 | Ellagawa (Kalu Ganga) | 6.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 23:01:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:01:33 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-10 23:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:01:02 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:00:21 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-10 23:00:16 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-10 22:34:57 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 23:02:53 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | 1.993 | 🔺 Rising |
| 2026-10-10 22:05:40 | Magura (Kalu Ganga) | 2.77 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-10-10 22:05:57 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-10-10 22:08:13 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-10-10 22:05:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.91 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-10-10 22:09:52 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-10 22:05:20 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-10 23:00:16 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-10 23:01:33 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-10 23:02:23 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-10 23:05:10 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-10 22:04:53 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-10-10 23:00:21 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-10 23:02:44 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-10 22:04:04 | Rathnapura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-10 23:03:54 | Hanwella (Kelani Ganga) | 2.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 23:01:51 | Ellagawa (Kalu Ganga) | 6.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 23:01:38 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:01:02 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:26 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 23:03:58 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-10 22:04:56 | Thaldena (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 22:09:43 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:00:50 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-10 22:34:57 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-10 22:07:26 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-10 22:14:48 | Panadugama (Nilwala Ganga) | 4.13 | 🟢 Normal | -0.009 |  |
| 2026-10-10 23:05:09 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:03:04 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:02:22 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-10-10 23:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-10 22:05:40 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.024 |  |
| 2026-10-10 23:04:31 | Badalgama (Maha Oya) | 3.81 | 🟢 Normal | -0.030 |  |
| 2026-10-10 22:09:57 | Giriulla (Maha Oya) | 2.91 | 🟢 Normal | -0.038 |  |
| 2026-10-10 22:11:11 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.038 |  |
| 2026-10-10 18:05:26 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.050 |  |
| 2026-10-10 23:02:43 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.150 |  |
| 2026-10-10 22:02:30 | Peradeniya (Mahaweli Ganga) | 3.65 | 🟢 Normal | -0.305 |  |
| 2026-10-10 23:02:45 | Nakkala (Kumbukkan Oya) | 2.03 | 🟢 Normal | -0.309 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)