# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_12:08:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,162 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 12:08:53 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:08:46 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:07:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-29 12:07:08 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-29 12:06:36 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-29 12:06:17 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:06:14 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:05:57 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:05:07 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 12:04:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.35 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-29 12:04:23 | Putupaula (Kalu Ganga) | 3.71 | 🟡 Alert | 0.000 |  |
| 2026-10-29 12:04:09 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | -0.039 |  |
| 2026-10-29 12:04:01 | Rathnapura (Kalu Ganga) | 4.68 | 🟢 Normal | -0.049 |  |
| 2026-10-29 12:03:34 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-29 12:03:26 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-10-29 12:03:23 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:03:14 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:03:01 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-29 12:03:01 | Dunamale (Aththanagalu Oya) | 2.49 | 🟢 Normal | -0.030 |  |
| 2026-10-29 12:02:59 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.029 |  |
| 2026-10-29 12:02:50 | Hanwella (Kelani Ganga) | 3.65 | 🟢 Normal | -0.071 |  |
| 2026-10-29 12:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-29 12:02:45 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | -0.021 |  |
| 2026-10-29 12:02:44 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:02:42 | Galgamuwa (Mee Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:02:40 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-10-29 12:02:36 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.062 |  |
| 2026-10-29 12:02:23 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-10-29 12:02:19 | Ellagawa (Kalu Ganga) | 9.98 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:02:17 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-29 12:02:11 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.060 |  |
| 2026-10-29 12:02:04 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.204 |  |
| 2026-10-29 12:02:01 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:01:19 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:01:15 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-29 12:00:55 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 12:00:40 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:00:28 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 12:05:07 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 12:04:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.35 | 🟠 Minor Flood | -0.020 |  |
| 2026-10-29 12:02:45 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | -0.021 |  |
| 2026-10-29 12:04:23 | Putupaula (Kalu Ganga) | 3.71 | 🟡 Alert | 0.000 |  |
| 2026-10-29 11:07:15 | Panadugama (Nilwala Ganga) | 5.82 | 🟡 Alert | -0.031 |  |
| 2026-10-29 12:07:08 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-10-29 12:07:38 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-29 12:01:15 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-29 12:06:36 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-29 12:03:34 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-29 12:00:55 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 12:00:40 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:02:44 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:02:42 | Galgamuwa (Mee Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:06:17 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:02:19 | Ellagawa (Kalu Ganga) | 9.98 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:01:19 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:03:14 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:05:57 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:03:23 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:08:53 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:02:01 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:08:46 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-29 12:03:26 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-10-29 12:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-10-29 12:00:28 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-29 12:03:01 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-10-29 12:02:17 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-10-29 12:02:40 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-10-29 12:02:23 | Moragaswewa (Deduru Oya) | 1.27 | 🟢 Normal | -0.021 |  |
| 2026-10-29 12:02:59 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | -0.029 |  |
| 2026-10-29 12:03:01 | Dunamale (Aththanagalu Oya) | 2.49 | 🟢 Normal | -0.030 |  |
| 2026-10-29 12:04:09 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | -0.039 |  |
| 2026-10-29 11:13:50 | Pitabeddara (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.041 |  |
| 2026-10-29 12:04:01 | Rathnapura (Kalu Ganga) | 4.68 | 🟢 Normal | -0.049 |  |
| 2026-10-29 12:02:11 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.060 |  |
| 2026-10-29 12:02:36 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.062 |  |
| 2026-10-29 12:02:50 | Hanwella (Kelani Ganga) | 3.65 | 🟢 Normal | -0.071 |  |
| 2026-10-29 12:02:04 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)