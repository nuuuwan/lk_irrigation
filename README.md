# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_00:08:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,106 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 00:08:50 | Hanwella (Kelani Ganga) | 5.96 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-25 00:08:38 | Baddegama (Gin Ganga) | 4.56 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 00:07:51 | Peradeniya (Mahaweli Ganga) | 4.62 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-25 00:07:09 | Magura (Kalu Ganga) | 5.05 | 🟡 Alert | -0.012 |  |
| 2026-09-25 00:07:04 | Panadugama (Nilwala Ganga) | 6.65 | 🟠 Minor Flood | -0.043 |  |
| 2026-09-25 00:07:04 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:06:33 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:06:14 | Norwood (Kelani Ganga) | 1.55 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-09-25 00:06:11 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:06:03 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 00:05:51 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 00:05:30 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:05:05 | Deraniyagala (Kelani Ganga) | 2.75 | 🟢 Normal | -0.384 |  |
| 2026-09-25 00:04:51 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-25 00:04:41 | Rathnapura (Kalu Ganga) | 6.45 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-09-25 00:04:26 | Glencourse (Kelani Ganga) | 14.68 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-25 00:04:16 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.051 |  |
| 2026-09-25 00:03:57 | Holombuwa (Kelani Ganga) | 1.78 | 🟢 Normal | -0.181 |  |
| 2026-09-25 00:03:50 | Thawalama (Gin Ganga) | 4.78 | 🟡 Alert | -0.174 |  |
| 2026-09-25 00:03:40 | Kithulgala (Kelani Ganga) | 2.94 | 🟢 Normal | -0.055 |  |
| 2026-09-25 00:03:22 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:02:38 | Dunamale (Aththanagalu Oya) | 3.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 00:02:31 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:02:16 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.051 |  |
| 2026-09-25 00:02:14 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | -0.021 |  |
| 2026-09-25 00:02:13 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:02:11 | Ellagawa (Kalu Ganga) | 8.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-25 00:02:04 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 00:02:03 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-25 00:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:01:45 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:01:33 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:01:15 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:00:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:59:56 | Moraketiya (Walawe Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:59:47 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:59:46 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 00:08:38 | Baddegama (Gin Ganga) | 4.56 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-24 23:05:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.80 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-25 00:06:03 | Thalgahagoda (Nilwala Ganga) | 1.74 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 00:07:04 | Panadugama (Nilwala Ganga) | 6.65 | 🟠 Minor Flood | -0.043 |  |
| 2026-09-25 00:04:41 | Rathnapura (Kalu Ganga) | 6.45 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-09-25 00:06:14 | Norwood (Kelani Ganga) | 1.55 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-09-25 00:07:09 | Magura (Kalu Ganga) | 5.05 | 🟡 Alert | -0.012 |  |
| 2026-09-25 00:03:50 | Thawalama (Gin Ganga) | 4.78 | 🟡 Alert | -0.174 |  |
| 2026-09-25 00:08:50 | Hanwella (Kelani Ganga) | 5.96 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-25 00:04:26 | Glencourse (Kelani Ganga) | 14.68 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-25 00:07:51 | Peradeniya (Mahaweli Ganga) | 4.62 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-09-25 00:02:03 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-25 00:04:51 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-25 00:02:11 | Ellagawa (Kalu Ganga) | 8.46 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-25 00:02:38 | Dunamale (Aththanagalu Oya) | 3.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-25 00:05:51 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 00:02:04 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 18:00:46 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:00:09 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:01:33 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:05:30 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:01:15 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-24 23:59:56 | Moraketiya (Walawe Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:07:04 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:02:13 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:03:22 | Putupaula (Kalu Ganga) | 2.68 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:02:31 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:01:45 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 00:02:14 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | -0.021 |  |
| 2026-09-25 00:04:16 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | -0.051 |  |
| 2026-09-25 00:02:16 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.051 |  |
| 2026-09-25 00:03:40 | Kithulgala (Kelani Ganga) | 2.94 | 🟢 Normal | -0.055 |  |
| 2026-09-24 22:07:04 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.097 |  |
| 2026-09-25 00:03:57 | Holombuwa (Kelani Ganga) | 1.78 | 🟢 Normal | -0.181 |  |
| 2026-09-25 00:05:05 | Deraniyagala (Kelani Ganga) | 2.75 | 🟢 Normal | -0.384 |  |
| 2026-09-24 23:02:29 | Nawalapitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -1.065 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)