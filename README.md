# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--02_12:11:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,847 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 12:11:50 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-10-02 12:11:42 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-10-02 12:08:05 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-10-02 12:07:25 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:06:49 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.180 |  |
| 2026-10-02 12:05:51 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:05:51 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.050 |  |
| 2026-10-02 12:05:48 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:05:20 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 1.114 | 🔺 Rising |
| 2026-10-02 12:05:12 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.059 |  |
| 2026-10-02 12:04:47 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:04:07 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:03:49 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-02 12:03:39 | Thaldena (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.048 |  |
| 2026-10-02 12:03:32 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-02 12:03:24 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.031 |  |
| 2026-10-02 12:03:12 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:03:10 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.098 |  |
| 2026-10-02 12:03:10 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:03:10 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.031 |  |
| 2026-10-02 12:03:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-02 12:02:57 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 12:02:52 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-02 12:02:49 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.129 |  |
| 2026-10-02 12:02:47 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-10-02 12:02:38 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.059 |  |
| 2026-10-02 12:02:21 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:01:55 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:01:48 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.210 |  |
| 2026-10-02 12:01:48 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:01:44 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.060 |  |
| 2026-10-02 12:01:26 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:01:17 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:00:33 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:00:28 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:00:14 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.030 |  |
| 2026-10-02 12:00:10 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-02 12:05:20 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 1.114 | 🔺 Rising |
| 2026-10-02 12:11:42 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.256 | 🔺 Rising |
| 2026-10-02 12:03:49 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-02 12:02:57 | Giriulla (Maha Oya) | 1.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-02 12:03:08 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-02 12:01:17 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:01:48 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:04:47 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:00:47 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:01:26 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:00:33 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:03:12 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:04:07 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:00:10 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:05:51 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:03:10 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:05:48 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:01:55 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:00:28 | Thanthirimale (Malwathu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:02:21 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:07:25 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | 0.000 |  |
| 2026-10-02 12:03:32 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-02 12:11:50 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.011 |  |
| 2026-10-02 12:08:05 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-10-02 12:02:47 | Putupaula (Kalu Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-10-02 12:02:52 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-02 12:00:14 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.030 |  |
| 2026-10-02 12:03:24 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.031 |  |
| 2026-10-02 12:03:10 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.031 |  |
| 2026-10-02 12:03:39 | Thaldena (Mahaweli Ganga) | 0.04 | 🟢 Normal | -0.048 |  |
| 2026-10-02 12:05:51 | Rathnapura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.050 |  |
| 2026-10-02 12:05:12 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.059 |  |
| 2026-10-02 12:02:38 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.059 |  |
| 2026-10-02 12:01:44 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.060 |  |
| 2026-10-02 12:03:10 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.098 |  |
| 2026-10-02 12:02:49 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.129 |  |
| 2026-10-02 12:06:49 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | -0.180 |  |
| 2026-10-02 12:01:48 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)