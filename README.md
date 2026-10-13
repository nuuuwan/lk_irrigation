# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_10:17:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,647 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 10:17:01 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | -0.008 |  |
| 2026-10-13 10:14:35 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | -0.016 |  |
| 2026-10-13 10:14:33 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.069 |  |
| 2026-10-13 10:10:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.22 | 🟡 Alert | -0.009 |  |
| 2026-10-13 10:09:38 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.114 |  |
| 2026-10-13 10:07:21 | Putupaula (Kalu Ganga) | 1.77 | 🟢 Normal | -0.040 |  |
| 2026-10-13 10:06:57 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:06:32 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:05:56 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.048 |  |
| 2026-10-13 10:05:53 | Rathnapura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.142 |  |
| 2026-10-13 10:05:42 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:05:36 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-13 10:05:34 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-13 10:05:29 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:04:42 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:04:07 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.252 |  |
| 2026-10-13 10:03:39 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-13 10:03:37 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-10-13 10:03:27 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | -0.061 |  |
| 2026-10-13 10:03:25 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:03:21 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.255 |  |
| 2026-10-13 10:03:02 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.158 |  |
| 2026-10-13 10:03:02 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-13 10:03:00 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:03:00 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:02:57 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-10-13 10:02:34 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.024 |  |
| 2026-10-13 10:02:23 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:01:57 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 10:01:35 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-13 10:01:28 | Panadugama (Nilwala Ganga) | 6.10 | 🟠 Minor Flood | -0.066 |  |
| 2026-10-13 10:01:26 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.039 |  |
| 2026-10-13 10:01:24 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.021 |  |
| 2026-10-13 10:01:23 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:01:19 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-13 10:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-13 10:00:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-13 10:00:27 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-13 10:00:12 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 10:01:28 | Panadugama (Nilwala Ganga) | 6.10 | 🟠 Minor Flood | -0.066 |  |
| 2026-10-13 10:03:39 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-13 10:10:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.22 | 🟡 Alert | -0.009 |  |
| 2026-10-13 10:00:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-10-13 10:01:57 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 10:05:36 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-13 10:00:12 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:04:42 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:03:00 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:03:25 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:02:23 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:06:32 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:03:00 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:06:57 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:05:42 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:05:29 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:01:23 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-13 10:17:01 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | -0.008 |  |
| 2026-10-13 10:05:34 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-10-13 10:00:27 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-13 10:03:02 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-13 10:01:19 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-10-13 10:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-10-13 10:14:35 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | -0.016 |  |
| 2026-10-13 10:02:57 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-10-13 10:03:37 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-10-13 10:01:35 | Moraketiya (Walawe Ganga) | 1.24 | 🟢 Normal | -0.020 |  |
| 2026-10-13 10:01:24 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.021 |  |
| 2026-10-13 10:02:34 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.024 |  |
| 2026-10-13 10:01:26 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.039 |  |
| 2026-10-13 10:07:21 | Putupaula (Kalu Ganga) | 1.77 | 🟢 Normal | -0.040 |  |
| 2026-10-13 10:05:56 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | -0.048 |  |
| 2026-10-13 10:03:27 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | -0.061 |  |
| 2026-10-13 10:14:33 | Magura (Kalu Ganga) | 2.60 | 🟢 Normal | -0.069 |  |
| 2026-10-13 10:09:38 | Peradeniya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.114 |  |
| 2026-10-13 10:05:53 | Rathnapura (Kalu Ganga) | 3.27 | 🟢 Normal | -0.142 |  |
| 2026-10-13 10:03:02 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.158 |  |
| 2026-10-13 10:04:07 | Urawa (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.252 |  |
| 2026-10-13 10:03:21 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.255 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)