# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_18:18:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,488 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Norwood — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 18:18:01 | Panadugama (Nilwala Ganga) | 5.70 | 🟡 Alert | -0.031 |  |
| 2026-10-18 18:08:58 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:06:34 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:05:45 | Moragaswewa (Deduru Oya) | 2.72 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-18 18:05:07 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:05:01 | Deraniyagala (Kelani Ganga) | 2.54 | 🟢 Normal | 0.952 | 🔺 Rising |
| 2026-10-18 18:04:43 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-18 18:04:17 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | -0.047 |  |
| 2026-10-18 18:04:00 | Ellagawa (Kalu Ganga) | 7.55 | 🟢 Normal | -0.051 |  |
| 2026-10-18 18:03:53 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-18 18:03:49 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:03:47 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-10-18 18:03:47 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.029 |  |
| 2026-10-18 18:03:42 | Baddegama (Gin Ganga) | 3.12 | 🟢 Normal | -0.021 |  |
| 2026-10-18 18:03:21 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-18 18:03:06 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.020 |  |
| 2026-10-18 18:03:01 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 18:03:00 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:02:54 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-18 18:02:45 | Norwood (Kelani Ganga) | 1.67 | 🟡 Alert | 0.065 | 🔺 Rising |
| 2026-10-18 18:02:31 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:02:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.057 |  |
| 2026-10-18 18:02:21 | Putupaula (Kalu Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-10-18 18:02:18 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-10-18 18:02:14 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | -0.082 |  |
| 2026-10-18 18:02:13 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 18:02:08 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.020 |  |
| 2026-10-18 18:01:52 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:01:43 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-18 18:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-10-18 18:01:21 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-18 18:01:17 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-18 18:01:17 | Rathnapura (Kalu Ganga) | 3.33 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-18 18:00:52 | Horowpothana (Yan Oya) | 2.87 | 🟢 Normal | -0.080 |  |
| 2026-10-18 18:00:47 | Pitabeddara (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 18:03:01 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 18:02:45 | Norwood (Kelani Ganga) | 1.67 | 🟡 Alert | 0.065 | 🔺 Rising |
| 2026-10-18 18:18:01 | Panadugama (Nilwala Ganga) | 5.70 | 🟡 Alert | -0.031 |  |
| 2026-10-18 18:05:01 | Deraniyagala (Kelani Ganga) | 2.54 | 🟢 Normal | 0.952 | 🔺 Rising |
| 2026-10-18 18:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-10-18 18:00:47 | Pitabeddara (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-18 18:05:45 | Moragaswewa (Deduru Oya) | 2.72 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-18 18:03:53 | Urawa (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-18 18:03:21 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-10-18 18:01:43 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-18 18:01:17 | Rathnapura (Kalu Ganga) | 3.33 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-18 18:01:21 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-18 18:02:54 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-18 18:02:13 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 18:01:17 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-18 18:04:43 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-18 18:03:00 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:03:49 | Magura (Kalu Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:06:34 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:05:07 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:02:31 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:02:26 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:08:58 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:01:52 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-18 18:05:26 | Galgamuwa (Mee Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-18 18:03:47 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-10-18 18:02:21 | Putupaula (Kalu Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-10-18 18:03:06 | Dunamale (Aththanagalu Oya) | 2.22 | 🟢 Normal | -0.020 |  |
| 2026-10-18 18:02:08 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.020 |  |
| 2026-10-18 18:03:42 | Baddegama (Gin Ganga) | 3.12 | 🟢 Normal | -0.021 |  |
| 2026-10-18 18:03:47 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | -0.029 |  |
| 2026-10-18 18:01:11 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-10-18 18:02:18 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.031 |  |
| 2026-10-18 18:04:17 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | -0.047 |  |
| 2026-10-18 18:00:10 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.050 |  |
| 2026-10-18 18:04:00 | Ellagawa (Kalu Ganga) | 7.55 | 🟢 Normal | -0.051 |  |
| 2026-10-18 18:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.057 |  |
| 2026-10-18 18:00:52 | Horowpothana (Yan Oya) | 2.87 | 🟢 Normal | -0.080 |  |
| 2026-10-18 18:02:14 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)