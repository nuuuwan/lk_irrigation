# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_01:35:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,213 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 01:35:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.95 | 🟢 Normal | -0.032 |  |
| 2026-10-14 01:30:37 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:26:09 | Magura (Kalu Ganga) | 5.12 | 🟡 Alert | 270.000 | 🔺 Rising |
| 2026-10-14 01:26:07 | Magura (Kalu Ganga) | 4.97 | 🟡 Alert | 270.000 | 🔺 Rising |
| 2026-10-14 01:26:06 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | 270.000 | 🔺 Rising |
| 2026-10-14 01:12:37 | Moraketiya (Walawe Ganga) | 0.00 | 🟢 Normal | -1.633 |  |
| 2026-10-14 01:11:02 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:10:38 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-14 01:07:30 | Rathnapura (Kalu Ganga) | 4.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-14 01:07:27 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:06:58 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-14 01:06:44 | Panadugama (Nilwala Ganga) | 6.01 | 🟠 Minor Flood | 0.065 | 🔺 Rising |
| 2026-10-14 01:06:25 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-14 01:06:17 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:05:58 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-14 01:05:35 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:04:42 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:04:39 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-14 01:04:35 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.010 |  |
| 2026-10-14 01:04:26 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-14 01:04:17 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.012 |  |
| 2026-10-14 01:04:17 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:03:48 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-14 01:03:47 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 01:03:17 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:02:52 | Thawalama (Gin Ganga) | 3.54 | 🟢 Normal | -0.060 |  |
| 2026-10-14 01:02:51 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 01:02:21 | Hanwella (Kelani Ganga) | 3.01 | 🟢 Normal | -0.031 |  |
| 2026-10-14 01:02:11 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 01:02:10 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:01:34 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-10-14 01:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:01:26 | Ellagawa (Kalu Ganga) | 7.52 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-14 01:01:11 | Pitabeddara (Nilwala Ganga) | 3.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-14 01:01:07 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:00:59 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-10-14 01:00:31 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.066 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 01:06:44 | Panadugama (Nilwala Ganga) | 6.01 | 🟠 Minor Flood | 0.065 | 🔺 Rising |
| 2026-10-14 01:26:09 | Magura (Kalu Ganga) | 5.12 | 🟡 Alert | 270.000 | 🔺 Rising |
| 2026-10-14 01:10:38 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-14 01:06:25 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-14 01:04:26 | Glencourse (Kelani Ganga) | 11.19 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-14 01:01:11 | Pitabeddara (Nilwala Ganga) | 3.45 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-14 01:04:39 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-14 01:01:26 | Ellagawa (Kalu Ganga) | 7.52 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-14 01:05:58 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-14 01:03:48 | Badalgama (Maha Oya) | 2.77 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-14 01:02:51 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-14 01:02:11 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 01:03:47 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 00:09:06 | Putupaula (Kalu Ganga) | 1.77 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 01:07:30 | Rathnapura (Kalu Ganga) | 4.30 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-14 01:04:42 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:04:17 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:01:32 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:02:10 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:01:07 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:05:16 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:30:37 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:07:27 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:06:17 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:03:17 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 01:11:02 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-14 00:26:20 | Urawa (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 18:04:16 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-10-14 01:06:58 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-13 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-10-14 01:04:35 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.010 |  |
| 2026-10-14 01:00:59 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-10-14 01:01:34 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.011 |  |
| 2026-10-14 01:04:17 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.012 |  |
| 2026-10-14 01:02:21 | Hanwella (Kelani Ganga) | 3.01 | 🟢 Normal | -0.031 |  |
| 2026-10-14 01:35:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.95 | 🟢 Normal | -0.032 |  |
| 2026-10-14 01:02:52 | Thawalama (Gin Ganga) | 3.54 | 🟢 Normal | -0.060 |  |
| 2026-10-14 01:00:31 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.066 |  |
| 2026-10-14 01:12:37 | Moraketiya (Walawe Ganga) | 0.00 | 🟢 Normal | -1.633 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)