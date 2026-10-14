# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_08:11:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,467 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 08:11:10 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 08:10:19 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:08:17 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-14 08:08:11 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-14 08:08:02 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 08:07:56 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | -0.019 |  |
| 2026-10-14 08:06:34 | Pitabeddara (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.046 |  |
| 2026-10-14 08:06:12 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | -0.010 |  |
| 2026-10-14 08:06:06 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-10-14 08:06:05 | Baddegama (Gin Ganga) | 2.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 08:05:19 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-10-14 08:04:57 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:04:57 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:04:41 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.123 |  |
| 2026-10-14 08:04:39 | Rathnapura (Kalu Ganga) | 4.01 | 🟢 Normal | -0.101 |  |
| 2026-10-14 08:04:37 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-14 08:04:36 | Panadugama (Nilwala Ganga) | 5.99 | 🟡 Alert | -0.036 |  |
| 2026-10-14 08:04:35 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-14 08:03:51 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:03:48 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.049 |  |
| 2026-10-14 08:03:25 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:03:17 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-10-14 08:03:17 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-10-14 08:03:11 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:03:01 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.322 |  |
| 2026-10-14 08:02:55 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | 0.138 | 🔺 Rising |
| 2026-10-14 08:02:48 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 08:02:30 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-14 08:01:57 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.073 |  |
| 2026-10-14 08:01:56 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-10-14 08:01:26 | Moraketiya (Walawe Ganga) | 1.34 | 🟢 Normal | -0.032 |  |
| 2026-10-14 08:01:01 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:00:59 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:00:55 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 08:00:27 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-14 07:31:09 | Panadugama (Nilwala Ganga) | 6.01 | 🟠 Minor Flood | -0.036 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 08:11:10 | Thalgahagoda (Nilwala Ganga) | 1.73 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 08:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | 0.138 | 🔺 Rising |
| 2026-10-14 07:04:39 | Magura (Kalu Ganga) | 5.41 | 🟡 Alert | -0.010 |  |
| 2026-10-14 08:04:36 | Panadugama (Nilwala Ganga) | 5.99 | 🟡 Alert | -0.036 |  |
| 2026-10-14 08:08:17 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-14 08:04:37 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-10-14 08:04:35 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-14 08:02:30 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-14 08:02:48 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 08:06:05 | Baddegama (Gin Ganga) | 2.74 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 08:08:02 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-14 08:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 08:03:25 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:00:55 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:04:57 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:10:19 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:01:01 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:04:57 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:03:11 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:00:27 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:03:51 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:02:55 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:00:59 | Thanthirimale (Malwathu Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-14 08:06:12 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | -0.010 |  |
| 2026-10-14 08:08:11 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-14 08:05:19 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.019 |  |
| 2026-10-14 08:07:56 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | -0.019 |  |
| 2026-10-14 08:03:17 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.020 |  |
| 2026-10-14 08:03:17 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-10-14 07:05:27 | Urawa (Nilwala Ganga) | 1.17 | 🟢 Normal | -0.020 |  |
| 2026-10-14 08:06:06 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-10-14 08:01:56 | Dunamale (Aththanagalu Oya) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-10-14 08:01:26 | Moraketiya (Walawe Ganga) | 1.34 | 🟢 Normal | -0.032 |  |
| 2026-10-14 08:06:34 | Pitabeddara (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.046 |  |
| 2026-10-14 08:03:48 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | -0.049 |  |
| 2026-10-14 08:01:57 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.073 |  |
| 2026-10-14 08:04:39 | Rathnapura (Kalu Ganga) | 4.01 | 🟢 Normal | -0.101 |  |
| 2026-10-14 08:04:41 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.123 |  |
| 2026-10-14 08:03:01 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.322 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)