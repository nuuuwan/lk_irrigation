# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_00:03:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,315 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Holombuwa — Alert; 🟡 Peradeniya — Alert; 🟡 Urawa — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 00:03:32 | Peradeniya (Mahaweli Ganga) | 5.04 | 🟡 Alert | 0.198 | 🔺 Rising |
| 2026-11-12 00:03:07 | Thawalama (Gin Ganga) | 5.17 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-11-12 00:02:59 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-12 00:02:52 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 00:02:31 | Dunamale (Aththanagalu Oya) | 4.00 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-12 00:02:11 | Thanamalwila (Kirindi Oya) | 2.78 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-11-12 00:02:10 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.256 |  |
| 2026-11-12 00:02:05 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-11-12 00:02:02 | Padiyathalawa (Maduru Oya) | 3.60 | 🟢 Normal | -0.225 |  |
| 2026-11-12 00:01:59 | Magura (Kalu Ganga) | 5.23 | 🟡 Alert | 0.081 | 🔺 Rising |
| 2026-11-12 00:01:38 | Giriulla (Maha Oya) | 2.91 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-11-12 00:01:31 | Siyambalanduwa (Heda Oya) | 2.20 | 🟢 Normal | 1.085 | 🔺 Rising |
| 2026-11-12 00:00:14 | Wellawaya (Kirindi Oya) | 3.61 | 🟢 Normal | -0.030 |  |
| 2026-11-11 23:34:49 | Nawalapitiya (Mahaweli Ganga) | 2.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 23:30:47 | Pitabeddara (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-11 23:27:10 | Peradeniya (Mahaweli Ganga) | 4.92 | 🟢 Normal | 0.198 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 23:01:54 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 23:10:21 | Baddegama (Gin Ganga) | 4.05 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-11 23:04:53 | Holombuwa (Kelani Ganga) | 3.30 | 🟡 Alert | 0.418 | 🔺 Rising |
| 2026-11-12 00:03:32 | Peradeniya (Mahaweli Ganga) | 5.04 | 🟡 Alert | 0.198 | 🔺 Rising |
| 2026-11-11 23:05:02 | Urawa (Nilwala Ganga) | 3.12 | 🟡 Alert | 0.097 | 🔺 Rising |
| 2026-11-12 00:01:59 | Magura (Kalu Ganga) | 5.23 | 🟡 Alert | 0.081 | 🔺 Rising |
| 2026-11-12 00:03:07 | Thawalama (Gin Ganga) | 5.17 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-11-11 23:05:55 | Panadugama (Nilwala Ganga) | 5.46 | 🟡 Alert | 0.057 | 🔺 Rising |
| 2026-11-12 00:02:31 | Dunamale (Aththanagalu Oya) | 4.00 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-11 23:02:07 | Moraketiya (Walawe Ganga) | 4.15 | 🟡 Alert | 0.000 |  |
| 2026-11-11 23:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | -0.011 |  |
| 2026-11-12 00:01:31 | Siyambalanduwa (Heda Oya) | 2.20 | 🟢 Normal | 1.085 | 🔺 Rising |
| 2026-11-12 00:01:38 | Giriulla (Maha Oya) | 2.91 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-11-12 00:02:11 | Thanamalwila (Kirindi Oya) | 2.78 | 🟢 Normal | 0.324 | 🔺 Rising |
| 2026-11-12 00:02:05 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-11-11 23:02:13 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-11-11 23:05:57 | Nakkala (Kumbukkan Oya) | 3.80 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-11 23:30:47 | Pitabeddara (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-11 23:07:23 | Katharagama (Menik Ganga) | 1.03 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-11 23:06:29 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-11 23:34:49 | Nawalapitiya (Mahaweli Ganga) | 2.91 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 23:06:16 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 23:06:06 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-11 23:05:32 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-11 23:01:28 | Moragaswewa (Deduru Oya) | 3.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 00:02:52 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-11 23:04:02 | Putupaula (Kalu Ganga) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-11-11 23:02:24 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-12 00:02:59 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-11 23:01:46 | Ellagawa (Kalu Ganga) | 8.38 | 🟢 Normal | -0.010 |  |
| 2026-11-11 22:01:29 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.025 |  |
| 2026-11-11 23:04:37 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | -0.030 |  |
| 2026-11-12 00:00:14 | Wellawaya (Kirindi Oya) | 3.61 | 🟢 Normal | -0.030 |  |
| 2026-11-11 23:02:58 | Thaldena (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.101 |  |
| 2026-11-12 00:02:02 | Padiyathalawa (Maduru Oya) | 3.60 | 🟢 Normal | -0.225 |  |
| 2026-11-12 00:02:10 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.256 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)