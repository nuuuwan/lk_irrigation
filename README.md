# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_04:03:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,358 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 04:03:12 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.049 |  |
| 2026-11-13 04:03:00 | Kuda Oya (Kirindi Oya) | 2.82 | 🟢 Normal | -0.029 |  |
| 2026-11-13 04:02:57 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | -0.091 |  |
| 2026-11-13 04:02:56 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-13 04:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-11-13 04:02:09 | Thanamalwila (Kirindi Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-11-13 04:02:08 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.023 |  |
| 2026-11-13 04:02:06 | Moraketiya (Walawe Ganga) | 3.14 | 🟡 Alert | 0.000 |  |
| 2026-11-13 04:01:49 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | -0.042 |  |
| 2026-11-13 04:01:21 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.040 |  |
| 2026-11-13 04:00:54 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 04:00:34 | Glencourse (Kelani Ganga) | 11.64 | 🟢 Normal | -0.010 |  |
| 2026-11-13 04:00:18 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | -0.054 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 03:14:45 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | 36.000 | 🔺 Rising |
| 2026-11-13 04:00:54 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-13 03:05:19 | Panadugama (Nilwala Ganga) | 6.41 | 🟠 Minor Flood | -0.016 |  |
| 2026-11-13 04:02:06 | Moraketiya (Walawe Ganga) | 3.14 | 🟡 Alert | 0.000 |  |
| 2026-11-13 03:04:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.18 | 🟡 Alert | -0.019 |  |
| 2026-11-13 03:06:33 | Dunamale (Aththanagalu Oya) | 3.60 | 🟡 Alert | -0.058 |  |
| 2026-11-13 03:08:54 | Magura (Kalu Ganga) | 4.35 | 🟡 Alert | -216.000 |  |
| 2026-11-12 18:00:35 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-13 03:06:31 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-12 18:01:04 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 03:07:10 | Badalgama (Maha Oya) | 3.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-13 03:21:22 | Thawalama (Gin Ganga) | 3.37 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-13 04:02:56 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-11-13 03:01:28 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-13 03:01:49 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:06:48 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-11-13 03:08:39 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-11-13 03:04:22 | Putupaula (Kalu Ganga) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-11-13 04:02:09 | Thanamalwila (Kirindi Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-11-13 04:00:34 | Glencourse (Kelani Ganga) | 11.64 | 🟢 Normal | -0.010 |  |
| 2026-11-13 03:06:58 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | -0.019 |  |
| 2026-11-13 03:05:35 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-11-13 03:11:25 | Ellagawa (Kalu Ganga) | 8.22 | 🟢 Normal | -0.020 |  |
| 2026-11-13 04:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-11-13 04:02:08 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.023 |  |
| 2026-11-13 04:03:00 | Kuda Oya (Kirindi Oya) | 2.82 | 🟢 Normal | -0.029 |  |
| 2026-11-13 04:01:21 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.040 |  |
| 2026-11-13 04:01:49 | Giriulla (Maha Oya) | 2.33 | 🟢 Normal | -0.042 |  |
| 2026-11-13 04:03:12 | Siyambalanduwa (Heda Oya) | 0.92 | 🟢 Normal | -0.049 |  |
| 2026-11-13 04:00:18 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | -0.054 |  |
| 2026-11-13 02:32:15 | Rathnapura (Kalu Ganga) | 4.48 | 🟢 Normal | -0.067 |  |
| 2026-11-13 03:02:18 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.071 |  |
| 2026-11-13 04:02:57 | Hanwella (Kelani Ganga) | 4.05 | 🟢 Normal | -0.091 |  |
| 2026-11-13 03:02:38 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.103 |  |
| 2026-11-13 03:04:27 | Thaldena (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.117 |  |
| 2026-11-13 03:05:51 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.126 |  |
| 2026-11-13 03:02:49 | Wellawaya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.145 |  |
| 2026-11-13 02:08:23 | Urawa (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.263 |  |
| 2026-11-13 03:01:25 | Pitabeddara (Nilwala Ganga) | 2.72 | 🟢 Normal | -288.000 |  |

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)