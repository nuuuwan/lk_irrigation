# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_10:32:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,076 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 10:32:46 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:15:28 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | -0.017 |  |
| 2026-10-19 10:14:30 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-10-19 10:09:40 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:09:02 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | -0.028 |  |
| 2026-10-19 10:08:41 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-19 10:08:19 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.009 |  |
| 2026-10-19 10:07:05 | Panadugama (Nilwala Ganga) | 5.39 | 🟡 Alert | -0.021 |  |
| 2026-10-19 10:06:19 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.019 |  |
| 2026-10-19 10:06:17 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-19 10:05:55 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-10-19 10:05:55 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -0.029 |  |
| 2026-10-19 10:05:46 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.039 |  |
| 2026-10-19 10:04:20 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-10-19 10:04:14 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-19 10:04:00 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.060 |  |
| 2026-10-19 10:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-19 10:03:29 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-10-19 10:03:26 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-10-19 10:03:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.063 |  |
| 2026-10-19 10:03:13 | Hanwella (Kelani Ganga) | 3.39 | 🟢 Normal | -0.075 |  |
| 2026-10-19 10:03:01 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-19 10:02:46 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.051 |  |
| 2026-10-19 10:02:41 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 10:02:40 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:02:30 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 10:02:29 | Ellagawa (Kalu Ganga) | 7.22 | 🟢 Normal | -0.040 |  |
| 2026-10-19 10:02:29 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:02:03 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-10-19 10:02:01 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:01:52 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.031 |  |
| 2026-10-19 10:01:23 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.041 |  |
| 2026-10-19 10:01:02 | Moragaswewa (Deduru Oya) | 1.77 | 🟢 Normal | -0.032 |  |
| 2026-10-19 10:00:59 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.033 |  |
| 2026-10-19 10:00:58 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.042 |  |
| 2026-10-19 10:00:45 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:00:38 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.110 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 10:02:30 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 10:07:05 | Panadugama (Nilwala Ganga) | 5.39 | 🟡 Alert | -0.021 |  |
| 2026-10-19 10:06:17 | Badalgama (Maha Oya) | 2.83 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-19 10:04:14 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-19 10:02:41 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 10:02:01 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:00:45 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:02:40 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:32:46 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:02:29 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:05:55 | Dunamale (Aththanagalu Oya) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:09:40 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-19 10:14:30 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-10-19 10:08:19 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.009 |  |
| 2026-10-19 10:03:41 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-19 10:03:01 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-19 10:02:03 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-10-19 10:04:20 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-10-19 10:08:41 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-10-19 10:15:28 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | -0.017 |  |
| 2026-10-19 10:06:19 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.019 |  |
| 2026-10-19 10:05:55 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-10-19 10:03:26 | Thawalama (Gin Ganga) | 2.36 | 🟢 Normal | -0.020 |  |
| 2026-10-19 09:00:46 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-10-19 10:09:02 | Baddegama (Gin Ganga) | 2.62 | 🟢 Normal | -0.028 |  |
| 2026-10-19 10:05:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -0.029 |  |
| 2026-10-19 10:03:29 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.029 |  |
| 2026-10-19 10:01:52 | Giriulla (Maha Oya) | 1.59 | 🟢 Normal | -0.031 |  |
| 2026-10-19 10:01:02 | Moragaswewa (Deduru Oya) | 1.77 | 🟢 Normal | -0.032 |  |
| 2026-10-19 10:00:59 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | -0.033 |  |
| 2026-10-19 10:05:46 | Glencourse (Kelani Ganga) | 11.20 | 🟢 Normal | -0.039 |  |
| 2026-10-19 10:02:29 | Ellagawa (Kalu Ganga) | 7.22 | 🟢 Normal | -0.040 |  |
| 2026-10-19 10:01:23 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.041 |  |
| 2026-10-19 10:00:58 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.042 |  |
| 2026-10-19 10:02:46 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.051 |  |
| 2026-10-19 10:04:00 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.060 |  |
| 2026-10-19 10:03:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.063 |  |
| 2026-10-19 10:03:13 | Hanwella (Kelani Ganga) | 3.39 | 🟢 Normal | -0.075 |  |
| 2026-10-19 10:00:38 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)