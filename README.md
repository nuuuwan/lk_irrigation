# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_10:11:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,275 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟡 Baddegama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 10:11:15 | Panadugama (Nilwala Ganga) | 6.40 | 🟠 Minor Flood | -0.027 |  |
| 2026-10-27 10:10:49 | Pitabeddara (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.062 |  |
| 2026-10-27 10:08:51 | Giriulla (Maha Oya) | 3.80 | 🟢 Normal | -0.121 |  |
| 2026-10-27 10:08:50 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 10:08:27 | Thawalama (Gin Ganga) | 4.20 | 🟡 Alert | -0.218 |  |
| 2026-10-27 10:06:21 | Peradeniya (Mahaweli Ganga) | 3.57 | 🟢 Normal | -0.046 |  |
| 2026-10-27 10:06:14 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | -0.172 |  |
| 2026-10-27 10:05:27 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-10-27 10:05:26 | Badalgama (Maha Oya) | 5.30 | 🟡 Alert | -0.140 |  |
| 2026-10-27 10:05:21 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-10-27 10:05:15 | Galgamuwa (Mee Oya) | 4.07 | 🟢 Normal | -0.009 |  |
| 2026-10-27 10:04:21 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-27 10:04:17 | Ellagawa (Kalu Ganga) | 9.92 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-27 10:04:10 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-27 10:03:49 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | -0.210 |  |
| 2026-10-27 10:03:40 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-10-27 10:03:30 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-27 10:03:30 | Baddegama (Gin Ganga) | 3.96 | 🟡 Alert | 0.033 | 🔺 Rising |
| 2026-10-27 10:03:15 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-10-27 10:03:08 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.050 |  |
| 2026-10-27 10:03:07 | Hanwella (Kelani Ganga) | 6.36 | 🟢 Normal | -0.113 |  |
| 2026-10-27 10:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.015 |  |
| 2026-10-27 10:03:06 | Rathnapura (Kalu Ganga) | 8.49 | 🟠 Minor Flood | -0.068 |  |
| 2026-10-27 10:02:41 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-27 10:02:40 | Moragaswewa (Deduru Oya) | 5.25 | 🟡 Alert | 0.000 |  |
| 2026-10-27 10:02:31 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-27 10:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.40 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-10-27 10:02:28 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-27 10:02:21 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 10:02:04 | Magura (Kalu Ganga) | 5.27 | 🟡 Alert | -0.031 |  |
| 2026-10-27 10:01:50 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 10:01:42 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.040 |  |
| 2026-10-27 10:01:34 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-27 10:01:15 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-27 10:01:12 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-27 10:00:45 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 10:00:41 | Thanthirimale (Malwathu Oya) | 3.16 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-27 10:00:31 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 10:00:14 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.016 |  |
| 2026-10-27 10:00:11 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-27 09:51:12 | Moragaswewa (Deduru Oya) | 5.25 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 10:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.40 | 🟠 Minor Flood | 0.031 | 🔺 Rising |
| 2026-10-27 10:05:21 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-10-27 10:11:15 | Panadugama (Nilwala Ganga) | 6.40 | 🟠 Minor Flood | -0.027 |  |
| 2026-10-27 10:03:06 | Rathnapura (Kalu Ganga) | 8.49 | 🟠 Minor Flood | -0.068 |  |
| 2026-10-27 10:03:30 | Baddegama (Gin Ganga) | 3.96 | 🟡 Alert | 0.033 | 🔺 Rising |
| 2026-10-27 10:03:30 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-27 10:02:40 | Moragaswewa (Deduru Oya) | 5.25 | 🟡 Alert | 0.000 |  |
| 2026-10-27 10:08:50 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 10:02:04 | Magura (Kalu Ganga) | 5.27 | 🟡 Alert | -0.031 |  |
| 2026-10-27 10:05:26 | Badalgama (Maha Oya) | 5.30 | 🟡 Alert | -0.140 |  |
| 2026-10-27 10:08:27 | Thawalama (Gin Ganga) | 4.20 | 🟡 Alert | -0.218 |  |
| 2026-10-27 10:01:12 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-27 10:04:21 | Horowpothana (Yan Oya) | 3.02 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-27 10:02:41 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-27 10:00:41 | Thanthirimale (Malwathu Oya) | 3.16 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-10-27 10:04:17 | Ellagawa (Kalu Ganga) | 9.92 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-27 10:01:15 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-27 10:02:31 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-27 10:00:11 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-10-27 10:00:31 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 10:01:34 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-27 10:02:21 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 10:00:45 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 10:05:15 | Galgamuwa (Mee Oya) | 4.07 | 🟢 Normal | -0.009 |  |
| 2026-10-27 10:03:40 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.010 |  |
| 2026-10-27 10:04:10 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-27 10:02:28 | Norwood (Kelani Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-10-27 10:03:06 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.015 |  |
| 2026-10-27 10:00:14 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.016 |  |
| 2026-10-27 10:05:27 | Manampitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.019 |  |
| 2026-10-27 10:03:15 | Deraniyagala (Kelani Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-10-27 10:01:42 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.040 |  |
| 2026-10-27 10:06:21 | Peradeniya (Mahaweli Ganga) | 3.57 | 🟢 Normal | -0.046 |  |
| 2026-10-27 10:03:08 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.050 |  |
| 2026-10-27 10:10:49 | Pitabeddara (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.062 |  |
| 2026-10-27 10:03:07 | Hanwella (Kelani Ganga) | 6.36 | 🟢 Normal | -0.113 |  |
| 2026-10-27 10:08:51 | Giriulla (Maha Oya) | 3.80 | 🟢 Normal | -0.121 |  |
| 2026-10-27 10:06:14 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | -0.172 |  |
| 2026-10-27 10:03:49 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)