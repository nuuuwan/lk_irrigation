# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--19_15:18:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,276 measurements** from **39** stations.
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
| 2026-10-19 15:18:45 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.061 |  |
| 2026-10-19 15:17:15 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-10-19 15:10:10 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.033 |  |
| 2026-10-19 15:06:30 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 15:05:59 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:05:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.015 |  |
| 2026-10-19 15:05:25 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:05:17 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | -18.000 |  |
| 2026-10-19 15:05:15 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | -18.000 |  |
| 2026-10-19 15:04:48 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:04:48 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.021 |  |
| 2026-10-19 15:04:41 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.029 |  |
| 2026-10-19 15:04:40 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.012 |  |
| 2026-10-19 15:04:38 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 15:04:30 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.083 |  |
| 2026-10-19 15:04:25 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.028 |  |
| 2026-10-19 15:04:22 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 15:04:18 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:04:14 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | -0.076 |  |
| 2026-10-19 15:04:04 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.048 |  |
| 2026-10-19 15:03:49 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-10-19 15:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.032 |  |
| 2026-10-19 15:03:35 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:03:34 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-10-19 15:03:23 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-10-19 15:03:14 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-10-19 15:02:42 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | -0.060 |  |
| 2026-10-19 15:02:40 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:02:36 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.061 |  |
| 2026-10-19 15:02:36 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:02:32 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.048 |  |
| 2026-10-19 15:02:20 | Panadugama (Nilwala Ganga) | 5.21 | 🟡 Alert | -0.065 |  |
| 2026-10-19 15:02:15 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:02:12 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:01:56 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:01:37 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:01:31 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:01:28 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:00:52 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:00:42 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-19 15:06:30 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-19 15:02:20 | Panadugama (Nilwala Ganga) | 5.21 | 🟡 Alert | -0.065 |  |
| 2026-10-19 15:04:22 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 15:04:38 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-19 15:01:31 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:01:41 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:02:12 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:05:25 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:03:35 | Thawalama (Gin Ganga) | 2.33 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:02:40 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:01:56 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:05:59 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-10-19 15:17:15 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-10-19 15:04:18 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:02:36 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:02:15 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:00:42 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:04:48 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:00:52 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:01:28 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-10-19 15:04:40 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.012 |  |
| 2026-10-19 15:05:39 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.015 |  |
| 2026-10-19 15:03:49 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-10-19 15:03:23 | Moraketiya (Walawe Ganga) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-10-19 15:03:34 | Moragaswewa (Deduru Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-10-19 15:04:48 | Badalgama (Maha Oya) | 2.79 | 🟢 Normal | -0.021 |  |
| 2026-10-19 15:04:25 | Putupaula (Kalu Ganga) | 1.38 | 🟢 Normal | -0.028 |  |
| 2026-10-19 15:04:41 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.029 |  |
| 2026-10-19 15:03:14 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.030 |  |
| 2026-10-19 15:03:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.032 |  |
| 2026-10-19 15:10:10 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.033 |  |
| 2026-10-19 15:04:04 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.048 |  |
| 2026-10-19 15:02:32 | Pitabeddara (Nilwala Ganga) | 1.71 | 🟢 Normal | -0.048 |  |
| 2026-10-19 15:02:42 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | -0.060 |  |
| 2026-10-19 15:02:36 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.061 |  |
| 2026-10-19 15:18:45 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | -0.061 |  |
| 2026-10-19 15:04:14 | Ellagawa (Kalu Ganga) | 6.95 | 🟢 Normal | -0.076 |  |
| 2026-10-19 15:04:30 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.083 |  |
| 2026-10-19 15:05:17 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)