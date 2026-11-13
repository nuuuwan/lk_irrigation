# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_08:23:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,532 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 08:23:48 | Urawa (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-11-13 08:20:05 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 08:13:28 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | -0.051 |  |
| 2026-11-13 08:12:22 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-13 08:12:08 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.018 |  |
| 2026-11-13 08:10:16 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.142 |  |
| 2026-11-13 08:10:04 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | -0.039 |  |
| 2026-11-13 08:09:02 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-13 08:08:26 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-13 08:08:02 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.038 |  |
| 2026-11-13 08:07:44 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.023 |  |
| 2026-11-13 08:07:10 | Giriulla (Maha Oya) | 2.23 | 🟢 Normal | -0.040 |  |
| 2026-11-13 08:07:04 | Moraketiya (Walawe Ganga) | 3.14 | 🟡 Alert | 0.000 |  |
| 2026-11-13 08:07:03 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.091 |  |
| 2026-11-13 08:05:48 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.019 |  |
| 2026-11-13 08:05:27 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:05:00 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:04:31 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:04:23 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-11-13 08:03:43 | Panadugama (Nilwala Ganga) | 6.32 | 🟠 Minor Flood | -0.026 |  |
| 2026-11-13 08:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.000 |  |
| 2026-11-13 08:03:29 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 08:03:23 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | -0.062 |  |
| 2026-11-13 08:03:19 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | -0.079 |  |
| 2026-11-13 08:03:14 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-11-13 08:03:14 | Thaldena (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.043 |  |
| 2026-11-13 08:03:09 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | -0.194 |  |
| 2026-11-13 08:03:01 | Kuda Oya (Kirindi Oya) | 2.43 | 🟢 Normal | -0.097 |  |
| 2026-11-13 08:02:38 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-13 08:02:28 | Ellagawa (Kalu Ganga) | 8.04 | 🟢 Normal | -0.040 |  |
| 2026-11-13 08:02:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.090 |  |
| 2026-11-13 08:02:14 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:02:08 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-11-13 08:02:07 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-11-13 08:01:45 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -0.039 |  |
| 2026-11-13 08:01:13 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-11-13 08:00:57 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-11-13 08:00:22 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:00:12 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | -0.125 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 08:12:22 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-13 08:20:05 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 08:03:43 | Panadugama (Nilwala Ganga) | 6.32 | 🟠 Minor Flood | -0.026 |  |
| 2026-11-13 08:07:04 | Moraketiya (Walawe Ganga) | 3.14 | 🟡 Alert | 0.000 |  |
| 2026-11-13 08:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.000 |  |
| 2026-11-13 08:13:28 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | -0.051 |  |
| 2026-11-13 08:01:13 | Manampitiya (Mahaweli Ganga) | 2.06 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-11-13 08:09:02 | Horowpothana (Yan Oya) | 2.59 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-13 08:03:29 | Weraganthota (Mahaweli Ganga) | -1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 08:00:22 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:05:00 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:05:27 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:02:14 | Putupaula (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:04:31 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-13 08:23:48 | Urawa (Nilwala Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-11-13 08:00:57 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-11-13 08:08:26 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-13 08:03:14 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-11-13 08:12:08 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.018 |  |
| 2026-11-13 08:05:48 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.019 |  |
| 2026-11-13 08:02:38 | Moragaswewa (Deduru Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-11-13 08:02:08 | Thanamalwila (Kirindi Oya) | 2.40 | 🟢 Normal | -0.020 |  |
| 2026-11-13 08:02:07 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.020 |  |
| 2026-11-13 08:07:44 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.023 |  |
| 2026-11-13 08:04:23 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.030 |  |
| 2026-11-13 08:08:02 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | -0.038 |  |
| 2026-11-13 08:01:45 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -0.039 |  |
| 2026-11-13 08:10:04 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | -0.039 |  |
| 2026-11-13 08:02:28 | Ellagawa (Kalu Ganga) | 8.04 | 🟢 Normal | -0.040 |  |
| 2026-11-13 08:07:10 | Giriulla (Maha Oya) | 2.23 | 🟢 Normal | -0.040 |  |
| 2026-11-13 08:03:14 | Thaldena (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.043 |  |
| 2026-11-13 08:03:23 | Hanwella (Kelani Ganga) | 3.88 | 🟢 Normal | -0.062 |  |
| 2026-11-13 08:03:19 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | -0.079 |  |
| 2026-11-13 08:02:23 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.090 |  |
| 2026-11-13 08:07:03 | Pitabeddara (Nilwala Ganga) | 2.30 | 🟢 Normal | -0.091 |  |
| 2026-11-13 08:03:01 | Kuda Oya (Kirindi Oya) | 2.43 | 🟢 Normal | -0.097 |  |
| 2026-11-13 08:00:12 | Nagalagam Street (Kelani Ganga) | 0.56 | 🟢 Normal | -0.125 |  |
| 2026-11-13 08:10:16 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | -0.142 |  |
| 2026-11-13 08:03:09 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)