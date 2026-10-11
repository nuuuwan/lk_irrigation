# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_17:17:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 17:17:56 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.029 |  |
| 2026-10-11 17:15:59 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-11 17:10:43 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.018 |  |
| 2026-10-11 17:10:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | -0.038 |  |
| 2026-10-11 17:09:39 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.056 |  |
| 2026-10-11 17:07:45 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | -0.028 |  |
| 2026-10-11 17:07:32 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-11 17:06:40 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-10-11 17:06:35 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-11 17:06:29 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.010 |  |
| 2026-10-11 17:06:18 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.047 |  |
| 2026-10-11 17:05:55 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.153 |  |
| 2026-10-11 17:05:53 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.022 |  |
| 2026-10-11 17:05:52 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-11 17:05:23 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 17:05:17 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.047 |  |
| 2026-10-11 17:05:03 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-11 17:04:57 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-11 17:04:53 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 17:04:51 | Norwood (Kelani Ganga) | 1.53 | 🟡 Alert | 0.247 | 🔺 Rising |
| 2026-10-11 17:04:49 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.082 |  |
| 2026-10-11 17:04:46 | Putupaula (Kalu Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-10-11 17:04:15 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 17:03:59 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-11 17:03:45 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.040 |  |
| 2026-10-11 17:03:36 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.012 |  |
| 2026-10-11 17:02:35 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-11 17:02:16 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 17:02:15 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | -0.041 |  |
| 2026-10-11 17:02:07 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 17:02:01 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 17:01:36 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.032 |  |
| 2026-10-11 17:01:27 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-11 17:01:19 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-10-11 17:01:15 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | -0.079 |  |
| 2026-10-11 17:01:12 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 17:00:45 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-10-11 17:00:23 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-11 17:00:08 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.161 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 17:04:51 | Norwood (Kelani Ganga) | 1.53 | 🟡 Alert | 0.247 | 🔺 Rising |
| 2026-10-11 17:06:40 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | 0.262 | 🔺 Rising |
| 2026-10-11 17:00:08 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-10-11 17:05:52 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-10-11 17:06:35 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-10-11 17:04:57 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-11 17:02:35 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-11 17:04:53 | Peradeniya (Mahaweli Ganga) | 2.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 17:03:59 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-11 17:02:16 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 17:02:07 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 17:01:12 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 17:02:01 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 17:04:15 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 17:05:23 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 17:01:27 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-11 17:15:59 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-11 17:00:23 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-11 17:05:03 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-11 17:07:32 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-10-11 17:06:29 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.010 |  |
| 2026-10-11 17:01:19 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-10-11 17:03:36 | Rathnapura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.012 |  |
| 2026-10-11 17:10:43 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.018 |  |
| 2026-10-11 17:00:45 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-10-11 17:04:46 | Putupaula (Kalu Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-10-11 17:05:53 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -0.022 |  |
| 2026-10-11 17:07:45 | Hanwella (Kelani Ganga) | 2.74 | 🟢 Normal | -0.028 |  |
| 2026-10-11 17:17:56 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.029 |  |
| 2026-10-11 17:01:36 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | -0.032 |  |
| 2026-10-11 17:10:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | -0.038 |  |
| 2026-10-11 17:03:45 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.040 |  |
| 2026-10-11 17:02:15 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | -0.041 |  |
| 2026-10-11 17:06:18 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | -0.047 |  |
| 2026-10-11 17:05:17 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.047 |  |
| 2026-10-11 17:09:39 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.056 |  |
| 2026-10-11 17:01:15 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | -0.079 |  |
| 2026-10-11 17:04:49 | Dunamale (Aththanagalu Oya) | 2.38 | 🟢 Normal | -0.082 |  |
| 2026-10-11 17:05:55 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)