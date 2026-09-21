# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_18:07:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,171 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **0** measurements in the last **1 hour**.*

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 18:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.06 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-09-21 18:03:17 | Baddegama (Gin Ganga) | 4.06 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-09-21 18:02:50 | Rathnapura (Kalu Ganga) | 5.51 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-09-21 18:00:15 | Thalgahagoda (Nilwala Ganga) | 1.54 | 🟡 Alert | 0.000 |  |
| 2026-09-21 18:02:18 | Panadugama (Nilwala Ganga) | 5.48 | 🟡 Alert | -0.032 |  |
| 2026-09-21 17:59:05 | Magura (Kalu Ganga) | 5.28 | 🟡 Alert | -0.056 |  |
| 2026-09-21 18:04:03 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-09-21 18:05:13 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-09-21 18:00:29 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-21 18:03:36 | Thawalama (Gin Ganga) | 2.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-21 18:02:25 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-21 18:00:09 | Putupaula (Kalu Ganga) | 2.75 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-21 18:00:14 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-21 18:02:28 | Deraniyagala (Kelani Ganga) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 18:03:08 | Glencourse (Kelani Ganga) | 12.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 18:04:53 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-09-21 18:02:11 | Ellagawa (Kalu Ganga) | 9.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-21 18:01:34 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:48 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:02:21 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:02:27 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:07:06 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:06 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:00:29 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:02:55 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:03:25 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-09-21 18:07:34 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-09-21 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:04:00 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:01:28 | Peradeniya (Mahaweli Ganga) | 3.65 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:00:14 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.032 |  |
| 2026-09-21 18:06:22 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.048 |  |
| 2026-09-21 18:02:27 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | -0.062 |  |
| 2026-09-21 18:05:10 | Badalgama (Maha Oya) | 3.12 | 🟢 Normal | -0.064 |  |
| 2026-09-21 18:03:27 | Hanwella (Kelani Ganga) | 5.48 | 🟢 Normal | -0.098 |  |
| 2026-09-21 18:02:09 | Nawalapitiya (Mahaweli Ganga) | 2.55 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)