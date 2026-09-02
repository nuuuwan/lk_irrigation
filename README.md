# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_14:10:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,879 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 14:10:31 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:10:05 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.009 |  |
| 2026-09-02 14:06:15 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.010 |  |
| 2026-09-02 14:06:02 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:05:59 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:05:56 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-02 14:05:42 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:05:12 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:04:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-02 14:04:24 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -72.000 |  |
| 2026-09-02 14:04:23 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -72.000 |  |
| 2026-09-02 14:04:00 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:03:42 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 14:03:33 | Siyambalanduwa (Heda Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-09-02 14:03:30 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-02 14:03:07 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:02:59 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:02:41 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.020 |  |
| 2026-09-02 14:02:36 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:02:30 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:02:29 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:02:13 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:02:11 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:01:53 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:01:48 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-02 14:01:40 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:01:24 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:01:13 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:01:12 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:00:54 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:00:51 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:00:46 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:00:34 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:00:31 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 14:04:27 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-02 14:01:48 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-09-02 14:05:56 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-02 14:03:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 14:01:24 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:02:11 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:00:51 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:00:46 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:01:53 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:05:42 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:01:13 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:02:56 | Galgamuwa (Mee Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 13:04:53 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:02:36 | Pitabeddara (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:03:07 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:04:00 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:02:30 | Ellagawa (Kalu Ganga) | 4.55 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:02:29 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:03:42 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:06:02 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:00:34 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:02:13 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:05:12 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:05:59 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:02:59 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:10:31 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:01:12 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:01:40 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 14:10:05 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | -0.009 |  |
| 2026-09-02 13:13:56 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-09-02 14:03:30 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-09-02 14:06:15 | Glencourse (Kelani Ganga) | 9.43 | 🟢 Normal | -0.010 |  |
| 2026-09-02 14:03:33 | Siyambalanduwa (Heda Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-09-02 13:06:07 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-09-02 14:02:41 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.020 |  |
| 2026-09-02 14:00:31 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.030 |  |
| 2026-09-02 13:05:06 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.037 |  |
| 2026-09-02 14:04:24 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)