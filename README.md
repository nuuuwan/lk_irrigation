# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_04:31:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,242 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Norwood — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 04:31:34 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:25:52 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-25 04:14:55 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:11:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.83 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-25 04:11:43 | Deraniyagala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.088 |  |
| 2026-09-25 04:11:37 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-09-25 04:09:41 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 04:08:39 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-25 04:08:08 | Panadugama (Nilwala Ganga) | 6.59 | 🟠 Minor Flood | -0.024 |  |
| 2026-09-25 04:07:05 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-25 04:06:45 | Thawalama (Gin Ganga) | 4.28 | 🟡 Alert | -0.021 |  |
| 2026-09-25 04:06:40 | Baddegama (Gin Ganga) | 4.62 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 04:06:00 | Urawa (Nilwala Ganga) | 1.53 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-25 04:05:42 | Rathnapura (Kalu Ganga) | 6.43 | 🟡 Alert | 0.000 |  |
| 2026-09-25 04:04:38 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:04:19 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:04:12 | Norwood (Kelani Ganga) | 1.75 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-09-25 04:03:50 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.020 |  |
| 2026-09-25 04:03:45 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 04:03:33 | Nawalapitiya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-25 04:03:14 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 04:03:01 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-25 04:02:39 | Peradeniya (Mahaweli Ganga) | 4.55 | 🟢 Normal | -0.303 |  |
| 2026-09-25 04:02:33 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:02:08 | Hanwella (Kelani Ganga) | 6.27 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-25 04:01:46 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:29 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:27 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:16 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:00:43 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:00:39 | Magura (Kalu Ganga) | 4.96 | 🟡 Alert | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 04:06:40 | Baddegama (Gin Ganga) | 4.62 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 04:11:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.83 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-09-25 04:03:14 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 04:08:08 | Panadugama (Nilwala Ganga) | 6.59 | 🟠 Minor Flood | -0.024 |  |
| 2026-09-25 04:04:12 | Norwood (Kelani Ganga) | 1.75 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-09-25 04:05:42 | Rathnapura (Kalu Ganga) | 6.43 | 🟡 Alert | 0.000 |  |
| 2026-09-25 04:00:39 | Magura (Kalu Ganga) | 4.96 | 🟡 Alert | -0.021 |  |
| 2026-09-25 04:06:45 | Thawalama (Gin Ganga) | 4.28 | 🟡 Alert | -0.021 |  |
| 2026-09-25 04:03:33 | Nawalapitiya (Mahaweli Ganga) | 3.05 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-25 04:06:00 | Urawa (Nilwala Ganga) | 1.53 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-25 04:02:08 | Hanwella (Kelani Ganga) | 6.27 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-25 04:07:05 | Kithulgala (Kelani Ganga) | 2.89 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-25 04:08:39 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-25 04:03:01 | Ellagawa (Kalu Ganga) | 8.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-25 04:03:45 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 04:09:41 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 04:25:52 | Putupaula (Kalu Ganga) | 2.71 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-24 18:00:46 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:14:55 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:31:34 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:00:43 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:27 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 03:05:35 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:02:59 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:29 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:46 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:02:33 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 03:05:32 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:04:19 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:04:38 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | 0.000 |  |
| 2026-09-24 18:04:50 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:01:16 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-25 04:11:37 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.019 |  |
| 2026-09-25 04:03:50 | Manampitiya (Mahaweli Ganga) | -0.34 | 🟢 Normal | -0.020 |  |
| 2026-09-25 03:02:25 | Dunamale (Aththanagalu Oya) | 3.22 | 🟢 Normal | -0.020 |  |
| 2026-09-25 03:07:12 | Glencourse (Kelani Ganga) | 14.74 | 🟢 Normal | -0.032 |  |
| 2026-09-25 03:17:04 | Pitabeddara (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.062 |  |
| 2026-09-25 04:11:43 | Deraniyagala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.088 |  |
| 2026-09-25 04:02:39 | Peradeniya (Mahaweli Ganga) | 4.55 | 🟢 Normal | -0.303 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)