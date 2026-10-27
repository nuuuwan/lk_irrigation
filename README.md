# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_05:40:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,074 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟡 Badalgama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 05:40:34 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.006 |  |
| 2026-10-27 05:28:57 | Nagalagam Street (Kelani Ganga) | 1.28 | 🟡 Alert | -0.090 |  |
| 2026-10-27 05:26:46 | Urawa (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.152 |  |
| 2026-10-27 05:24:59 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.016 |  |
| 2026-10-27 05:16:43 | Moragaswewa (Deduru Oya) | 5.28 | 🟡 Alert | -0.020 |  |
| 2026-10-27 05:10:39 | Rathnapura (Kalu Ganga) | 8.67 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-27 05:10:38 | Baddegama (Gin Ganga) | 3.80 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-10-27 05:10:25 | Moraketiya (Walawe Ganga) | 2.40 | 🟢 Normal | -0.017 |  |
| 2026-10-27 05:07:55 | Pitabeddara (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.076 |  |
| 2026-10-27 05:06:26 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-27 05:06:26 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-27 05:05:56 | Glencourse (Kelani Ganga) | 14.44 | 🟢 Normal | -0.189 |  |
| 2026-10-27 05:05:29 | Peradeniya (Mahaweli Ganga) | 3.92 | 🟢 Normal | -0.160 |  |
| 2026-10-27 05:04:51 | Putupaula (Kalu Ganga) | 3.20 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2026-10-27 05:04:50 | Holombuwa (Kelani Ganga) | 2.09 | 🟢 Normal | -0.122 |  |
| 2026-10-27 05:04:47 | Badalgama (Maha Oya) | 5.77 | 🟡 Alert | 0.077 | 🔺 Rising |
| 2026-10-27 05:04:31 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-27 05:04:13 | Norwood (Kelani Ganga) | 1.64 | 🟡 Alert | -0.050 |  |
| 2026-10-27 05:03:58 | Giriulla (Maha Oya) | 4.63 | 🟢 Normal | -0.188 |  |
| 2026-10-27 05:03:56 | Ellagawa (Kalu Ganga) | 9.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 05:03:54 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-10-27 05:03:44 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 05:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 05:02:30 | Dunamale (Aththanagalu Oya) | 4.74 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-10-27 05:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-10-27 05:02:25 | Panadugama (Nilwala Ganga) | 6.55 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 05:10:39 | Rathnapura (Kalu Ganga) | 8.67 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-27 05:04:47 | Badalgama (Maha Oya) | 5.77 | 🟡 Alert | 0.077 | 🔺 Rising |
| 2026-10-27 05:02:21 | Thalgahagoda (Nilwala Ganga) | 1.57 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2026-10-27 05:04:51 | Putupaula (Kalu Ganga) | 3.20 | 🟡 Alert | 0.038 | 🔺 Rising |
| 2026-10-27 05:10:38 | Baddegama (Gin Ganga) | 3.80 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-10-27 05:00:50 | Magura (Kalu Ganga) | 5.28 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-27 05:16:43 | Moragaswewa (Deduru Oya) | 5.28 | 🟡 Alert | -0.020 |  |
| 2026-10-27 05:04:13 | Norwood (Kelani Ganga) | 1.64 | 🟡 Alert | -0.050 |  |
| 2026-10-27 05:28:57 | Nagalagam Street (Kelani Ganga) | 1.28 | 🟡 Alert | -0.090 |  |
| 2026-10-27 05:02:05 | Thawalama (Gin Ganga) | 5.10 | 🟡 Alert | -0.200 |  |
| 2026-10-26 18:02:01 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-27 05:03:06 | Manampitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-26 18:05:52 | Galgamuwa (Mee Oya) | 4.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-27 05:04:31 | Horowpothana (Yan Oya) | 2.55 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-27 05:03:56 | Ellagawa (Kalu Ganga) | 9.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 05:01:19 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 05:03:44 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 05:02:10 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 05:06:26 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-27 04:01:14 | Kuda Oya (Kirindi Oya) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-10-27 05:40:34 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.006 |  |
| 2026-10-27 05:06:26 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-27 05:03:54 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-10-27 05:24:59 | Deraniyagala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.016 |  |
| 2026-10-27 05:10:25 | Moraketiya (Walawe Ganga) | 2.40 | 🟢 Normal | -0.017 |  |
| 2026-10-27 05:00:51 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-10-27 05:03:04 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | -0.020 |  |
| 2026-10-27 05:02:08 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.040 |  |
| 2026-10-27 05:02:30 | Hanwella (Kelani Ganga) | 6.71 | 🟢 Normal | -0.052 |  |
| 2026-10-26 18:02:45 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.058 |  |
| 2026-10-27 05:07:55 | Pitabeddara (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.076 |  |
| 2026-10-27 05:04:50 | Holombuwa (Kelani Ganga) | 2.09 | 🟢 Normal | -0.122 |  |
| 2026-10-27 05:26:46 | Urawa (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.152 |  |
| 2026-10-27 05:05:29 | Peradeniya (Mahaweli Ganga) | 3.92 | 🟢 Normal | -0.160 |  |
| 2026-10-27 05:03:58 | Giriulla (Maha Oya) | 4.63 | 🟢 Normal | -0.188 |  |
| 2026-10-27 05:05:56 | Glencourse (Kelani Ganga) | 14.44 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)