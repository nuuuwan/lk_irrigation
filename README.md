# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_04:19:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,847 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 04:19:13 | Rathnapura (Kalu Ganga) | 5.25 | 🟡 Alert | -0.055 |  |
| 2026-10-29 04:18:59 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:15:34 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | -0.039 |  |
| 2026-10-29 04:13:10 | Putupaula (Kalu Ganga) | 3.75 | 🟡 Alert | 0.000 |  |
| 2026-10-29 04:12:05 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -36.000 |  |
| 2026-10-29 04:12:04 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -36.000 |  |
| 2026-10-29 04:12:02 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -36.000 |  |
| 2026-10-29 04:09:43 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:09:28 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.018 | 🔺 Rising |
| 2026-10-29 04:08:39 | Badalgama (Maha Oya) | 3.24 | 🟢 Normal | -0.029 |  |
| 2026-10-29 04:08:08 | Panadugama (Nilwala Ganga) | 6.00 | 🟠 Minor Flood | -0.028 |  |
| 2026-10-29 04:08:05 | Thawalama (Gin Ganga) | 2.73 | 🟢 Normal | -0.151 |  |
| 2026-10-29 04:06:46 | Baddegama (Gin Ganga) | 4.19 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 04:06:41 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-10-29 04:06:36 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:06:18 | Pitabeddara (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-10-29 04:05:51 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-10-29 04:04:43 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-10-29 04:04:42 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:04:35 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-29 04:04:09 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.029 |  |
| 2026-10-29 04:04:00 | Ellagawa (Kalu Ganga) | 10.23 | 🟡 Alert | -0.011 |  |
| 2026-10-29 04:03:31 | Glencourse (Kelani Ganga) | 11.46 | 🟢 Normal | -0.049 |  |
| 2026-10-29 04:03:26 | Magura (Kalu Ganga) | 3.92 | 🟢 Normal | -0.125 |  |
| 2026-10-29 04:03:11 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:03:08 | Hanwella (Kelani Ganga) | 4.01 | 🟢 Normal | -0.034 |  |
| 2026-10-29 04:02:44 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.040 |  |
| 2026-10-29 04:02:36 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:02:25 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.039 |  |
| 2026-10-29 04:02:23 | Moragaswewa (Deduru Oya) | 1.83 | 🟢 Normal | -0.120 |  |
| 2026-10-29 04:02:09 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.58 | 🟠 Minor Flood | -0.031 |  |
| 2026-10-29 04:02:06 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:01:47 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.041 |  |
| 2026-10-29 04:01:05 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 04:09:28 | Thalgahagoda (Nilwala Ganga) | 1.86 | 🟠 Minor Flood | 0.018 | 🔺 Rising |
| 2026-10-29 04:06:46 | Baddegama (Gin Ganga) | 4.19 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 04:08:08 | Panadugama (Nilwala Ganga) | 6.00 | 🟠 Minor Flood | -0.028 |  |
| 2026-10-29 04:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.58 | 🟠 Minor Flood | -0.031 |  |
| 2026-10-29 04:13:10 | Putupaula (Kalu Ganga) | 3.75 | 🟡 Alert | 0.000 |  |
| 2026-10-29 04:04:00 | Ellagawa (Kalu Ganga) | 10.23 | 🟡 Alert | -0.011 |  |
| 2026-10-29 04:19:13 | Rathnapura (Kalu Ganga) | 5.25 | 🟡 Alert | -0.055 |  |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-29 04:01:05 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-29 04:04:35 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-28 18:08:56 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-29 04:02:09 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:02:36 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:03:11 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:04:42 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:02:06 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:09:43 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:18:59 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:06:36 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 03:07:02 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-29 03:07:18 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 04:06:18 | Pitabeddara (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-10-29 04:06:41 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-10-29 04:04:43 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.019 |  |
| 2026-10-29 04:05:51 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-10-29 04:04:09 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.029 |  |
| 2026-10-29 04:08:39 | Badalgama (Maha Oya) | 3.24 | 🟢 Normal | -0.029 |  |
| 2026-10-29 04:03:08 | Hanwella (Kelani Ganga) | 4.01 | 🟢 Normal | -0.034 |  |
| 2026-10-29 04:02:25 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.039 |  |
| 2026-10-29 03:07:06 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | -0.039 |  |
| 2026-10-29 04:15:34 | Urawa (Nilwala Ganga) | 1.56 | 🟢 Normal | -0.039 |  |
| 2026-10-29 04:02:44 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | -0.040 |  |
| 2026-10-29 04:01:47 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.041 |  |
| 2026-10-29 04:03:31 | Glencourse (Kelani Ganga) | 11.46 | 🟢 Normal | -0.049 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-29 04:02:23 | Moragaswewa (Deduru Oya) | 1.83 | 🟢 Normal | -0.120 |  |
| 2026-10-29 04:03:26 | Magura (Kalu Ganga) | 3.92 | 🟢 Normal | -0.125 |  |
| 2026-10-29 04:08:05 | Thawalama (Gin Ganga) | 2.73 | 🟢 Normal | -0.151 |  |
| 2026-10-29 04:12:05 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)