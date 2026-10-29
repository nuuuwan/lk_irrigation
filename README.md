# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_13:32:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,202 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 13:32:14 | Rathnapura (Kalu Ganga) | 4.66 | 🟢 Normal | -0.014 |  |
| 2026-10-29 13:31:46 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:19:11 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 13:16:57 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:11:48 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-29 13:10:02 | Panadugama (Nilwala Ganga) | 5.79 | 🟡 Alert | -0.010 |  |
| 2026-10-29 13:09:09 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.009 |  |
| 2026-10-29 13:08:41 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.018 |  |
| 2026-10-29 13:07:09 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:06:25 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:06:24 | Pitabeddara (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.053 |  |
| 2026-10-29 13:04:54 | Dunamale (Aththanagalu Oya) | 2.47 | 🟢 Normal | -0.019 |  |
| 2026-10-29 13:04:33 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.048 |  |
| 2026-10-29 13:04:23 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:04:14 | Putupaula (Kalu Ganga) | 3.70 | 🟡 Alert | -0.010 |  |
| 2026-10-29 13:03:59 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:03:59 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-10-29 13:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.28 | 🟠 Minor Flood | -0.071 |  |
| 2026-10-29 13:03:46 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:03:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-29 13:03:34 | Hanwella (Kelani Ganga) | 3.59 | 🟢 Normal | -0.059 |  |
| 2026-10-29 13:03:17 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:03:15 | Ellagawa (Kalu Ganga) | 9.96 | 🟢 Normal | -0.020 |  |
| 2026-10-29 13:03:13 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:02:29 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-29 13:02:16 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-29 13:02:11 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.040 |  |
| 2026-10-29 13:02:02 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-29 13:01:58 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:01:58 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-29 13:01:42 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-10-29 13:01:40 | Magura (Kalu Ganga) | 3.41 | 🟢 Normal | -0.031 |  |
| 2026-10-29 13:01:32 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-29 13:01:14 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:00:45 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:00:44 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-29 13:00:39 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.195 |  |
| 2026-10-29 13:00:29 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 13:19:11 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 13:01:58 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-29 13:03:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.28 | 🟠 Minor Flood | -0.071 |  |
| 2026-10-29 13:04:14 | Putupaula (Kalu Ganga) | 3.70 | 🟡 Alert | -0.010 |  |
| 2026-10-29 13:10:02 | Panadugama (Nilwala Ganga) | 5.79 | 🟡 Alert | -0.010 |  |
| 2026-10-29 13:03:46 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-29 13:02:29 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-29 13:01:32 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-29 13:02:16 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-29 13:02:02 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-29 13:00:45 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:00:29 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:16:57 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:03:46 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:31:46 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:03:13 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:01:58 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:03:59 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:06:25 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:03:17 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:04:23 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:07:09 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:01:14 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 13:09:09 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.009 |  |
| 2026-10-29 13:11:48 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-10-29 13:01:42 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-10-29 13:00:44 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-10-29 13:32:14 | Rathnapura (Kalu Ganga) | 4.66 | 🟢 Normal | -0.014 |  |
| 2026-10-29 13:08:41 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.018 |  |
| 2026-10-29 13:04:54 | Dunamale (Aththanagalu Oya) | 2.47 | 🟢 Normal | -0.019 |  |
| 2026-10-29 13:03:59 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-10-29 13:03:15 | Ellagawa (Kalu Ganga) | 9.96 | 🟢 Normal | -0.020 |  |
| 2026-10-29 13:01:40 | Magura (Kalu Ganga) | 3.41 | 🟢 Normal | -0.031 |  |
| 2026-10-29 13:02:11 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.040 |  |
| 2026-10-29 13:04:33 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | -0.048 |  |
| 2026-10-29 13:06:24 | Pitabeddara (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.053 |  |
| 2026-10-29 13:03:34 | Hanwella (Kelani Ganga) | 3.59 | 🟢 Normal | -0.059 |  |
| 2026-10-29 13:00:39 | Weraganthota (Mahaweli Ganga) | -2.57 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)