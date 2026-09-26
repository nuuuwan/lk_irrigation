# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_05:03:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,071 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 05:03:03 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-27 05:02:54 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.005 |  |
| 2026-09-27 05:02:43 | Dunamale (Aththanagalu Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-09-27 05:02:42 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.146 |  |
| 2026-09-27 05:02:41 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:02:41 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.059 |  |
| 2026-09-27 05:02:38 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:02:37 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.071 |  |
| 2026-09-27 05:02:21 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:01:47 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.074 |  |
| 2026-09-27 05:01:32 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:01:21 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-09-27 05:01:15 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | -0.030 |  |
| 2026-09-27 05:00:42 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:49:22 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.026 |  |
| 2026-09-27 04:32:17 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.059 |  |
| 2026-09-27 04:29:55 | Baddegama (Gin Ganga) | 4.76 | 🟠 Minor Flood | -0.007 |  |
| 2026-09-27 04:22:35 | Putupaula (Kalu Ganga) | 2.87 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 04:09:34 | Thalgahagoda (Nilwala Ganga) | 1.97 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 04:29:55 | Baddegama (Gin Ganga) | 4.76 | 🟠 Minor Flood | -0.007 |  |
| 2026-09-27 04:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.79 | 🟠 Minor Flood | -0.014 |  |
| 2026-09-27 04:06:05 | Panadugama (Nilwala Ganga) | 5.61 | 🟡 Alert | -0.031 |  |
| 2026-09-27 04:00:23 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 04:01:53 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-27 05:00:42 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:02:21 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:04:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:02:41 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:02:38 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-27 03:01:08 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:02:24 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-27 04:02:00 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:01:32 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-27 05:02:54 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.005 |  |
| 2026-09-27 04:22:35 | Putupaula (Kalu Ganga) | 2.87 | 🟢 Normal | -0.008 |  |
| 2026-09-27 04:07:42 | Urawa (Nilwala Ganga) | 0.93 | 🟢 Normal | -0.009 |  |
| 2026-09-27 05:03:03 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-27 04:03:25 | Thawalama (Gin Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-09-27 05:02:43 | Dunamale (Aththanagalu Oya) | 2.39 | 🟢 Normal | -0.010 |  |
| 2026-09-27 04:02:17 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.010 |  |
| 2026-09-27 05:01:21 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:02:21 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-27 03:00:54 | Manampitiya (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.020 |  |
| 2026-09-27 04:06:26 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | -0.022 |  |
| 2026-09-27 04:49:22 | Magura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.026 |  |
| 2026-09-27 05:01:15 | Ellagawa (Kalu Ganga) | 8.69 | 🟢 Normal | -0.030 |  |
| 2026-09-27 04:08:02 | Deraniyagala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.045 |  |
| 2026-09-27 05:02:41 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.059 |  |
| 2026-09-27 04:06:11 | Hanwella (Kelani Ganga) | 4.77 | 🟢 Normal | -0.067 |  |
| 2026-09-27 03:14:15 | Rathnapura (Kalu Ganga) | 4.20 | 🟢 Normal | -0.069 |  |
| 2026-09-27 05:02:37 | Pitabeddara (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.071 |  |
| 2026-09-27 05:01:47 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.074 |  |
| 2026-09-27 04:04:10 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.076 |  |
| 2026-09-27 04:03:26 | Peradeniya (Mahaweli Ganga) | 3.35 | 🟢 Normal | -0.080 |  |
| 2026-09-26 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |
| 2026-09-27 05:02:42 | Glencourse (Kelani Ganga) | 12.30 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)