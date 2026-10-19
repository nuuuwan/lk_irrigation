# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_06:39:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,918 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 06:39:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | -0.004 |  |
| 2026-10-19 06:39:01 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:26:45 | Panadugama (Nilwala Ganga) | 5.55 | 🟡 Alert | -0.035 |  |
| 2026-10-19 06:11:42 | Pitabeddara (Nilwala Ganga) | 2.14 | 🟢 Normal | -72.000 |  |
| 2026-10-19 06:11:41 | Pitabeddara (Nilwala Ganga) | 2.16 | 🟢 Normal | -72.000 |  |
| 2026-10-19 06:09:43 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.057 |  |
| 2026-10-19 06:07:39 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:07:21 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-19 06:07:06 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | -0.110 |  |
| 2026-10-19 06:05:58 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.024 |  |
| 2026-10-19 06:05:41 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:05:12 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | -0.034 |  |
| 2026-10-19 06:05:12 | Baddegama (Gin Ganga) | 2.73 | 🟢 Normal | -0.055 |  |
| 2026-10-19 06:05:02 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-19 06:04:46 | Moragaswewa (Deduru Oya) | 2.00 | 🟢 Normal | -0.198 |  |
| 2026-10-19 06:04:44 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.024 |  |
| 2026-10-19 06:04:34 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.077 |  |
| 2026-10-19 06:04:06 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:03:54 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.019 |  |
| 2026-10-19 06:03:47 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-19 06:03:35 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.884 |  |
| 2026-10-19 06:03:15 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.130 |  |
| 2026-10-19 06:03:05 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:03:01 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.021 |  |
| 2026-10-19 06:02:58 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | -0.019 |  |
| 2026-10-19 06:02:57 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-10-19 06:02:52 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:02:51 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-19 06:02:35 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.048 |  |
| 2026-10-19 06:02:18 | Moraketiya (Walawe Ganga) | 1.34 | 🟢 Normal | -0.061 |  |
| 2026-10-19 06:02:14 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.080 |  |
| 2026-10-19 06:02:09 | Putupaula (Kalu Ganga) | 1.58 | 🟢 Normal | -0.072 |  |
| 2026-10-19 06:01:58 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:01:57 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.040 |  |
| 2026-10-19 06:01:54 | Hanwella (Kelani Ganga) | 3.69 | 🟢 Normal | -0.100 |  |
| 2026-10-19 06:01:44 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:01:37 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | -2.010 |  |
| 2026-10-19 06:01:27 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-10-19 06:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:00:34 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 06:05:12 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | -0.034 |  |
| 2026-10-19 06:26:45 | Panadugama (Nilwala Ganga) | 5.55 | 🟡 Alert | -0.035 |  |
| 2026-10-19 06:02:51 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-19 06:05:02 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-19 06:03:47 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-19 06:01:37 | Wellawaya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:01:58 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:00:52 | Nawalapitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:01:44 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:02:52 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:03:05 | Dunamale (Aththanagalu Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:04:06 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:07:39 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:39:01 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-19 06:39:13 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | -0.004 |  |
| 2026-10-19 06:07:21 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-10-19 06:02:57 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-10-19 06:01:27 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-10-19 06:02:58 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | -0.019 |  |
| 2026-10-19 06:03:54 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.019 |  |
| 2026-10-19 06:03:01 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.021 |  |
| 2026-10-19 06:05:58 | Kuda Oya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.024 |  |
| 2026-10-19 06:04:44 | Holombuwa (Kelani Ganga) | 0.97 | 🟢 Normal | -0.024 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-19 06:01:57 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.040 |  |
| 2026-10-19 06:02:35 | Magura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.048 |  |
| 2026-10-19 06:05:12 | Baddegama (Gin Ganga) | 2.73 | 🟢 Normal | -0.055 |  |
| 2026-10-19 06:09:43 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | -0.057 |  |
| 2026-10-19 06:02:18 | Moraketiya (Walawe Ganga) | 1.34 | 🟢 Normal | -0.061 |  |
| 2026-10-19 06:02:09 | Putupaula (Kalu Ganga) | 1.58 | 🟢 Normal | -0.072 |  |
| 2026-10-19 06:04:34 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | -0.077 |  |
| 2026-10-19 06:02:14 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.080 |  |
| 2026-10-19 06:01:54 | Hanwella (Kelani Ganga) | 3.69 | 🟢 Normal | -0.100 |  |
| 2026-10-19 06:07:06 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | -0.110 |  |
| 2026-10-19 06:03:15 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.130 |  |
| 2026-10-19 06:04:46 | Moragaswewa (Deduru Oya) | 2.00 | 🟢 Normal | -0.198 |  |
| 2026-10-19 06:03:35 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.884 |  |
| 2026-10-19 06:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.14 | 🟢 Normal | -2.010 |  |
| 2026-10-19 06:11:42 | Pitabeddara (Nilwala Ganga) | 2.14 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)