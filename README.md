# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_01:02:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,346 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Peradeniya — Alert; 🟡 Holombuwa — Alert; 🟡 Magura — Alert; 🟡 Norwood — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 01:02:52 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-11-12 01:02:44 | Thanamalwila (Kirindi Oya) | 3.10 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-12 01:02:37 | Glencourse (Kelani Ganga) | 13.67 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-11-12 01:02:24 | Thaldena (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.133 |  |
| 2026-11-12 01:02:16 | Wellawaya (Kirindi Oya) | 3.45 | 🟢 Normal | -0.155 |  |
| 2026-11-12 01:02:12 | Hanwella (Kelani Ganga) | 4.90 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-12 01:02:04 | Nakkala (Kumbukkan Oya) | 3.10 | 🟢 Normal | -0.379 |  |
| 2026-11-12 01:02:03 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-12 01:01:24 | Ellagawa (Kalu Ganga) | 8.37 | 🟢 Normal | 0.000 |  |
| 2026-11-12 01:00:57 | Kuda Oya (Kirindi Oya) | 2.07 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 00:07:28 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.018 | 🔺 Rising |
| 2026-11-12 00:15:17 | Baddegama (Gin Ganga) | 4.05 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 00:03:32 | Peradeniya (Mahaweli Ganga) | 5.04 | 🟡 Alert | 0.198 | 🔺 Rising |
| 2026-11-12 00:08:26 | Holombuwa (Kelani Ganga) | 3.39 | 🟡 Alert | 0.085 | 🔺 Rising |
| 2026-11-12 00:01:59 | Magura (Kalu Ganga) | 5.23 | 🟡 Alert | 0.081 | 🔺 Rising |
| 2026-11-12 00:05:31 | Norwood (Kelani Ganga) | 1.52 | 🟡 Alert | 0.071 | 🔺 Rising |
| 2026-11-12 00:03:07 | Thawalama (Gin Ganga) | 5.17 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-11-12 00:08:41 | Urawa (Nilwala Ganga) | 3.19 | 🟡 Alert | 0.066 | 🔺 Rising |
| 2026-11-12 00:04:12 | Panadugama (Nilwala Ganga) | 5.52 | 🟡 Alert | 0.062 | 🔺 Rising |
| 2026-11-12 01:02:52 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-11-12 00:12:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | 0.000 |  |
| 2026-11-12 00:13:00 | Moraketiya (Walawe Ganga) | 4.10 | 🟡 Alert | -0.042 |  |
| 2026-11-12 00:01:31 | Siyambalanduwa (Heda Oya) | 2.20 | 🟢 Normal | 1.085 | 🔺 Rising |
| 2026-11-12 00:01:38 | Giriulla (Maha Oya) | 2.91 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-11-12 01:02:44 | Thanamalwila (Kirindi Oya) | 3.10 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-12 01:02:37 | Glencourse (Kelani Ganga) | 13.67 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-11-12 00:12:24 | Nawalapitiya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-12 01:02:12 | Hanwella (Kelani Ganga) | 4.90 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-12 00:11:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-12 00:03:50 | Katharagama (Menik Ganga) | 1.10 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-11 23:30:47 | Pitabeddara (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-12 00:05:12 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-12 00:05:42 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-12 01:02:03 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-12 00:02:52 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 00:07:48 | Badalgama (Maha Oya) | 3.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-12 01:01:24 | Ellagawa (Kalu Ganga) | 8.37 | 🟢 Normal | 0.000 |  |
| 2026-11-12 00:06:25 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-11-12 00:06:10 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-12 00:02:59 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-12 01:00:57 | Kuda Oya (Kirindi Oya) | 2.07 | 🟢 Normal | -0.015 |  |
| 2026-11-12 01:02:24 | Thaldena (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.133 |  |
| 2026-11-12 01:02:16 | Wellawaya (Kirindi Oya) | 3.45 | 🟢 Normal | -0.155 |  |
| 2026-11-12 00:02:02 | Padiyathalawa (Maduru Oya) | 3.60 | 🟢 Normal | -0.225 |  |
| 2026-11-12 00:02:10 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.256 |  |
| 2026-11-12 01:02:04 | Nakkala (Kumbukkan Oya) | 3.10 | 🟢 Normal | -0.379 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)