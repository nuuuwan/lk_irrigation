# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_13:23:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,393 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 13:23:55 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 13:10:04 | Baddegama (Gin Ganga) | 4.04 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-27 13:09:34 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 13:07:28 | Glencourse (Kelani Ganga) | 12.90 | 🟢 Normal | -0.140 |  |
| 2026-10-27 13:07:15 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.036 |  |
| 2026-10-27 13:06:45 | Giriulla (Maha Oya) | 3.52 | 🟢 Normal | -0.082 |  |
| 2026-10-27 13:06:38 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-10-27 13:06:32 | Holombuwa (Kelani Ganga) | 1.70 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-27 13:06:27 | Badalgama (Maha Oya) | 4.79 | 🟢 Normal | -0.175 |  |
| 2026-10-27 13:06:07 | Peradeniya (Mahaweli Ganga) | 3.47 | 🟢 Normal | -0.028 |  |
| 2026-10-27 13:05:26 | Rathnapura (Kalu Ganga) | 8.26 | 🟠 Minor Flood | -0.039 |  |
| 2026-10-27 13:05:11 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 13:05:02 | Thawalama (Gin Ganga) | 3.47 | 🟢 Normal | -0.210 |  |
| 2026-10-27 13:04:19 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-10-27 13:04:15 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-10-27 13:04:11 | Putupaula (Kalu Ganga) | 3.30 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-27 13:03:45 | Magura (Kalu Ganga) | 5.13 | 🟡 Alert | -0.038 |  |
| 2026-10-27 13:03:20 | Urawa (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.032 |  |
| 2026-10-27 13:03:02 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-27 13:02:53 | Panadugama (Nilwala Ganga) | 6.32 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-27 13:02:49 | Hanwella (Kelani Ganga) | 6.00 | 🟢 Normal | -0.138 |  |
| 2026-10-27 13:02:42 | Ellagawa (Kalu Ganga) | 10.00 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-10-27 13:02:39 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-10-27 13:02:21 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-27 13:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.53 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-10-27 13:02:17 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 13:02:14 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 11.250 | 🔺 Rising |
| 2026-10-27 13:02:12 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-10-27 13:02:01 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-10-27 13:01:42 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.101 |  |
| 2026-10-27 13:01:42 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 11.250 | 🔺 Rising |
| 2026-10-27 13:01:41 | Moragaswewa (Deduru Oya) | 5.16 | 🟡 Alert | -0.042 |  |
| 2026-10-27 13:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-10-27 13:01:23 | Weraganthota (Mahaweli Ganga) | -2.59 | 🟢 Normal | -0.112 |  |
| 2026-10-27 13:01:15 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-27 13:01:06 | Horowpothana (Yan Oya) | 3.32 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-27 13:00:53 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-27 13:00:25 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 13:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.53 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-10-27 13:10:04 | Baddegama (Gin Ganga) | 4.04 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-27 12:02:40 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 13:02:53 | Panadugama (Nilwala Ganga) | 6.32 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-27 13:05:26 | Rathnapura (Kalu Ganga) | 8.26 | 🟠 Minor Flood | -0.039 |  |
| 2026-10-27 13:02:42 | Ellagawa (Kalu Ganga) | 10.00 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-10-27 13:04:11 | Putupaula (Kalu Ganga) | 3.30 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-27 13:23:55 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 13:03:45 | Magura (Kalu Ganga) | 5.13 | 🟡 Alert | -0.038 |  |
| 2026-10-27 13:01:41 | Moragaswewa (Deduru Oya) | 5.16 | 🟡 Alert | -0.042 |  |
| 2026-10-27 13:02:14 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 11.250 | 🔺 Rising |
| 2026-10-27 13:06:32 | Holombuwa (Kelani Ganga) | 1.70 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-10-27 13:01:06 | Horowpothana (Yan Oya) | 3.32 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-27 13:03:02 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-27 13:09:34 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 13:00:53 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-27 13:01:15 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-27 13:02:01 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | 0.000 |  |
| 2026-10-27 13:05:11 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 13:02:17 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 13:02:39 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-10-27 13:02:21 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-10-27 12:03:42 | Galgamuwa (Mee Oya) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-10-27 13:00:25 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-27 13:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-10-27 13:04:19 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-10-27 13:04:15 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-10-27 13:06:07 | Peradeniya (Mahaweli Ganga) | 3.47 | 🟢 Normal | -0.028 |  |
| 2026-10-27 13:02:12 | Deraniyagala (Kelani Ganga) | 1.29 | 🟢 Normal | -0.030 |  |
| 2026-10-27 13:03:20 | Urawa (Nilwala Ganga) | 1.46 | 🟢 Normal | -0.032 |  |
| 2026-10-27 13:07:15 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.036 |  |
| 2026-10-27 13:06:38 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | -0.050 |  |
| 2026-10-27 13:06:45 | Giriulla (Maha Oya) | 3.52 | 🟢 Normal | -0.082 |  |
| 2026-10-27 13:01:42 | Pitabeddara (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.101 |  |
| 2026-10-27 13:01:23 | Weraganthota (Mahaweli Ganga) | -2.59 | 🟢 Normal | -0.112 |  |
| 2026-10-27 13:02:49 | Hanwella (Kelani Ganga) | 6.00 | 🟢 Normal | -0.138 |  |
| 2026-10-27 13:07:28 | Glencourse (Kelani Ganga) | 12.90 | 🟢 Normal | -0.140 |  |
| 2026-10-27 13:06:27 | Badalgama (Maha Oya) | 4.79 | 🟢 Normal | -0.175 |  |
| 2026-10-27 13:05:02 | Thawalama (Gin Ganga) | 3.47 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)