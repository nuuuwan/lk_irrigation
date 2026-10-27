# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_20:16:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,669 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 20:16:43 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -4.235 |  |
| 2026-10-27 20:16:26 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -4.235 |  |
| 2026-10-27 20:16:01 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:09:21 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-10-27 20:09:20 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -4.235 |  |
| 2026-10-27 20:08:18 | Glencourse (Kelani Ganga) | 12.08 | 🟢 Normal | -0.083 |  |
| 2026-10-27 20:07:22 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-27 20:07:15 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 20:06:33 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-10-27 20:06:23 | Putupaula (Kalu Ganga) | 3.42 | 🟡 Alert | 0.000 |  |
| 2026-10-27 20:06:12 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-10-27 20:05:27 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:04:40 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-10-27 20:04:32 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-27 20:04:32 | Badalgama (Maha Oya) | 4.14 | 🟢 Normal | -0.087 |  |
| 2026-10-27 20:04:21 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:04:15 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | 1.124 | 🔺 Rising |
| 2026-10-27 20:03:46 | Giriulla (Maha Oya) | 3.02 | 🟢 Normal | -0.060 |  |
| 2026-10-27 20:03:31 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:03:21 | Ellagawa (Kalu Ganga) | 10.20 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-10-27 20:03:05 | Dunamale (Aththanagalu Oya) | 4.72 | 🟠 Minor Flood | -0.030 |  |
| 2026-10-27 20:03:00 | Rathnapura (Kalu Ganga) | 7.61 | 🟠 Minor Flood | -0.094 |  |
| 2026-10-27 20:02:50 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.032 |  |
| 2026-10-27 20:02:45 | Moragaswewa (Deduru Oya) | 4.52 | 🟢 Normal | -0.090 |  |
| 2026-10-27 20:02:40 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | -0.040 |  |
| 2026-10-27 20:02:37 | Pitabeddara (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.68 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 20:02:28 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-10-27 20:02:08 | Hanwella (Kelani Ganga) | 5.15 | 🟢 Normal | -0.140 |  |
| 2026-10-27 20:02:06 | Horowpothana (Yan Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:02:00 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-27 20:01:56 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.013 |  |
| 2026-10-27 20:01:47 | Panadugama (Nilwala Ganga) | 6.12 | 🟠 Minor Flood | -0.032 |  |
| 2026-10-27 20:01:12 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:01:09 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:00:25 | Thawalama (Gin Ganga) | 2.85 | 🟢 Normal | -0.036 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 20:04:40 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.040 | 🔺 Rising |
| 2026-10-27 20:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.68 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 20:07:15 | Baddegama (Gin Ganga) | 4.14 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 20:03:05 | Dunamale (Aththanagalu Oya) | 4.72 | 🟠 Minor Flood | -0.030 |  |
| 2026-10-27 20:01:47 | Panadugama (Nilwala Ganga) | 6.12 | 🟠 Minor Flood | -0.032 |  |
| 2026-10-27 20:03:00 | Rathnapura (Kalu Ganga) | 7.61 | 🟠 Minor Flood | -0.094 |  |
| 2026-10-27 20:03:21 | Ellagawa (Kalu Ganga) | 10.20 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-10-27 20:06:23 | Putupaula (Kalu Ganga) | 3.42 | 🟡 Alert | 0.000 |  |
| 2026-10-27 20:02:40 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | -0.040 |  |
| 2026-10-27 20:04:15 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | 1.124 | 🔺 Rising |
| 2026-10-27 20:04:32 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-27 20:01:12 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:02:06 | Horowpothana (Yan Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:02:37 | Pitabeddara (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:16:01 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:04:21 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:01:09 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:02:28 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:03:31 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-10-27 20:05:27 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:23:14 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | -0.008 |  |
| 2026-10-27 20:09:21 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.009 |  |
| 2026-10-27 20:07:22 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-10-27 20:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-10-27 20:02:00 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-27 20:01:56 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | -0.013 |  |
| 2026-10-27 20:06:12 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-10-27 20:06:33 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-10-27 20:02:50 | Manampitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.032 |  |
| 2026-10-27 20:00:25 | Thawalama (Gin Ganga) | 2.85 | 🟢 Normal | -0.036 |  |
| 2026-10-27 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.059 |  |
| 2026-10-27 20:03:46 | Giriulla (Maha Oya) | 3.02 | 🟢 Normal | -0.060 |  |
| 2026-10-27 20:08:18 | Glencourse (Kelani Ganga) | 12.08 | 🟢 Normal | -0.083 |  |
| 2026-10-27 20:04:32 | Badalgama (Maha Oya) | 4.14 | 🟢 Normal | -0.087 |  |
| 2026-10-27 20:02:45 | Moragaswewa (Deduru Oya) | 4.52 | 🟢 Normal | -0.090 |  |
| 2026-10-27 18:00:41 | Thanthirimale (Malwathu Oya) | 2.72 | 🟢 Normal | -0.133 |  |
| 2026-10-27 20:02:08 | Hanwella (Kelani Ganga) | 5.15 | 🟢 Normal | -0.140 |  |
| 2026-10-27 19:01:57 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.151 |  |
| 2026-10-27 20:16:43 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -4.235 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)