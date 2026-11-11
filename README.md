# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_05:24:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,602 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Dunamale — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 05:24:32 | Dunamale (Aththanagalu Oya) | 4.29 | 🟡 Alert | -0.015 |  |
| 2026-11-11 05:24:16 | Pitabeddara (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:14:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 05:13:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-11-11 05:10:14 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.072 |  |
| 2026-11-11 05:09:02 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-11-11 05:08:45 | Hanwella (Kelani Ganga) | 4.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 05:08:22 | Panadugama (Nilwala Ganga) | 5.99 | 🟡 Alert | -0.090 |  |
| 2026-11-11 05:07:48 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | -0.114 |  |
| 2026-11-11 05:07:11 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.074 |  |
| 2026-11-11 05:06:34 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:06:33 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:06:11 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-11 05:05:58 | Badalgama (Maha Oya) | 4.30 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-11-11 05:05:20 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | -0.094 |  |
| 2026-11-11 05:05:02 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-11 05:04:34 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:04:05 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-11 05:03:49 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.042 |  |
| 2026-11-11 05:03:33 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 05:03:29 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | -0.282 |  |
| 2026-11-11 05:02:53 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.120 |  |
| 2026-11-11 05:02:43 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -0.030 |  |
| 2026-11-11 05:02:36 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.066 |  |
| 2026-11-11 05:02:27 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.061 |  |
| 2026-11-11 05:02:24 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:02:03 | Thawalama (Gin Ganga) | 3.63 | 🟢 Normal | -0.190 |  |
| 2026-11-11 05:02:00 | Glencourse (Kelani Ganga) | 12.70 | 🟢 Normal | -0.197 |  |
| 2026-11-11 05:01:36 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-11 05:01:34 | Kuda Oya (Kirindi Oya) | 2.01 | 🟢 Normal | -0.040 |  |
| 2026-11-11 05:01:29 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:01:25 | Moragaswewa (Deduru Oya) | 2.80 | 🟢 Normal | -0.182 |  |
| 2026-11-11 05:00:24 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.012 |  |
| 2026-11-11 05:00:12 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.220 |  |
| 2026-11-11 05:00:09 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-11 05:00:07 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 05:03:33 | Baddegama (Gin Ganga) | 4.26 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 05:00:07 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 05:14:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.66 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 05:24:32 | Dunamale (Aththanagalu Oya) | 4.29 | 🟡 Alert | -0.015 |  |
| 2026-11-11 03:11:08 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | -0.028 |  |
| 2026-11-11 05:08:22 | Panadugama (Nilwala Ganga) | 5.99 | 🟡 Alert | -0.090 |  |
| 2026-11-11 05:05:58 | Badalgama (Maha Oya) | 4.30 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-11-11 05:00:09 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-10 18:00:51 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-11 05:06:11 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-11 05:05:02 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-11 05:04:05 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-11 05:08:45 | Hanwella (Kelani Ganga) | 4.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 05:06:34 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:24:16 | Pitabeddara (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:01:29 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:04:34 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:02:24 | Manampitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-10 18:04:35 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-11 05:13:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.008 |  |
| 2026-11-10 18:10:04 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-11 05:00:24 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.012 |  |
| 2026-11-11 05:01:36 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-11-11 05:09:02 | Norwood (Kelani Ganga) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-11-11 05:02:43 | Horowpothana (Yan Oya) | 2.62 | 🟢 Normal | -0.030 |  |
| 2026-11-11 05:01:34 | Kuda Oya (Kirindi Oya) | 2.01 | 🟢 Normal | -0.040 |  |
| 2026-11-11 05:03:49 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.042 |  |
| 2026-11-11 05:02:27 | Siyambalanduwa (Heda Oya) | 0.93 | 🟢 Normal | -0.061 |  |
| 2026-11-11 05:02:36 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.066 |  |
| 2026-11-11 05:10:14 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.072 |  |
| 2026-11-11 05:07:11 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.074 |  |
| 2026-11-11 05:05:20 | Moraketiya (Walawe Ganga) | 2.20 | 🟢 Normal | -0.094 |  |
| 2026-11-11 05:07:48 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | -0.114 |  |
| 2026-11-11 05:02:53 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.120 |  |
| 2026-11-11 05:01:25 | Moragaswewa (Deduru Oya) | 2.80 | 🟢 Normal | -0.182 |  |
| 2026-11-11 05:02:03 | Thawalama (Gin Ganga) | 3.63 | 🟢 Normal | -0.190 |  |
| 2026-11-11 05:02:00 | Glencourse (Kelani Ganga) | 12.70 | 🟢 Normal | -0.197 |  |
| 2026-11-11 05:00:12 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.220 |  |
| 2026-11-11 05:03:29 | Giriulla (Maha Oya) | 3.70 | 🟢 Normal | -0.282 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)