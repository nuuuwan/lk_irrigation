# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_03:24:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,145 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 03:24:52 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:21:50 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | -0.008 |  |
| 2026-11-15 03:21:45 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.067 |  |
| 2026-11-15 03:11:16 | Baddegama (Gin Ganga) | 2.96 | 🟢 Normal | -144.000 |  |
| 2026-11-15 03:11:15 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | -144.000 |  |
| 2026-11-15 03:10:11 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 03:10:11 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:09:38 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:08:54 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:08:33 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:08:03 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:08:00 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-15 03:07:43 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-15 03:07:34 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.038 |  |
| 2026-11-15 03:07:06 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | -0.030 |  |
| 2026-11-15 03:06:59 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.018 |  |
| 2026-11-15 03:06:49 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-15 03:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -0.078 |  |
| 2026-11-15 03:06:09 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-15 03:06:01 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-15 03:05:43 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:05:42 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | 5.447 | 🔺 Rising |
| 2026-11-15 03:04:59 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:04:36 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-11-15 03:04:24 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -1.500 |  |
| 2026-11-15 03:04:17 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:04:09 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.005 |  |
| 2026-11-15 03:04:08 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.049 |  |
| 2026-11-15 03:04:00 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -1.500 |  |
| 2026-11-15 03:03:45 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.067 |  |
| 2026-11-15 03:03:36 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:03:24 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:03:13 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.020 |  |
| 2026-11-15 03:03:10 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | 5.447 | 🔺 Rising |
| 2026-11-15 03:02:29 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:02:28 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | -0.021 |  |
| 2026-11-15 03:02:07 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:02:04 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:01:51 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:00:44 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:00:34 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 03:10:11 | Thalgahagoda (Nilwala Ganga) | 1.89 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 03:05:42 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | 5.447 | 🔺 Rising |
| 2026-11-15 03:07:43 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-15 03:06:49 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-15 03:06:01 | Thanamalwila (Kirindi Oya) | 1.75 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-11-15 03:08:00 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-14 18:01:52 | Weraganthota (Mahaweli Ganga) | -1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 03:24:52 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:08:03 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-15 02:06:57 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-14 18:04:59 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:08:54 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:10:11 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:00:34 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:01:51 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:05:43 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:09:38 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-15 03:04:09 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.005 |  |
| 2026-11-15 03:21:50 | Ellagawa (Kalu Ganga) | 5.76 | 🟢 Normal | -0.008 |  |
| 2026-11-15 03:03:36 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:02:04 | Kuda Oya (Kirindi Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:03:24 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:04:59 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:02:29 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:02:07 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:04:17 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-11-15 03:06:09 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-14 18:00:25 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.011 |  |
| 2026-11-15 03:06:59 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.018 |  |
| 2026-11-15 03:03:13 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.020 |  |
| 2026-11-15 03:04:36 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-11-15 03:02:28 | Glencourse (Kelani Ganga) | 10.67 | 🟢 Normal | -0.021 |  |
| 2026-11-15 03:07:06 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | -0.030 |  |
| 2026-11-15 03:07:34 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.038 |  |
| 2026-11-15 03:04:08 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.049 |  |
| 2026-11-15 03:21:45 | Magura (Kalu Ganga) | 2.07 | 🟢 Normal | -0.067 |  |
| 2026-11-15 03:06:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.44 | 🟢 Normal | -0.078 |  |
| 2026-11-15 03:04:24 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -1.500 |  |
| 2026-11-15 03:11:16 | Baddegama (Gin Ganga) | 2.96 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)