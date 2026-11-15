# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_17:26:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,683 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 17:26:53 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.016 |  |
| 2026-11-15 17:22:29 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:14:27 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-11-15 17:13:45 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 17:11:41 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:09:05 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | -0.056 |  |
| 2026-11-15 17:09:01 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.062 |  |
| 2026-11-15 17:08:21 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.019 |  |
| 2026-11-15 17:06:58 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:06:38 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.019 |  |
| 2026-11-15 17:06:32 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | -0.020 |  |
| 2026-11-15 17:06:11 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-11-15 17:05:51 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-15 17:05:23 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.012 |  |
| 2026-11-15 17:05:23 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:05:21 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:04:52 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:04:44 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-11-15 17:04:23 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | -0.021 |  |
| 2026-11-15 17:03:40 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:03:32 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.031 |  |
| 2026-11-15 17:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-11-15 17:02:48 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:02:44 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.099 |  |
| 2026-11-15 17:02:38 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-15 17:02:24 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-11-15 17:02:23 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-11-15 17:02:16 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-15 17:02:16 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:02:09 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-11-15 17:02:03 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:59 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-11-15 17:01:48 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:40 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:35 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | -0.039 |  |
| 2026-11-15 17:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:00:49 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.043 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 17:13:45 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 17:02:38 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-15 17:00:49 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-15 17:05:51 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-15 17:02:03 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:01 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:40 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:01:48 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:03:40 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:02:48 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 15:03:41 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 16:01:10 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:06:58 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:05:21 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:04:52 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:05:23 | Manampitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:22:29 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:11:41 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:02:16 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-11-15 17:06:11 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-11-15 17:02:16 | Nakkala (Kumbukkan Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-15 17:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-11-15 17:04:44 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-11-15 17:14:27 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-11-15 17:05:23 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.012 |  |
| 2026-11-15 17:26:53 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.016 |  |
| 2026-11-15 17:08:21 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | -0.019 |  |
| 2026-11-15 17:06:38 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.019 |  |
| 2026-11-15 17:02:24 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.020 |  |
| 2026-11-15 17:06:32 | Panadugama (Nilwala Ganga) | 4.71 | 🟢 Normal | -0.020 |  |
| 2026-11-15 17:01:59 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-11-15 17:04:23 | Glencourse (Kelani Ganga) | 10.48 | 🟢 Normal | -0.021 |  |
| 2026-11-15 17:02:09 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.029 |  |
| 2026-11-15 17:03:32 | Dunamale (Aththanagalu Oya) | 1.90 | 🟢 Normal | -0.031 |  |
| 2026-11-15 17:01:35 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | -0.039 |  |
| 2026-11-15 17:09:05 | Weraganthota (Mahaweli Ganga) | -1.78 | 🟢 Normal | -0.056 |  |
| 2026-11-15 17:02:23 | Thanamalwila (Kirindi Oya) | 1.60 | 🟢 Normal | -0.060 |  |
| 2026-11-15 17:09:01 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.062 |  |
| 2026-11-15 17:02:44 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)