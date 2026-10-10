# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_07:11:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,841 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 07:11:15 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | -0.005 |  |
| 2026-10-10 07:11:15 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.038 |  |
| 2026-10-10 07:09:36 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.009 |  |
| 2026-10-10 07:09:02 | Giriulla (Maha Oya) | 4.00 | 🟢 Normal | -0.189 |  |
| 2026-10-10 07:09:02 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 07:08:37 | Glencourse (Kelani Ganga) | 11.42 | 🟢 Normal | -0.093 |  |
| 2026-10-10 07:08:23 | Rathnapura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.100 |  |
| 2026-10-10 07:08:13 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-10-10 07:07:44 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 07:07:22 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.028 |  |
| 2026-10-10 07:06:27 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.029 |  |
| 2026-10-10 07:06:12 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 07:06:10 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-10 07:05:52 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.050 |  |
| 2026-10-10 07:05:46 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | -0.156 |  |
| 2026-10-10 07:05:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 07:03:01 | Dunamale (Aththanagalu Oya) | 3.36 | 🟡 Alert | 0.000 |  |
| 2026-10-10 07:04:50 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | 0.292 | 🔺 Rising |
| 2026-10-10 07:05:09 | Badalgama (Maha Oya) | 4.79 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-10 07:01:56 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-10 07:06:10 | Kithulgala (Kelani Ganga) | 2.13 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-10 07:02:37 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-10 07:06:12 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 07:05:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 07:00:46 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 07:05:01 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-10 07:09:02 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 06:01:06 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-10 07:07:44 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 07:11:15 | Thanthirimale (Malwathu Oya) | 0.79 | 🟢 Normal | -0.005 |  |
| 2026-10-10 07:09:36 | Thawalama (Gin Ganga) | 2.11 | 🟢 Normal | -0.009 |  |
| 2026-10-10 07:02:34 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-10 07:01:24 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | -0.011 |  |
| 2026-10-10 07:08:13 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.019 |  |
| 2026-10-10 07:03:17 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.019 |  |
| 2026-10-10 07:04:30 | Moragaswewa (Deduru Oya) | 2.49 | 🟢 Normal | -0.020 |  |
| 2026-10-10 07:02:12 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.021 |  |
| 2026-10-10 07:00:27 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.021 |  |
| 2026-10-10 07:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.026 |  |
| 2026-10-10 07:07:22 | Magura (Kalu Ganga) | 2.18 | 🟢 Normal | -0.028 |  |
| 2026-10-10 07:03:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.87 | 🟢 Normal | -0.028 |  |
| 2026-10-10 07:06:27 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.029 |  |
| 2026-10-10 07:02:10 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-10-10 07:11:15 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.038 |  |
| 2026-10-10 07:04:59 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.047 |  |
| 2026-10-10 07:05:52 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | -0.050 |  |
| 2026-10-10 07:02:21 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.058 |  |
| 2026-10-10 07:04:08 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.063 |  |
| 2026-10-10 07:03:29 | Panadugama (Nilwala Ganga) | 4.53 | 🟢 Normal | -0.066 |  |
| 2026-10-10 07:04:20 | Hanwella (Kelani Ganga) | 3.80 | 🟢 Normal | -0.088 |  |
| 2026-10-10 07:08:37 | Glencourse (Kelani Ganga) | 11.42 | 🟢 Normal | -0.093 |  |
| 2026-10-10 07:08:23 | Rathnapura (Kalu Ganga) | 3.13 | 🟢 Normal | -0.100 |  |
| 2026-10-10 07:05:46 | Peradeniya (Mahaweli Ganga) | 3.32 | 🟢 Normal | -0.156 |  |
| 2026-10-10 07:00:28 | Pitabeddara (Nilwala Ganga) | 1.66 | 🟢 Normal | -0.162 |  |
| 2026-10-10 07:09:02 | Giriulla (Maha Oya) | 4.00 | 🟢 Normal | -0.189 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)