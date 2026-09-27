# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--28_04:34:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,935 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 04:34:43 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | -112.500 |  |
| 2026-09-28 04:33:39 | Magura (Kalu Ganga) | 4.33 | 🟡 Alert | -112.500 |  |
| 2026-09-28 04:21:13 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.009 |  |
| 2026-09-28 04:14:57 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:08:42 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:07:25 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.020 |  |
| 2026-09-28 04:06:21 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.021 |  |
| 2026-09-28 04:05:37 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:04:38 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:04:16 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.019 |  |
| 2026-09-28 04:04:01 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-09-28 04:03:43 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-28 04:03:33 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:03:26 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:03:22 | Kithulgala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-28 04:03:12 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.020 |  |
| 2026-09-28 04:02:59 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | -0.010 |  |
| 2026-09-28 04:02:49 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:02:21 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:02:12 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-09-28 04:02:05 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-28 04:02:03 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:01:53 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:01:45 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-09-28 04:01:44 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:01:30 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:01:28 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | -0.061 |  |
| 2026-09-28 04:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:00:14 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-09-28 04:00:00 | Baddegama (Gin Ganga) | 4.35 | 🟠 Minor Flood | 0.006 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-28 04:00:00 | Baddegama (Gin Ganga) | 4.35 | 🟠 Minor Flood | 0.006 | 🔺 Rising |
| 2026-09-28 04:02:05 | Thalgahagoda (Nilwala Ganga) | 1.79 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-28 04:03:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.88 | 🟡 Alert | -0.020 |  |
| 2026-09-28 04:04:01 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-09-28 04:03:22 | Kithulgala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-09-28 04:03:43 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 18:01:18 | Weraganthota (Mahaweli Ganga) | -3.54 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:01:30 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:01:44 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:02:49 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:00:32 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:01:53 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:02:03 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:02:15 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:03:12 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:02:21 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:00:08 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:05:37 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:03:33 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:14:57 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:00:58 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:04:38 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-09-28 04:08:42 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-27 18:02:06 | Thanthirimale (Malwathu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:03:10 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-28 03:06:46 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.003 |  |
| 2026-09-28 04:21:13 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.009 |  |
| 2026-09-28 04:02:12 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-09-28 04:02:59 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | -0.010 |  |
| 2026-09-28 04:01:45 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.011 |  |
| 2026-09-28 04:04:16 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.019 |  |
| 2026-09-28 03:03:03 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-09-28 04:00:14 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-09-28 04:07:25 | Hanwella (Kelani Ganga) | 3.42 | 🟢 Normal | -0.020 |  |
| 2026-09-28 04:06:21 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.021 |  |
| 2026-09-28 03:05:27 | Panadugama (Nilwala Ganga) | 4.83 | 🟢 Normal | -0.038 |  |
| 2026-09-28 04:01:28 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | -0.061 |  |
| 2026-09-27 18:01:49 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | -36.000 |  |
| 2026-09-28 04:34:43 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | -112.500 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)