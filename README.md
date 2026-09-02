# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_12:16:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,806 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 12:16:11 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:11:29 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.665 | 🔺 Rising |
| 2026-09-02 12:11:10 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:07:40 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-09-02 12:07:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-02 12:06:15 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-02 12:06:04 | Panadugama (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.665 | 🔺 Rising |
| 2026-09-02 12:05:34 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:05:11 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:05:00 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:48 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:47 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:41 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:40 | Galgamuwa (Mee Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:36 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:26 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-09-02 12:04:24 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:14 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 12:03:38 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:03:28 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:03:22 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -72.000 |  |
| 2026-09-02 12:03:21 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -72.000 |  |
| 2026-09-02 12:03:17 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:03:17 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-09-02 12:03:00 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | -0.010 |  |
| 2026-09-02 12:02:57 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:02:53 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:02:52 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:02:47 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-09-02 12:02:26 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:02:25 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 12:02:14 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:02:10 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.020 |  |
| 2026-09-02 12:01:57 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-02 12:01:47 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.034 |  |
| 2026-09-02 12:01:17 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:00:58 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:00:49 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-02 12:00:34 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-09-02 12:00:29 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 12:11:29 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.665 | 🔺 Rising |
| 2026-09-02 12:00:34 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-09-02 12:07:27 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-02 12:06:15 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-02 12:04:14 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 12:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 12:02:57 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:02:52 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:05:11 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:03:38 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:02:25 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:03:17 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:40 | Galgamuwa (Mee Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:03:28 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:02:53 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:00:29 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:41 | Glencourse (Kelani Ganga) | 9.44 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:02:14 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:05:34 | Siyambalanduwa (Heda Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:24 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:00:49 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:02:26 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:48 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:04:36 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:00:58 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:11:10 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:16:11 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:01:17 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:05:00 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 12:03:00 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | -0.010 |  |
| 2026-09-02 12:03:17 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-09-02 12:01:57 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-09-02 12:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-09-02 12:07:40 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-09-02 12:02:10 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.020 |  |
| 2026-09-02 12:04:26 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-09-02 12:02:47 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.030 |  |
| 2026-09-02 12:01:47 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.034 |  |
| 2026-09-02 12:03:22 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)