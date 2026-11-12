# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_13:02:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,804 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Dunamale — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 13:02:54 | Hanwella (Kelani Ganga) | 5.37 | 🟢 Normal | -0.090 |  |
| 2026-11-12 13:02:51 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.061 |  |
| 2026-11-12 13:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | -0.010 |  |
| 2026-11-12 13:02:46 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-11-12 13:02:33 | Kuda Oya (Kirindi Oya) | 2.47 | 🟢 Normal | -0.135 |  |
| 2026-11-12 13:02:21 | Nagalagam Street (Kelani Ganga) | 0.90 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-12 13:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-12 13:02:14 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | -0.041 |  |
| 2026-11-12 13:02:13 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-11-12 13:02:10 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.062 |  |
| 2026-11-12 13:01:59 | Magura (Kalu Ganga) | 5.22 | 🟡 Alert | -0.097 |  |
| 2026-11-12 13:01:56 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-11-12 13:01:36 | Giriulla (Maha Oya) | 2.78 | 🟢 Normal | -0.071 |  |
| 2026-11-12 13:01:14 | Moragaswewa (Deduru Oya) | 3.16 | 🟢 Normal | -0.070 |  |
| 2026-11-12 13:01:11 | Dunamale (Aththanagalu Oya) | 4.22 | 🟡 Alert | -0.022 |  |
| 2026-11-12 13:01:02 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-12 13:00:53 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-12 13:00:16 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | -0.147 |  |
| 2026-11-12 12:18:35 | Rathnapura (Kalu Ganga) | 5.12 | 🟢 Normal | -0.088 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 12:00:51 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 12:03:12 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | -0.011 |  |
| 2026-11-12 13:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | -0.010 |  |
| 2026-11-12 12:02:19 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.020 |  |
| 2026-11-12 13:01:11 | Dunamale (Aththanagalu Oya) | 4.22 | 🟡 Alert | -0.022 |  |
| 2026-11-12 12:04:51 | Moraketiya (Walawe Ganga) | 3.85 | 🟡 Alert | -0.047 |  |
| 2026-11-12 13:01:59 | Magura (Kalu Ganga) | 5.22 | 🟡 Alert | -0.097 |  |
| 2026-11-12 12:01:28 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-11-12 13:02:21 | Nagalagam Street (Kelani Ganga) | 0.90 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-12 12:07:15 | Galgamuwa (Mee Oya) | 0.75 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-12 12:03:02 | Ellagawa (Kalu Ganga) | 8.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-12 13:00:53 | Horowpothana (Yan Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-11-12 13:01:02 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-12 13:01:56 | Wellawaya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-11-12 12:02:45 | Deraniyagala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-12 12:01:12 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-12 13:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-11-12 13:02:46 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-11-12 13:02:13 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-11-12 12:02:44 | Putupaula (Kalu Ganga) | 2.52 | 🟢 Normal | -0.021 |  |
| 2026-11-12 12:07:13 | Thaldena (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.024 |  |
| 2026-11-12 12:04:55 | Katharagama (Menik Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-11-12 12:08:11 | Holombuwa (Kelani Ganga) | 1.67 | 🟢 Normal | -0.038 |  |
| 2026-11-12 13:02:14 | Nakkala (Kumbukkan Oya) | 1.53 | 🟢 Normal | -0.041 |  |
| 2026-11-12 12:04:36 | Urawa (Nilwala Ganga) | 1.68 | 🟢 Normal | -0.044 |  |
| 2026-11-12 12:01:28 | Peradeniya (Mahaweli Ganga) | 4.80 | 🟢 Normal | -0.056 |  |
| 2026-11-12 13:02:51 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.061 |  |
| 2026-11-12 13:02:10 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | -0.062 |  |
| 2026-11-12 13:01:14 | Moragaswewa (Deduru Oya) | 3.16 | 🟢 Normal | -0.070 |  |
| 2026-11-12 13:01:36 | Giriulla (Maha Oya) | 2.78 | 🟢 Normal | -0.071 |  |
| 2026-11-12 12:06:23 | Badalgama (Maha Oya) | 4.31 | 🟢 Normal | -0.071 |  |
| 2026-11-12 12:04:32 | Thanamalwila (Kirindi Oya) | 2.41 | 🟢 Normal | -0.072 |  |
| 2026-11-12 12:06:35 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.083 |  |
| 2026-11-12 12:18:35 | Rathnapura (Kalu Ganga) | 5.12 | 🟢 Normal | -0.088 |  |
| 2026-11-12 13:02:54 | Hanwella (Kelani Ganga) | 5.37 | 🟢 Normal | -0.090 |  |
| 2026-11-12 13:02:33 | Kuda Oya (Kirindi Oya) | 2.47 | 🟢 Normal | -0.135 |  |
| 2026-11-12 13:00:16 | Weraganthota (Mahaweli Ganga) | -2.01 | 🟢 Normal | -0.147 |  |
| 2026-11-12 12:03:56 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.187 |  |
| 2026-11-12 12:03:14 | Glencourse (Kelani Ganga) | 12.85 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)