# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_21:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,118 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Norwood — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 21:03:15 | Thanamalwila (Kirindi Oya) | 2.68 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-12 21:03:09 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-12 21:03:03 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | 0.000 |  |
| 2026-11-12 21:03:00 | Siyambalanduwa (Heda Oya) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-11-12 21:02:55 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-11-12 21:02:52 | Moraketiya (Walawe Ganga) | 3.16 | 🟡 Alert | -0.042 |  |
| 2026-11-12 21:02:47 | Glencourse (Kelani Ganga) | 11.91 | 🟢 Normal | -0.081 |  |
| 2026-11-12 21:02:46 | Moragaswewa (Deduru Oya) | 2.18 | 🟢 Normal | -0.138 |  |
| 2026-11-12 21:02:42 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | -0.041 |  |
| 2026-11-12 21:02:38 | Wellawaya (Kirindi Oya) | 2.17 | 🟢 Normal | -0.060 |  |
| 2026-11-12 21:02:38 | Norwood (Kelani Ganga) | 1.69 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-11-12 21:02:36 | Thaldena (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.372 |  |
| 2026-11-12 21:02:36 | Nakkala (Kumbukkan Oya) | 2.39 | 🟢 Normal | -0.059 |  |
| 2026-11-12 21:02:25 | Putupaula (Kalu Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 21:02:21 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.040 |  |
| 2026-11-12 21:02:15 | Kuda Oya (Kirindi Oya) | 3.11 | 🟢 Normal | -0.041 |  |
| 2026-11-12 21:02:13 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-11-12 21:02:11 | Thawalama (Gin Ganga) | 3.21 | 🟢 Normal | -0.049 |  |
| 2026-11-12 21:02:05 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 21:02:04 | Peradeniya (Mahaweli Ganga) | 4.64 | 🟢 Normal | -0.051 |  |
| 2026-11-12 21:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-12 21:00:11 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-12 20:33:19 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 20:18:23 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | -0.041 |  |
| 2026-11-12 20:17:38 | Magura (Kalu Ganga) | 4.85 | 🟡 Alert | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 20:09:50 | Panadugama (Nilwala Ganga) | 6.38 | 🟠 Minor Flood | 0.080 | 🔺 Rising |
| 2026-11-12 21:02:05 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 20:33:19 | Thalgahagoda (Nilwala Ganga) | 1.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 21:02:38 | Norwood (Kelani Ganga) | 1.69 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-11-12 20:10:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.000 |  |
| 2026-11-12 20:17:38 | Magura (Kalu Ganga) | 4.85 | 🟡 Alert | -0.040 |  |
| 2026-11-12 21:02:42 | Dunamale (Aththanagalu Oya) | 3.95 | 🟡 Alert | -0.041 |  |
| 2026-11-12 21:02:52 | Moraketiya (Walawe Ganga) | 3.16 | 🟡 Alert | -0.042 |  |
| 2026-11-12 20:07:48 | Urawa (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.442 | 🔺 Rising |
| 2026-11-12 18:00:35 | Weraganthota (Mahaweli Ganga) | -1.97 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-12 21:00:11 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-12 21:03:15 | Thanamalwila (Kirindi Oya) | 2.68 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-12 18:01:04 | Thanthirimale (Malwathu Oya) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 21:03:09 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-12 20:00:11 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 21:03:03 | Ellagawa (Kalu Ganga) | 8.25 | 🟢 Normal | 0.000 |  |
| 2026-11-12 21:02:25 | Putupaula (Kalu Ganga) | 2.51 | 🟢 Normal | 0.000 |  |
| 2026-11-12 18:06:48 | Galgamuwa (Mee Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-11-12 21:02:55 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-11-12 21:01:58 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-12 20:04:46 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-11-12 21:02:13 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-11-12 20:02:16 | Katharagama (Menik Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-11-12 21:03:00 | Siyambalanduwa (Heda Oya) | 1.24 | 🟢 Normal | -0.030 |  |
| 2026-11-12 21:02:21 | Manampitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.040 |  |
| 2026-11-12 21:02:15 | Kuda Oya (Kirindi Oya) | 3.11 | 🟢 Normal | -0.041 |  |
| 2026-11-12 20:05:12 | Rathnapura (Kalu Ganga) | 4.90 | 🟢 Normal | -0.043 |  |
| 2026-11-12 21:02:11 | Thawalama (Gin Ganga) | 3.21 | 🟢 Normal | -0.049 |  |
| 2026-11-12 21:02:04 | Peradeniya (Mahaweli Ganga) | 4.64 | 🟢 Normal | -0.051 |  |
| 2026-11-12 20:02:27 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.054 |  |
| 2026-11-12 21:02:36 | Nakkala (Kumbukkan Oya) | 2.39 | 🟢 Normal | -0.059 |  |
| 2026-11-12 21:02:38 | Wellawaya (Kirindi Oya) | 2.17 | 🟢 Normal | -0.060 |  |
| 2026-11-12 20:07:22 | Badalgama (Maha Oya) | 3.83 | 🟢 Normal | -0.061 |  |
| 2026-11-12 21:02:47 | Glencourse (Kelani Ganga) | 11.91 | 🟢 Normal | -0.081 |  |
| 2026-11-12 20:03:52 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.090 |  |
| 2026-11-12 20:03:27 | Hanwella (Kelani Ganga) | 4.65 | 🟢 Normal | -0.099 |  |
| 2026-11-12 20:02:23 | Pitabeddara (Nilwala Ganga) | 3.36 | 🟢 Normal | -0.105 |  |
| 2026-11-12 21:02:46 | Moragaswewa (Deduru Oya) | 2.18 | 🟢 Normal | -0.138 |  |
| 2026-11-12 21:02:36 | Thaldena (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.372 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)