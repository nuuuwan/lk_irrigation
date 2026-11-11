# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_18:08:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,122 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Magura — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 18:08:01 | Deraniyagala (Kelani Ganga) | 3.16 | 🟢 Normal | 1.868 | 🔺 Rising |
| 2026-11-11 18:07:36 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.074 |  |
| 2026-11-11 18:06:37 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | -0.021 |  |
| 2026-11-11 18:06:28 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-11-11 18:06:25 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-11 18:05:44 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | -0.022 |  |
| 2026-11-11 18:05:16 | Thawalama (Gin Ganga) | 3.29 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-11-11 18:04:49 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.021 |  |
| 2026-11-11 18:04:48 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:04:31 | Moraketiya (Walawe Ganga) | 2.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-11 18:04:20 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | 0.654 | 🔺 Rising |
| 2026-11-11 18:04:19 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 18:03:27 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:03:23 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:03:12 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:03:10 | Padiyathalawa (Maduru Oya) | 1.01 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-11 18:03:10 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 18:02:53 | Rathnapura (Kalu Ganga) | 4.41 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-11-11 18:02:51 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 18:02:35 | Ellagawa (Kalu Ganga) | 8.41 | 🟢 Normal | -0.039 |  |
| 2026-11-11 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.49 | 🟡 Alert | -0.010 |  |
| 2026-11-11 18:02:14 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-11 18:02:14 | Glencourse (Kelani Ganga) | 11.88 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-11-11 18:02:00 | Magura (Kalu Ganga) | 4.36 | 🟡 Alert | 0.596 | 🔺 Rising |
| 2026-11-11 18:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:51 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-11 18:01:49 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.039 |  |
| 2026-11-11 18:01:48 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:37 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:01:13 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:00:53 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-11-11 18:00:49 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | -0.026 |  |
| 2026-11-11 18:00:43 | Moragaswewa (Deduru Oya) | 3.46 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-11 18:00:27 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 18:00:11 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:00:09 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 18:00:27 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 18:06:37 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | -0.021 |  |
| 2026-11-11 18:02:00 | Magura (Kalu Ganga) | 4.36 | 🟡 Alert | 0.596 | 🔺 Rising |
| 2026-11-11 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.49 | 🟡 Alert | -0.010 |  |
| 2026-11-11 18:05:44 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | -0.022 |  |
| 2026-11-11 18:00:49 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | -0.026 |  |
| 2026-11-11 18:08:01 | Deraniyagala (Kelani Ganga) | 3.16 | 🟢 Normal | 1.868 | 🔺 Rising |
| 2026-11-11 18:04:20 | Holombuwa (Kelani Ganga) | 2.16 | 🟢 Normal | 0.654 | 🔺 Rising |
| 2026-11-11 18:05:16 | Thawalama (Gin Ganga) | 3.29 | 🟢 Normal | 0.580 | 🔺 Rising |
| 2026-11-11 18:01:48 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-11-11 18:02:14 | Glencourse (Kelani Ganga) | 11.88 | 🟢 Normal | 0.328 | 🔺 Rising |
| 2026-11-11 18:02:53 | Rathnapura (Kalu Ganga) | 4.41 | 🟢 Normal | 0.237 | 🔺 Rising |
| 2026-11-11 18:06:28 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-11-11 18:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-11 18:06:25 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-11 18:00:43 | Moragaswewa (Deduru Oya) | 3.46 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-11-11 18:01:51 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-11 18:02:14 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-11 18:04:31 | Moraketiya (Walawe Ganga) | 2.45 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-11-11 18:02:51 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-11 18:03:10 | Padiyathalawa (Maduru Oya) | 1.01 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-11 18:04:19 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 18:03:10 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:03:23 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:13 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:37 | Putupaula (Kalu Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:03:12 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:03:27 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:00:11 | Wellawaya (Kirindi Oya) | 1.61 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:04:48 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:04:49 | Hanwella (Kelani Ganga) | 3.92 | 🟢 Normal | -0.021 |  |
| 2026-11-11 18:00:53 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.031 |  |
| 2026-11-11 18:01:49 | Manampitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.039 |  |
| 2026-11-11 18:02:35 | Ellagawa (Kalu Ganga) | 8.41 | 🟢 Normal | -0.039 |  |
| 2026-11-11 18:00:09 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | -0.043 |  |
| 2026-11-11 18:07:36 | Kithulgala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)