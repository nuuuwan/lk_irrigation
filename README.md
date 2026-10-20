# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_04:05:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,655 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 04:05:27 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:04:33 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:04:26 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-21 04:03:59 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:03:56 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:03:41 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.033 |  |
| 2026-10-21 04:03:40 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:02:48 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:02:44 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:02:37 | Dunamale (Aththanagalu Oya) | 1.89 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-21 04:02:23 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 04:02:20 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 04:02:19 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:02:15 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:02:01 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:01:40 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:01:18 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:01:11 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.034 |  |
| 2026-10-21 04:00:49 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-10-21 04:00:49 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-10-21 04:00:48 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:00:31 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-21 04:00:22 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:00:08 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.329 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 03:09:58 | Thalgahagoda (Nilwala Ganga) | 1.48 | 🟡 Alert | -0.017 |  |
| 2026-10-20 18:02:39 | Galgamuwa (Mee Oya) | 0.61 | 🟢 Normal | 9.000 | 🔺 Rising |
| 2026-10-21 04:00:08 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | 0.329 | 🔺 Rising |
| 2026-10-21 04:00:49 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-10-21 03:02:21 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-10-21 04:00:31 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-21 04:04:26 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-21 04:02:37 | Dunamale (Aththanagalu Oya) | 1.89 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-21 03:14:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.95 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-21 04:02:23 | Moragaswewa (Deduru Oya) | 1.06 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 03:01:41 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-20 18:04:50 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 04:02:20 | Norwood (Kelani Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-21 04:02:19 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:03:56 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:03:59 | Hanwella (Kelani Ganga) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:03:40 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:04:33 | Badalgama (Maha Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:02:44 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-20 18:01:22 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:06:19 | Thawalama (Gin Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:02:15 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 03:04:59 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-21 04:05:27 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:05:11 | Rathnapura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:05:45 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:02:48 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:00:48 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:02:01 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-10-21 03:02:05 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:01:18 | Ellagawa (Kalu Ganga) | 5.64 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:00:22 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-21 04:00:49 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-10-21 03:07:48 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | -0.026 |  |
| 2026-10-21 04:03:41 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.033 |  |
| 2026-10-21 04:01:11 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.034 |  |
| 2026-10-21 03:14:37 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.042 |  |
| 2026-10-21 03:14:41 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | -0.078 |  |
| 2026-10-21 03:06:50 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)