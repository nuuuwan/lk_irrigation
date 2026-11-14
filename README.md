# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--14_21:03:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **315,908 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 21:03:17 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.020 |  |
| 2026-11-14 21:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 21:03:10 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:03:04 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:03:03 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:02:59 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.021 |  |
| 2026-11-14 21:02:56 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:02:52 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-11-14 21:02:50 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-14 21:02:39 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-14 21:02:14 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:02:11 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:02:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.066 |  |
| 2026-11-14 21:02:01 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:01:43 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-14 21:01:32 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:00:40 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:00:22 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 20:23:32 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-14 21:00:22 | Thalgahagoda (Nilwala Ganga) | 1.91 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-14 20:08:48 | Panadugama (Nilwala Ganga) | 5.19 | 🟡 Alert | -0.027 |  |
| 2026-11-14 21:02:50 | Wellawaya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-11-14 20:04:37 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-14 20:04:27 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-14 21:02:39 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-14 21:01:43 | Dunamale (Aththanagalu Oya) | 2.06 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-14 18:01:52 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-14 21:03:17 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-14 20:01:46 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:03:04 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:02:14 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:01:32 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:23:32 | Horowpothana (Yan Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:59 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:10:49 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:08:05 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:02:11 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:03:43 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:03:10 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-14 21:00:40 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:04:28 | Manampitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:09:37 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-11-14 20:11:26 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.009 |  |
| 2026-11-14 20:04:04 | Moragaswewa (Deduru Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:03:03 | Rathnapura (Kalu Ganga) | 2.22 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:02:01 | Kuda Oya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-14 20:05:59 | Badalgama (Maha Oya) | 2.92 | 🟢 Normal | -0.010 |  |
| 2026-11-14 21:02:56 | Hanwella (Kelani Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-11-14 18:00:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-11-14 21:03:17 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.020 |  |
| 2026-11-14 20:06:19 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-11-14 20:06:43 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.021 |  |
| 2026-11-14 21:02:59 | Magura (Kalu Ganga) | 2.17 | 🟢 Normal | -0.021 |  |
| 2026-11-14 21:02:52 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-11-14 20:01:47 | Glencourse (Kelani Ganga) | 10.77 | 🟢 Normal | -0.032 |  |
| 2026-11-14 20:04:15 | Baddegama (Gin Ganga) | 3.22 | 🟢 Normal | -0.042 |  |
| 2026-11-14 21:02:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.066 |  |
| 2026-11-14 20:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)