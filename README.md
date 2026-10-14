# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_15:08:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,751 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 15:08:31 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-14 15:08:21 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:08:11 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:06:48 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.042 |  |
| 2026-10-14 15:06:38 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 15:06:20 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:06:04 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-14 15:05:22 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-10-14 15:05:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:05:09 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:05:09 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-10-14 15:04:59 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:04:54 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.021 |  |
| 2026-10-14 15:04:33 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:04:21 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:04:17 | Rathnapura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.099 |  |
| 2026-10-14 15:04:14 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-14 15:04:08 | Magura (Kalu Ganga) | 4.98 | 🟡 Alert | -0.045 |  |
| 2026-10-14 15:03:42 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:03:39 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.206 |  |
| 2026-10-14 15:03:39 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:03:32 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-14 15:03:31 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:03:25 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.029 |  |
| 2026-10-14 15:03:18 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-14 15:02:46 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.040 |  |
| 2026-10-14 15:02:35 | Thalgahagoda (Nilwala Ganga) | 1.71 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-14 15:02:35 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-10-14 15:02:32 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.011 |  |
| 2026-10-14 15:02:21 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | -0.040 |  |
| 2026-10-14 15:02:11 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-14 15:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.133 | 🔺 Rising |
| 2026-10-14 15:01:12 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.033 |  |
| 2026-10-14 15:01:10 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:01:09 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:00:52 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.032 |  |
| 2026-10-14 15:00:29 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:00:23 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:00:14 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 15:02:35 | Thalgahagoda (Nilwala Ganga) | 1.71 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-14 15:01:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.133 | 🔺 Rising |
| 2026-10-14 15:04:08 | Magura (Kalu Ganga) | 4.98 | 🟡 Alert | -0.045 |  |
| 2026-10-14 14:07:07 | Panadugama (Nilwala Ganga) | 5.80 | 🟡 Alert | -0.059 |  |
| 2026-10-14 15:08:31 | Holombuwa (Kelani Ganga) | 0.95 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-10-14 15:06:38 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 15:06:04 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-14 15:01:09 | Weraganthota (Mahaweli Ganga) | -3.38 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:01:10 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:03:39 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:04:21 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:03:42 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:03:31 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:04:59 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:05:21 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:06:20 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:00:14 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:05:09 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:03:18 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:00:29 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:08:11 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:08:21 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-14 15:03:32 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-14 15:02:11 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-14 15:02:35 | Dunamale (Aththanagalu Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-10-14 15:04:14 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-14 15:05:09 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -0.010 |  |
| 2026-10-14 15:02:46 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.011 |  |
| 2026-10-14 15:02:32 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.011 |  |
| 2026-10-14 15:05:22 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.019 |  |
| 2026-10-14 15:04:54 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.021 |  |
| 2026-10-14 15:03:25 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.029 |  |
| 2026-10-14 15:00:52 | Pitabeddara (Nilwala Ganga) | 1.75 | 🟢 Normal | -0.032 |  |
| 2026-10-14 15:01:12 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.033 |  |
| 2026-10-14 15:02:21 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | -0.040 |  |
| 2026-10-14 15:02:46 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.040 |  |
| 2026-10-14 15:06:48 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | -0.042 |  |
| 2026-10-14 15:04:17 | Rathnapura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.099 |  |
| 2026-10-14 15:03:39 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.206 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)