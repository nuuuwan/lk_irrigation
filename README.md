# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_23:26:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,858 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟡 Thawalama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 23:26:03 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-26 23:22:22 | Pitabeddara (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-26 23:17:43 | Moraketiya (Walawe Ganga) | 2.35 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-10-26 23:17:03 | Ellagawa (Kalu Ganga) | 9.70 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-26 23:16:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.84 | 🟠 Minor Flood | 0.049 | 🔺 Rising |
| 2026-10-26 23:15:40 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-10-26 23:14:28 | Panadugama (Nilwala Ganga) | 6.20 | 🟠 Minor Flood | 0.066 | 🔺 Rising |
| 2026-10-26 23:14:17 | Rathnapura (Kalu Ganga) | 8.60 | 🟠 Minor Flood | 0.036 | 🔺 Rising |
| 2026-10-26 23:12:52 | Holombuwa (Kelani Ganga) | 3.19 | 🟡 Alert | -0.189 |  |
| 2026-10-26 23:12:31 | Moragaswewa (Deduru Oya) | 4.60 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-26 23:11:42 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-26 23:09:13 | Kithulgala (Kelani Ganga) | 2.67 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-10-26 23:08:21 | Thalgahagoda (Nilwala Ganga) | 1.43 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-10-26 23:07:17 | Norwood (Kelani Ganga) | 1.86 | 🟡 Alert | -0.043 |  |
| 2026-10-26 23:06:57 | Hanwella (Kelani Ganga) | 6.65 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-26 23:06:41 | Glencourse (Kelani Ganga) | 15.20 | 🟡 Alert | -0.066 |  |
| 2026-10-26 23:06:29 | Baddegama (Gin Ganga) | 3.46 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-26 23:06:08 | Putupaula (Kalu Ganga) | 2.97 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-26 23:06:03 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-10-26 23:05:52 | Thawalama (Gin Ganga) | 5.20 | 🟡 Alert | 0.195 | 🔺 Rising |
| 2026-10-26 23:05:39 | Urawa (Nilwala Ganga) | 2.56 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-10-26 23:04:53 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-26 23:04:33 | Giriulla (Maha Oya) | 5.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 23:03:54 | Nawalapitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.092 |  |
| 2026-10-26 23:03:33 | Moraketiya (Walawe Ganga) | 2.30 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-10-26 23:03:32 | Peradeniya (Mahaweli Ganga) | 4.88 | 🟢 Normal | -0.081 |  |
| 2026-10-26 23:03:27 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-26 23:03:15 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-26 23:02:41 | Deraniyagala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.110 |  |
| 2026-10-26 23:02:35 | Dunamale (Aththanagalu Oya) | 4.50 | 🟠 Minor Flood | 0.060 | 🔺 Rising |
| 2026-10-26 23:02:34 | Magura (Kalu Ganga) | 5.08 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-10-26 23:02:23 | Badalgama (Maha Oya) | 5.42 | 🟡 Alert | 0.132 | 🔺 Rising |
| 2026-10-26 23:02:09 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 23:14:28 | Panadugama (Nilwala Ganga) | 6.20 | 🟠 Minor Flood | 0.066 | 🔺 Rising |
| 2026-10-26 23:02:35 | Dunamale (Aththanagalu Oya) | 4.50 | 🟠 Minor Flood | 0.060 | 🔺 Rising |
| 2026-10-26 23:16:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.84 | 🟠 Minor Flood | 0.049 | 🔺 Rising |
| 2026-10-26 23:14:17 | Rathnapura (Kalu Ganga) | 8.60 | 🟠 Minor Flood | 0.036 | 🔺 Rising |
| 2026-10-26 23:05:52 | Thawalama (Gin Ganga) | 5.20 | 🟡 Alert | 0.195 | 🔺 Rising |
| 2026-10-26 23:02:23 | Badalgama (Maha Oya) | 5.42 | 🟡 Alert | 0.132 | 🔺 Rising |
| 2026-10-26 23:02:34 | Magura (Kalu Ganga) | 5.08 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-10-26 23:05:39 | Urawa (Nilwala Ganga) | 2.56 | 🟡 Alert | 0.032 | 🔺 Rising |
| 2026-10-26 23:08:21 | Thalgahagoda (Nilwala Ganga) | 1.43 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-10-26 23:07:17 | Norwood (Kelani Ganga) | 1.86 | 🟡 Alert | -0.043 |  |
| 2026-10-26 23:06:41 | Glencourse (Kelani Ganga) | 15.20 | 🟡 Alert | -0.066 |  |
| 2026-10-26 23:12:52 | Holombuwa (Kelani Ganga) | 3.19 | 🟡 Alert | -0.189 |  |
| 2026-10-26 23:09:13 | Kithulgala (Kelani Ganga) | 2.67 | 🟢 Normal | 0.287 | 🔺 Rising |
| 2026-10-26 23:17:43 | Moraketiya (Walawe Ganga) | 2.35 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-10-26 18:02:01 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-26 23:17:03 | Ellagawa (Kalu Ganga) | 9.70 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-26 22:03:37 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-10-26 23:06:57 | Hanwella (Kelani Ganga) | 6.65 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-26 23:03:27 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-26 23:06:29 | Baddegama (Gin Ganga) | 3.46 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-10-26 18:05:52 | Galgamuwa (Mee Oya) | 4.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-26 23:12:31 | Moragaswewa (Deduru Oya) | 4.60 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-26 23:06:08 | Putupaula (Kalu Ganga) | 2.97 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-26 23:11:42 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-26 23:22:22 | Pitabeddara (Nilwala Ganga) | 3.66 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-26 22:03:45 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 23:04:33 | Giriulla (Maha Oya) | 5.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 23:26:03 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-10-26 23:02:09 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-26 22:06:37 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-10-26 23:04:53 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-26 21:03:46 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-26 23:06:03 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-10-26 23:03:15 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-26 23:15:40 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.029 |  |
| 2026-10-26 18:02:45 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.058 |  |
| 2026-10-26 23:03:32 | Peradeniya (Mahaweli Ganga) | 4.88 | 🟢 Normal | -0.081 |  |
| 2026-10-26 23:03:54 | Nawalapitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.092 |  |
| 2026-10-26 23:02:41 | Deraniyagala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)