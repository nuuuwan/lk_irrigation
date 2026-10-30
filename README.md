# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_17:11:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **302,260 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Putupaula — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 17:11:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | -0.038 |  |
| 2026-10-30 17:11:19 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.009 |  |
| 2026-10-30 17:10:43 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:09:22 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-10-30 17:07:42 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:07:10 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-10-30 17:06:40 | Baddegama (Gin Ganga) | 3.21 | 🟢 Normal | -0.037 |  |
| 2026-10-30 17:06:03 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:04:43 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:04:32 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.019 |  |
| 2026-10-30 17:04:28 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:04:21 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:04:07 | Glencourse (Kelani Ganga) | 10.72 | 🟢 Normal | -0.032 |  |
| 2026-10-30 17:04:02 | Putupaula (Kalu Ganga) | 3.22 | 🟡 Alert | -0.020 |  |
| 2026-10-30 17:03:54 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-30 17:03:52 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.079 |  |
| 2026-10-30 17:03:42 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.032 |  |
| 2026-10-30 17:03:41 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:03:34 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 17:03:30 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.031 |  |
| 2026-10-30 17:03:28 | Panadugama (Nilwala Ganga) | 5.20 | 🟡 Alert | -0.039 |  |
| 2026-10-30 17:03:25 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:03:09 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:03:06 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-30 17:03:02 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:03:01 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-10-30 17:02:57 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.052 |  |
| 2026-10-30 17:02:55 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:02:32 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:02:16 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-10-30 17:02:10 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-30 17:02:10 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 17:01:41 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.020 |  |
| 2026-10-30 17:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:01:11 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-30 17:00:55 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:00:25 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-10-30 17:00:12 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.080 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 16:14:27 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-30 17:04:02 | Putupaula (Kalu Ganga) | 3.22 | 🟡 Alert | -0.020 |  |
| 2026-10-30 17:11:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | -0.038 |  |
| 2026-10-30 17:03:28 | Panadugama (Nilwala Ganga) | 5.20 | 🟡 Alert | -0.039 |  |
| 2026-10-30 16:04:26 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-30 17:00:12 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-30 17:03:06 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-30 17:03:54 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-30 17:01:11 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-30 17:02:10 | Thanamalwila (Kirindi Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 17:03:34 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 17:02:32 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:04:21 | Moragaswewa (Deduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:10:43 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:01:37 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:06:03 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:00:55 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:07:42 | Galgamuwa (Mee Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:04:43 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:04:28 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:03:09 | Moraketiya (Walawe Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:03:02 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:03:41 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:03:25 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-10-30 17:11:19 | Thawalama (Gin Ganga) | 2.16 | 🟢 Normal | -0.009 |  |
| 2026-10-30 17:09:22 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-10-30 17:07:10 | Badalgama (Maha Oya) | 2.82 | 🟢 Normal | -0.010 |  |
| 2026-10-30 17:02:10 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-30 17:04:32 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | -0.019 |  |
| 2026-10-30 17:01:41 | Weraganthota (Mahaweli Ganga) | -3.04 | 🟢 Normal | -0.020 |  |
| 2026-10-30 17:02:16 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-10-30 17:00:25 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-10-30 17:03:01 | Hanwella (Kelani Ganga) | 2.91 | 🟢 Normal | -0.020 |  |
| 2026-10-30 17:03:30 | Nagalagam Street (Kelani Ganga) | 0.59 | 🟢 Normal | -0.031 |  |
| 2026-10-30 17:03:42 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.032 |  |
| 2026-10-30 17:04:07 | Glencourse (Kelani Ganga) | 10.72 | 🟢 Normal | -0.032 |  |
| 2026-10-30 17:06:40 | Baddegama (Gin Ganga) | 3.21 | 🟢 Normal | -0.037 |  |
| 2026-10-30 17:02:57 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.052 |  |
| 2026-10-30 17:03:52 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)