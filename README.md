# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--13_20:21:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **314,996 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 20:21:12 | Moraketiya (Walawe Ganga) | 3.60 | 🟡 Alert | -0.082 |  |
| 2026-11-13 20:15:18 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | -0.008 |  |
| 2026-11-13 20:14:12 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.012 |  |
| 2026-11-13 20:09:11 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.028 |  |
| 2026-11-13 20:07:09 | Kuda Oya (Kirindi Oya) | 2.27 | 🟢 Normal | -0.009 |  |
| 2026-11-13 20:06:55 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-13 20:06:19 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.084 |  |
| 2026-11-13 20:06:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.78 | 🟡 Alert | -0.023 |  |
| 2026-11-13 20:06:01 | Putupaula (Kalu Ganga) | 2.23 | 🟢 Normal | -0.021 |  |
| 2026-11-13 20:05:59 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:05:56 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:05:53 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 20:05:51 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.010 |  |
| 2026-11-13 20:05:48 | Thanamalwila (Kirindi Oya) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-11-13 20:05:33 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.023 | 🔺 Rising |
| 2026-11-13 20:05:29 | Peradeniya (Mahaweli Ganga) | 3.66 | 🟢 Normal | -0.057 |  |
| 2026-11-13 20:05:01 | Ellagawa (Kalu Ganga) | 7.45 | 🟢 Normal | -0.060 |  |
| 2026-11-13 20:04:59 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.039 |  |
| 2026-11-13 20:04:30 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-11-13 20:04:29 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.038 |  |
| 2026-11-13 20:04:08 | Baddegama (Gin Ganga) | 4.01 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-13 20:03:44 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:03:14 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-11-13 20:03:12 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.051 |  |
| 2026-11-13 20:03:09 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.063 |  |
| 2026-11-13 20:03:09 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:03:03 | Manampitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.052 |  |
| 2026-11-13 20:02:59 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 20:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.005 |  |
| 2026-11-13 20:02:28 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:02:26 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.049 |  |
| 2026-11-13 20:02:09 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:01:21 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:00:16 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.021 |  |
| 2026-11-13 20:00:12 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-13 20:05:33 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.023 | 🔺 Rising |
| 2026-11-13 20:04:08 | Baddegama (Gin Ganga) | 4.01 | 🟠 Minor Flood | -0.020 |  |
| 2026-11-13 20:03:12 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.051 |  |
| 2026-11-13 20:06:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.78 | 🟡 Alert | -0.023 |  |
| 2026-11-13 20:21:12 | Moraketiya (Walawe Ganga) | 3.60 | 🟡 Alert | -0.082 |  |
| 2026-11-13 18:01:48 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-13 20:05:53 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 20:02:59 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-13 20:06:55 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-13 20:00:12 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:02:09 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:05:56 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:02:28 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 18:04:50 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:03:44 | Padiyathalawa (Maduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:05:59 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:01:21 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-11-13 20:02:55 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.005 |  |
| 2026-11-13 20:15:18 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | -0.008 |  |
| 2026-11-13 20:07:09 | Kuda Oya (Kirindi Oya) | 2.27 | 🟢 Normal | -0.009 |  |
| 2026-11-13 20:03:14 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-11-13 20:05:51 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.010 |  |
| 2026-11-13 20:14:12 | Urawa (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.012 |  |
| 2026-11-13 20:05:48 | Thanamalwila (Kirindi Oya) | 1.98 | 🟢 Normal | -0.019 |  |
| 2026-11-13 20:04:30 | Deraniyagala (Kelani Ganga) | 0.89 | 🟢 Normal | -0.019 |  |
| 2026-11-13 20:00:16 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.021 |  |
| 2026-11-13 20:06:01 | Putupaula (Kalu Ganga) | 2.23 | 🟢 Normal | -0.021 |  |
| 2026-11-13 20:09:11 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | -0.028 |  |
| 2026-11-13 18:04:09 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.029 |  |
| 2026-11-13 20:04:29 | Thawalama (Gin Ganga) | 2.40 | 🟢 Normal | -0.038 |  |
| 2026-11-13 20:04:59 | Hanwella (Kelani Ganga) | 3.30 | 🟢 Normal | -0.039 |  |
| 2026-11-13 19:01:42 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.042 |  |
| 2026-11-13 20:02:26 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.049 |  |
| 2026-11-13 20:03:03 | Manampitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.052 |  |
| 2026-11-13 20:05:29 | Peradeniya (Mahaweli Ganga) | 3.66 | 🟢 Normal | -0.057 |  |
| 2026-11-13 20:05:01 | Ellagawa (Kalu Ganga) | 7.45 | 🟢 Normal | -0.060 |  |
| 2026-11-13 19:02:04 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.060 |  |
| 2026-11-13 20:03:09 | Rathnapura (Kalu Ganga) | 3.04 | 🟢 Normal | -0.063 |  |
| 2026-11-13 20:06:19 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.084 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)