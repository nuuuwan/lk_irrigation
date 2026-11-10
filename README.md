# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_18:03:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,195 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 18:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.059 |  |
| 2026-11-10 18:03:44 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -2.876 |  |
| 2026-11-10 18:03:39 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-11-10 18:03:23 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 18:03:10 | Glencourse (Kelani Ganga) | 11.76 | 🟢 Normal | -0.032 |  |
| 2026-11-10 18:03:05 | Ellagawa (Kalu Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:02:56 | Siyambalanduwa (Heda Oya) | 1.81 | 🟢 Normal | 0.513 | 🔺 Rising |
| 2026-11-10 18:02:55 | Giriulla (Maha Oya) | 2.19 | 🟢 Normal | -0.040 |  |
| 2026-11-10 18:02:43 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-10 18:02:33 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-11-10 18:02:22 | Panadugama (Nilwala Ganga) | 5.75 | 🟡 Alert | -0.010 |  |
| 2026-11-10 18:02:21 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | 0.725 | 🔺 Rising |
| 2026-11-10 18:02:19 | Horowpothana (Yan Oya) | 2.64 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-10 18:01:59 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.050 |  |
| 2026-11-10 18:01:40 | Kuda Oya (Kirindi Oya) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 18:01:19 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-10 18:00:49 | Dunamale (Aththanagalu Oya) | 4.54 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-10 18:00:36 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-11-10 18:00:16 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:47:12 | Nagalagam Street (Kelani Ganga) | 1.52 | 🟠 Minor Flood | -2.876 |  |
| 2026-11-10 17:24:27 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 17:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.70 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-11-10 18:00:36 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-11-10 17:07:37 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 18:00:49 | Dunamale (Aththanagalu Oya) | 4.54 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-10 17:03:38 | Moraketiya (Walawe Ganga) | 3.03 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-10 18:02:22 | Panadugama (Nilwala Ganga) | 5.75 | 🟡 Alert | -0.010 |  |
| 2026-11-10 17:09:03 | Magura (Kalu Ganga) | 4.46 | 🟡 Alert | -0.105 |  |
| 2026-11-10 17:03:46 | Deraniyagala (Kelani Ganga) | 2.40 | 🟢 Normal | 1.046 | 🔺 Rising |
| 2026-11-10 17:05:15 | Hanwella (Kelani Ganga) | 4.79 | 🟢 Normal | 0.947 | 🔺 Rising |
| 2026-11-10 18:02:21 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | 0.725 | 🔺 Rising |
| 2026-11-10 18:02:56 | Siyambalanduwa (Heda Oya) | 1.81 | 🟢 Normal | 0.513 | 🔺 Rising |
| 2026-11-10 18:03:39 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.264 | 🔺 Rising |
| 2026-11-10 18:02:33 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-11-10 18:02:43 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-10 18:01:19 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-11-10 17:07:57 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-10 17:09:09 | Norwood (Kelani Ganga) | 1.44 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-10 18:02:19 | Horowpothana (Yan Oya) | 2.64 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-10 18:01:40 | Kuda Oya (Kirindi Oya) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 18:03:23 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 17:08:33 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-10 18:00:16 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:04:14 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:04:35 | Galgamuwa (Mee Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:03:05 | Ellagawa (Kalu Ganga) | 8.62 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:08:52 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:04:10 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:03:56 | Thanamalwila (Kirindi Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-11-10 17:04:40 | Urawa (Nilwala Ganga) | 1.28 | 🟢 Normal | -0.015 |  |
| 2026-11-10 17:00:47 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.017 |  |
| 2026-11-10 17:24:27 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.030 |  |
| 2026-11-10 17:08:05 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | -0.030 |  |
| 2026-11-10 18:03:10 | Glencourse (Kelani Ganga) | 11.76 | 🟢 Normal | -0.032 |  |
| 2026-11-10 18:02:55 | Giriulla (Maha Oya) | 2.19 | 🟢 Normal | -0.040 |  |
| 2026-11-10 18:01:59 | Manampitiya (Mahaweli Ganga) | 1.53 | 🟢 Normal | -0.050 |  |
| 2026-11-10 18:03:46 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.059 |  |
| 2026-11-10 17:07:29 | Moragaswewa (Deduru Oya) | 4.01 | 🟢 Normal | -0.088 |  |
| 2026-11-10 18:03:44 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -2.876 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)