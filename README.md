# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_12:23:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,352 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 12:23:26 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 12:12:46 | Holombuwa (Kelani Ganga) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-10-27 12:11:52 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-27 12:08:07 | Giriulla (Maha Oya) | 3.60 | 🟢 Normal | -0.089 |  |
| 2026-10-27 12:06:28 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.057 |  |
| 2026-10-27 12:06:28 | Urawa (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.053 |  |
| 2026-10-27 12:06:15 | Hanwella (Kelani Ganga) | 6.13 | 🟢 Normal | -0.113 |  |
| 2026-10-27 12:05:34 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-27 12:05:24 | Baddegama (Gin Ganga) | 4.02 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-10-27 12:04:53 | Ellagawa (Kalu Ganga) | 9.97 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-27 12:04:44 | Badalgama (Maha Oya) | 4.97 | 🟢 Normal | -0.155 |  |
| 2026-10-27 12:04:36 | Rathnapura (Kalu Ganga) | 8.30 | 🟠 Minor Flood | -0.116 |  |
| 2026-10-27 12:03:59 | Moragaswewa (Deduru Oya) | 5.20 | 🟡 Alert | -0.020 |  |
| 2026-10-27 12:03:42 | Galgamuwa (Mee Oya) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-10-27 12:03:42 | Norwood (Kelani Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-27 12:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.50 | 🟠 Minor Flood | 0.049 | 🔺 Rising |
| 2026-10-27 12:03:24 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.158 |  |
| 2026-10-27 12:02:58 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 12:02:43 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.000 |  |
| 2026-10-27 12:02:40 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 12:02:39 | Putupaula (Kalu Ganga) | 3.29 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-27 12:02:26 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-10-27 12:02:25 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.148 |  |
| 2026-10-27 12:02:16 | Thawalama (Gin Ganga) | 3.69 | 🟢 Normal | -0.292 |  |
| 2026-10-27 12:02:12 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 12:02:10 | Panadugama (Nilwala Ganga) | 6.34 | 🟠 Minor Flood | -0.030 |  |
| 2026-10-27 12:01:56 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.030 |  |
| 2026-10-27 12:01:55 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-27 12:01:51 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.151 |  |
| 2026-10-27 12:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-10-27 12:01:41 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-10-27 12:01:34 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 12:01:06 | Peradeniya (Mahaweli Ganga) | 3.50 | 🟢 Normal | -0.033 |  |
| 2026-10-27 12:01:01 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-27 12:00:25 | Horowpothana (Yan Oya) | 3.26 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-27 12:00:22 | Magura (Kalu Ganga) | 5.17 | 🟡 Alert | -0.061 |  |
| 2026-10-27 12:00:15 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-27 12:00:14 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 12:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.50 | 🟠 Minor Flood | 0.049 | 🔺 Rising |
| 2026-10-27 12:05:24 | Baddegama (Gin Ganga) | 4.02 | 🟠 Minor Flood | 0.030 | 🔺 Rising |
| 2026-10-27 12:02:40 | Dunamale (Aththanagalu Oya) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-27 12:02:10 | Panadugama (Nilwala Ganga) | 6.34 | 🟠 Minor Flood | -0.030 |  |
| 2026-10-27 12:04:36 | Rathnapura (Kalu Ganga) | 8.30 | 🟠 Minor Flood | -0.116 |  |
| 2026-10-27 12:02:39 | Putupaula (Kalu Ganga) | 3.29 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-27 12:23:26 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 12:03:59 | Moragaswewa (Deduru Oya) | 5.20 | 🟡 Alert | -0.020 |  |
| 2026-10-27 12:00:22 | Magura (Kalu Ganga) | 5.17 | 🟡 Alert | -0.061 |  |
| 2026-10-27 12:00:25 | Horowpothana (Yan Oya) | 3.26 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-27 12:11:52 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-27 12:01:55 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-27 12:04:53 | Ellagawa (Kalu Ganga) | 9.97 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-27 12:02:43 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.000 |  |
| 2026-10-27 12:01:34 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 10:00:31 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 12:01:01 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-27 12:05:34 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-27 12:02:12 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-27 12:02:58 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-27 12:12:46 | Holombuwa (Kelani Ganga) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-10-27 12:03:42 | Galgamuwa (Mee Oya) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-10-27 12:00:14 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-27 12:00:15 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-10-27 12:01:41 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.020 |  |
| 2026-10-27 12:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-10-27 12:03:42 | Norwood (Kelani Ganga) | 1.44 | 🟢 Normal | -0.021 |  |
| 2026-10-27 12:02:26 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-10-27 12:01:56 | Manampitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.030 |  |
| 2026-10-27 12:01:06 | Peradeniya (Mahaweli Ganga) | 3.50 | 🟢 Normal | -0.033 |  |
| 2026-10-27 12:06:28 | Urawa (Nilwala Ganga) | 1.49 | 🟢 Normal | -0.053 |  |
| 2026-10-27 12:06:28 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | -0.057 |  |
| 2026-10-27 12:08:07 | Giriulla (Maha Oya) | 3.60 | 🟢 Normal | -0.089 |  |
| 2026-10-27 12:06:15 | Hanwella (Kelani Ganga) | 6.13 | 🟢 Normal | -0.113 |  |
| 2026-10-27 12:02:25 | Pitabeddara (Nilwala Ganga) | 2.60 | 🟢 Normal | -0.148 |  |
| 2026-10-27 12:01:51 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.151 |  |
| 2026-10-27 12:04:44 | Badalgama (Maha Oya) | 4.97 | 🟢 Normal | -0.155 |  |
| 2026-10-27 12:03:24 | Glencourse (Kelani Ganga) | 13.05 | 🟢 Normal | -0.158 |  |
| 2026-10-27 12:02:16 | Thawalama (Gin Ganga) | 3.69 | 🟢 Normal | -0.292 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)