# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_08:18:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,331 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 08:18:49 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.016 |  |
| 2026-11-15 08:13:16 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:11:00 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-11-15 08:09:54 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:09:47 | Panadugama (Nilwala Ganga) | 4.85 | 🟢 Normal | -0.018 |  |
| 2026-11-15 08:09:35 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:08:57 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:08:26 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-11-15 08:07:58 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.009 |  |
| 2026-11-15 08:07:39 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:07:35 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.010 |  |
| 2026-11-15 08:07:26 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:07:10 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-11-15 08:07:10 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.037 |  |
| 2026-11-15 08:06:04 | Baddegama (Gin Ganga) | 2.79 | 🟢 Normal | -0.037 |  |
| 2026-11-15 08:05:55 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.054 |  |
| 2026-11-15 08:05:12 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 08:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.031 |  |
| 2026-11-15 08:03:39 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | -0.010 |  |
| 2026-11-15 08:03:31 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.045 |  |
| 2026-11-15 08:03:29 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:03:20 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-11-15 08:03:05 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:02:44 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-15 08:02:21 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | -0.005 |  |
| 2026-11-15 08:02:12 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 08:02:12 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | -0.061 |  |
| 2026-11-15 08:02:09 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 08:02:07 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.041 |  |
| 2026-11-15 08:01:59 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.051 |  |
| 2026-11-15 08:01:55 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:01:39 | Thanamalwila (Kirindi Oya) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-11-15 08:01:32 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.091 |  |
| 2026-11-15 08:01:14 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:01:13 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:01:13 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-15 08:01:06 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 08:02:12 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-15 08:07:10 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-11-15 08:02:44 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-15 08:02:09 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 08:05:12 | Manampitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 08:09:35 | Moragaswewa (Deduru Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:13:16 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:01:55 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:01:14 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:03:05 | Hanwella (Kelani Ganga) | 2.52 | 🟢 Normal | 0.000 |  |
| 2026-11-15 07:43:48 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:09:54 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:01:06 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:03:29 | Dunamale (Aththanagalu Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:07:26 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:08:57 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:01:13 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:07:39 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-15 08:02:21 | Kuda Oya (Kirindi Oya) | 1.83 | 🟢 Normal | -0.005 |  |
| 2026-11-15 08:07:58 | Rathnapura (Kalu Ganga) | 2.02 | 🟢 Normal | -0.009 |  |
| 2026-11-15 08:07:35 | Glencourse (Kelani Ganga) | 10.66 | 🟢 Normal | -0.010 |  |
| 2026-11-15 08:03:39 | Ellagawa (Kalu Ganga) | 5.67 | 🟢 Normal | -0.010 |  |
| 2026-11-15 08:11:00 | Magura (Kalu Ganga) | 2.06 | 🟢 Normal | -0.010 |  |
| 2026-11-15 08:01:13 | Nakkala (Kumbukkan Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-11-15 08:18:49 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | -0.016 |  |
| 2026-11-15 08:09:47 | Panadugama (Nilwala Ganga) | 4.85 | 🟢 Normal | -0.018 |  |
| 2026-11-15 08:08:26 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.019 |  |
| 2026-11-15 08:03:20 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-11-15 08:01:39 | Thanamalwila (Kirindi Oya) | 1.81 | 🟢 Normal | -0.020 |  |
| 2026-11-15 08:05:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.031 |  |
| 2026-11-15 08:07:10 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.037 |  |
| 2026-11-15 08:06:04 | Baddegama (Gin Ganga) | 2.79 | 🟢 Normal | -0.037 |  |
| 2026-11-15 08:02:07 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.041 |  |
| 2026-11-15 08:03:31 | Horowpothana (Yan Oya) | 2.08 | 🟢 Normal | -0.045 |  |
| 2026-11-15 08:01:59 | Wellawaya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.051 |  |
| 2026-11-15 08:05:55 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.054 |  |
| 2026-11-15 08:02:12 | Weraganthota (Mahaweli Ganga) | -2.19 | 🟢 Normal | -0.061 |  |
| 2026-11-15 08:01:32 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)