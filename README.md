# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_04:06:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **237,358 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 04:06:16 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:06:13 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.006 |  |
| 2026-08-19 04:05:25 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:05:14 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:05:02 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:05:00 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-19 04:03:39 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-19 04:03:25 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.050 |  |
| 2026-08-19 04:03:23 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-08-19 04:03:23 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-08-19 04:03:08 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-08-19 04:02:56 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:02:33 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:02:32 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:02:29 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-08-19 04:02:23 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:02:15 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:02:13 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:01:41 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-08-19 04:01:40 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-19 04:01:28 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:01:26 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:01:18 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 04:01:16 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:01:12 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.086 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 03:02:30 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-19 03:02:55 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-19 04:05:00 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-19 04:03:39 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-19 04:01:40 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-19 04:01:18 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 04:05:02 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-08-18 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:01:16 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:02:33 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:06:16 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:01:28 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:02:23 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-18 18:06:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:02:56 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-19 03:07:56 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:05:14 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 03:09:21 | Glencourse (Kelani Ganga) | 9.81 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:05:25 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:02:15 | Dunamale (Aththanagalu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-19 03:04:17 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-19 03:03:03 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-19 03:10:36 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-18 18:04:43 | Thanthirimale (Malwathu Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-19 02:06:48 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:02:13 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:01:26 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-19 04:06:13 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.006 |  |
| 2026-08-19 03:05:29 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-08-19 04:03:23 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-08-19 04:02:29 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-08-19 04:03:23 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-08-19 04:01:41 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-08-19 03:15:50 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-08-19 04:03:08 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-08-19 03:04:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -0.022 |  |
| 2026-08-19 04:03:25 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.050 |  |
| 2026-08-19 04:01:12 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.086 |  |
| 2026-08-19 03:05:06 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)