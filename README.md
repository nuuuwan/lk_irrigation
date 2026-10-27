# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_21:16:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,704 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 21:16:16 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.041 |  |
| 2026-10-27 21:10:20 | Baddegama (Gin Ganga) | 4.15 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-27 21:09:20 | Ellagawa (Kalu Ganga) | 10.26 | 🟡 Alert | 0.055 | 🔺 Rising |
| 2026-10-27 21:08:16 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-10-27 21:07:25 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 21:07:08 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 21:06:42 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-10-27 21:06:22 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-27 21:06:10 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-10-27 21:06:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.70 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-27 21:05:56 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-27 21:05:48 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.012 |  |
| 2026-10-27 21:05:27 | Putupaula (Kalu Ganga) | 3.42 | 🟡 Alert | 0.000 |  |
| 2026-10-27 21:05:00 | Badalgama (Maha Oya) | 4.10 | 🟢 Normal | -0.040 |  |
| 2026-10-27 21:04:21 | Pitabeddara (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-27 21:03:52 | Rathnapura (Kalu Ganga) | 7.52 | 🟠 Minor Flood | -0.089 |  |
| 2026-10-27 21:03:47 | Horowpothana (Yan Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 21:03:27 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-27 21:03:17 | Glencourse (Kelani Ganga) | 12.02 | 🟢 Normal | -0.065 |  |
| 2026-10-27 21:02:49 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 21:02:49 | Giriulla (Maha Oya) | 2.95 | 🟢 Normal | -0.071 |  |
| 2026-10-27 21:02:35 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-27 21:02:29 | Dunamale (Aththanagalu Oya) | 4.68 | 🟠 Minor Flood | -0.040 |  |
| 2026-10-27 21:02:11 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-10-27 21:02:06 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-27 21:02:05 | Panadugama (Nilwala Ganga) | 6.09 | 🟠 Minor Flood | -0.030 |  |
| 2026-10-27 21:01:56 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-10-27 21:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-10-27 21:01:43 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-10-27 21:01:19 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | -0.049 |  |
| 2026-10-27 21:01:14 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-27 21:00:50 | Moragaswewa (Deduru Oya) | 4.39 | 🟢 Normal | -0.134 |  |
| 2026-10-27 21:00:16 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-27 21:00:10 | Magura (Kalu Ganga) | 4.68 | 🟡 Alert | -0.042 |  |
| 2026-10-27 21:00:06 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 21:06:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.70 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-27 21:10:20 | Baddegama (Gin Ganga) | 4.15 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-10-27 21:07:25 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 21:02:05 | Panadugama (Nilwala Ganga) | 6.09 | 🟠 Minor Flood | -0.030 |  |
| 2026-10-27 21:02:29 | Dunamale (Aththanagalu Oya) | 4.68 | 🟠 Minor Flood | -0.040 |  |
| 2026-10-27 21:03:52 | Rathnapura (Kalu Ganga) | 7.52 | 🟠 Minor Flood | -0.089 |  |
| 2026-10-27 21:09:20 | Ellagawa (Kalu Ganga) | 10.26 | 🟡 Alert | 0.055 | 🔺 Rising |
| 2026-10-27 21:05:27 | Putupaula (Kalu Ganga) | 3.42 | 🟡 Alert | 0.000 |  |
| 2026-10-27 21:00:10 | Magura (Kalu Ganga) | 4.68 | 🟡 Alert | -0.042 |  |
| 2026-10-27 21:04:21 | Pitabeddara (Nilwala Ganga) | 2.32 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-27 21:06:22 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-27 21:02:49 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 21:02:11 | Kithulgala (Kelani Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-10-27 21:01:14 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-10-27 21:03:47 | Horowpothana (Yan Oya) | 3.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 21:00:06 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-27 21:02:06 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-27 21:07:08 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 21:02:35 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-27 18:23:14 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | -0.008 |  |
| 2026-10-27 21:06:10 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | -0.009 |  |
| 2026-10-27 21:05:56 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-27 21:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-10-27 21:03:27 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-10-27 21:00:16 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-10-27 21:01:43 | Moraketiya (Walawe Ganga) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-10-27 21:08:16 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-10-27 21:05:48 | Deraniyagala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.012 |  |
| 2026-10-27 21:06:42 | Holombuwa (Kelani Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-10-27 21:01:56 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-10-27 21:05:00 | Badalgama (Maha Oya) | 4.10 | 🟢 Normal | -0.040 |  |
| 2026-10-27 21:16:16 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.041 |  |
| 2026-10-27 21:01:19 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | -0.049 |  |
| 2026-10-27 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.059 |  |
| 2026-10-27 21:03:17 | Glencourse (Kelani Ganga) | 12.02 | 🟢 Normal | -0.065 |  |
| 2026-10-27 21:02:49 | Giriulla (Maha Oya) | 2.95 | 🟢 Normal | -0.071 |  |
| 2026-10-27 18:00:41 | Thanthirimale (Malwathu Oya) | 2.72 | 🟢 Normal | -0.133 |  |
| 2026-10-27 21:00:50 | Moragaswewa (Deduru Oya) | 4.39 | 🟢 Normal | -0.134 |  |
| 2026-10-27 20:02:08 | Hanwella (Kelani Ganga) | 5.15 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)